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
adjectival_modifier = [item.text for item in doc if item.dep_ == 'amod']
nominal_subject = [item.text for item in doc if item.dep_ == 'nsubj']
clausal_complement = [item.text for item in doc if item.dep_ == 'ccomp']
coordinating_conjunction = [item.text for item in doc if item.dep_ == 'cc']
conjunct = [item.text for item in doc if item.dep_ == 'conj']
expletive = [item.text for item in doc if item.dep_ == 'expl']
attribute = [item.text for item in doc if item.dep_ == 'attr']
appositional_modifiel = [item.text for item in doc if item.dep_ == 'appos']
prepositional_modifier = [item.text for item in doc if item.dep_ == 'prep']
object_of_preposition = [item.text for item in doc if item.dep_ == 'pobj']
possession_modifier = [item.text for item in doc if item.dep_ == 'poss']
marker = [item.text for item in doc if item.dep_ == 'mark']
open_clausal_complement = [item.text for item in doc if item.dep_ == 'xcomp']
auxiliary = [item.text for item in doc if item.dep_ == 'aux']
determiner = [item.text for item in doc if item.dep_ == 'det']
direct_object = [item.text for item in doc if item.dep_ == 'dobj']
adverbial_modifier = [item.text for item in doc if item.dep_ == 'advmod']
root = [item.text for item in doc if item.dep_ == 'ROOT']
relative_clause = [item.text for item in doc if item.dep_ == 'relcl']
negation_modifier = [item.text for item in doc if item.dep_ == 'neg']



# for word in doc:
#     print word.text, word.dep_
def gen_sentence_dep_a():
    print ' '.join([choice(nominal_subject), choice(clausal_complement), choice(attribute)]),
    print ' '.join([choice(prepositional_modifier), choice(object_of_preposition), choice(marker), choice(open_clausal_complement)])


# We nsubj
# , punct
# the det
# European compound
# Pirates appos
# , punct
# want ROOT
# society nsubj
# to aux
# welcome ccomp
# and cc
# adjust conj
# to prep
# the det
# digital amod
# revolution pobj
# : punct
# choice(doc.ents), 

def gen_sentence_dep_b():
	# We, the European Pirates, want society to welcome and adjust to the digital revolution:
	print ' '.join([choice(nominal_subject), choice(determiner),  choice(appositional_modifiel), ', ']), 
	print ' '.join([choice(root), choice(nominal_subject), choice(auxiliary), choice(clausal_complement), choice(coordinating_conjunction)]), 
	print ' '.join([choice(conjunct), choice(prepositional_modifier), choice(determiner)]), 
	print ' '.join([choice(adjectival_modifier), choice(object_of_preposition), '.'])

# You have no sovereignty where we gather.
# You nsubj
# have ROOT
# no det
# sovereignty dobj
# where advmod
# we nsubj
# gather relcl
# . punct

def gen_sentence_dep_c():
	# You have no sovereignty where we gather.
	print ' '.join([choice(nominal_subject), choice(root), choice(determiner)]),
	print ' '.join([choice(direct_object), choice(adverbial_modifier), choice(nominal_subject)]),
	print ' '.join([choice(relative_clause),'.'])

# You nsubj
# have aux
# not neg
# engaged ROOT
# in prep
# our poss
# great amod
# and cc
# gathering conj
# conversation pobj
# , punct
# nor cc
# did aux
# you nsubj
# create conj
# the det
# wealth dobj
# of prep
# our poss
# marketplaces pobj
# . punct



def gen_sentence_dep_d(): 
	print ' '.join([choice(nominal_subject), choice(auxiliary), choice(negation_modifier), choice(root)]), 
	print ' '.join([choice(prepositional_modifier), choice(possession_modifier), choice(adjectival_modifier)]), 
	print ' '.join([choice(coordinating_conjunction), choice(conjunct), choice(object_of_preposition), ',']), 
	print ' '.join([choice(coordinating_conjunction),  choice(auxiliary), choice(nominal_subject), choice(conjunct)]), 
	print ' '.join([choice(determiner), choice(direct_object), choice(prepositional_modifier), choice(possession_modifier), choice(object_of_preposition), '.'])

for i in range(50):
	gen_sentence_dep_a()
	# You claim there are problems among us that you need to solve 
	# # nsubj + ccomp + expl + attr
	# # prep + pobj + mark + xcomp

	gen_sentence_dep_b()
		# We, the European Pirates, want society to welcome and adjust to the digital revolution:

	gen_sentence_dep_c()
		# You have no sovereignty where we gather.

	gen_sentence_dep_d()
	# You have not engaged in our great and gathering conversation, nor did you create the wealth of our marketplaces.

	print "\n\n ----------------------------------------------------- \n\n"