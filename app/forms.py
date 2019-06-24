from flask_wtf          import FlaskForm
from wtforms            import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models         import User, Chat

class LoginForm(FlaskForm):
    id          = StringField(  'Tag',           validators=[DataRequired()])
    #username    = StringField(  'Username',      validators=[DataRequired()])
    password    = PasswordField('Password',      validators=[DataRequired()])
    remember_me = BooleanField( 'Remember Me')
    submit      = SubmitField(  'Sign In')
    #def __repr__(self):
    #    return '<login form \n\tid: {},\n\tusername: {} \n\tpassword: {}>'.format(self.id.data, self.username.data, self.password.data)


class RegistrationForm(FlaskForm):
    id        = StringField(  'Tag',             validators=[DataRequired()])
    username  = StringField(  'Username',        validators=[DataRequired()])
    email     = StringField(  'Email',           validators=[DataRequired(), Email()])
    password  = PasswordField('Password',        validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit    = SubmitField(  'Register')

    def validate_userid(self, id):
        user = User.query.filter_by(id=id.data).first()
        if user is not None:
            raise ValidationError('Please use a different tag.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username    = StringField(  'Username',    validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    submit      = SubmitField(  'Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class ChatCreateForm(FlaskForm):
    title       = StringField('Title',      validators=[DataRequired()])
    description = StringField('Description', validators=[])
    submit      = SubmitField('Create')
