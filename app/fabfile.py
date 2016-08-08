from fabric.api import *

env.hosts = ['ivan@104.236.39.222']
env.user = 'ivan'
env.password = 'pared111'

def mk():
    local('git add --all :/ && git commit')
    local('git push')


def virt():
    with prefix('source apps/pfa_api/bin/activate'):
        yield

def dep():
    run('sudo service nginx stop')
    run('source apps/pfa_api/venv/bin/activate')
    with cd('apps/pfa_api'):
        run('git pull origin master')
    run('sudo service nginx start')
