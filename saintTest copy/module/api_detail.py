from flask import jsonify,Blueprint,request,render_template
from datetime import datetime
from module.model_detail import connect_mongodb
from response import handle_response

api_mongo = Blueprint('api_mongo', __name__,)

@api_mongo.route('/api/v1/api_mongo', methods=['GET'])
def api_mongo_get():
    # return jsonify ({"meseges":"heelo"}),200
    try:
        args = request.args
        hospital_name = args.get('hospital_name')
        raw_tags = args.get('raw_tags')
        
        client = connect_mongodb()
        database = client["SaintTest"]
        collection = database["mini"] # not the samwe
        
        # rows = collection.find(
        #     {"$and":[
        #         {"hospital_name": hospital_name}]}, {"_id":0,"create_date":0}
        #     ).sort([("create_date", 1)]) # 1 = 0>9 , -1 = 9>0 
        # #if (hospital_name is None );    
       
        rows = collection.find({},{"_id":0})
        #     # {"$and":[
        #     #     {"last_name": lastname}, {"gender": gender}]}, {"_id":0}
        #     # ).sort([("created_date", 1)])
        
        result = list(rows)

        # print (result)
        # # Clean data
        # for row in rows:
        #     row['_id'] = str(row['_id'])
        
        return handle_response(200, "Query Success", result)
    
    except Exception as error:
        print(repr(error))
        return handle_response(500, 'Server error')
    
@api_mongo.route('/api/v1/api_mongo', methods=['POST'])
def api_mongo_insert():
    '''insert with body'''
    try:
        body = request.json
        
        hospital_name = body['hospital_name']
        raw_tags = body['raw_tags']
        hid = body.get("hid","-")

        cluster = connect_mongodb()
        database = cluster["SaintTest"]
        collection = database["mini"]
        
        created_date = datetime.now()
        updated_date = datetime.now()
        
        newValues = {"hospital_name": hospital_name, "raw_tags": raw_tags,"hid": hid,
                     "created_date" : created_date, "updated_date" : updated_date}

        insert = collection.insert_one(newValues)
        print(insert.inserted_id)

        return handle_response(201, 'insert success')
    
    except Exception as error:
        print(repr(error))
        return handle_response(500, 'Server error')
    
@api_mongo.route('/api/v1/api_mongo', methods=['PUT'])
def api_mongo_update():
    try:
        body = request.json
        
        hospital_name = body['hospital_name']
        raw_tags = body['raw_tags']
        hid = body.get("hid","-")

        cluster = connect_mongodb()
        database = cluster["SaintTest"]
        collection = database["mini"]
        
        updated_date = datetime.now()
        
        # filter = {'email': email}
        # filter = ({'_id': ObjectId(key)})
        # updated_date = datetime.now()
        
        newValues = {"hospital_name": hospital_name, "raw_tags": raw_tags,"hid": hid,
                     "created_date" : created_date, "updated_date" : updated_date}

        update = collection.update_one(filter, {"$set": newValues})
        print(update.matched_count)
        
        return handle_response(200, 'update success')
    
    except Exception as error:
        print(repr(error))
        return handle_response(500, 'Server error')


@api_mongo.route('/api/v1/api_mongo', methods=['DELETE'])
def api_mongo_delete():
    try:
        body = request.json
        
        # key = body['key']
        hospital_name = body['hospital_name']
        raw_tags = body['raw_tags']
        hid = body.get("hid","-")

        cluster = connect_mongodb()
        database = cluster["SaintTest"]
        collection = database["mini"]
        
        # filter = ({'_id': ObjectId(key)})
        filter = {"$and": [{"email" : email} ] } # filter by key
        delete = collection.delete_one(filter)
        print(delete.deleted_count)
        
        return handle_response(200, 'delete success')

    except Exception as error:
        print(repr(error))
        return handle_response(500, 'Server error') 

@api_mongo.route('/api/v1/api_datetime', methods=['GET'])
def home():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('datetime.html', date=current_date)

