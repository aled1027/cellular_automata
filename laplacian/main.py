from schelling import Graph
import csv

if __name__ == '__main__':
    path = "data/data.csv"

    with open(path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        moving_mu = 0.1
        num_agents = 1000
        pref_alike = 0.5
        b = Graph(num_agents=num_agents, moving_mu=moving_mu, pref_alike=pref_alike)

        print ("num agents: %d" % len(b))
        exp_num_edges = moving_mu * num_agents * (num_agents - 1)

        csvwriter.writerow(["iter", "num_edges", "avg_hap", "avg_sim"])
        for i in range(100):
            if i % 25 == 0:
                print (i)
            b.update()
            csvwriter.writerow([i, b.num_edges, b.happiness_ratio, b.avg_similarity])

