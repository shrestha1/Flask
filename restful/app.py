from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

bulbs = []

bulb = {"bulb_id":1,
        "of_room":"kitchen",
        "status":"ON"
        }

class BulbItem(Resource):
    '''
    lets you get bulb by id
    '''

    def get(self, bulb_id):
        return {"data":[bulb for bulb in bulbs if bulb["bulb_id"]==int(bulb_id)]}


class BulbList(Resource):
    '''
    Lets you add bulb and get all bulbs 
    '''
    def get(self):
            
        return {"data":bulbs}

    def post(self):
        """
         For adding the bulb
        """
        new_bulb = request.get_json(force=True)
        bulbs.append(new_bulb)
        return new_bulb



api.add_resource(BulbItem, '/api/bulb/<bulb_id>')
api.add_resource(BulbList, '/api/bulb')


if __name__ == '__main__':
    app.run(debug=True)