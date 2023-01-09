from itertools import product


def main():
    class artefacto():
        def __init__(self, value, weight):
            self.value = value
            self.weight = weight
        
        def __str__(self):
            return "Value: %d - Weight: %d" % (self.value, self.weight)


    def backtracking(items, peso_maximo, N):
        soluciones = list(product([0,1], repeat=N))
        valor_maximo = -10000000
        final_solucion = []

        for solucion in soluciones:  #[0,1,0...]
            peso_actual = 0 
            valor_actual = 0

            for indice, item_bit in enumerate(solucion):
                if item_bit == 1:
                    item_tomado = items[indice]
                    peso_actual = peso_actual + item_tomado.weight
                    valor_actual = valor_actual + item_tomado.value
            
            if peso_actual <= peso_maximo:
                if valor_actual > valor_maximo:
                    valor_maximo = valor_actual
                    final_solucion = solucion
                    final_peso = peso_actual
                    

        return final_solucion, valor_maximo, final_peso

    # ejecucion
    items = [artefacto(103, 12),
                artefacto(60, 23),
                artefacto(70, 11),
                artefacto(5, 15),
                artefacto(15, 7)
            ]

    N = 5
    peso_maximo = 100
    print(backtracking(artefacto, peso_maximo=peso_maximo, N=N))

if __name__ == '__main__':
	main()