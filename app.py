from flask import Flask, request
from neo4j import GraphDatabase
import config
import business_center
import role
import people

uri = config.getNeo4jUri()
driver = GraphDatabase.driver(uri, auth=(config.username, config.password))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Success"

@app.route('/getAllBusinessCenters',methods=['GET'])
def getBusinessCenters():
    return business_center.getBusinessCenters(driver)

@app.route('/getAllRoles',methods=['GET'])
def getRoles():
    return role.getRoles(driver)

@app.route('/getAllPeople',methods=['GET'])
def getPeople():
    return people.getPeople(driver)

@app.route('/getPersonWithRole/<id>',methods=['GET'])
def getPeopleWithRole(id):
    return people.getPeopleWithRole(driver, id)

@app.route('/getPersonWithBCenter/<id>',methods=['GET'])
def getPeopleWithBCenter(id):
    return people.getPeopleWithBCenter(driver, id)

@app.route('/getPersonWithRoleUnderBCenter/<id>',methods=['GET'])
def getPersonWithRoleUnderBCenter(id=None):
    role = request.args.get('role')
    return people.getPersonWithRoleUnderBCenter(driver, id, role)

if __name__=='__main__':
    app.run(debug=True)