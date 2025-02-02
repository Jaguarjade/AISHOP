from flask import Flask, render_template

# Ensure Flask looks in the "templates" folder
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html', products=[
        {'title': 'Product 1', 'price': '$10'},
        {'title': 'Product 2', 'price': '$20'}
    ])

if __name__ == "__main__":
    app.run(debug=True)
