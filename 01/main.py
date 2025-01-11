from flask import Flask, render_template
app = Flask(__name__)

titleWeb = "FlaskKu"

data1 = ["I", "G", "S"]

data = [
    {
        'author' : 'God',
        'content' : 'MY LOVE STORY WITH JO YURI',
        'date' : '9 Jan 2025'
    },
    { 
        'author' : 'Creator',
        'content' : 'MY LOVE STORY WITH JANG WONYOUNG',
        'date' : '9 Jan 2022'
    }
]

bio = {
        "name": "Jonathan Alvino",
        "age": 16,
        "profession": "jobless rn",
        "hobbies": ["makan", "tedok", "halu"]
    }

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', titleWeb = titleWeb, data=data, usia = 20, bio=bio )

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/content")
def content():
    return render_template('content.html')

@app.route("/igs")
def igs():
    return render_template('igs.html', data=data1)



if __name__ == '__main__':
    app.run(debug=True)