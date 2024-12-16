from flask import jsonify,Blueprint,request,render_template
from flask_sqlalchemy import SQLAlchemy

# MySQL / MariaDB
"mysql://scott:tiger@localhost/project"

db = SQLAlchemy()
class ClusterCheck(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    cluster_name: str = db.Column(db.String(100))
    platform: str = db.Column(db.String(100))
    status: str = db.Column(db.String(10))

api_maria = Blueprint('api_maria', __name__,)

@api_maria.route('/test',methods=['GET'])
def get_data():
    custer = db.session.query(ClusterCheck).all()
    re_custer = []
    for u in custer:
        temp = u.__dict__
        del temp["_sa_instance_state"]
        re_custer.append(temp)

    print(re_custer)
    return re_custer

@api_maria.route('/t',methods=['POST'])
def post_data():
    custer = db.session








    
    # custer = db.session.query(ClusterCheck).all()
    # re_custer = []
    # for u in custer:
    #     temp = u.__dict__
    #     temp["_sa_instance_state"] = ""
    #     re_custer.append(temp)

    # print(re_custer)
    # return re_custer
 




