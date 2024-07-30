class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    def set_idade(self, NovaIdade):
        self.__idade = NovaIdade

class Aluno (Pessoa):
    def __init__(self, nome, idade, turma):
        super().__init__(nome, idade)
        self.__turma = turma
        self.lista_notas = []
        
    def lista_notas(self):
        nota = nota
        self.lista_notas.append()
        

    def get_turma(self):
        return self.__turma
    def set_turma(self, NovaTurma):
        self.__turma = NovaTurma
      
class Disciplina(Aluno):
    def __init__(self, nome, turma, professor, nomeD):
        super().__init__(nome, turma)
        self.__professor = professor
        self.__nomeD = nomeD

    def get_professor(self):
        return self.__professor
    def set_professor(self, NovoProf):
         self.__professor = NovoProf
    

class Nota(Disciplina):
    def __init__(self, nome, turma, professor, nota):
        super().__init__(nome, turma, professor)
        self.__nota = nota
    def get_nota(self):
        return self.__nota
    def set_nome(self):
        return self.__nota 
