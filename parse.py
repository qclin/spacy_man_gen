from __future__ import unicode_literals
import sys
import spacy
import random

# load and feed text in right format
nlp = spacy.load('en')
text = sys.stdin.read().decode('utf8', errors="replace")
doc = nlp(text)

people = [item.text for item in doc.ents if item.label_ == 'PERSON']
gerunds = [item.text for item in doc if item.tag_ == 'VBG']

noun_phrase_text = [item.text.strip() for item in doc.noun_chunks]

adjective_text = [item.text for item in doc if item.tag_ == 'ADJ']

only_past_tense_verbs=[]

### .pos_ is more general part of speech, .tag_ give more species to the type, ie past tense


print "----------------- NOUN PHRASES-----------------"
print noun_phrase_text

print "----------------- ADJECTIVES -----------------"
print adjective_text


for item in doc:
    if item.tag_ == 'VBN':
        only_past_tense_verbs.append(item.text)

print "----------------- VERBs in PAST TENSE -----------------"
print only_past_tense_verbs

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

print "----------------- subjects -----------------"
print subjects

print "----------------- prep_phrases -----------------"
print prep_phrases
### entity objects with labels
print "----------------- ENTITIES -----------------"

for item in doc.ents:
    print item.text, item.label_






# Patterns to look for
# 1 - We ws You: Comparison
# 2 - Direct Speech (verbs)
# 3 - Descriptive: Lots of Adjectives
# 4 - Metaphors
# 5 - Present & Future tenses
