from flask import Flask, jsonify
from neo4j import GraphDatabase
import config

uri = config.getNeo4jUri()
driver = GraphDatabase.driver(uri, auth=(config.username, config.password))


app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    session = driver.session()
    query = "MATCH (n) where exists(n.address) Return Distinct 'node' as entity, n.address AS address LIMIT 25 UNION ALL MATCH ()-[r]-() WHERE EXISTS (r.address) Return Distinct 'relationship' AS entity, r.addess AS address"
    records = session.run(query)
    data = [dict(record)['address'] for record in records]
    return jsonify({'data':data})

@app.route('/getAllBusinessCenters',methods=['POST','GET'])
def getBusinessCenters():
    session = driver.session()
    query = "MATCH (n:Business_Center) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)
    #data = [dict(record)['address'] for record in records]
    #return jsonify({'data':data})

@app.route('/getAllRoles',methods=['POST','GET'])
def getRoles():
    session = driver.session()
    query = "MATCH (n:Role) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)

@app.route('/getAllPeople',methods=['POST','GET'])
def getPeople():
    session = driver.session()
    query = "MATCH (n:Person) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)

@app.route('/getPersonWithRole/<id>',methods=['POST','GET'])
def getPeopleWithRole(id):
    session = driver.session()
    query = "MATCH (:Role{name:'"+id+"'})<-[IS]-(Person) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)

@app.route('/getPersonWithBCenter/<id>',methods=['POST','GET'])
def getPeopleWithBCenter(id):
    session = driver.session()
    query = "MATCH (:Business_Center{bc_number:'"+id+"'})<-[Works_For]-(Person) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)

@app.route('/getPersonWithRoleUnderBCenter/<id>/<role>',methods=['POST','GET'])
def getPersonWithRoleUnderBCenter(id=None,role=None):
    session = driver.session()
    query = "MATCH (:Business_Center{bc_number:'"+id+"'})<-[WORKS_FOR]-(Person)-[:IS]->" \
                                                     "(:Role{name:'"+role+"'}) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)