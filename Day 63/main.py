from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()
    # Check if the book exists before adding
    if not Book.query.filter_by(title="Harry Potter").first():
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

@app.route('/')
def home():
    with app.app_context():
        all_books = Book.query.all()
    return render_template('index.html', books=all_books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            with app.app_context():
                book = Book(
                    title=request.form['title'],
                    author=request.form['author'],
                    rating=float(request.form['rating'])
                )
                db.session.add(book)
                db.session.commit()
            return redirect(url_for('home'))
        except ValueError:
            return "Error: Rating must be a number", 400
        except db.exc.IntegrityError:
            return "Error: This book title already exists", 400
    return render_template('add.html')



if __name__ == '__main__':
    app.run(debug=True)