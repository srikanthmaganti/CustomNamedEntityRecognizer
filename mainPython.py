# coding: utf-8
import nltk
from nltk.tag.stanford import StanfordNERTagger

sentence = u"aman marched through London"

jar='C:\\Users\\DELL_PC\\Desktop\\ner\\stanford-ner.jar'
model='C:\\Users\\DELL_PC\\Desktop\\ner\\dummy-ner-model-indian.ser.gz'

# Prepare NER tagger with english model
ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

# Tokenize: Split sentence into words
words = nltk.word_tokenize(sentence)

# Run NER tagger on words
print(ner_tagger.tag(words))