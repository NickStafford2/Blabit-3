from datetime           import datetime
from flask              import render_template, flash, redirect, url_for, request
from flask              import jsonify
from flask_login        import current_user, login_user, logout_user, login_required
from werkzeug.security  import generate_password_hash
from werkzeug.urls      import url_parse
from app                import app, db
from app.forms          import LoginForm, RegistrationForm, EditProfileForm, ChatCreateForm
from app.models         import User, Chat
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
    print('logout called')
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



@app.route('/user/<id>')
#@login_required
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

@app.route('/subscribe/<id>')
@login_required
def subscribe(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        flash('Can not subscribe. User {} not found.'.format(id))
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot subscribe yourself!')
        return redirect(url_for('user', id=id))
    current_user.subscribeTo(user)
    db.session.commit()
    flash('You are subscribed to {}!'.format(id))
    return redirect(url_for('user', id=id))

@app.route('/unsubscribe/<id>')
@login_required
def unsubscribe(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        flash('User {} not found.'.format(id))
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot unsubscribe yourself!')
        return redirect(url_for('user', id=id))
    current_user.unsubscribeFrom(user)
    db.session.commit()
    flash('You are not subscribed to {}.'.format(id))
    return redirect(url_for('user', id=id))


@app.route('/chats')
def chats():
    chats = Chat.query.all()
    return render_template('chatIndex.html', chats=chats)

@app.route('/chat/<id>')
#@login_required
def chat(id):
    #print('view chat called')

    chat = Chat.query.filter_by(id=id).first_or_404()
    #print(type(chat.id))
    #chat = jsonify(chat)

    return render_template('chat.html', chat=chat)

@login_required
@app.route('/create_chat', methods=['GET', 'POST'])
def create_chat():
    #print('create chat called')
    form = ChatCreateForm()
    if form.validate_on_submit():
        #print('validated')
        chat = Chat(user_id=current_user.id, title=form.title.data, description=form.description.data)
        #print(chat)
        #print('chat created')
        #chat.set
        db.session.add(chat)
        db.session.commit()
        flash('new chat created')
        #return 'chat finished'
        return redirect(url_for('chat', id=chat.id))
    return  render_template('chatCreate.html', title='create chat', form=form)

@login_required
@app.route('/chat_delete/<id>')  
def chat_delete(id):
    chat = Chat.query.filter_by(id=id).first_or_404()
    if current_user == chat.user_id:
        db.session.delete(chat)
        db.session.commit()
        flash('chat deleted')
    else:
        print('illegal delete')
        flash('This is not your chat. login to delete it')
    return redirect(url_for('home'))

@login_required
#@app.route('/chat_setLive/<id>/<liveStatus>')  
@app.route('/chat_setLive', methods=['POST'])
def chat_setLive(id, liveStatus):
    print('liveStatus called')
    return 'liveStatus called'
    #print(type(liveStatus))
    #if type(liveStatus) is bool:
    #    chat = Chat.query.filter_by(id=id).first_or_404()
    #    chat.setLiveStatus(liveStatus)
    #else:
    #    return 'liveStatus must be a Boolean'
    #return redirect(url_for('chat', id=chat.id))
