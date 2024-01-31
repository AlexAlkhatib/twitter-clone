from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/anasa/OneDrive/Bureau/twitter-clone/engage.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ksdlfkdsofidsithnaljnfadksjhfdskjfbnjewrhewuirhfsenfdsjkfhdksjhfdslfjasldkj'

configure_uploads(app, photos)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(30), unique=True)
    image = db.Column(db.String(100))  # Add column for image path
    password = db.Column(db.String(50))

login_manager = LoginManager(app)  # Initialize LoginManager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_session():
    engine = db.engine  # Access the engine within context
    Session = sessionmaker(bind=engine)
    return Session()

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    image = FileField('Profile Image', validators=[
        FileAllowed(photos, 'Images only!')
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')

@app.route('/')
def index():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>Username: {}, Password: {}, Remember: {}</h1>'.format(form.username.data, form.password.data, form.remember.data)

    return render_template('index.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            return 'Login failed'

        if check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            return redirect(url_for('profile'))

        return 'Login failed'

    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = create_session()

        # Save the uploaded image
        filename = photos.save(form.image.data)
        image_url = url_for('uploaded_file', filename=filename)

        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        new_user = User(
            name=form.name.data,
            username=form.username.data,
            password=hashed_password,
            image=image_url
        )
        session.add(new_user)
        session.commit()

        # Redirect to the profile route
        return redirect(url_for('profile'))

    return render_template('register.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    app.run(debug=True)
