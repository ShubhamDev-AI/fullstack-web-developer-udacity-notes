# Requests and APIs

## AJAX
- Update new data without reloading page

#### Callback

#### Project to build
- Using Google Street View to get image and set to background
- New York Time API to get articles
- Wikipedia to get articles

#### CORS
- CORS is set in the server-side to works around the same-origin policy
- same-origin policy was implemented by browser to prevent bad guys from running script on other site. 
- But executing scripts on different domains is not absolutely harm. Sometimes, It's so necessary to do it. 
- Then, web developer maintained server-side API to enable other site can execute scripts on their site. 
- When the certain headers are returned from server, browser will allow cross-domain request to occur.
- If API not allow cross-domain request, we need to use other trick called `JSON-P`

#### JSON-P
- ???
- Error Handling is not built-in the JsonP. So, we need to handle it manually. It means, we cannot use `.fail` function of `$.ajax`. Instead, we should make a timeOut to wait, if it's longer than an instant time, abort it.

#### Speed up the render
- Step 1: Request generic HTML
- Step 2: Request unique HTML
- Step 3: Render generic HTML
- Step 4: Render unique HTML

 
