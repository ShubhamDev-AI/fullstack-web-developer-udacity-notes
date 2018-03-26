# Project 2: Blog web app

## Requirements
- [x] python2
- [x] Google App Engine SDK
- [x] Jinja2

## Features
- Create basic blog
    - [x] Front page that lists blog posts
    - [x] A form submit new post
    - [x] Blog posts have their own page
- Add user registration
    - [x] Have a registration form that validates user input, and displays the error(s) when necessary.
    - [x] After a successful registration, a user is directed to a welcome page with a greeting, “Welcome, [User]” where [User] is a name set in a cookie.
If a user attempts to visit the welcome page without being signed in (without having a cookie), then redirect to the Signup page.
    - [x] Store passwords securely.
- Add Login
    - [x] Have a login form that validates user input, and displays the error(s) when necessary.
    - [x] After a successful login, the user is directed to the same welcome page.
- Add Logout
    - [x] Have a logout form that validates user input, and displays the error(s) when necessary.
    - [x] After logging out, the cookie is cleared and user is redirected to the Signup/Login page from Step 2.
- Add Other Features on Your Own
    - [ ] Users should only be able to edit/delete their posts. They receive an error message if they disobey this rule.
    - [ ] Users can like/unlike posts, but not their own. They receive an error message if they disobey this rule.
    - [ ] Users can comment on posts. They can only edit/delete their own posts, and they should receive an error message if they disobey this rule.

## Deploy
- [x] Create README.md
- [ ] Refactor code so it is well structured, well commented, and conforms to the Python Style Guide.
- [ ] Deploy app to appspot.com using `gcloud app deploy`