from flask              import Flask, render_template
from flask_bootstrap    import Bootstrap
from flask_sqlalchemy   import SQLAlchemy
from flask_migrate      import Migrate
from config             import Config

app = Flask(__name__)
app.config.from_object(Config)  #apply config file
bootstrap = Bootstrap(app)
db        = SQLAlchemy(app)
migrate   = Migrate(app, db)

from app import routes, models
