# from flask import Flask, render_template, request, redirect, url_for
#
#
#
# app = Flask(__name__)
#
# all_books = []
#
#
# @app.route('/')
# def home():
#     return render_template(template_name_or_list='index.html', books=all_books)
#
#
# @app.route("/add", methods=['POST','GET'])
# def add():
#     if request.method == 'POST':
#         all_books.append({
#             'title': request.form['name'],
#             'author': request.form['author'],
#             'rating': request.form['rate']
#         })
#         return redirect(url_for('home'))
#
#     return render_template('add.html')
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    balance: Mapped[float] = mapped_column(Float, default=0.0)

    def __repr__(self):
        return f'<Book {self.name}>'


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)