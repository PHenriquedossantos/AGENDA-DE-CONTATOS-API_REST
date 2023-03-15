from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help='The field login cannot be left blank')
atributos.add_argument('senha', type=str, required=True, help='The field password cannot be left blank')

class User(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404
    
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted'}
        return {'message': 'User not found'}, 404
    
class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists".format(dados['login'])}
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'user created successfully'}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])
        if user and hmac.compare_digest(user.senha.encode('utf-8'), dados['senha'].encode('utf-8')):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}
        return {'message': 'The username or password is incorrect.'}, 401 # Não autorizado
    

class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT TOKEN IDENTIFIER
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully'}, 200
