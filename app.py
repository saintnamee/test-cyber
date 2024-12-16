from flask import Flask, render_template
from module.query import db,api_maria
#from module.api_detail import api_mongo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:w,ji^hlb0Ut@203.151.154.99/resource_planning_detail"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# Register Blueprint
app.register_blueprint(api_maria)

@app.route('/')
def home():
    return render_template('index.html', title="Home Page", message="Welcome to Flask!")

if __name__ == '__main__':
    app.run(debug=True)