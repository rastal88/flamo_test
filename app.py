from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
users = db['users']


@app.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    username = user_data.get('username')
    email = user_data.get('email')
    user_id = users.insert_one({'username': username, 'email': email}).inserted_id
    return jsonify({'message': 'Пользователь создан успешно', 'user_id': str(user_id)}), 201


if __name__ == '__main__':
    app.run(debug=True)
