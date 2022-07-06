import torch
import torch.nn as nn
class NueralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NueralNet, self).__init__()
        self.l1 = nn.Linear(input_size,hidden_size)
        self.l2 = nn.Linear(hidden_size,hidden_size)
        self.l3 = nn.Linear(hidden_size,num_classes)
        self.relu = nn.ReLU()
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
3:02
nltk_utils
# from lib2to3.pgen2 import token
import nltk
import numpy as np
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())
def bag_of_words(tokenized_sentence, all_words):
    """
    sentance = ["hello","how","are","you"]
    words = ["hi", "hello", "I", "you", "bye", "thank","cool"]
    bag = [0 , 1, 0, 1, 0, 0, 0]
    """
    sentence_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_words:
            bag[idx] = 1.0
    return bag
sentence = ["hello","how","are","you"]
words = ["hi", "hello", "I", "you", "bye", "thank","cool"]
bag = bag_of_words(sentence, words)