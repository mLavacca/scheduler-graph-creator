#!/usr/bin/python3

import random
import yaml
import os

path = "/Users/mattialavacca/Desktop/fedGraphs"


def compute_graph(d, y1):
    stats = {}
    graph = "graph{\n"

    graph += "\tcentral" + \
             "[label=\"cpu - amount:" + \
             str("{0:.2f}".format(d['central_amount'])) + \
             " - cost:" + str("{0:.2f}".format(d['central_cost']))

    graph += " - minR:" + str(d['minR']) + \
             " - maxR:" + str("{0:.2f}".format(d['central_maxR'])) + \
             " - minL:" + str(d['minL']) + \
             " - maxL:" + str("{0:.2f}".format(d['central_maxL']))
    graph += "\""
    graph += ", label=\"central\""
    graph += "];\n"

    for i in range(0, d['n_nodes']):
        amount = random.uniform(d['min_amount'], d['max_amount'])
        maxL = amount
        maxR = amount
        cost = random.uniform(d['min_cost'], d['max_cost'])

        graph += "\t" + str(i) + \
                 "[label=\"cpu - amount:" + str("{0:.2f}".format(amount)) + " - cost:" + str("{0:.2f}".format(cost))
        graph += " - minR:" + str(d['minR']) + " - maxR:" + str("{0:.2f}".format(maxR)) + \
                 " - minL:" + str(d['minL']) + " - maxL:" + str("{0:.2f}".format(maxL))
        graph += "\""
        graph += ", label=\"n" + str(i) + "\""
        graph += "];\n"

    for i in range(0, d['n_nodes']):
        latency = random.uniform(d['min_latency'], d['max_latency'])
        cost = random.uniform(d['min_latency_cost'], d['max_latency_cost'])

        graph += "\t" + str(i) + " -- central" + \
                 "[label=\"latency - value:" + str("{0:.2f}".format(latency)) + \
                 " - cost:" + str("{0:.2f}".format(cost)) + "\""
        graph += ", label=\"n" + str(i) + "-central" + "\""
        graph += "];\n"

        stats[str(i)] = {'latency': latency, 'cost': cost}

    for i in range(0, d['n_nodes']):
        for j in range(0, i):
            latency = stats[str(i)]['latency'] + stats[str(j)]['latency']
            cost = stats[str(i)]['cost'] + stats[str(j)]['cost']

            graph += "\t" + str(i) + " -- " + str(j) + \
                     "[label=\"latency - value:" + str("{0:.2f}".format(latency)) + \
                     " - cost:" + str("{0:.2f}".format(cost)) + "\""
            graph += ", label=\"n" + str(i) + "-n" + str(j) + "\""
            graph += "];\n"

    graph += "}\n"
    graph_path = path + "/fedGraphs" + str(d["n_nodes"])
    if y1 == "0":
        cmd = "mkdir " + graph_path
        os.system(cmd)

    fn = graph_path + "/fedGraph" + str(y) + ".dot"
    f = open(fn, "w")
    f.write(graph)
    f.close()


with open('fed_config.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

fedGraphSize = [999]

for x in range(0, 1, 1):
    for y in range(0, 10, 1):
        data["n_nodes"] = fedGraphSize[x]
        compute_graph(data, str(y))




