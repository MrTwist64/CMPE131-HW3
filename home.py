from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def home():
    name = 'Aaron'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    output_str = f"""
    <html>
    <head>
        <title>CMPE 131 HW 3</title>
    </head>
    <body>
        <h1>Welcome {name}!</h1>
        <a href="https://www.google.com/">not google</a>
        <ul>"""
    for city in city_names:
        output_str += f"<li>{city}</li>\n"
    output_str += """
        </ul>
    </body>
    </html>
    """
    return output_str

myapp.run()