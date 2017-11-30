import ast
from collections import Counter
import json

'''This file finds the 'super hubs' in the data and makes files with their
number of citations every 3 years.
'''


y1 = range(1975, 2017, 3)
y2 = range(1978, 2017, 3)

pairs = [(y1[i], y2[i]) for i in range(len(y1))

for pair in pairs:

    years = range(pair[0], pair[1])

    # Files to load
    references_files =  ['/Volumes/Isabella/papers-metadata/fields/biology-edges-%s.json' % year for year in years]

    all_references=[]
    for f in references_files:
        aux=[]

        #Append all the edges to
        with open(f) as my_file:
            for line in my_file:
                tup=ast.literal_eval(line)
                aux.append(tup)
            aux1=[i[1] for i in aux]
            all_references.extend(aux1)

    # Get the degree of each node for those three years
    degree = Counter(all_references)

    # Threshold for 'super hubs'
    thresh = max(degree.values())*0.20    # 0.50 was too stringent
    print(thresh)
    super_hubs = [(k,v) for k,v in degree.items() if v > thresh]

    # dump in a file
    f = open('superhubs-%d-%d.csv' % (pair[0],pair[1]-1), 'w+')
    json.dump(super_hubs,f)
