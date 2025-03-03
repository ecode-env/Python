from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6tykiu9oiuO6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_list.db"
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):

    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[int] = mapped_column(Integer)
    img_url: Mapped[str] = mapped_column(String)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


class From(FlaskForm):
    rating = StringField(label='Your Rating out of 10, eg. 7.5')
    review = StringField(label='Your Review')
    submit = SubmitField(label='Done')


@app.route("/edit", methods= ["GET", "POST"])
def edit():
    form = From()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if not movie_id:
        return redirect(url_for('home'))


    if request.method == 'POST':
        rating = request.form.get('rating')
        review = request.form.get('review')
        movie.rating= float(rating)
        movie.review=review

        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
