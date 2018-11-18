from flask              import Flask, render_template
from flask_bootstrap    import Bootstrap
from flask_login        import LoginManager
from flask_migrate      import Migrate
from flask_sqlalchemy   import SQLAlchemy
from config             import Config
from logging.handlers 	import RotatingFileHandler
import os
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(Config)  #apply config file
bootstrap = Bootstrap(app)
db        = SQLAlchemy(app)
migrate   = Migrate(app, db)
login     = LoginManager(app)
login.login_view = 'login'

#app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
#app.config['SECRET_KEY'] = 'totalyManbearpigcerial'
#toolbar = DebugToolbarExtension(app)


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')



from app import routes, models, errors
