#Caíque Góes de Oliveira e Maria Eduarda da Silva
class Carro:
    def _init_(self, carro,marca ,modelo ,ano ,cor ):
        self.carro = carro
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"{self.carro} está ligado ."
    def desligar(self):
        return f"{self.carro} foi desligado ."
    def acelerar(self):
        return f"{self.carro} está acerelerando ."
if __name__ == "_main_":
    carro = Carro("carro", "marca","modelo","ano","cor") 
    print(carro.ligar())
    print(carro.desligar())
    print(carro.acelerar())