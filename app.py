from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.json_util import dumps
import json

app = Flask(__name__)

client = MongoClient("localhost", 27017)

## Creating database
db = client['datacampdb']
articles = db.articles

'''''
article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]
            }

#Insert Document

result = articles.insert_one(article)

print("First article key: {}".format(result.inserted_id))
print(db.list_collection_names())
'''''

'''''
##Insert Many
article1 = {"author": "Emmanuel Kens",
            "about": "Knn and Python",
            "tags":
                ["Knn","pymongo"]}
article2 = {"author": "Daniel Kimeli",
            "about": "Web Development and Python",
            "tags":
                ["web", "design", "HTML"]}
new_articles = articles.insert_many([article1,article2])
print("The name article IDs are {}".format(new_articles.inserted_ids))
'''''

##Retrieving single Document with find_one()
'''''
for article in articles.find():
    print(article)

'''''

'''''
for article in articles.find({},{"_id":0,"author":1,"about":1}).sort("author", -1):
    print(article)
'''''


### Deleting the

@app.route('/framework', methods=['GET'])
def getframe():
    output = []

    for q in articles.find():
        output.append({'author': q['author']})

    return jsonify({'result': output})


@app.route('/lang', methods=['POST'])
def addOne():

    author = request.json['author']

    data_id = articles.insert_one({'author': author}).inserted_id

    data = articles.find_one({'_id': data_id})

    output = {'author': data['author']}

    return jsonify({'result': output})


    '''''
    data = request.get_json()
    author = data['author']

    return jsonify({'result': 'successful!', 'author': author})
    '''''


    '''''
    try:
        data = json.loads(request.data)
        user_name = data['author']
        if user_name:
            status = articles.insert_one({
                "author": user_name
            })
        return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})
    '''''


if __name__ == '__main__':
    app.run(debug=True)
