class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
def solicitar_medidas_retangulo():
    altura = float(input("Insira a altura do retângulo: "))
    largura = float(input("Insira a largura do retângulo: "))
    return Retangulo(altura, largura)

# Função principal
def main():
    retangulo = solicitar_medidas_retangulo()
    print("Área do retângulo:", retangulo.calcular_area())
    print("Perímetro do retângulo:", retangulo.calcular_perimetro())

if __name__ == "__main__":
    main()
