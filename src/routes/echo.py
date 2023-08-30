from flask import request
from app import app


@app.route("/echo", methods=['GET', 'POST'])
def echo():
    if request.method == "GET":
        return """
<form action="/echo" method="post">
  <label for="name">Person to echo:</label><br>
  <input type="text" id="name" name="name" value=""><br>
  <input type="submit" value="Submit">
</form> """
    if "name" not in request.form.keys():
        return "Bad POST data"
    name = request.form["name"]

    return f"""
    <a>{name}</a>
    """
