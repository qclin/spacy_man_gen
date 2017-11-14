# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle
from spacy.symbols import nsubj

nlp = spacy.load('en_core_web_sm')

# load and feed text in right format
text = sys.stdin.read().decode('utf8', errors="ignore")
doc = nlp(text)

adverbs = [item.text for item in doc if item.pos_ == 'ADV']
gerunds = [item.text for item in doc if item.tag_ == 'VBG']
entities = [item.text for item in doc.ents]
# for item in doc.noun_chunks:
#     print len(item.text.split(' '))


def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

noun_phrase = [item.text.strip() for item in doc.noun_chunks if len(item.text.split(' ')) > 1]

subjects = []
for word in doc:
    if word.dep_ in ('nsubj', 'nsubjpass'):
        subjects.append(flatten_subtree(word.subtree))


prep_phrases = []
for word in doc:
    if word.dep_ == 'prep':
        prep_phrases.append(flatten_subtree(word.subtree))

verbs_non_modal = []

for item in doc:
    if item.pos_ == 'VERB':
      # print item.text, item.tag_
      if item.tag_ == 'MD':
        #   do nothing
        string = "useless"
      else:
        verbs_non_modal.append(item.text)

pronoun_possessive = [item.text for item in doc if item.tag_ == 'PRP$']
pronoun_personal = [item.text for item in doc if item.tag_ == 'PRP']
adjective_superlative = [item.text for item in doc if item.tag_ == 'JJS']
noun_singular = [item.text for item in doc if item.tag_ == 'NN']
noun_plural = [item.text for item in doc if item.tag_ == 'NNS']

verb_singular_third_present = [item.text for item in doc if item.tag_ == 'VBZ']
verb_non_third_present = [item.text for item in doc if item.tag_ == 'VBP']
infinitival_to = [item.text for item in doc if item.tag_ == 'TO']
verb_base = [item.text for item in doc if item.tag_ == 'VB']
verbs_modal = [item.text for item in doc if item.tag_ == 'MD']
determiner = [item.text for item in doc if item.tag_ == 'DT']
conjunction_sub_pre = [item.text for item in doc if item.tag_ == 'IN']
existential_there = [item.text for item in doc if item.tag_ == 'EX']
adjective_base = [item.text for item in doc if item.tag_ == 'JJ']
conjunction_coor = [item.text for item in doc if item.tag_ == 'CC']


def gen_three_adj():
    print ', '.join([choice(adjective_base), choice(adjective_base), choice(adjective_base)])
def gen_sentence_a():
    string = "Our highest priority is to satisfy the customer through early and continuous delivery of valuable software"
    print ' '.join([choice(pronoun_possessive), choice(adjective_base), choice(noun_singular)]),
    print ' '.join([choice(verb_singular_third_present),choice(infinitival_to)]),
    print ' '.join([choice(verb_base), choice(determiner), choice(noun_singular)]),

    print ' '.join([choice(conjunction_sub_pre), choice(adjective_base), choice(conjunction_coor), choice(adjective_base), choice(noun_singular)]),
    print ' '.join([choice(conjunction_sub_pre), choice(adjective_base), choice(noun_singular)])
    # print '----------------------------------------------'

def gen_sentence_b():
    string = "You claim there are problems among us that you need to solve."
    for i in range(20):
        print ' '.join(["You", choice(verb_base), choice(adverbs)]),
        print ' '.join([choice(verb_non_third_present), choice(noun_plural), choice(conjunction_sub_pre)]),
        print ' '.join(["our", choice(conjunction_sub_pre), choice(pronoun_personal)]),
        print ' '.join([choice(verb_non_third_present), choice(infinitival_to), choice(verb_base)])


def gen_sentence_c():
        print ' '.join(["You", choice(verb_non_third_present), choice(noun_phrase)])


def gen_sentence_d():
        # DT + NN + MD + VB + NNS
        # noun_singular maybe replace with entity
        print ' '.join([choice(determiner), choice(noun_singular), choice(verbs_modal)]),
        print ' '.join([choice(verb_base), choice(noun_plural)])


def gen_sentence_e():
    # TO + VB + DT + NN + VBZ + RB + DT + NN
    # [this is not that] should try to use antynomns
    print ' '.join([choice(infinitival_to), choice(verb_base), choice(determiner)]),
    print ' '.join([choice(noun_singular), "is not "]), #choice(verb_non_third_present), choice(adverbs)
    # print ' '.join([choice(determiner), choice(noun_singular)])
    print choice(subjects)

# kaomoji = [  "__φ(．．)", "( ￣ー￣)φ__",	"__φ(。。)",	"__φ(．．;)", "ヾ( `ー´)シφ__", "__〆(￣ー￣ )", "....φ(・∀・*)", "___〆(・∀・)", "( ^▽^)ψ__", "....φ(︶▽︶)φ....", "( . .)φ__	", "__φ(◎◎ヘ)"]


for i in range(21):
    print "\n  ---------------- Manifesto for the noble self ----------------  \n"
    gen_sentence_a()
    gen_sentence_d()
    gen_sentence_a()
    gen_three_adj()
    gen_sentence_d()
    gen_sentence_d()
