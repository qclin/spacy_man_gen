from __future__ import unicode_literals
import sys
import spacy
from random import choice, shuffle

# load and feed text in right format
nlp = spacy.load('en')
text = sys.stdin.read().decode('utf8', errors="replace")
doc = nlp(text)

people = [item.text for item in doc.ents if item.label_ == 'PERSON']
gerunds = [item.text for item in doc if item.tag_ == 'VBG']

noun_phrase = [item.text.strip() for item in doc.noun_chunks]


# POS___
nouns = [item.text for item in doc if item.pos_ == 'NOUN']
adjectives = [item.text for item in doc if item.pos_ == 'ADJ']
adjectives_tag = [item.tag_ for item in doc if item.pos_ == 'ADJ']


conjunctions = [item.text for item in doc if item.pos_ == 'CONJ']
conjunctions_placeholders = ["and", "but", "or", "also"]

adverbs = [item.text for item in doc if item.pos_ == 'ADV']
verbs = [item.text for item in doc if item.pos_ == 'VERB']

verbs_modal = []
verbs_non_modal = []

for item in doc:
    if item.pos_ == 'VERB':
      # print item.text, item.tag_
      if item.tag_ == 'MD':
        verbs_modal.append(item.text)
      else:
        verbs_non_modal.append(item.text)

# verbstag = [item.tag_ for item in doc if item.pos_ == 'VERB']

prepositions = [item.text for item in doc if item.pos_ == 'ADP']

proper_nouns = [item.text for item in doc if item.pos_ == 'PROPN']
pronouns = [item.text for item in doc if item.pos_ == 'PRON']
particles = [item.text for item in doc if item.pos_ == 'PART']

#### TAG___



modal_tags = ["VMFIN", "VMINF", "VMPP"]





auxillary_be = [item.text for item in doc if item.tag_ == 'BES']
determiners = [item.text for item in doc if item.tag_ == 'DT']
pure_adjectives = [item.text for item in doc if item.tag_ == 'JJ']


coor_conjunction = [item.text for item in doc if item.tag_ == 'KON']


comparative_adj = [item.text for item in doc if item.tag_ == 'JJR']
superlative_adj = [item.text for item in doc if item.tag_ == 'JJS']


adverbs = [item.text for item in doc if item.tag_ == 'RB']

comparative_adverbs = [item.text for item in doc if item.tag_ == 'RBR']

pure_verbs = [item.text for item in doc if item.tag_ == 'VB']
verb_singular_third = [item.text for item in doc if item.tag_ == 'VBZ']

prepositions_prep = [item.text for item in doc if item.tag_ == 'ADPR']
prepositions_post = [item.text for item in doc if item.tag_ == 'ADPO']


only_past_tense_verbs=[]

### .pos_ is more general part of speech, .tag_ give more species to the type, ie past tense


# print "----------------- NOUN PHRASES-----------------"
# print noun_phrase

# for sent in doc.sents:
#    words = list(sent)
#    print words[0].text

sentences = list(doc.sents)

# text match thru loop
# for item in sentences:
#   if item[0].text == "We":
#     print(item.text)


### sentences with more than 2 commas
# for item in sentences:
#   if item.text.count(',') > 2:
#     print(item.text)

# cause = ["because", "therefore", "that's why","so", "thus", "so that"]

# ### text match with regEX
# for sent in sentences:
#   words = list(sent)
#   for word in words:
#     if word == "because":
#       print sent


# find sentences with 2 or more commas






# print "----------------- ADJECTIVES -----------------"
# print adjectives


for item in doc:
    if item.tag_ == 'VBN':
        only_past_tense_verbs.append(item.text)

# print "----------------- VERBs in PAST TENSE -----------------"
# print only_past_tense_verbs

### using subtrees and dependency relations to grab larger syntactic units
def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

subjects = []
prep_phrases = []
for word in doc:
    if word.dep_ in('nsubj', 'nsubjpass'):
        subjects.append(flatten_subtree(word.subtree))
    elif word.dep_ == 'prep':
        prep_phrases.append(flatten_subtree(word.subtree))

# print "----------------- subjects -----------------"
# print subjects

# print "----------------- prep_phrases -----------------"
# print prep_phrases
# ### entity objects with labels

# print "----------------- ENTITIES -----------------"

# for item in doc.ents:
#     print item.text, item.label_




# **** print out all the sentences that start with noun phrase

# Patterns to look for
# 1 - We vs You: Comparison
# 2 - Direct Speech (verbs)
# 3 - Descriptive: Lots of Adjectives
# 4 - Metaphors ____ is like ____  ABJ, NOUN
# 5 - Present & Future tenses


# you weary giant of flesh and steel
# NP + ADJ + N + P + N   |  CONJ + NP
# for i in range(20):

#   print ' '.join([choice(noun_phrase),choice(adjectives),choice(nouns),choice(prep_phrases),choice(nouns)])

#   print ' '.join([choice(conjunctions), choice(noun_phrase)])


print "our highest priority "
print "DET + ADJ + N "

print "is to"
print "V + COMP"

print "satisfy the consumer"
print "V_non_modal + DET + N"

print "through"
print "ADP"

print "early and continous"
print "ADJ + CONJ + ADJ"

print "delivery of valuable software"
print "N + P + ADJ + N"

print "----------------------------------------------------- "

def run_sentence():
  for i in range(20):
    print ' ,'.join([choice(pure_adjectives), choice(pure_adjectives), choice(pure_adjectives)]),
    np_sentence = ' '.join([choice(determiners), choice(pure_adjectives), choice(nouns)])
    print np_sentence ,
    # print ' '.join([choice(adverbs), choice(comparative_adverbs)])
    print ' '.join([choice(verbs_modal), choice(adverbs)]),
    print ' '.join([choice(pure_verbs), choice(determiners), choice(nouns)]) ,
    print choice(prepositions),
    print ' '.join([choice(pure_adjectives), choice(conjunctions_placeholders), choice(pure_adjectives)]),
    print ' '.join([choice(nouns), choice(prepositions), choice(pure_adjectives), choice(nouns)]),
    print "."
    print np_sentence.split()[-1]
    print " ----------------------------------------------------- "

# run_sentence()
