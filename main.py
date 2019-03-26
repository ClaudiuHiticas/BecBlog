from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Adi',
        'title': 'Blog post 1',
        'content': 'This is the first post!',
        'date_posted': 'Match 26, 2019'
    },
    {
        'author': 'Clau',
        'title': 'Blog post 2',
        'content': 'This is the second post!',
        'date_posted': 'Match 26, 2019'
    },
    {
        'author': 'Sebi',
        'title': 'Blog post 3',
        'content': 'This is the third post!',
        'date_posted': 'Match 26, 2019'
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