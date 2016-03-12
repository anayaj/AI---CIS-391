############################################################
# CIS 391: Homework 1
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Strongly Typed - 
    Def - Unable to perform operations on an object that does
    not support the object's type. 

    Ex  - " 1 + 'one' "  would not be an allowed operation as we 
    have not defined a cross concatentation operation for 
    strings and numbers


Dynamically Typed - 
    Def - The type of a variable is determined by what object
    has been assigned to it, not at decleration.

    Ex  - In java we have to declare a variable as int if we 
    want it to be a number, but in Python we can just create a
    variable and assign an int to it, without explicity saying
    its an int. As a result, type errors for Python are only caught 
    at Runtime. 
"""

python_concepts_question_2 = """
The problem is that [0,0], [1,2], and [-1,1] are all lists - hence
they are mutable, which is not allowed for keys in a python dict.
Instead we can make them immutable tuples to represent the same 
information.
"""

python_concepts_question_3 = """
The '.join' is superior to '+' because as we iterate throught the for 
loop for '+' we have to create a new string everytime (as strings are
immutable), whereas join is optimized to take all the items in the list
and create one massive string at once.

"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(li) for li in l if p(li)]

def concatenate(seqs):
    return [li for seq in seqs for li in seq]

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))] 

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    return (seq[:i] for i in range(len(seq)+1))

def suffixes(seq):
    return (seq[:i] for i in range(len(seq), -1, -1))

def slices(seq):
    return (seq[i:j] for i in range(0,len(seq)+1) for j in range(i+1,len(seq)+1))

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().strip().split()) 

def no_vowels(text):
    return ''.join([s for s in text if s.lower() not in ('a', 'e', 'i', 'o', 'u')])

def digits_to_words(text):
    digits = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine", '0':"zero"}
    return ' '.join([digits[s] for s in text if s in digits])

def to_mixed_case(name):
    result = ''.join(s.capitalize() for s in name.lower().split('_'))
    return result[0].lower() + result[1:] if result else ' '

############################################################
# Section 6: Polynomials
############################################################
class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial(((term[0] * -1,term[1]) for term in self.get_polynomial()))

    def __add__(self, other):
        return Polynomial(self.get_polynomial() + other.get_polynomial())

    def __sub__(self, other):
        return Polynomial(self.get_polynomial() + (-other).get_polynomial())

    def __mul__(self, other):
        return Polynomial((termS[0] * termO[0], termS[1] + termO[1]) for termS in self.get_polynomial() for termO in other.get_polynomial())

    def __call__(self, x):
        return sum((((x ** term[1]) * term[0]) for term in self.get_polynomial()))

    def simplify(self):
        pairs = dict({});
        #combine terms into a dictionary (add all terms with same exponents)
        for termD in [{term[1]:term[0]} for term in self.get_polynomial()]:
            pairs = {x: pairs.get(x, 0) + termD.get(x, 0) for x in set(pairs).union(termD)}

        # checks if all coefficients are zero
        if all(elem == 0 for elem in pairs.values()) :
            self.polynomial = ((0,0))

        #otherwise
        else :
            # remove coefficients of zero
            pairs = {k:v for (k,v) in pairs.iteritems() if k > 0}

            # sort the elements
            powers = pairs.keys()
            powers.sort(reverse = True)
            self.polynomial = tuple([(pairs[x],x) for x in powers])

    def __str__(self):
        string =  " ".join([formatTerm(term) for term in self.get_polynomial()])
        if(string[0]=="+") :
            return string[3:]
        else :
            return string[0]+string[3:]

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
~7 hours
"""

feedback_question_2 = """
I think the most challenging part was coming up with succint code that 
actually made sense when you read it. But it was an awesome learning experience,
and I think I'm already a lot better at reading intense python code now.
"""

feedback_question_3 = """
I liked how the assignment progressed in difficulty, and that it forced us to
use succint code to write seemingly complex methods in simple manner. 
"""
