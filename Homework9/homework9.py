############################################################
# CIS 391: Homework 9
############################################################

student_name = "Arjun Raj Jain"

############################################################
# Imports
############################################################

import homework9_data as data

# Include your imports here, if any are used.
from collections import defaultdict


############################################################
# Section 1: Perceptrons
############################################################

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.w = defaultdict(float)
        for i in range(iterations): 
            for x_i, y_i in examples:
                y_hat_i = self.predict(x_i)
                if y_hat_i != y_i:
                    for x_key in x_i.keys():
                        self.w[x_key] += -((-1)**(int(y_i))) * x_i[x_key]  

    def predict(self, x):
        return sum([x[x_key] * self.w[x_key] for x_key in x.keys()]) > 0

class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.labels = set([y_i for x_i, y_i in examples])
        self.w = {label:defaultdict(float) for label in self.labels}
        for i in range(iterations):
            for x_i, y_i in examples:
                y_hat_i = self.predict(x_i)
                if y_hat_i != y_i:
                    for x_key in x_i.keys():
                        self.w[y_i][x_key] += x_i[x_key]
                        self.w[y_hat_i][x_key] += -1 * x_i[x_key]

    def predict(self, x):
        return max((sum([x[x_key] * self.w[label][x_key] for x_key in x.keys()]), label) for label in self.labels)[1]

############################################################
# Section 2: Applications
############################################################

class IrisClassifier(object):

    def __init__(self, data):
        self.percept = MulticlassPerceptron([(dict(enumerate(x)), label) for (x, label) in data], 500)

    def classify(self, instance):
        return self.percept.predict(dict(enumerate(instance)))

class DigitClassifier(object):

    def __init__(self, data):
        self.percept = MulticlassPerceptron([(dict(enumerate(x)), label) for (x, label) in data],25)

    def classify(self, instance):
        return self.percept.predict(dict(enumerate(instance)))

class BiasClassifier(object):

    def __init__(self, data):
        newData = map(lambda (x,label): ((x,1),label),data)
        self.percept = BinaryPerceptron([(dict(enumerate(x)), label) for (x, label) in newData], 100)

    def classify(self, instance):
        return self.percept.predict(dict(enumerate((instance,1))))

class MysteryClassifier1(object):

    def __init__(self, data):
        newData = map(lambda ((a, b), label): ((a,b,a**2,b**2,1),label),data)
        self.percept = BinaryPerceptron([(dict(enumerate(x)), label) for (x, label) in newData], 200)

    def classify(self, instance):
        return self.percept.predict(dict(enumerate(instance + (instance[0]**2,instance[1]**2,1))))     

class MysteryClassifier2(object):

    def __init__(self, data):
        newData = map(lambda ((a, b,c), label): ((a,b,c,a*b*c,1),label),data)
        self.percept = BinaryPerceptron([(dict(enumerate(x)), label) for (x, label) in newData], 200)

    def classify(self, instance):
        return self.percept.predict(dict(enumerate(instance + (instance[0]*instance[1]*instance[2],1))))   


############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = """
About 7 Hours
"""

feedback_question_2 = """
I think finding the ways to edit the data for the mystery ones 
was the most time consuming. This required me to use excel to 
see appropriate trends. 
"""

feedback_question_3 = """
I liked the abstraction that I built to easily use the Perceptron
classes and classify appropriately. This was good practice in how 
to actually apply algorithms to real life data.
"""