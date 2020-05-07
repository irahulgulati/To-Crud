from api import application, jsonify, request, make_response
from .database import Product, patient_schema, patients_schema, db, ma
from redis import StrictRedis
import hashlib
import json
# initializing redis instance
redis = StrictRedis(host='redis', port=6379,
                    charset="utf-8", decode_responses=True)

# create a patient's record
@application.route('/api/patients', methods=['POST'])
def createPatient():
    """ 
    Below code will construct a dictonary with recieved variables in request
    and will cache the record into redis memory
    """
    _tmpDict = {
        "name": request.json['name'],
        "location": request.json['location'],
        "streetname": request.json['streetname'],
        "status": request.json['status']
    }
    hash = "id_" + hashlib.md5(str.encode(_tmpDict["name"])).hexdigest()
    if redis.exists(hash) == 0:
        print("creating cache entry")
        redis.set(hash, json.dumps(_tmpDict), 120)
        return jsonify(_tmpDict)
    else:
        print("exist")
        return jsonify({'name': 'patient already exists'})

    """ 
    Below code will make a batch request to store records from redis cache
    to database i.e. dbsqlite/postgres dependening on the environment(Dev/Prod)
    """
    # name = request.json['name']
    # location = request.json['location']
    # streetname = request.json['streetname']
    # status = request.json['status']
    # new_product = Product(name, location, streetname, status)
    # if db.session.query(Product).filter(Product.name == name).count() == 0:
    #     db.session.add(new_product)
    #     db.session.commit()
    #     return patient_schema.jsonify(new_product)
    # else:
    #     return jsonify({'name': 'patient already exists'})

# get all records of patients stored in database
@application.route('/api/patients', methods=['GET'])
def getPatients():
    cachedResults = redis.keys()
    if not cachedResults:
        all_Products = Product.query.all()
        result = patients_schema.dump(all_Products)
        for resu in result:
            hash = "id_" + hashlib.md5(str.encode(resu["name"])).hexdigest()
            print(hashlib.md5(str.encode(resu["name"])).hexdigest())
            redis.set(hash, json.dumps(resu), 120)
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(redis.mget(cachedResults)), 202)

# #get only one record, to use it, this feature needs to implemented in frontend first
# @application.route('/api/patients/<int:id>', methods=['GET'])
# def getPatient(id):
#     _Product=Product.query.get(id)
#     return patient_schema.jsonify(_Product)

# update a patient record to use it, this feature needs to implemented in frontend first
# @application.route('/api/patients/<int:id>', methods=['PUT'])
# def updatePatient(id):
#     getRecord=Product.query.get(id)
#     getRecord.name=request.json['name']
#     getRecord.location=request.json['location']
#     getRecord.streetname=request.json['streetname']
#     getRecord.status=request.json['status']
#     db.session.commit()

# delete a patient record
@application.route('/api/patients/<int:id>', methods=['DELETE'])
def deletePatient(id):
    checkRecord = Product.query.filter_by(id=id).count()
    if checkRecord != 0:
        getRecord = Product.query.get(id)
        db.session.delete(getRecord)
        db.session.commit()
        return jsonify({'msg': 'Patient Record deleted'})
    else:
        return jsonify({'msg': 'Patient does not exists'})
