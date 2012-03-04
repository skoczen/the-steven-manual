from fabric.api import *
import os

env.PROJECT_NAME = "my-new-project"
env.GITHUB_USER = "skoczen"
env.GITHUB_REPO = PROJECT_NAME
env.VIRTUALENV_NAME = PROJECT_NAME

def initial_setup(cmd):
    local("mkvirtualenv %(VIRTUALENV_NAME)s")
    local("echo cd `pwd` >> ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/postactivate" % env)
    local("git remote rename origin artechetype")
    local("git remote set-url origin git@github.com:%(GITHUB_USER)s/%(GITHUB_REPO)s.git" % env)
    local("git push -u origin")


def run_ve(cmd):
    env.cmd = cmd
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate;cd ~/workingCopy/%(PROJECT_NAME)s/project;%(cmd)s" % env)

def deploy():
    run_ve("./manage.py collectstatic --noinput --settings=envs.live")
    run_ve("./manage.py compress --force --settings=envs.live")
    run_ve("./manage.py sync_static --gzip --expires --settings=envs.live")
    deploy_code()

def deploy_code():
    run_ve("git push heroku live:master")
    run_ve("heroku run project/manage.py syncdb")
    run_ve("heroku run project/manage.py migrate")
    run_ve("heroku restart")