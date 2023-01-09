def main():
    class artefactosvaliosos():
        def __innit__ (self, peso ,nombre,precio,fechacadu):
            self.peso= peso
            self.nombre = nombre
            self.precio=precio
            self.fechacadu = fechacadu
            print("  artefactosvaliosos se ha creado con exito")
        def __str__ (self):
         return'peso{}, nombre{}, precio{}, fechacadu{},'. format(self.peso,self.nombre,self.precio,self.fechacadu)



artefactosvaliosos = []

artefactosvaliosos1 = artefactosvaliosos (1, 'agua', 1, 2024)
artefactosvaliosos2= artefactosvaliosos (2,'comida', 20, 2023)
artefactosvaliosos3 = artefactosvaliosos (2,'cuchillo', 45,2030)
artefactosvaliosos4= artefactosvaliosos (100, 'mechero', 1,2028 )

if __name__ == "_main_":
    main()