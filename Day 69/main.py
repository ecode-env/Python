from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from forms import CreatePostForm



# abb
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donxcrtvybuijojzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# generate avatar image
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):

    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship(argument="User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")




# Create a User table for all your registered users.
class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

    posts = relationship(argument="BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

# New table for the database
class Comment(db.Model):

    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))

    comment_author = relationship("User", back_populates="comments")
    parent_post = relationship("BlogPost", back_populates="comments")

with app.app_context():
    db.create_all()


# Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        # if the email exist pop up error
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if result:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        # hash the password interned from user

        hash_password = generate_password_hash(
            request.form.get('password'),
            method='scrypt',
            salt_length=16
        )
        #create new user
        new_user = User(
            name=request.form.get('name'),
            email =  request.form.get('email'),
            password=hash_password
        )
        # save into db
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for('get_all_posts'))

    return render_template(template_name_or_list="register.html", form=form)


# Retrieve a user from the database based on their email.
@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = db.session.execute(db.select(User).filter_by(email=email)).scalar()

        if not user:
            flash("That email does not exist, please try again.", "danger")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.', "danger")
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=form)

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


# logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

# home page
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template(template_name_or_list="index.html",
                           all_posts=posts,
                           logged_in=current_user.is_authenticated,
                           )


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods= ['GET','POST'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You need to login or register to comment.')
            return redirect(url_for('login'))

        new_comment = Comment(
            text=comment_form.comment.data,
            author_id=current_user.id,
            parent_post=requested_post
        )


        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html",
                           post=requested_post,
                           form=comment_form,
                           current_user=current_user
                           )


# Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# about route
@app.route("/about")
def about():
    return render_template("about.html")

# contatct route
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
