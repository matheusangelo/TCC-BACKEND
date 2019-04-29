from pymongo import MongoClient
#from mock import mock_pacientes


class Conexao:

    def carga_pacientes(self):

        mock_pacientes = [
            {
                "id": "1",
                "nome": "Matheus",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "2",
                "nome": "Marcos",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "3",
                "nome": "Lucas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "4",
                "nome": "Judas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "5",
                "nome": "Thiago",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "6",
                "nome": "Pedro",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "7",
                "nome": "Paulo",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
        ]

        # conexao com o banco
        cliente = MongoClient('localhost', 17017)

        # selecionando o banco
        banco = cliente['tcc']

        # acessando a respectiva tabela
        prontuario = banco['pacientes']

        paciente_id = prontuario.insert_many(mock_pacientes)

        print("ok")