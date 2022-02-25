from flask import Flask
import git

app = Flask(__name__)


@app.route("/")
def task_git():
    repository = git.Repo('/home/kelvin/Documents/PersonalProjects/Flask-Git/')
    return repository
