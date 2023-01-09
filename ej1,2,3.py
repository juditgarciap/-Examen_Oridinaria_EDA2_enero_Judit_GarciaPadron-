def main():
    class stormtrooper():
        def __innit__ (self, nombre ,rango):
            self.nombre = nombre
            self.rango = rango 

print(" stormtrooper se ha creado con exito")
def clasificar():
    class rango (stormtrooper):
        def __init__(self, nombre,rango,codigolegion )
            stormtrooper().__init__(self,nombre,rango)
            self.codigolegion= codigolegion 
        def __str__ (self):
            return'nombre{}, rango {}, Codigo de la legión{}'. format(self.nombre,self.rango,self.codigolegion)

        
    
    class nombre (stormtrooper):
        def __init__(self, nombre,rango,codigolegion,idco,ids,idesc,ntrooper)
            stormtrooper().__init__(self,nombre,rango,codigolegion)
            self.idco = idco
            self.ids= ids
            self.idesc = idesc
            self.ntrooper = ntrooper
        def __str__ (self):
            return'nombre{}, rango {}, Codigo de la legión{}-,idco{},ids{},idesc{},ntrooper{} '. format(self.nombre,self.rango,self.codigolegion,self.idco, self.ids, self.idesc, self.ntrooper)
            


stormtrooper = []

stormtrooper1 =  stormtrooper('FL', 2, 4,9,5)
stormtrooper2 = stormtrooper ('TF', 2, 3, 5,5)
stormtrooper3 = stormtrooper ('TK', 1,7,9 ,0)
stormtrooper4= stormtrooper ('CN', 3, 7, 0,1)

stormtrooper.append(stormtrooper1)
stormtrooper.append(stormtrooper2)
stormtrooper.append(stormtrooper3)
stormtrooper.append(stormtrooper4)









if __name__ == "__main__":
    main()
