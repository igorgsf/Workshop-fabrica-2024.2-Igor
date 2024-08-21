class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo = Retangulo(5, 3)

area = retangulo.calcular_area()
print(f'Área do retângulo: {area} m²')

perimetro = retangulo.calcular_perimetro()
print(f'Perímetro do retângulo: {perimetro} metros')