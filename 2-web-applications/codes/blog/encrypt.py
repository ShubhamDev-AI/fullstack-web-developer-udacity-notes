import hashlib
import random
import string
import hmac

SECRETE_KEY = "129jcn299jcji"


# SECURE COOKIES
# For speed up, we don't need to use SHA-256 to encrypt cookies.
# md5 and a SECRETE KEY is good enough
def make_hmac(value):
    """
    Generate a hash-based message authentication code
    :param value: cookie's value
    :return: A hmac
    """
    return hmac.new(SECRETE_KEY, value).hexdigest()


def check_secure_cookie(s):
    """
    Check if cookie sent from browser is valid or not
    :param s: cookie string
    :return: If cookie is valid, return its right value, unless return None
    """
    try:
        value, hashing_value = s.split('|')
        if make_hmac(value) == hashing_value:
            return value
    except Exception as e:
        pass
    return None


def make_secure_cookie(value):
    """
    Create secure cookie for a value
    :param s: cookie's value
    :return: a string contains 2 part: cookie's value, hmac's value splited
    by `|` sign
    """
    return "{}|{}".format(value, make_hmac(str(value)))


# SECURE PASSWORD
# To make password cannot be reverted, even in case loosing all, we use
# sha256 to encrypt password with a random salt.
def make_salt():
    """Generate a random 5 character length salt"""
    return ''.join([random.choice(string.letters) for i in xrange(5)])


def make_pw_hash(name, pw, salt=None):
    """
    Generate hashing password from username, password and salt
    :param name: username
    :param pw: raw password
    :param salt: random salt
    :return: a string includes hashed password and its salt separated by `|`
    sign
    """
    if not salt:
        salt = make_salt()
    hash = hashlib.sha256(name + pw + salt).hexdigest()
    return "{}|{}".format(hash, salt)


def valid_pwd(name, pwd, h):
    """
    Check if username and password is valid
    :param name: username string from browser
    :param pwd: password string from browser
    :param h: password get from database in form `<hashing>|<salt>`
    :return:
    """
    if h:
        _, salt = h.split("|")
        actual_hash = make_pw_hash(name, pwd, salt)
        if actual_hash != h:
            return False
    return True
