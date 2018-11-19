
from google import google
import pandas as pd
from time import sleep
import csv
import pickle
import re
import spacy
import numpy as np
from sklearn.preprocessing import StandardScaler


# load spacy object
nlp = spacy.load('en')

#tokenize
#remove punctionations
def preprocess(sent):
    #remove punctustion
    sent = re.sub(r'[^\w\s]','',sent)
    words = sent.split()
    new_words = []
    for w in words:      
        new_words.append(w.lower())
        
    return ' '.join(new_words)



class mySearchRes:
    def __init__(self,text):
        self.quoteText = text
        self.quoteID = hash(self.quoteText)
        self.link = []
        self.name = []
        self.description = []
        self.scores = []
        self.cos = []

    def __hash__(self):
        return self.quoteID


def search_google_DF(file):
    objects = {}
    for row in file:
        texthash = hash(row)
        search_results = google.search(row, 1)
        if texthash not in objects:
            #print(row)
            objects[texthash] = mySearchRes(row)       
            #search_results = [[text, i.link, i.name,i.description] for i in google.search(text, num_page)]
            for i in search_results:
                objects[texthash].name.append(i.name)
                objects[texthash].description.append(i.description)
                line = preprocess(i.name)
                count = line.count("lyric") + line.count("lyrics") + line.count("quote") + line.count("quotes")
                objects[texthash].scores.append(count)
    return objects

def cosineSim(results):
    for item in results:
        str1 = ''.join (results[item].description)
        doc2 = nlp(preprocess(str1))
        doc1 = nlp(preprocess(results[item].quoteText))
        results[item].cos.append(doc1.similarity(doc2))

#pack the score to 10
def align_scores(objects):
    for item in objects:
        count = 0
        for i in range(len(objects[item].scores)): # add 1 to all the scores 
            objects[item].scores[i] = objects[item].scores[i] +1           
            if objects[item].scores[i] is not None:
                count = count + 1 
               # score = score + 1 won't work because score is a shallow copy
        #print(objects[item].scores)
        while count < 10:
            objects[item].scores.append(0) #empty result is replaced by 0
            count = count + 1

def append_features(ob):
    proto_matrix = []
    for item in ob:
        col2 = np.append(ob[item].scores, ob[item].cos)
        #print(col2)
        proto_matrix.append(col2)
      
    return proto_matrix



class QuoteClassfier:
    def __init__(self, modelfile):
        #load the model
        #whatever
        self.model = modelfile

    #def isQuote(quotetext):
    #   return -1

    def isQuotes(quotetext)
        return -1
    def trainNewModel(myQuotesFile):
        return -1

ob = search_google_DF(posts['text'][400:410])
cosineSim(ob)
align_scores(ob)


proto_matrix = append_features(ob)
FeatureMatrix = np.matrix(proto_matrix)
scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(FeatureMatrix)
scaled_matrix

a = QuoteClassifier()
a.isQuote("dasda")