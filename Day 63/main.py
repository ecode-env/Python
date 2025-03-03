from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Define Base class for SQLAlchemy
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with Base model class
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)



# Define Book model
class Book(db.Model):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

with app.app_context():
    db.create_all()

# Home route to display books
@app.route('/')
def home():
    all_books = db.session.query(Book).all()  # Retrieve all books from DB
    return render_template('index.html', books=all_books)

# Add new book route
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"])
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
