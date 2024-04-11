class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self, media_minima=6):
        media = self.calcular_media()
        if media >= media_minima:
            return f"{self.nome} foi aprovado com média {media:.2f}."
        else:
            return f"{self.nome} foi reprovado com média {media:.2f}."

# Exemplo de uso
notas_joao = [7, 8, 6.5, 9]
joao = Estudante(nome="João", idade=20, notas=notas_joao)
print(joao.verificar_aprovacao())

notas_maria = [5, 4, 6, 5.5]
maria = Estudante(nome="Maria", idade=21, notas=notas_maria)
print(maria.verificar_aprovacao())
