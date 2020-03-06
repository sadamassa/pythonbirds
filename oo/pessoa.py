class Pessoa:
    def __init__(self, *filhos, nome=None, idade=51):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Rodrigo = Pessoa(nome='Sadamassa')
    Sada = Pessoa(Rodrigo, nome='Sada')
    print(Pessoa.cumprimentar(Sada))
    print(id(Sada))
    print(Sada.cumprimentar())
    print(Sada.nome)
    print(Sada.idade)
    for filho in Sada.filhos:
        print(filho.nome)

