class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma
    def exibir_informacoes(self):
       print(f"Aluno - Nome: {self.nome}, Turma: {self.turma}")
  
class Disciplina(Aluno):
    def __init__(self, nome, turma, professor, nomeD):
        super().__init__(nome, turma)
        self.professor = professor
        self. nomeD = nomeD
    
    def exibir_informacoes(self):
        return super().exibir_informacoes()
        print(f"Disciplina - Nome: {self.nomeD}, Professor: {self.professor}")
    
class Nota(Disciplina):
    def __init__(self, nome, turma, professor, nota):
        super().__init__(nome, turma, professor)
        self.nota = nota

    def exibir_informacoes(self):
        return super().exibir_informacoes()
        print(f"Nota: {self.nota}")

 
