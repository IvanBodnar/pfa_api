from fabric.api import *

env.hosts = ['ivan@104.236.39.222']
env.user = 'ivan'
env.password = 'pared111'

def mk():
    local('git add --all :/ && git commit')
    local('git push')
    run('sudo service nginx stop')
    run('cd apps/pfa_api')
    with prefix('source bin/activate'):
        run('git pull origin master')
    run('sudo service nginx start')
