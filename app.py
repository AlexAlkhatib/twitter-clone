from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_bcrypt import Bcrypt  # Import Flask-Bcrypt
from forms import RegisterForm

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
bcrypt = Bcrypt(app)  # Initialize Flask-Bcrypt

app.config['UPLOADED_PHOTOS_DEST'] = 'images'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/anasa/OneDrive/Bureau/twitter-clone/engage.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ksdlfkdsofidsithnaljnfadksjhfdskjfbnjewrhewuirhfsenfdsjkfhdksjhfdslfjasldkj'

configure_uploads(app, photos)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(30))
    image = db.Column(db.String(100))  # Add column for image path
    password = db.Column(db.String(100))  # Increase length for hashed password

def create_session():
    engine = db.engine  # Access the engine within context
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/')
def index():
    return render_template('index.html')

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

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Save the uploaded image
        filename = photos.save(form.image.data)
        image_url = url_for('uploaded_file', filename=filename)

        new_user = User(
            name=form.name.data,
            username=form.username.data,
            password=hashed_password,  # Store hashed password
            image=image_url  
        )
        session.add(new_user)
        session.commit()

        # Render the template directly
        return render_template('registration_result.html',
                               name=form.name.data,
                               username=form.username.data,
                               password="Hashed Password",  # Display hashed password
                               image_url=image_url)

    return render_template('register.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    app.run(debug=True)