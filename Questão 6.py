class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_informacoes(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        return f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} metros de altura."
def solicitar_informacoes_pessoa():
    nome = input("Insira o nome da pessoa: ")
    idade = int(input("Insira a idade da pessoa: "))
    altura = float(input("Insira a altura da pessoa em metros: "))
    return Pessoa(nome, idade, altura/100)

# Função principal
def main():
    pessoa = solicitar_informacoes_pessoa()
    print(pessoa.cumprimentar())

if __name__ == "__main__":
    main()
