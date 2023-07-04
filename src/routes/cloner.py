from flask import request
from git import Repo
import subprocess
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
    else:
        if "repo" not in request.form.keys():
            return "Bad POST data"
        repo = request.form["repo"]
        #rm = subprocess.run(["rm", "-r", "-f", "/tmp/*"], shell=True, capture_output=True, text=True)
        rm = subprocess.run(["rm", "-rf", "/tmp/*"], capture_output=True, text=True)

        r = Repo.init('', bare=True)
        r.clone_from(repo, f'/tmp/{repo}', multi_options=["-c protocol.ext.allow=always"])
        ls_output = subprocess.Popen(["ls", "-l", f"/tmp/{repo}"], stdout = subprocess.PIPE)
        return (str(ls_output.communicate()).replace("\\n", "<br>"))

