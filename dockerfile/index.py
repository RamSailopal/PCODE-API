from flask import Flask, request, jsonify
import json, os, yottadb, time
app = Flask(__name__)

@app.route('/pcode', methods=['GET'])
def user():

    if request.method == 'GET':
       pcode = request.args.get('pcode',type=str)
       key=yottadb.Key("^PCODE")[pcode]
       if (key.get() == None ):
          lat = "Not found"
          lng = "Not found"
       else :
          dat = key.get().decode()
          datbit = dat.split(",")
          lng = datbit[1]
          lat = datbit[0]
       json_data = []
       content = {}
       content = {'pcode': pcode, 'long': lng, 'lat': lat }
       json_data.append(content)
       return(jsonify(json_data))
