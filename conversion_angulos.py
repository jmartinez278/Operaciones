import math

class ConversionAngulos:
    def convertir_grados_radianes(self, grados):
        """Convierte grados sexagesimales a radianes"""
        radianes = grados * math.pi / 180
        return radianes

    def convertir_radianes_grados(self, radianes):
        """Convierte radianes a grados sexagesimales"""
        grados = radianes * 180 / math.pi
        return grados