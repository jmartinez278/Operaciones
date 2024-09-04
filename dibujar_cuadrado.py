class DibujoCuadrado:
    def dibujar_cuadrado(self, lado):
        """Dibuja un cuadrado utilizando asteriscos"""
        for i in range(lado):
            print('*' * lado)
