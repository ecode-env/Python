from flask import Flask, render_template
import requests


posts = requests.get("https://api.npoint.io/d9d504779f838de6e2b3").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry")
def receive_data():
    return ''



if __name__ == "__main__":
    app.run(debug=True, port=5001)
