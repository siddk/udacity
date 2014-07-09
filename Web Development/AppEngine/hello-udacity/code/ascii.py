"""
ascii.py

Sample web application to demonstrate basic databases in Google App Engine.
Mockup of the website 4chan, asciiChan, a platform to share asciiArt.
"""

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class AsciiChanHandler(Handler):
    def render_page(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("ascii.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        self.render_page()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()

            self.redirect("/unit3/asciichan")
        else:
            error = "We need both a title and some artwork!"
            self.render_page(title, art, error)