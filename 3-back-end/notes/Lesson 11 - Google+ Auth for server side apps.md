# Google+ Auth for server side apps

## How it work?
- First, the client made a request sign up for our app
- Next, Our app redirects to a page of Auth Provider to ask client allows using their information.
- Then, Auth Provider provides client a Token
- Client takes this Token and sends to our app
- Out app holds client's Token and makes request to Auth Provide to get Token
- Auth Provider gives our app Token, and we use this Token to create user account

## Anti forgery
- Forgery means the authenticated user is fake.
- To prevent it, we use a token session to verify both client and server side.