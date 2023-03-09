class AgendaModel:
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