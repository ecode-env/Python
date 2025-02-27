from flask import Flask, render_template, request
import requests
import smtplib



posts = requests.get("https://api.npoint.io/d9d504779f838de6e2b3").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# SOLUTION to Challenge:
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        try:
            name = data["name"]
            email = data["email"]
            phone = data["phone"]
            message = data["message"]

            email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            message_handler(email_body)

            return render_template("contact.html", successfull="Successfully sent your message")
        except KeyError:
            pass
        except Exception:
            pass

    return render_template("contact.html")


def message_handler(message):
    my_gmail = 'eyobbmulugeta@gmail.com'
    password = 'ftgpfxwyebrazxdf'
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs='maranataa10@gmail.com',
                msg=f"Subject: New Contact Form Submission\n\n{message}"
            )
    except Exception:

        pass

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True)