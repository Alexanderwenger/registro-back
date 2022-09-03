"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
    

@api.route('/registro', methods=['POST'])
def registro():
    body = request.get_json()
    #coprobar si existe un usuario con mismo correo
    one_people = User.query.filter_by(email=body['email']).first()
    if one_people:
        return jsonify({"error": "ya existe"}),418
    else:
        usuarioNuevo = User(email=body['email'], password=body['password'], is_active=True) 
        db.session.add(usuarioNuevo)
        db.session.commit()
        return jsonify(body),201 # created



