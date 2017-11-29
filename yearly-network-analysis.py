import networkx as nx
import json
import ast



'''
This file reads in the yearly networks and gives
us some insight in to what is in each of them
'''

field = 'biology'
years = range(1850,2017)

node_files = ['/Volumes/Isabella/papers-metadata/fields/%s-nodes-%d.json' % (field, year) for year in years]
edge_files = ['/Volumes/Isabella/papers-metadata/fields/%s-edges-%d.json' % (field, year) for year in years]
metrics = open('%s-metrics.csv' % field, 'w+')


for f in range(len(node_files)):

    nodes = json.loads(open(node_files[f]).read())


    for i in nodes:
        g.add_node(
                    i['id'],
                    year=i['year'],
                    keys=i['keywords'],
                    fos=i['fos']
                    )

    pre_edges = nx.number_of_nodes(g)
    # Add edges
    edges=[]

    with open(edge_files[f]) as k:

        for line in k:
            edges.append(ast.literal_eval(line))
        g.add_edges_from(edges)

    mets = [pre_edges, nx.number_of_nodes(g), nx.number_of_edges(g), nx.density(g)]
    print(mets, file=metrics)
