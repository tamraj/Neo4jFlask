from flask import jsonify

def getRoles(driver):
    session = driver.session()
    query = "MATCH (n:Role) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)