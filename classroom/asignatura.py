class Asignatura:

    #Simulacion sobrecarga constructores.
    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
         impresion=self._nombre+" "+self._salon
         return impresion
