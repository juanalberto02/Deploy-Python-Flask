# API using flask_restful
from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
from flask_cors import CORS
import random 

app = Flask(__name__)
api = Api(app)
CORS(app)

list_kata = ["Kamu botak", "Tidurlah-tidurlah", "uang, uang, uang", "aku senang, aku senang", "Aku benci semua orang", "Aku wumbo, kau wumbo", "Betul, betul, betul", "Itik labih sedap oooo", "Sendirian, sendirian, sendirian", "Aku suka uang"]
class Home(Resource):
    def get(self):
        acak = random.choice(list_kata)
        return acak

class Hello(Resource):
    def get(self, name):
        return (name+","+random.choice(list_kata))
class Masuk(Resource):
    def post(self):
        if not request.json or 'nama' not in request.json:
            return jsonify({"pesan" : "Error: No id field provided"})
        name = request.json["nama"]

        return "Selamat datang,"+  name + ", anda berhasil masuk ke Puja Kerang Ajaib"

api.add_resource(Home, '/')
api.add_resource(Hello, '/<name>')
api.add_resource(Masuk, '/Masuk')

if __name__ == "__main__":
    app.run(host='0.0.0.0')