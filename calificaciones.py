class Calificaciones:
    def convertir_calificacion(self, calificacion):
        """Convierte una calificación numérica a su equivalente literal"""
        if calificacion >= 20:
            return "AD"
        elif calificacion >= 16:
            return "A"
        elif calificacion >= 11:
            return "B"
        else:
            return "C"
