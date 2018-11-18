from flask_login        import UserMixin
from werkzeug.security  import generate_password_hash, check_password_hash
from datetime           import datetime
from app                import db, login
from hashlib            import md5

class User(UserMixin, db.Model):
    id          = db.Column(db.String(32),  primary_key=True)
    name        = db.Column(db.String(64),  index=True, unique=True, nullable=False)
    email       = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password    = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(255))
    created_at  = db.Column(db.DateTime,    index=True, default=datetime.utcnow, nullable=False)
    last_seen   = db.Column(db.DateTime,    index=True, default=datetime.utcnow, nullable=False)
    chats       = db.relationship('Chat',   backref='owner')
    
    def __repr__(self):
        return '<User {}>'.format(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(id)



class Chat(db.Model):
    id          = db.Column(db.Integer,    primary_key=True)
    user_id     = db.Column(db.String(32), db.ForeignKey('user.id'), nullable=False)
    title       = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(255))
    created_at  = db.Column(db.DateTime,   index=True, default=datetime.utcnow, nullable=False)
    is_live     = db.Column(db.Boolean,    default='false', nullable=False)

    def __repr__(self):
        return '<Chat {}>'.format(self.id)



### for use when you change to mysql
###https://docs.sqlalchemy.org/en/latest/core/compiler.html#utc-timestamp-function

##from sqlalchemy.sql import expression
##from sqlalchemy.ext.compiler import compiles
##from sqlalchemy.types import DateTime
##
##class utcnow(expression.FunctionElement):
##    type = DateTime()
##
##@compiles(utcnow, 'postgresql')
##def pg_utcnow(element, compiler, **kw):
##    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
##
##@compiles(utcnow, 'mssql')
##def ms_utcnow(element, compiler, **kw):
##    return "GETUTCDATE()"
### revision identifiers, used by Alembic.
##revision = '069ecf8ab0bb'
##down_revision = None
##branch_labels = None
##depends_on = None
##
##    Column("timestamp", DateTime, server_default=utcnow())