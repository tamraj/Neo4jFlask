from flask import Flask, jsonify
from neo4j import GraphDatabase


uri = "bolt://18.234.106.185:36228"
driver = GraphDatabase.driver(uri, auth=("neo4j", "control-skirts-longitudes"))


app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    try:
        session = driver.session()
        query = "MATCH (n) where exists(n.address) Return Distinct 'node' as entity, n.address AS address LIMIT 25 UNION ALL MATCH ()-[r]-() WHERE EXISTS (r.address) Return Distinct 'relationship' AS entity, r.addess AS address"
        records = session.run(query)
        data = [dict(record)['address'] for record in records]
        return jsonify({'data': data})
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getAllBusinessCenters',methods=['POST','GET'])
def getBusinessCenters():
    try:
        session = driver.session()
        query = "MATCH (n:Business_Center) RETURN n"
        records = session.run(query)
        data = [dict(dict(i)['n'].items()) for i in records]
        return jsonify(data)
        # data = [dict(record)['address'] for record in records]
        # return jsonify({'data':data})
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getAllRoles',methods=['POST','GET'])
def getRoles():
    try:
        session = driver.session()
        query = "MATCH (n:Role) RETURN n"
        records = session.run(query)
        data = [dict(dict(i)['n'].items()) for i in records]
        return jsonify(data)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getAllPeople',methods=['POST','GET'])
def getPeople():
    try:
        session = driver.session()
        query = "MATCH (n:Person) RETURN n"
        records = session.run(query)
        data = [dict(dict(i)['n'].items()) for i in records]
        return jsonify(data)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithRole/<id>',methods=['POST','GET'])
def getPeopleWithRole(id):
    try:
        session = driver.session()
        query = "MATCH (:Role{name:'" + id + "'})<-[IS]-(Person) RETURN Person"
        records = session.run(query)
        data = [dict(dict(i)['Person'].items()) for i in records]
        return jsonify(data)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithBCenter/<id>',methods=['POST','GET'])
def getPeopleWithBCenter(id):
    try:
        session = driver.session()
        query = "MATCH (:Business_Center{bc_number:'" + id + "'})<-[Works_For]-(Person) RETURN Person"
        records = session.run(query)
        data = [dict(dict(i)['Person'].items()) for i in records]
        return jsonify(data)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithRoleUnderBCenter/<id>/<role>',methods=['POST','GET'])
def getPersonWithRoleUnderBCenter(id=None,role=None):
    try:
        session = driver.session()
        query = "MATCH (:Business_Center{bc_number:'" + id + "'})<-[WORKS_FOR]-(Person)-[:IS]->" \
                                                             "(:Role{name:'" + role + "'}) RETURN Person"
        records = session.run(query)
        data = [dict(dict(i)['Person'].items()) for i in records]
        return jsonify(data)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")


if __name__=='__main__':
    app.run(debug=True)