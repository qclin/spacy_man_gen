from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle

nlp = spacy.load('en')

# ###### get the tags of a sample sentence
def parse_sen():
    sentence = "To tell the truth is not a crime."
    print sentence
    doc = nlp(sentence)
    for item in doc:
      print item.text, item.pos_, item.tag_, item.dep_

parse_sen()
