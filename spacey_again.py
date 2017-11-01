from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle

nlp = spacy.load('en')


# ###### get the tags of a sample sentence
# docc = nlp("Our highest priority is to satisfy the customer through early and continuous delivery of valuable software")
# for item in docc: 
#   print item.text, item.pos_, item.tag_ 



# load and feed text in right format
text = sys.stdin.read().decode('utf8', errors="ignore")
doc = nlp(text)


pronoun_possessive = [item.text for item in doc if item.tag_ == 'PRP$']
adjective_superlative = [item.text for item in doc if item.tag_ == 'JJS']
noun_singular = [item.text for item in doc if item.tag_ == 'NN']
verb_singular_third_present = [item.text for item in doc if item.tag_ == 'VBZ']
infinitival_to = [item.text for item in doc if item.tag_ == 'TO']
verb_base = [item.text for item in doc if item.tag_ == 'VB']
determiner = [item.text for item in doc if item.tag_ == 'DT']
conjunction_sub_pre = [item.text for item in doc if item.tag_ == 'IN']
adjective_base = [item.text for item in doc if item.tag_ == 'JJ']
conjunction_coor = [item.text for item in doc if item.tag_ == 'CC']

# print pronoun_possessive
# print adjective_superlative
# print noun_singular

for i in range(20): 
  print ', '.join([choice(adjective_base), choice(adjective_base), choice(adjective_base)])

  print ' '.join([choice(pronoun_possessive), choice(adjective_base), choice(noun_singular)])

  print ' '.join([choice(verb_singular_third_present),choice(infinitival_to)])

  print ' '.join([choice(verb_base), choice(determiner), choice(noun_singular)])

  print ' '.join([choice(conjunction_sub_pre), choice(adjective_base), choice(conjunction_coor), choice(adjective_base), choice(noun_singular)])

  print ' '.join([choice(conjunction_sub_pre), choice(adjective_base), choice(noun_singular)])

  print '----------------------------------------------'

# Our ADJ PRP$
# highest ADJ JJS
# priority NOUN NN

# is VERB VBZ
# to PART TO

# satisfy VERB VB
# the DET DT
# customer NOUN NN

# through ADP IN
# early ADJ JJ
# and CCONJ CC
# continuous ADJ JJ
# delivery NOUN NN

# of ADP IN
# valuable ADJ JJ
# software NOUN NN




