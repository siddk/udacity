"""
template.py

Basic application that demonstrates the use of jinja2 templates.
"""
import webapp2

class TemplateHandler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render('shopping_list.html', items = items)

class HardCodedTemplateHandler(Handler):
    def get(self):
        output = template_form
        output_hidden = ""
        output_items = ""

        items = self.request.get_all("food")
        if items:
            for item in items:
                output_hidden += template_hidden % item
                output_items += template_item % item

            output_shopping = template_shopping_list % output_items
            output += output_shopping

        output = output % output_hidden

        self.write(output)

template_form = """<form><h2>Add a Food</h2><input type="text" name="food">%s<button>Add</button></form>"""

template_hidden = """<input type="hidden" name="food" value="%s">"""

template_item = """<li>%s</li>"""

template_shopping_list = """<br><br><h2>Shopping List</h2><ul>%s</u"""

