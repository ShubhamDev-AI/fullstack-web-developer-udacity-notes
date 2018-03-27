import os
import webapp2
import jinja2
import encrypt

from models import Post, Account
from google.appengine.ext import db

# create env to handle rendering template
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    """Request Handler"""

    def write(self, text):
        self.response.write(text)

    def check_cookies(self):
        cookie = self.request.cookies.get('user_id')
        if encrypt.check_secure_cookie(cookie):
            return True
        return False

    def render_str(self, template, **kwargs):
        """Read file template and render a big string"""
        t = jinja_env.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    """Main page, listing all posts"""

    def get(self):
        # get posts from database
        posts = db.GqlQuery("SELECT * from Post\
                            ORDER BY created DESC")
        # check cookies
        username = ""
        if self.check_cookies():
            username = self.request.cookies.get("username")

        # render page
        self.render("index.html", posts=posts, username=username)

    def post(self):
        pass


class CreateNewPostPage(Handler):
    """Handle creating new post"""

    def get(self):
        if not self.check_cookies():
            self.redirect("/login")
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
    """Page show a single post"""

    def get(self, post_id):
        if post_id.isdigit():
            # get post by id
            post_id = int(post_id)
            post = Post.get_by_id(post_id)
            subject = post.subject
            content = post.content
            created = post.created.strftime("%d-%m-%Y %H:%M:%S")

            # check cookies
            username = ""
            if self.check_cookies():
                username = self.request.cookies.get("username")

            # render page
            self.render("single_post.html", subject=post.subject,
                        content=post.content,
                        created=created,
                        username=username)


class SignUpPage(Handler):
    """Handle sign up function"""

    def get(self):
        self.render("sign_up.html")

    def is_username_exist(self, username):
        """Check if account has existed in database"""
        account = db.GqlQuery(
            "SELECT * FROM Account WHERE username='{}'".format(
                username))
        if account.count():
            return True
        return False

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_password = self.request.get('verify')
        email = self.request.get('email')
        error = ""

        if username and password and verify_password:
            if password != verify_password:
                error = "Verify password is not matched"
            elif self.is_username_exist(username):
                error = "Username has already existed"
            else:
                hash_pw = encrypt.make_pw_hash(username, password)
                account = Account(username=username, password=hash_pw,
                                  email=email)
                account.put()
                account_id = account.key().id()
                cookie_account_id = encrypt.make_secure_cookie(account_id)
                # TODO: What is Path=/?
                self.response.headers.add_header(
                    "Set-Cookie", "user_id={}; Path=/".format(cookie_account_id)
                )
                self.response.headers.add_header(
                    "Set-Cookie", "username={}; Path=/".format(username)
                )
                self.redirect("/welcome")
        else:
            error = "Username, password and verify password is required!"
        self.render("sign_up.html", error=error, username=username, email=email)


class LoginPage(Handler):
    """Handle login function"""

    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        error = ""

        if username and password:
            accounts = db.GqlQuery("Select * FROM Account WHERE username='{"
                                   "}'".format(username))
            if accounts.count():
                account = accounts[0]
                if encrypt.valid_pwd(username, password, account.password):
                    account_id = account.key().id()
                    cookie_account_id = encrypt.make_secure_cookie(account_id)
                    self.response.headers.add_header(
                        "Set-Cookie",
                        "user_id={}; Path=/".format(cookie_account_id)
                    )
                    self.response.headers.add_header(
                        "Set-Cookie", "username={}; Path=/".format(username)
                    )
                    self.redirect("/welcome")
            error = "Password or username is not valid"
        else:
            error = "Username and Password are required"

        self.render("login.html", error=error)


class LogOutPage(Handler):
    """Set cookie to None, redirect to login"""
    def get(self):
        self.response.headers.add_header(
            "Set-Cookie", "user_id={}; Path=/".format("")
        )
        self.redirect("/login")


class WelcomePage(Handler):
    """Welcome page after signing up or logging up successfully"""

    def get(self):
        if not self.check_cookies():
            self.redirect("/login")
        username = self.request.cookies.get("username")
        self.render("welcome.html", username=username)


class AccountPage(Handler):
    """Listing all accounts"""
    
    def get(self):
        accounts = db.GqlQuery("SELECT * FROM Account ORDER BY created DESC")
        self.render("account_list.html", accounts=accounts)
