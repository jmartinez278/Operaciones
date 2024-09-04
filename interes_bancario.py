class InteresBancario:
    def calcular_interes_compuesto(self, capital_inicial, tasa_interes, anios):
        """Calcula el interés compuesto de una cuenta bancaria"""
        monto_final = capital_inicial * (1 + tasa_interes / 100) ** anios
        return monto_final
