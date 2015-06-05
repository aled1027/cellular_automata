from schelling import Graph

if __name__ == '__main__':
    b = Graph(num_agents=30, edge_threshold=0.33)
    l = b.laplacian
    a = b[0]

    print ("num agents: %d" % len(b))

    for i in range(30):
        b.update()
        print(i, b.num_edges, b.happiness_ratio)

