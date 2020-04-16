#!/usr/bin/python3

import random
import yaml

path = "/Users/mattialavacca/Desktop/"

x = 0

def get_random_color():
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    random_color = '#'

    for c in range(0, 6, 1):
        random_color += letters[random.randint(0, 15000) % 16]
        
    return random_color


def compute_graph(d):
    global x
    color = get_random_color()

    graph = "graph{\n"
    graph += "\tnode[style=\"filled\", color=\"" + color + "\"]\n"

    for i in range(0, d['n_nodes']):
        request = random.uniform(d['min_request'], d['max_request'])
        limit = random.uniform(request, d['max_limit'])
        graph += "\t" + str(i) + "[label=\"cpuOffloading - request:" + str(
            "{0:.2f}".format(request)) + " - limit:" + str("{0:.2f}".format(limit))
        graph += "\""
        graph += ", label=\"n" + str(i) + "\""
        graph += "];\n"

    n_nodes = d['n_nodes']
    n_edges = d['n_edges']

    for i in range(0, n_edges):
        k = random.randint(0, n_nodes - 1)
        j = k

        while k == j:
            j = random.randint(0, n_nodes - 1)

        latency = random.uniform(d['min_latency'], d['max_latency'])
        graph += "\t" + str(k) + " -- " + str(j) + "[label=\"latency - value:" + str("{0:.2f}".format(latency)) + "\""
        graph += ", label=\"n" + str(k) + "-n" + str(j) + "\""
        graph += "];\n"

    graph += "}\n"

    graph_path = path + "/depGraph" + str(x) + ".dot"
    x += 1

    f = open(graph_path, "w")
    f.write(graph)
    f.close()


with open('dep_config.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

depGraphSize = [{"n_nodes": 5, "n_edges": 15},
                {"n_nodes": 10, "n_edges": 20},
                {"n_nodes": 20, "n_edges": 40}]

'''{"n_nodes": 40, "n_edges": 80},
{"n_nodes": 70, "n_edges": 150},
{"n_nodes": 100, "n_edges": 200},
{"n_nodes": 200, "n_edges": 380},
{"n_nodes": 50, "n_edges": 90},
{"n_nodes": 30, "n_edges": 50},
{"n_nodes": 10, "n_edges": 22}]'''

for n in depGraphSize:
    data["n_nodes"] = n["n_nodes"]
    data["n_edges"] = n["n_edges"]
    compute_graph(data)






