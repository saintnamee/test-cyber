from flask import Flask, render_template
from module.api_detail import api_mongo

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(api_mongo)

@app.route('/')
def home():
    return render_template('index.html', title="Home Page", message="Welcome to Flask!")

if __name__ == '__main__':
    app.run(debug=True)