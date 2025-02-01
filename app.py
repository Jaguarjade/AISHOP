from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', products=[
        {"title": "Wireless Earbuds", "price": "$59.99", "url": "https://www.affiliate-link.com/earbuds", "image_url": "earbuds.jpg"},
        {"title": "Smart Watch", "price": "$99.99", "url": "https://www.affiliate-link.com/watch", "image_url": "watch.jpg"}
    ])

if __name__ == '__main__':
    app.run(debug=True)
