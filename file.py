import csv
from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer
import nltk
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import itertools
from sklearn.manifold import TSNE
import numpy as np
class TFIDF:

    def compute_tf(word_dict,l):
        tf = {}
        sum_nk = l


    def main(self):
        corpus = []
        state = []
        firstLine = True
        with open("consumer_complaints.csv") as data_file:
            read_csv = csv.reader(data_file, delimiter=',')
            for row in read_csv:
                if firstLine:
                    firstLine = False
                    continue
                #    print str(row[3]).lower()
                corpus.append(str(row[3]).lower())
                state.append(str(row[8]).lower())
        # clearing and tokenizing\
        # l_A in tokenizedarray
        tokenized_array = []
        wordset = set()
        total = 0
        # print type(wordset)
        for list in corpus:
            tokenized_array.append(list.split(','))
            # print list.split(',')
            # print tokenized_array
            wordset = set(wordset).union(set(list.split(',')))
            total = total + len(list.split(','))

        print "Total words = " + str(total)
        print wordset
        print len(wordset)
    # for bag of words
        tok_arr_bag_of_words = []

        for list in tokenized_array:
            # print list
            tok_arr_bag_of_words.append(dict.fromkeys(wordset, 0))
        i = 0
        # print "wordset"
        # print len(wordset)
        # print len(tok_arr_bag_of_words)
        print tokenized_array
        model = Word2Vec(tokenized_array, min_count=1)
        print "Model"
        print model
        X = model[model.wv.vocab]
        NUM_CLUSTERS = 3

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        y_kmeans = kmeans.predict(X)

        plt.scatter(X[:, 0], X[:, 1], c="rgb", s=100, cmap='viridis')
        centers = kmeans.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], c="rgb", s=500, alpha=0.5)
        plt.show()
        # labels = ["cl1","cl2","cl3"]
        # print ("labels:",labels)
        # kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
        #
        # assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
        # print ("assi:",assigned_clusters)
        #
        #
        # plt.scatter(X[:, 0], X[:, 1], c=labels,
        #             s=50, cmap='viridis')
        #
        # plt.title(" chutiya")
        # plt.show()
        # words = model.wv.vocab
        # A= []
        # B=[]
        # C=[]
        # for i, word in enumerate(words):
        #     if(assigned_clusters[i] == 0):
        #        A.append(word)
        #     if (assigned_clusters[i] == 1):
        #         B.append(word)
        #     if (assigned_clusters[i] == 2):
        #         C.append(word)
        #
        #     print (word + ":" + str(assigned_clusters[i]))
        #
        # print "a:",A
        # print B
        # print C

        # print ("A:",len(A)," B:",len(B)," c:",len(C))
        # print("A:",A[:, 0]+" 1:", A[:, 1])
        # plt.
        # plt.scatter(B[:, 0], B[:, 1], c='r')
        # plt.scatter(C[:, 0], C[:, 1], c='b')

        # plt.xlabel('Test Data'), plt.ylabel('Z samples')
        # plt.show()


        # model = TSNE(n_components=2, random_state=1200)
        # np.set_printoptions(suppress=True)
        #
        # Y = model.fit_transform(X)
        # print "Y",len(Y)
        # print "Corpus",len(wordset)
        # plt.scatter(Y[:, 0], Y[:, 1], c=assigned_clusters, s=300, alpha=.8)
        #
        # for j in range(len(wordset)):
        #     plt.annotate(assigned_clusters[j], xy=(Y[j][0], Y[j][1]), xytext=(0, 0), textcoords='offset points')
        #     print ("%s %s" % (assigned_clusters[j], corpus[j]))


        # for list in tok_arr_bag_of_words:
        #     for word in list:
        #         # print tok_arr_bag_of_words[i]
        #
        #         # print word
        #         # print tok_arr_bag_of_words[i][word]
        #         if word in tokenized_array[i]:
        #             tok_arr_bag_of_words[i][word] = tok_arr_bag_of_words[i][word] + 1
        #         # print tok_arr_bag_of_words[i][word]
        #         # print 1
        #     i = i + 1
        #
        # print tok_arr_bag_of_words


if __name__ == '__main__':
    fun = TFIDF()
    fun.main()