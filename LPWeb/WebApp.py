from flask import Flask, jsonify, make_response
from flask import abort, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

#TODO:
#maybe add usernames?? I know how to do that
#Require authorization

#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#That's a blog I'm using for reference on how to make an API

#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
#That's a blog for implementing the SQL database

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)

#This is a fake set of data. We will need to 
#include a database for this to work
devices = [
    {
        'id': 1,
        'title': u'Rumbaaa',
        'done': False
    },
    {
        'id': 2,
        'title': u'Smart House',
        'done': False
    },
    {
        'id': 3,
        'title': u'Computer',
        'done': False
    },
    {
        'id': 4,
        'title': u'Something else',
        'done': False
    }
]
# class Devices(Resource):
#     def get(self):
#         return {'devices': devices} 

# class Device(Resource):
#     def get(self, device_id):

#curl -i <localhost_url>
@app.route('/', methods=['GET'])
def getDevices():
    return jsonify({'devices' : devices})

#Returns a specific device based on its id
@app.route('/<int:deviceId>', methods=['GET'])
def getDevice(deviceId):
    targetDevice = []
    for device in devices:
        if device.get('id') == deviceId:
            targetDevice.append(device)
    if len(targetDevice) == 0:
        abort(404)
    return jsonify({'devices': targetDevice})

#curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" <localhost_url>
##The above command isn't working right now, I'll figure it out later
@app.route('/', methods=['POST'])
def addDevice():
    #this will change when we get a new database
    #right now it is based off of my fake database
    if not request.json or not 'title' in request.json: 
        abort(400)
    addedDevice = {
        'id': devices[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    devices.append(addedDevice)
    return jsonify({'devices': addedDevice}), 201


# api.add_resource(Devices, '/')
# api.add_resource()

if __name__ == '__main__':
    app.run()
