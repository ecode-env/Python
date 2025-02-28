from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap4

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
    if form.validate_on_submit():
        print(type(form.password.data))
        if form.email.data == 'admin@email.com' and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template(template_name_or_list="login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
