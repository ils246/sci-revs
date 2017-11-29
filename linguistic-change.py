import json
import pandas as pd
import nltk
from nltk import MLEProbDist, word_tokenize
from nltk.corpus import stopwords
import numpy as np
from gensim import corpora, models
import gensim
import matplotlib.pyplot as plt


# nltk.download('punkt
# nltk.download('stopwords')

# Maybe compute the coherence of each topic
# top_topics(corpus=None, texts=None, dictionary=None, window_size=None, coherence='u_mass', topn=20, processes=-1)

# Filter out words that occur less than 20 documents, or more than 50% of the documents. --- ASK NICK IF THIS IS A THING
# dictionary.filter_extremes(no_below=20, no_above=0.5)

## Now I need to make the word frequency in time:
years = range(1900,2017,5)
terms = ['evolution', 'computation', 'computating', 'bioinformatics',
         'systems biology','genes', 'gene', 'genomics', 'genetic', 'genomic', 'systems', 'systemic', 'machine learning', 'deep learning']

files = ['/Volumes/Isabella/papers-metadata/fields/biology-nodes-%s.json' % year for year in years]

word_timeseries = open('word_timeseries.csv', 'w+')
word_dists = open('word_prob_dists.csv', 'w+')

df = pd.DataFrame(columns=years)
df_dists = pd.DataFrame(columns=years)

total_dists=[]
genetics=[]
compsci=[]

frequencies = [[] for i in range(len(terms)+1)]

# Get stopwords ready
stop_words = stopwords.words('english')

# Add stop words domain related
words = ['thesis', 'theses', 'article', 'research', 'paper', 'conference',
             'proceedings', 'scientific', 'vol', 'sciences', 'europe', 'uk',
             'journal', 'journals', 'science', 'sciences', 'search', 'america', 'citation',
             'biology']

stop_words.extend(words)

for f in range(len(files)):

    print(years[f])

    nodes = json.loads(open(files[f]).read())

    # # Get the keywords from each item
    # keywords = [i['keywords'] for i in nodes ]
    #
    # #Filter and remove all the missing data in terms of 'None'
    # keys = list(filter(lambda x : x != None, keywords))
    # # print(len(keys))
    #
    # # Flatten list keywords
    # # keys_flat = [item for sublist in keys for item in sublist]
    #
    # # Make all the keywords into one gigantic string
    # strs = [' '.join(i) for i in keys]
    #
    # # Tokenize the lists
    # tokens = [word_tokenize(i) for i in strs]
    #
    # # Remove stopwords
    # tokens = [[i for i in j if i not in stop_words] for j in tokens]
    # # print(tokens[0])
    # # print(type(tokens))
    # # print(tokens[:20])
    #
    # # Should I stem the words?
    #
    # # turn tokenized documents into an id / term dictionary
    # dictionary = corpora.Dictionary(tokens)
    #
    # # convert tokenized documents into a document-term matrix
    # corpus = [dictionary.doc2bow(t) for t in tokens]
    #
    # # generate the LDA model
    # ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=8, id2word = dictionary, passes=20)
    # print(ldamodel.print_topics(num_topics=, num_words=10))


    #      Fos during those years
    # ----------------------------------

    fos = [i['fos'] for i in nodes ]
    fos = list(filter(lambda x : x != None, fos))
    fos_flat = [item for sublist in fos for item in sublist]
    fos_stopped = [[i for i in j if i not in stop_words] for j in fos_flat]
    fos_freq=nltk.FreqDist(fos_flat).most_common(40)
    print("fos frequent")
    # print(fos_freq)

    print('my attempt at probability distribution')
    probs = [round(i[1]/len(nodes), 5)*100 for i in fos_freq]
    fos_freq_mod = [ (fos_freq[i][0], fos_freq[i][1], str(probs[i])+'%') for i in range(len(fos_freq)) ]
    print(fos_freq_mod)

    # # Plot the probabilities
    # plt.figure(figsize=(9,8))
    # plt.bar(range(len(probs[1:])), probs[1:] )
    # plt.title('Most likely folds in %d' % years[f])
    # plt.xticks(range(len(probs[1:])), [i[0] for i in fos_freq_mod[1:]], size=5.5, rotation=90)
    # plt.ylabel('Probability (%)')
    # plt.savefig('./most-likely-fos-%d' % years[f])
    # plt.close()

    g = 0
    cs = 0
    for i in fos_freq_mod:
        if i[0] =='Genetics':
            g=i[2]
        elif i[0] == 'Computer Science':
            cs=i[2]


    genetics.append((years[f],g))
    compsci.append((years[f],cs))
    print(genetics)
    print(compsci)








#
#
#
#
#     # make word cloud of that year
#     # keys_freq=nltk.FreqDist(keys_flat)
#     # keys_prob = MLEProbDist(keys_freq)
#     # print(keys_prob)
#     # print(keys_freq['evolution'])
#     # print(keys_prob)
#
# #     frequencies[0].append(len(nodes))
# #     frequencies[1].append(keys_freq['evolution'])
# #     frequencies[2].append(keys_freq['computation'])
# #     frequencies[3].append(keys_freq['computating'])
# #     frequencies[4].append(keys_freq['bioinformatics'])
# #     frequencies[5].append(keys_freq['systems biology'])
# #     frequencies[6].append(keys_freq['genes'])
# #     frequencies[7].append(keys_freq['gene'])
# #     frequencies[8].append(keys_freq['genomics'])
# #     frequencies[9].append(keys_freq['genetic'])
# #     frequencies[10].append(keys_freq['genomic'])
# #     frequencies[11].append(keys_freq['systems'])
# #     frequencies[12].append(keys_freq['systemic'])
# #     frequencies[13].append(keys_freq['machine learning'])
# #     frequencies[14].append(keys_freq['deep learning'])
# #
# #
# #     nodes=0
# #     print('finished', str(years[f]))
# #     # print(frequencies[0])
# #
# #     dist_aux=[[] for i in range(len(terms))]
# #
# #     # distributions
# #     counter=0
# #     for i in terms:
# #         for j in keys:
# #             if i in j:
# #                 dist_aux[counter].append(j)
# #         counter+=1
# #
# #     dist_flat=[]
# #     for i in dist_aux:
# #         a = [item for sublist in  i for item in sublist]
# #         a = nltk.FreqDist(a)
# #         dist_flat.append(a.most_common(100))
# #     total_dists.append(dist_flat)
# #
# # print(np.shape(total_dists))
# # print(total_dists, file=word_dists)
# #
# # for f in range(len(terms)):
# #     df.loc[terms[f]]=frequencies[f]
# #
# # df.to_csv(word_timeseries)
