"""
ascii.py

Sample web application to demonstrate basic databases in Google App Engine.
Mockup of the website 4chan, asciiChan, a platform to share asciiArt.
"""
from google.appengine.ext import db
from code.handler import Handler
import urllib2
from xml.dom import minidom

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

IP_URL = "http://api.hostip.info/?ip="
def get_coords(ip):
    url = IP_URL + ip
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except URLError:
        return

    if content:
        #Parse xml and find the coordinates
        x = minidom.parseString(content)
        x = x.getElementsByTagName("gml:coordinates")
        if x:
            cord = x[0].childNodes[0].nodeValue
            c = cord.split(',')
            return db.GeoPt(c[1], c[0])


class AsciiChanHandler(Handler):
    def render_page(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC LIMIT 10")
        self.render("ascii.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        self.render_page()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            # Lookup user's coordinates from their IP
            # If we have coordinates, add them to Art
            a.put()

            self.redirect("/unit3/asciichan")
        else:
            error = "We need both a title and some artwork!"
            self.render_page(title, art, error)