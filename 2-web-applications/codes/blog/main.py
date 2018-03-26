import webapp2

from urls import MainPage, CreateNewPostPage, LoginPage, SignUpPage, \
    SinglePostPage, AccountPage, WelcomePage, LogOutPage

# Routing
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', CreateNewPostPage),
    ('/login', LoginPage),
    ('/logout', LogOutPage),
    ('/signup', SignUpPage),
    ('/welcome', WelcomePage),
    ('/(\d+)', SinglePostPage),
    ('/accounts', AccountPage)
], debug=True)
