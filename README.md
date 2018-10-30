# CustomNamedEntityRecognizer
Trained using Supervised Learning

Implementing NER with Stanford NER / NLTK

1. Because Stanford NER tagger is written in Java, you are going to need a proper Java Virtual Machine to be installed on your computer.

To do so, install Java JRE 8 or higher. You can install Java JDK (developer kit) if you want because it contains JRE. For Linux users, you will find all needed information on this guide on How To Install Java with Apt-Get on Ubuntu 16.04. For other users, please have a look at Java official documentation.

2. Get Stanford NER Tagger. Download zip file stanford-ner-xxxx-xx-xx.zip: see ‘Download’ section from The Stanford NLP website.

Unzip it and move ner-tagger ner-tagger.jar and gzipped English model english.all.3class.distsim.crf.ser.gz to your application folder:

3.We now have two files in our stanford-ner-tagger folder:

ner-tagger.jar: NER tagger engine properly said ;
ner-model-english.ser.gz : NER model trained on an english corpus.gi
Copy the following ner_english.py script to perform english Named Entities Recognition:
->run it

4.Training our own model
Now, you know how to run NER on an English corpus.

You need to train your own model. To do so, create a sampledataset.tsv file in {yourAppFolder}/stanford-ner-tagger/train with the following syntax:
->Create a prop.txt file in the same folder too and train it

5.This should output dummy-ner-model-indian.ser.gz file. Create a new mainPython.py script to use it:
->run it and check out the output.

6.I just ran with sampledataset and checked the output as because my system is getting crashed for large dataset.I have mentioned large dataset as originaldatasets  i.e:(ner_dataset and indiannames)
check this out.we will get very good accuracy

## Dependencies

1. Scikit-learn
2. NLTK
