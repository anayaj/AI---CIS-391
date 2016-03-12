############################################################
# CIS 391: Homework 6
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
import re
import string

############################################################
# Section 1: Probability
############################################################

# Set the following variables to True or False.
section_1_problem_1a = False
section_1_problem_1b = True
section_1_problem_1c = False

# Set the following variables to True or False.
section_1_problem_2a = True
section_1_problem_2b = True
section_1_problem_2c = False
section_1_problem_2d = False
section_1_problem_2e = False
section_1_problem_2f = True
section_1_problem_2g = False
section_1_problem_2h = True

# Set the following variables to probabilities, expressed as decimals between 0
# and 1.
section_1_problem_3a = 0.01162455
section_1_problem_3b = 0.98837545
section_1_problem_3c = 0.1087184125
section_1_problem_3d = 0.00051055739
section_1_problem_3e = 0.00000504868
section_1_problem_3f = 0.0000074625
section_1_problem_3g = 0.0005145525


############################################################
# Section 2: Spam Filter
############################################################
def load_tokens(email_path):
	fileInstance = open(email_path, 'r')
	message = email.message_from_file(fileInstance)
	fileInstance.close()

	headerTokens = []
	unigramTokens = []
	emailAddressTokens = []

	for header in message.walk():
		headerTokens.append(header.get_content_type())

	for line in email.iterators.body_line_iterator(message):
		for word in line.split():
			if len(word) >=5 and len(word)<14 :
				unigramTokens.append(word.lower())
				
			if len(word) >=14 and re.match(r"[^@]+@[^@]+\.[^@]+", word) :
				emailAddressTokens.extend(word.lower().split('@'))

	return [unigramTokens,headerTokens,emailAddressTokens]

def log_probs(email_paths, smoothing):
	typeTokens = [[],[],[]]
	log_prob_dictionary = {}

	for email_path in email_paths :
		email_tokens = load_tokens(email_path)
		for i in xrange(len(email_tokens)) : 
			typeTokens[i].extend(email_tokens[i])

	for i in xrange(len(typeTokens)) : 
	    count = Counter(typeTokens[i])
	    num_words = len(typeTokens[i])
	    num_vocabulary = len(count)

	    if(i == 0) :
	    	log_prob_dictionary["<UNK>"] = math.log(smoothing / (num_words + smoothing * (num_vocabulary +1)));

	    for word in count:
	        log_prob_dictionary[word] = math.log((count[word] + smoothing ) / (num_words + smoothing * (num_vocabulary +1)))

	return log_prob_dictionary

class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir):
    	smoothing = 1e-9;
        self.spam_files = os.listdir(spam_dir)
        self.ham_files = os.listdir(ham_dir)
        self.spam_dict = log_probs([spam_dir+'/'+spam_file for spam_file in self.spam_files],smoothing)
        self.ham_dict = log_probs([ham_dir+'/'+ham_file for ham_file in self.ham_files],smoothing)
        self.p_spam = len(self.spam_files) / float(len(self.spam_files) + len(self.ham_files))
        self.p_ham = 1 - self.p_spam
    
    def is_spam(self, email_path):
        count = Counter(reduce(lambda x,y: x + y, load_tokens(email_path),[]))
        p_spam = self.p_spam
        p_ham = self.p_ham
        for word in count:
            p_spam += self.spam_dict[word]*count[word] if self.spam_dict.has_key(word) else self.spam_dict["<UNK>"]*count[word]
            p_ham += self.ham_dict[word]*count[word] if self.ham_dict.has_key(word) else self.ham_dict["<UNK>"]*count[word]
        return p_ham < p_spam

def test() :
	sf = SpamFilter("data/train/spam","data/train/ham")
	numHamIsHam = 0
	numHamIsSpam = 0
	numSpamIsHam = 0
	numSpamIsSpam = 0
	for i in xrange(1,201) :
		if sf.is_spam("data/dev/ham/dev"+str(i)) :
			numHamIsSpam +=1
			print i
		else :
			numHamIsHam+= 1
	for i in xrange(201,401):
		if sf.is_spam("data/dev/spam/dev"+str(i)) :
			numSpamIsSpam +=1
		else :
			print i
			numSpamIsHam+= 1

	print "Ham is Ham :",numHamIsHam
	print "Ham is Spam :",numHamIsSpam
	print "Spam is Ham :",numSpamIsHam
	print "Spam is Spam :",numSpamIsSpam