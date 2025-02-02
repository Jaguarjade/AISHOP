from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")  # Explicitly set template folder

@app.route('/')
def home():
    return render_template('index.html', products=[
        {'title': 'Product 1', 'price': '$10'},
        {'title': 'Product 2', 'price': '$20'}
    ])

if __name__ == "__main__":
    app.run(debug=True)