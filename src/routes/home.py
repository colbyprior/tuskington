from app import app


#
@app.route("/", methods=['GET'])
def home():
    return """<body>
    <a href=\"/cloner\">cloner page</a>
    <a href=\"/selector\">selector page</a>
    <a href=\"/echo\">echo page</a>
    </body>
    """
