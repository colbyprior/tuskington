""" Module allows to check http method """
import subprocess
from flask import request
from git import Repo
from app import app


# ext::sh -c touch% /tmp/pwned
@app.route("/cloner", methods=['GET', 'POST'])
def cloner():
    if request.method == "GET":
        return """
<form action="/cloner" method="post">
  <label for="repo">Git Repo to Clone:</label><br>
  <input type="text" id="repo" name="repo" value="https://github.com/..."><br>
  <input type="submit" value="Submit">
</form> """
    if "repo" not in request.form.keys():
        return "Bad POST data"
    repo_name = request.form["repo"]
    subprocess.run(["rm", "-rf", "/tmp/*"], capture_output=True, text=True)

    repo = Repo.init('', bare=True)
    repo.clone_from(repo_name, f'/tmp/{repo_name}', multi_options=["-c protocol.ext.allow=always"])
    ls_output = subprocess.Popen(["ls", "-l", f"/tmp/{repo_name}"], stdout=subprocess.PIPE)
    return str(ls_output.communicate()).replace("\\n", "<br>")
