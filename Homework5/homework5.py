############################################################
# CIS 391: Homework 5
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email 
import math
import os
from collections import Counter

############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):
    fileInstance = open(email_path, 'r')
    message = email.message_from_file(fileInstance)
    fileInstance.close()
    return reduce(lambda arr,line : arr + line.split(), email.iterators.body_line_iterator(message),[])

def log_probs(email_paths, smoothing):
    tokens = reduce(lambda arr,email_path : arr + load_tokens(email_path), email_paths,[])
    count = Counter(tokens)
    num_words = len(tokens)
    num_vocabulary = len(count)
    log_prob_dictionary = {"<UNK>":math.log(smoothing / (num_words + smoothing * (num_vocabulary +1)))}
    for word in count:
        log_prob_dictionary[word] = math.log((count[word] + smoothing ) / (num_words + smoothing * (num_vocabulary +1)))
    return log_prob_dictionary

class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        self.spam_files = os.listdir(spam_dir)
        self.ham_files = os.listdir(ham_dir)
        self.spam_dict = log_probs([spam_dir+'/'+spam_file for spam_file in self.spam_files],smoothing)
        self.ham_dict = log_probs([ham_dir+'/'+ham_file for ham_file in self.ham_files],smoothing)
        self.p_spam = math.log(len(self.spam_files) / float(len(self.spam_files) + len(self.ham_files)))
        self.p_ham = math.log(1 - self.p_spam)
    
    def is_spam(self, email_path):
        count = Counter(load_tokens(email_path))
        p_spam = self.p_spam
        p_ham = self.p_ham
        for word in count:
            p_spam += self.spam_dict[word]*count[word] if self.spam_dict.has_key(word) else self.spam_dict["<UNK>"]*count[word]
            p_ham += self.ham_dict[word]*count[word] if self.ham_dict.has_key(word) else self.ham_dict["<UNK>"]*count[word]
        return p_ham < p_spam

    def most_indicative(self,n,prob_dict) :
        indicative = {}
        for word in set(self.spam_dict).intersection(self.ham_dict):
            indicative[word] = prob_dict[word] - math.log(math.exp(self.spam_dict[word] + self.p_spam) + math.exp(self.ham_dict[word] + self.p_ham))
        return sorted(indicative, key=indicative.get,reverse=True)[:n]

    def most_indicative_spam(self, n):
        return self.most_indicative(n,self.spam_dict)

    def most_indicative_ham(self, n):
        return self.most_indicative(n,self.ham_dict)

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
5 Hours
"""

feedback_question_2 = """
I found the manipulation of probabilities to be the hardest
i.e - making sure the switch between log and exp
"""

feedback_question_3 = """
I really liked the progression of the homework assignment
It was very clear to understand what is going on
"""
