import hmac
import hashlib
import random
import string

SECRETE = 'imsosecrete'


def hash_str(s):
    return hmac.new(SECRETE, s).hexdigest()


def make_hashing(s):
    return hashlib.md5(s).hexdigest()


def check_secure_cookie(s):
    try:
        value, hashing_value = s.split(',')
        if make_hashing(value) == hashing_value:
            return value
    except Exception as e:
        pass
    return None


def make_secure_cookie(s):
    return "{},{}".format(s, make_hashing(str(s)))


def make_salt():
    return ''.join([random.choice(string.letters) for i in xrange(5)])


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    hash = hashlib.sha256(name + pw + salt).hexdigest()
    return "{}|{}".format(hash, salt)


def valid_pwd(name, pwd, h):
    if h:
        _, salt = h.split("|")
        actual_hash = make_pw_hash(name, pwd, salt)
        if actual_hash != h:
            return False
    return True


print(hashlib.md5("0").hexdigest())
print(check_secure_cookie("0,cfcd208495d565ef66e7dff9f98764da"))
print(make_secure_cookie(1))
print(hash_str("0"))
print(make_salt())
h = make_pw_hash('meo', 'grrr')
print(valid_pwd('meo', 'grrr', h))
