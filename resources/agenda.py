from flask_restful import Resource, reqparse
from models.agenda import AgendaModel


class Agenda(Resource):
    def get(self):
        return {'agenda': [contato.json() for contato in AgendaModel.query.all()]}

class Contato(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('numero')
    argumentos.add_argument('email')
    argumentos.add_argument('cidade')


    def get(self, agenda_id):
        contato = AgendaModel.find_agenda(agenda_id)
        if contato:
            return contato.json()
        return {'message': 'contato not found'}, 404

    def post(self, agenda_id):
        if AgendaModel.find_agenda(agenda_id):
            return {"message": "agenda id '{}' already exists.".format(agenda_id)}, 400

        dados = Contato.argumentos.parse_args()
        contato = AgendaModel(agenda_id, **dados)
        try:
            contato.save_agenda()
        except:
            return {'message': 'An internal error ocurred trying to save contato'}, 500 # Internal Server Error
        return contato.json()

    def put(self, agenda_id):
        dados = Contato.argumentos.parse_args()
        contato_encontrado = AgendaModel.find_agenda(agenda_id)
        if contato_encontrado:
            contato_encontrado.update_contato(**dados)
            contato_encontrado.save_agenda()
            return contato_encontrado.json(), 200
        contato = AgendaModel(agenda_id, **dados)
        try:
            contato.save_agenda()
        except:
            return {'message': 'An internal error ocurred trying to save contato'}, 500 # Internal Server Error
        return contato.json(), 201


    def delete(self, agenda_id):
        contato = AgendaModel.find_agenda(agenda_id)
        if contato:
            try:
                contato.delete_contato()
            except:
                return {'message': 'An error ocurred trying to delete contato'}, 500
            return {'message': 'Contato deleted.'}
        return {'message': 'Contato not found'}, 404