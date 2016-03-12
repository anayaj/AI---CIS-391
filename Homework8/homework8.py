############################################################
# CIS 391: Homework 8
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from collections import Counter
from collections import defaultdict

############################################################
# Section 1: Hidden Markov Models
############################################################
SMOOTHING = 1e-10

def load_corpus(path):
    with open(path,'r') as f:
    	return [[tuple(word.split('=')) for word in line.split()] for line in f]

def prob(count_w, total_count, vocab_size):
    return (count_w + SMOOTHING) / float(total_count + SMOOTHING * vocab_size)

class Tagger(object):

    def __init__(self, sentences):
        pi_freq = defaultdict(int)
        pi_freq['<UNK>'] = 0
        a_freq = defaultdict(int)
        b_freq = defaultdict(int)
        allTags = defaultdict(int)

        self.tags = ['NOUN', 'VERB', 'ADJ', 'ADV', 'PRON', 'DET', 'ADP', 'NUM', 'CONJ', 'PRT', '.', 'X']
        for sentence in sentences:
            pi_freq[sentence[0][1]] += 1
            for index in xrange(len(sentence)):
                b_freq[(sentence[index][1], sentence[index][0])] += 1
                allTags[sentence[index][1]] += 1
                if index < len(sentence) - 1:
                    a_freq[(sentence[index][1], sentence[index+1][1])] += 1

        a_counter =  Counter(list(a_freq))
        b_counter = Counter(list(b_freq))
        
        self.a = defaultdict(float)
        self.b = defaultdict(float)
        self.pi = dict((t,prob(pi_freq[t], len(sentences), len(pi_freq))) for t in pi_freq)

        for (t, w) in b_freq:
            self.b[(t, w)] = prob(b_freq[(t, w)], allTags[t], b_counter[t])            
            self.b[('<UNK>', w)] = prob(0, allTags[t], b_counter[t])

        for (t, t_j) in a_freq:
            self.a[(t, t_j)] = prob(a_freq[(t, t_j)], allTags[t], a_counter[t])
            self.a[('<UNK>', t_j)] = prob(0, allTags[t], a_counter[t])

    def most_probable_tags(self, tokens):
        dicts = [dict((key,value) for key, value in self.b.iteritems() if key[1] == token) for token in tokens];
        return [max(d,key=d.get)[0] for d in dicts]

    def viterbi_tags(self, tokens):
        delta = [{} for i in xrange(len(tokens))]
        psi = [{} for i in xrange(len(tokens))]

        for tag in self.tags: 
            delta[0][tag] = self.pi[tag] * self.b[(tag, tokens[0])]

        for t in xrange(1, len(tokens)): 
            for tag_j in self.tags:
                (delta[t][tag_j], psi[t][tag_j]) = max((delta[t-1][tag] * self.a[(tag, tag_j) ]* self.b[(tag_j, tokens[t])], tag) for tag in self.tags)

        states = [max((delta[-1][tag], tag) for tag in self.tags)[1]]
        for t in xrange(len(tokens)-1,0,-1):
            states.append(psi[t][states[-1]])

        return list(reversed(states))

############################################################
# Section 2: Feedback
############################################################
feedback_question_1 = """
8 hours
"""

feedback_question_2 = """
I found the initialization to be the most challenging. Keeping track of
everything in the most efficient manner was difficult.
"""

feedback_question_3 = """
I liked the simplicity of the Viterbi algorithm, it was pretty much as described
in the slides
"""