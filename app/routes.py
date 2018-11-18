from datetime           import datetime
from flask              import render_template, flash, redirect, url_for, request
from flask_login        import current_user, login_user, logout_user, login_required
from werkzeug.security  import generate_password_hash
from werkzeug.urls      import url_parse
from app                import app, db
from app.forms          import LoginForm, RegistrationForm, EditProfileForm
from app.models         import User
import sys
 
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/terms')
def terms():
    return render_template('termsOfService.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid tag or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(id=form.id.data, name=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data))
        #user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route('/index')
def index():
    return 'index page. This is yet to be defined.'


@app.route('/user/<id>')
@login_required
def user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('user.html', user=user)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('userIndex.html', users=users)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.name     = form.username.data
        current_user.description = form.description.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', id=current_user.id))
    elif request.method == 'GET':
        form.username.data = current_user.name
        form.description.data = current_user.description
    return render_template('userEdit.html', title='Edit Profile',
                           form=form) 