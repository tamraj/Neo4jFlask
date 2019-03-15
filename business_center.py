from flask import jsonify

def getBusinessCenters(driver):
    session = driver.session()
    query = "MATCH (n:Business_Center) RETURN n"
    records = session.run(query)
    data = [dict(dict(i)['n'].items()) for i in records]
    return jsonify(data)
    #data = [dict(record)['address'] for record in records]
    #return jsonify({'data':data})
