# User accounts and security

## What will we learn?
- Build a log system for blog web app
- Using cookies
- Password and hashing password

## Cookies
> Cookies is a small (< 4 Kb) piece of data stored in the browser for a website

- Cookies store some temporary information of a website such as: name of web site, user id. The most common role of cookies is to allow user not have to log everytime he goes to that website. 
- Each website can store 20 cookies
- Each cookie is used for only one website
- Use for tracking user for advertisement
- Cookie shoud le as simple as possible. It should only store information about particular user, or particular browser.

#### Where are cookies?
Cookies are sent between browser and web server through http header.

- Web server set cookies for browser through `set-cookie`  header
- Browser sends cookies to web server throudh `Cookies` header

#### Setting cookies
In chrome go to `chrome://settings/content/cookies` to set options for cookies
- [x] Allow sites to save and read cookies data
- [ ] Keep local data only until you quit your browser. (It's meam when you log into a website again, every your login information will be disappeared)
- [x] Block third-parth cookies (This cookies often use to analysis ad tracker. For example, you go to `reddit.com` then `reddit.com` will send your cookies to `google`. Google will use that cookies to add suitable advertisements in other website)

#### Edit cookies
Cookies is just strings. So we can edit it.
Open console in dev tools.
```
document.cookie
```

#### Prevent editing cookies (Cheating)
**Hashing**
```
H(x) -> y
x: data
y: fixed length bit string (32 - 256 bit)
```

To learn detail about hashing learning course `CS387`

**Hashing algorithms**
- crc32: checksums, fast, but easy to collision
- md5: quite fast, not secure (pretty secure in the past, but nearly years, it's not!)
- sha1: not as fast as md5, fairly secure
- sha256: slow, pretty secure

**Hashing in python**
```python
import hashlib
x = hashlib.sha256(b"Hello")
x.hexdigest()
```

**Hashing cookies**
Instead of `Set-Cookie` like this:
```
Set-Cookie visits=1
```

We need to add the hashing of value to the cookies
```
Set-Cookie visits=1,hashing_algorithm(1)
hashing_algorithm can be: md5, sha1, sha256, ...
```

But, if attacker knows the hashing algorithm, they can modify both real value, and hashing value. So, we need to add extra secrete value to origin value
```
H(value) -> y
H(secrete + value) -> y'
```

**Hash-based message authentication code in Python**
use a secrete key to generate the new hash value
```python
import hmac
SECRETE = "sosecrete" # no public
hmac.new(SECRETE, "value")
```

**Summary**
- `visits=1` -> so easy to cheat
- `visits=1|md5(1)` -> still easy if know the hashing algorithm
- `visits=1|hmac(Secrete, 1)` -> Impossible to forge unless leaking secrete key

## Password hashing
User's password should be hashed before writing in the database

#### Rainbow table
Hacker can create a table that look from hashing value to clear text.

https://en.wikipedia.org/wiki/Rainbow_table
https://crackstation.net/

#### Bcrypt
In the real world, let's use `Bscrypt`




