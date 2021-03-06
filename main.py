from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
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
        textarea{{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
        <form method='POST'>
            <label>Rotate by:
                <input type="text" name="rot" value='0' />
            </label>
            <label>
                <textarea name="text">{0}</textarea>
            </label>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    text = ""
    return form.format(text)

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    new_text = rotate_string(text, rot)
    
    return form.format(new_text)


app.run()