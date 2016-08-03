import os, sys
from flask_migrate import MigrateCommand

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from flask_script import Manager, Server
import app

manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='localhost',
    port=5000
))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
