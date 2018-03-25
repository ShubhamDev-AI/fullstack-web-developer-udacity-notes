import os
import webapp2
import jinja2

from google.appengine.ext import db

# create env to handle rendering template
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, text):
        self.response.write(text)

    def render_str(self, template, **kwargs):
        """Read file template and render a big string"""
        t = jinja_env.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * from Post\
                            ORDER BY created DESC")
        print(posts)
        self.render("index.html", posts=posts)

    def post(self):
        pass


class CreateNewPostPage(Handler):
    def get(self):
        self.render("new_post.html")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            post = Post(subject=subject, content=content)
            post.put()
            post_id = post.key().id()
            self.redirect("/{}".format(post_id))

        error = "We need both subject and content"
        self.render("new_post.html", error=error, subject=subject,
                    content=content)


class SinglePostPage(Handler):
    def get(self, post_id):
        if post_id.isdigit():
            post_id = int(post_id)
            post = Post.get_by_id(post_id)
            self.render("single_post.html", subject=post.subject,
                        content=post.content)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', CreateNewPostPage),
    ('/(\d+)', SinglePostPage),
], debug=True)
