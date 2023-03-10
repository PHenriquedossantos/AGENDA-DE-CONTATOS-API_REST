from sql_alchemy import banco

class AgendaModel(banco.Model):

    __tablename__ = 'agenda'

    agenda_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(50), nullable=False)
    numero = banco.Column(banco.String(15), nullable=False)
    email = banco.Column(banco.String(50), nullable=False)
    cidade = banco.Column(banco.String(50), nullable=False)


    def __init__(self, agenda_id, nome, numero, email, cidade):
        self.agenda_id = agenda_id
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cidade = cidade

    def json(self):
        return {
            'agenda_id': self.agenda_id,
            'nome': self.nome,
            'numero': self.numero,
            'email': self.email,
            'cidade':self.cidade,
        }
    
    @classmethod
    def find_agenda(cls, agenda_id):
        agenda = cls.query.filter_by(agenda_id=agenda_id).first() #SELECT * FROM agenda WHERE agenda_id = agenda_id
        if agenda:
            return agenda
        return None


    def save_agenda(self):
        banco.session.add(self)
        banco.session.commit()


    def update_contato(self, nome, numero, email, cidade):
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cidade = cidade



    def delete_contato(self):
        banco.session.delete(self)
        banco.session.commit()
        


    #def find_agenda(agenda_id):
     #   for contato in agenda:
      #      if contato['agenda_id'] == agenda_id:
       #         return contato
       # return None