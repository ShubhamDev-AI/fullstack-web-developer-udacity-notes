import webapp2

from urls import MainPage, CreateNewPostPage, LoginPage, SignUpPage, \
    SinglePostPage, AccountPage, WelcomePage, LogOutPage

# Routing
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', CreateNewPostPage),
    ('/signup', SignUpPage),
    ('/login', LoginPage),
    ('/logout', LogOutPage),
    ('/welcome', WelcomePage),
    ('/(\d+)', SinglePostPage),
    ('/accounts', AccountPage)
], debug=True)
