from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


choices = []
# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    category = SelectField("Category", choices=choices, validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    link_url = StringField("Link Url", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up ")


# TODO: Create a LoginForm to login existing users
class LoginUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentPostForm(FlaskForm):
    body = CKEditorField("Comment",  validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
    

class addCategory(FlaskForm):
    category = StringField("Category", validators=[DataRequired()] )  
    submit = SubmitField("Add Category")  
