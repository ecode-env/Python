from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6tykiu9oiuO6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate(app, db)

# create the app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_list.db"
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):

    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer,nullable=True)
    description: Mapped[str] = mapped_column(String ,nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[int] = mapped_column(Integer, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    #all_movies = db.session.execute(select(Movie).order_by(Movie.rating)).scalars().all()
    all_movies = db.session.execute(select(Movie).order_by(Movie.rating.desc())).scalars().all()

    for index, movie in enumerate(all_movies, start=1):
        movie.ranking = index
    db.session.commit()


    return render_template("index.html", movies=all_movies)


class MovieFrom(FlaskForm):

    rating = StringField(label='Your Rating out of 10, eg. 7.5')
    review = StringField(label='Your Review')
    submit = SubmitField(label='Done')


@app.route("/edit", methods= ["GET", "POST"])
def edit():

    form = MovieFrom()
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


class AddMovie(FlaskForm):

    title = StringField(label='Movie Title')
    add_btn = SubmitField(label='Add Movie')


@app.route('/add', methods=['POST', 'GET'])
def add():

    url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODEyZjk0MWQyZTA5NDlkODYyOGE4ZWVjNTcyYjU2MSIsIm5iZiI6MTcyODA1NTY4Ni40OTksInN1YiI6IjY3MDAwOTg2NzgzMGMxMzAxZTdjYzg0NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cEpmiZJ_QotkxMMz3bztiDZKbHL9exFfWn2Z6bxr_xQ"
    }

    if request.method == 'POST':

        search_movie = {
            "query": request.form.get('title')
        }

        response = requests.get(url, headers=headers, params=search_movie)
        result = response.json()['results']

        return render_template('select.html', movie_list=result)

    if request.args.get('id'):

        movie_id = int(request.args.get('id'))

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODEyZjk0MWQyZTA5NDlkODYyOGE4ZWVjNTcyYjU2MSIsIm5iZiI6MTcyODA1NTY4Ni40OTksInN1YiI6IjY3MDAwOTg2NzgzMGMxMzAxZTdjYzg0NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cEpmiZJ_QotkxMMz3bztiDZKbHL9exFfWn2Z6bxr_xQ"
        }

        response = requests.get(url, headers=headers).json()
        year = int(response['release_date'].split('-')[0])
        print(year)
        new_movie = Movie(
            title=response['title'],
            img_url=f"https://image.tmdb.org/t/p/original{response['poster_path']}",
            year=year,
            description=response['overview'],
            rating=None,
            ranking=None,
            review=None
        )

        db.session.add(new_movie)
        db.session.commit()

        movie = Movie.query.filter_by(title=response['title']).first()

        return redirect(url_for("edit", id=movie.id))


    add_movie = AddMovie()
    return render_template('add.html', add=add_movie)


@app.route('/remove')
def remove():

    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if movie:

        db.session.delete(movie)
        db.session.commit()
        flash(message="Movie deleted successfully")

        return redirect(url_for('home'))


    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)
