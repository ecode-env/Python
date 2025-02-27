from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/d9d504779f838de6e2b3"
all_posts = requests.get(url=blog_url).json()


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/post/<post_id>")
def post(post_id):
    selected_blog = [post for post in all_posts if post['id'] == int(post_id)][0]
    return render_template('post.html', posts=selected_blog)

if __name__ == "__main__":
    app.run(debug=True)