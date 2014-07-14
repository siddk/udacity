"""
wiki.py

Final project for Udacity course CS 253. Implements a fully editable wiki, with page creation, and page editing fully available. Built with webapp2, deployed on Google App Engine, with SQLite backend.
"""
from code.handler import Handler

class WikiMainPageHandler(Handler):
    def render_page(self):
        self.render("wiki.html")

    def get(self):
        self.render_page()

class WikiSignupHandler(Handler):
    pass

class WikiLogin(Handler):
    pass

class WikiLogout(Handler):
    pass

class EditPage(Handler):
    pass

class WikiPageHandler(Handler):
    pass