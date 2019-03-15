from flask import jsonify

def getPeople(driver):
    session = driver.session()
    query = "MATCH (n:Person) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)

def getPeopleWithRole(driver, id):
    session = driver.session()
    query = "MATCH (:Role{name:'"+id+"'})<-[IS]-(Person) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)

def getPeopleWithBCenter(driver, id):
    session = driver.session()
    query = "MATCH (:Business_Center{bc_number:'"+id+"'})<-[Works_For]-(Person) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)

def getPersonWithRoleUnderBCenter(driver, id=None,role=None):
    session = driver.session()
    query = "MATCH (:Business_Center{bc_number:'"+id+"'})<-[WORKS_FOR]-(Person)-[:IS]->" \
                                                     "(:Role{name:'"+role+"'}) RETURN Person"
    records = session.run(query)
    data = [dict(dict(i)['Person'].items()) for i in records]
    return jsonify(data)