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
    try:
        return business_center.getBusinessCenters(driver)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getAllRoles',methods=['GET'])
def getRoles():
    try:
        return role.getRoles(driver)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getAllPeople',methods=['GET'])
def getPeople():
    try:
        return people.getPeople(driver)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithRole/<id>',methods=['POST','GET'])
def getPeopleWithRole(id):
    try:
        return people.getPeopleWithRole(driver, id)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithBCenter/<id>',methods=['POST','GET'])
def getPeopleWithBCenter(id):
    try:
        return people.getPeopleWithBCenter(driver, id)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")

@app.route('/getPersonWithRoleUnderBCenter/<id>',methods=['POST','GET'])
def getPersonWithRoleUnderBCenter(id=None):
    try:
        role = request.args.get('role')
        return people.getPersonWithRoleUnderBCenter(driver, id, role)
    except(ValueError, KeyError, TypeError):
        print("Some error which you'll need to debug")


if __name__=='__main__':
    app.run(debug=True)