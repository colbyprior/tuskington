""" Module allows to check http method """
from flask import request
import sqlite3
from app import app


#
@app.route("/selector", methods=['GET', 'POST'])
def cloner():
    if request.method == "GET":
        return """
<form action="/cloner" method="post">
  <label for="repo">Person to find:</label><br>
  <input type="text" id="user" name="user" value=""><br>
  <input type="submit" value="Submit">
</form> """
    if "user" not in request.form.keys():
        return "Bad POST data"
    user = request.form["user"]
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("select displayName from users where name=\"" + user + "\"")

    return str(res.fetchall())
