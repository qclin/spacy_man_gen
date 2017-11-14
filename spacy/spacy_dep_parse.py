from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle

nlp = spacy.load('en')

# ###### get the tags of a sample sentence
def parse_sen():
    sentence = "You have not engaged in our great and gathering conversation, nor did you create the wealth of our marketplaces."
    print sentence
    doc = nlp(sentence)
    for item in doc:
      print item.text, item.dep_

parse_sen()
