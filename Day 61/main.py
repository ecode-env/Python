from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email format. Must contain '@' and '.'")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')



app = Flask(__name__)
app.secret_key = 'b_5#y2L"F4Q8z:{}]/'


@app.route("/")
def home():
    return render_template('index.html')

@app.route(rule="/login", methods=['POST','GET'])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
