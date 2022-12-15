from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Aryan Ali',
        'title': 'First Blog',
        'content': 'This is the first blog on my website',
        'date_posted': 'November 20, 20222, '
    },
    {
        'author': 'Aditya Tiwari',
        'title': 'Second Blog',
        'content': 'This is my second blog on this website',
        'date_posted': 'November 25, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
