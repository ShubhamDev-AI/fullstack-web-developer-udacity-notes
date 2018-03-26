# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import hmac

import webapp2
import hashlib

form = """
<form method="post">
  What is your birthday?
  <br>
  <label>Month
    <input name="month" type="text" value="%(month)s">
  </label>
  <label>Day
    <input name="day" type="text" value="%(day)s">
  </label>
  <label>Year
    <input name="year" type="text" value="%(year)s">
  </label>
  <div style="color: red">%(error)s</div>
  <br>
  <br>
  <input type="submit">
</form>"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# Create list abbreviation of months. Each item is 3 character
# length and lowercase
abbr_month = [m[:3].lower() for m in months]


def valid_month(month):
    """Validation of a month"""
    if month:
        if month.lower() in abbr_month or month.title() in months:
            return month.title()
    return None


def valid_day(day):
    """Validation of a day"""
    if not day.isdigit():
        return None
    d = int(day)
    if 1 <= d <= 31:
        return d
    return None


def valid_year(year):
    """Validation of a year"""
    if not year.isdigit():
        return None
    year = int(year)
    if 1900 < year < 2100:
        return year


def escape_html(s):
    """Replace specific character by its escape html"""
    s = s.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;") \
        .replace('"', "&quot;")
    return s


class MainPage(webapp2.RequestHandler):
    SECRETE = "iamsosecrete"
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {
            "error": error,
            "month": escape_html(month),
            "day": escape_html(day),
            "year": escape_html(year),
        })

    def make_hashing(self, s):
        return hashlib.md5(s).hexdigest()

    def make_hmac(self, s):
        return hmac.new(self.SECRETE, s).hexdigest()

    def check_secure_cookie(self, s):
        try:
            value, hashing_value = s.split('|')
            if self.make_hmac(value) == hashing_value:
                return value
        except Exception as e:
            pass
        return None

    def make_secure_cookie(self, s):
        return "{}|{}".format(s, self.make_hmac(str(s)))

    def get(self):
        # self.write_form()
        self.response.headers['Content-Type'] = 'text/plain'

        visits = 0
        visit_cookie_str = self.request.cookies.get('visits')

        if visit_cookie_str:
            cookie_val = self.check_secure_cookie(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)

        visits += 1

        cookies = self.make_secure_cookie(visits)

        # set header for response
        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(
            cookies))
        self.response.write("You've been here {} times".format(visits))

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a totally valid day")


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/thanks', ThanksHandler),
], debug=True)
