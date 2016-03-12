############################################################
# CIS 391: Homework 7
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
from collections import Counter
import math
import re


############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    return re.findall(r"[\w]+|[^\s\w]", text)

def ngrams(n, tokens):
    tokens.append('<END>')
    if n > 1 : 
        return [tuple([tuple(['<START>' if j < 0 else tokens[j] for j in xrange(i-(n-1),i)]),item]) for i, item in enumerate(tokens)]
    else :
        return [tuple([(),item]) for i, item in enumerate(tokens)]

class NgramModel(object):

    def __init__(self, n):
        self.order = n
        self.dict = Counter()
        self.context = Counter()

    def update(self, sentence):
        grams = ngrams(self.order, tokenize(sentence))
        self.context.update(Counter([word[0] for word in grams]))
        self.dict.update(Counter(grams)) 

    def prob(self, context, token):
        if (context, token) not in self.dict:
            return 0.0
        return float(self.dict[(context, token)]) / self.context[context]

    def random_token(self, context):
        r = random.random()
        T = sorted(list(set([word[1] for word in self.dict if word[0] == context])))
        prob = 0
        for i in range(len(T)):
            prob  = prob + self.prob(context, T[i])
            if r < prob:
                return T[i]

    def random_text(self, token_count):
        result = ''
        if self.order == 1:
            result = reduce(lambda str,token: str + self.random_token(()) + ' ',xrange(token_count),'')
        else:
            context = ['<START>' for i in xrange(self.order-1)]
            for i in xrange(token_count):
                token = self.random_token(tuple(context))
                result+= token +' '
                context.append(token); 
                context.pop();
                if token == '<END>':
                    context = ['<START>' for i in xrange(self.order-1)]
        return result.strip()

    def perplexity(self, sentence):
        lis = ngrams(self.order, tokenize(sentence))
        return math.exp(reduce(lambda result,word : result + (math.log(1)-math.log(self.prob(word[0], word[1]))),lis,0)) ** (float(1)/len(lis))        

def create_ngram_model(n, path):
    m = NgramModel(n)
    f = open(path,'r')
    for line in f:
        m.update(line)
    f.close()
    return m

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
5 hours
"""

feedback_question_2 = """
Writing effecient code
"""

feedback_question_3 = """
I liked the simplicity.
"""

