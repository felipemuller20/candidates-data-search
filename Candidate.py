class Candidate:
    def __init__(self, name, cpf, score):
        self.name = name
        self.score = score
        cpf = str(cpf)
        if self.cpf_is_valid(cpf):
            self.cpf = cpf
        else:
            print(f"O CPF {cpf} é invalido")
            self.cpf = None

    
    def cpf_is_valid(self, cpf):
        if len(cpf) == 11:
            return True
        return False
