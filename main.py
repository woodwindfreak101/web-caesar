from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='POST'>
            <label>Rotate by:
                <input name="integer" type="text" value="0" />
            </label>
            <br>
            <label>Text to encrypt:
                <textarea name="message" type="text" value="message">{0}</textarea>
            </label>
            <input type="submit" />
        </form>            
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():

    integer = request.form['integer']
    message = request.form['message']

    encrypted_message = rotate_string(message, int(integer))
    return form.format(encrypted_message)


app.run()