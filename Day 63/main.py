from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template(template_name_or_list='index.html', books=all_books)


@app.route("/add", methods=['POST','GET'])
def add():
    if request.method == 'POST':
        all_books.append({
            'title': request.form['name'],
            'author': request.form['author'],
            'rating': request.form['rate']
        })
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

