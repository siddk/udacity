"""
ascii.py

Sample web application to demonstrate basic databases in Google App Engine.
Mockup of the website 4chan, asciiChan, a platform to share asciiArt.
"""
from google.appengine.ext import db
from google.appengine.ext import memcache
from code.handler import Handler
import urllib2
from xml.dom import minidom

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    coords = db.GeoPtProperty()

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

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"
def gmaps_img(points):
    temp_url = GMAPS_URL
    for point in points:
        temp_url += "markers=%s,%s&" % (str(point.lat), str(point.lon))
    temp_url = temp_url[:-1]
    return temp_url

def top_arts(update = False):
    key = 'top'
    arts = memcache.get(key)
    if arts is None or update:
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC LIMIT 10")
        arts = list(arts)
        memcache.set(key, arts)

    return arts

class AsciiChanHandler(Handler):
    def render_page(self, title="", art="", error=""):
        arts = top_arts()

        # Find which arts have coords
        points = []
        for a in arts:
            if a.coords:
                points.append(a.coords)

        img_url = None
        if points:
            img_url = gmaps_img(points)

        self.render("ascii.html", title = title, art = art, error = error, arts = arts, img_url = img_url)

    def get(self):
        self.render_page()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            coords = get_coords(self.request.remote_addr)
            if coords:
                a.coords = coords
            a.put()
            top_arts(True)

            self.redirect("/unit3/asciichan")
        else:
            error = "We need both a title and some artwork!"
            self.render_page(title, art, error)