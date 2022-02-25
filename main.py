from flask import Flask
import git
import os

app = Flask(__name__)


@app.route("/")
def task_git():
    repository = git.Repo('/home/kelvin/Documents/PersonalProjects/Flask-Git/')
    repository.active_branch.log().to_file(os.path.join(os.getcwd() + '/log.txt'))
    return "done"
