class Persona:
    def __init__(self, nombre='', dni='', edad=''):
        self.nombre = nombre
        self.dni =dni
        self.edad = edad

class Docente(Persona):
    def __init__(self,nombre,edad,dni):
       Persona.__init__(self, nombre, edad, dni)

    def registro_docente(self):
        try:
            file = open('docente.txt', 'a')
            texto = f"Docente: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
            file.write(texto)
        except Exception as e:
            print(f"{e}")
        finally:
            file.close()

docente1 = Docente("Inowsky",24,12345678)
docente1.registro_docente()

class Alumno(Persona):
    def __init__(self, nombre, edad, dni, notas):
        self.notas = notas
        Persona.__init__(self, nombre, edad, dni)
    
    def calculo_notas(self):
        self.promedio = sum(self.notas)/len(self.notas)
        self.nota_max = max(self.notas,key=float)
        self.nota_min = min(self.notas,key=float)

    def registro_alumno(self):
        try:
            file = open('alumno.txt', 'a')
            texto = f"Alumno: {self.nombre}, máxima nota:  {self.nota_max}, minima nota: {self.nota_min}, Promedio : {self.promedio}\n"
            file.write(texto)
        except Exception as e:
            print(f"{e}")
        finally:
            file.close()

alumno1 = Alumno("Jose", 25, 12356789, [10,20,15,5])
alumno1.calculo_notas()
alumno1.registro_alumno()



        

