class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=51):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    Sadamassa = Mutante(nome='Sadamassa')
    Rodrigo = Homem(Sadamassa, nome='Rodrigo')
    print(Pessoa.cumprimentar(Rodrigo))
    print(id(Rodrigo))
    print(Rodrigo.cumprimentar())
    print(Rodrigo.nome)
    print(Rodrigo.idade)
    for filho in Rodrigo.filhos:
        print(filho.nome)
    Rodrigo.sobrenome = "Higa"
    del Rodrigo.filhos
    Rodrigo.olhos = 1
    del Rodrigo.olhos
    print(Rodrigo.__dict__)
    print(Sadamassa.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(Rodrigo.olhos)
    print(Sadamassa.olhos)
    print(id(Pessoa.olhos), id(Rodrigo.olhos), id(Sadamassa.olhos))
    print(Pessoa.metodo_estatico(), Rodrigo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Rodrigo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Sadamassa, Pessoa))
    print(isinstance(Sadamassa, Homem))
    print(Sadamassa.olhos)
    print(Rodrigo.cumprimentar())
    print(Sadamassa.cumprimentar())
