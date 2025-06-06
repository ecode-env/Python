from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a RegisterForm to register new users
class RegisterForm(FlaskForm):

    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='email', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Create a LoginForm to login existing users

class LoginForm(FlaskForm):

    email = StringField(label='email', validators=[DataRequired()])
    password = StringField(label='password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Create a CommentForm so users can leave comments below posts

class CommentForm(FlaskForm):

    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
