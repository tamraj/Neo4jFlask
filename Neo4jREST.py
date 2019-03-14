from flask import Flask, jsonify
from neo4j import GraphDatabase


uri = "bolt://18.234.106.185:36228"
driver = GraphDatabase.driver(uri, auth=("neo4j", "control-skirts-longitudes"))


app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    session = driver.session()
    query = "MATCH (n) where exists(n.address) Return Distinct 'node' as entity, n.address AS address LIMIT 25 UNION ALL MATCH ()-[r]-() WHERE EXISTS (r.address) Return Distinct 'relationship' AS entity, r.addess AS address"
    records = session.run(query)
    data = [dict(record)['address'] for record in records]
    return jsonify({'data':data})

app.run(debug=True)