"""
Rot13.py

Simple web app that Rot13 encrypts some input.
"""
import webapp2

class ROT13Handler(webapp2.RequestHandler):
    def rot13(self, cipher_text):
        return_string = ""
        for character in cipher_text:
            if character.isalpha():
                int_char = ord(character) + 13
                if character.isupper():
                    if int_char > ord('Z'): int_char -= 26
                else:
                    if int_char > ord('z'): int_char -= 26
                return_string += chr(int_char)
            else:
                return_string += character
        return return_string

    def write_form(self, input_text=""):
        input_text = self.rot13(input_text)
        self.response.out.write(rot_13_form % {"textarea": input_text})

    def get(self):
        self.write_form()

    def post(self):
        input_text = self.request.get('text')
        self.write_form(input_text)
rot_13_form = """
<form method="post">
    Enter text to be ROT13 Encrypted:
    <br>

    <textarea name="text">%(textarea)s</textarea>

    <br>
    <br>
    <input type="submit">
</form>
"""