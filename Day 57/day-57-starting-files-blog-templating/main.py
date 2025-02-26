from flask import Flask, render_template
import requests



app = Flask(__name__)
blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
all_posts = requests.get(url=blog_url).json()

@app.route('/')
def home():
    return render_template(template_name_or_list='index.html', posts=all_posts)

@app.route('/post/<num>')
def post(num):
    filtered_posts = [post for post in all_posts if str(post['id']) == num]
    return render_template(template_name_or_list='post.html', posts=filtered_posts)

if __name__ == "__main__":
    app.run(debug=True)
