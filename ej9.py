def main():
    def prims(N, graph_matrix):
        # Prim's Algorithm in Python
        INF = 9999999
        # number of vertices in graph
        N = N # numero de nodos
        #creating graph by adjacency matrix method
        G = graph_matrix

        selected_node = [0]*N

        no_edge = 0

        selected_node[0] = True

        # printing for edge and weight
        print("Edge : Weight\n")
        while (no_edge < N - 1): # 1 < 5 - 1 ## 4 = 4
            minimum = INF
            a = 0
            b = 0
            for m in range(N): # m=0, m =1, m=2
                #print('m:',m)
                #print('first if:', selected_node[m])
                if selected_node[m]:
                    for n in range(N):
                        #print('n:',n)
                        #print((not selected_node[n]),G[m][n])
                        if ((not selected_node[n]) and G[m][n]):  
                            #print('entra')
                            # not in selected and there is an edge
                            if minimum > G[m][n]:
                                minimum = G[m][n]
                                a = m # nodo origen
                                b = n # nodo destino
                            #print('minimun:', minimum)
            print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
            selected_node[b] = True  # [True, 0, True, 0, 0] --> [True, 0, True, True, 0] --> [True, 0, True, True, True]
            #print('selected node:', selected_node)
            no_edge += 1

    graph_matrix = [[0, 19, 5, 0, 0],
                     [19, 0, 5, 9, 2],
                     [5, 5, 0, 1, 6],
                     [0, 9, 1, 0, 1],
                     [0, 2, 6, 1, 0]]

    #graph_matrix = =[[0, 19-19, 19-5, 0, 0],
    #                 [19-19, 0, 19-5, 19-9, 19-2],
    #                 [19-5, 19-5, 0, 19-1, 19-6],
    #                 [0, 19-9, 19-1, 0, 19-1],
    #                 [0, 19-2, 19-6, 19-1, 0]]

    prims(N=5, graph_matrix=graph_matrix)

if __name__ == "__main__":
    main()
def main():
    def prims(N, graph_matrix):
        # Prim's Algorithm in Python
        INF = 9999999
        # number of vertices in graph
        N = N # numero de nodos
        #creating graph by adjacency matrix method
        G = graph_matrix

        selected_node = [0]*N

        no_edge = 0

        selected_node[0] = True

        # printing for edge and weight
        print("Edge : Weight\n")
        while (no_edge < N - 1): # 1 < 5 - 1 ## 4 = 4
            minimum = INF
            a = 0
            b = 0
            for m in range(N): # m=0, m =1, m=2
                #print('m:',m)
                #print('first if:', selected_node[m])
                if selected_node[m]:
                    for n in range(N):
                        #print('n:',n)
                        #print((not selected_node[n]),G[m][n])
                        if ((not selected_node[n]) and G[m][n]):  
                            #print('entra')
                            # not in selected and there is an edge
                            if minimum > G[m][n]:
                                minimum = G[m][n]
                                a = m # nodo origen
                                b = n # nodo destino
                            #print('minimun:', minimum)
            print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
            selected_node[b] = True  # [True, 0, True, 0, 0] --> [True, 0, True, True, 0] --> [True, 0, True, True, True]
            #print('selected node:', selected_node)
            no_edge += 1

    graph_matrix = [[0, 19, 5, 0, 0],
                     [19, 0, 5, 9, 2],
                     [5, 5, 0, 1, 6],
                     [0, 9, 1, 0, 1],
                     [0, 2, 6, 1, 0]]

    #graph_matrix = =[[0, 19-19, 19-5, 0, 0],
    #                 [19-19, 0, 19-5, 19-9, 19-2],
    #                 [19-5, 19-5, 0, 19-1, 19-6],
    #                 [0, 19-9, 19-1, 0, 19-1],
    #                 [0, 19-2, 19-6, 19-1, 0]]

    prims(N=5, graph_matrix=graph_matrix)

if __name__ == "__main__":
    main()

