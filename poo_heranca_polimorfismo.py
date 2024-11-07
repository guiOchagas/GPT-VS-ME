class Veiculo():
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        
    def info(self):
        print(f'{"MODELO:":12} {self.modelo}\n{"ANO:":12} {self.ano}')
    
    def ligar(self):
        print('Ligando...')
        print('Veiculo ligado!')
        print()
        
        
class Carro(Veiculo):
    def __init__(self, modelo, ano, tipo='Carro'):
        super().__init__(modelo, ano)
        self.tipo = tipo
        
    def info(self):
        print(f'{"TIPO:":12} {self.tipo}\n{"MODELO:":12} {self.modelo}\n{"ANO:":12} {self.ano}')
        print()

class Caminhao(Veiculo):
    def __init__(self, modelo, ano, carga, tipo='Caminhão'):
        super().__init__(modelo, ano)
        self.tipo = tipo
        self.carga = carga
    
    def info(self):
        print(f'{"TIPO:":12} {self.tipo}\n{"MODELO:":12} {self.modelo}\n{"ANO:":12} {self.ano}\n{"CARGA:":12} {self.carga}')
        print()
    

class Motocicleta(Veiculo):
    def __init__(self, modelo, ano, cilindrada, tipo='Moto'):
        super().__init__(modelo, ano)
        self.cilindrada = cilindrada
        self.tipo = tipo
    
    def info(self):
        print(f'{"TIPO:":12} {self.tipo}\n{"MODELO:":12} {self.modelo}\n{"ANO:":12} {self.ano}\n{"CC:":12} {self.cilindrada}')
        print()


audi = Carro('A3', 2016,)
caminhao = Caminhao('Mercedez', 2011, 5000)
moto = Motocicleta('Fazer', 2015, 150)
bmw = Carro('320i', 2020)
moto2 = Motocicleta('CG', 2018, 160)
fox = Carro('Fox', 2013)


lista = [audi, caminhao, moto, bmw, moto2, fox]

for i in lista:
    if isinstance(i, Carro):
        i.info()
        
print(len(lista))
