class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=51):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Sadamassa = Pessoa(nome='Sadamassa')
    Rodrigo = Pessoa(Sadamassa, nome='Rodrigo')
    print(Pessoa.cumprimentar(Rodrigo))
    print(id(Rodrigo))
    print(Rodrigo.cumprimentar())
    print(Rodrigo.nome)
    print(Rodrigo.idade)
    for filho in Rodrigo.filhos:
        print(filho.nome)
    Rodrigo.sobrenome = "Higa"
    del Rodrigo.filhos
    Rodrigo.olhos = 3
    del Rodrigo.olhos
    print(Rodrigo.__dict__)
    print(Sadamassa.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(Rodrigo.olhos)
    print(Sadamassa.olhos)
    print(id(Pessoa.olhos), id(Rodrigo.olhos), id(Sadamassa.olhos))

