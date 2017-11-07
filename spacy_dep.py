from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle

nlp = spacy.load('en')

# load and feed text in right format
text = sys.stdin.read().decode('utf8', errors="ignore")
# text= "You have not engaged in our great and gathering conversation, nor did you create the wealth of our marketplaces."
doc = nlp(text)

# .dep_  is for Syntactic dependency relation.
nominal_subject = [item.text for item in doc if item.dep_ == 'nsubj']
clausal_complement = [item.text for item in doc if item.dep_ == 'ccomp']
expletive = [item.text for item in doc if item.dep_ == 'expl']
attribute = [item.text for item in doc if item.dep_ == 'attr']
prepositional_modifier = [item.text for item in doc if item.dep_ == 'prep']
object_of_preposition = [item.text for item in doc if item.dep_ == 'pobj']
marker = [item.text for item in doc if item.dep_ == 'mark']
open_clausal_complement = [item.text for item in doc if item.dep_ == 'xcomp']
auxiliary = [item.text for item in doc if item.dep_ == 'aux']


for word in doc:
    print word.text, word.dep_
def gen_sentence_dep():
    print ' '.join([choice(nominal_subject), choice(clausal_complement), choice(attribute)])
    print ' '.join([choice(prepositional_modifier), choice(object_of_preposition), choice(marker), choice(open_clausal_complement)])

# gen_sentence_dep()
# nsubj + ccomp + expl + attr
# prep + pobj + mark + xcomp
