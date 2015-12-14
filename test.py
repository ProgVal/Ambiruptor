#!/usr/bin/python3

import os.path, re

from ambiruptor.data_mining.wikipedia import DataMining
from ambiruptor.feature_extraction.part_of_speech import FeatureExtraction
from ambiruptor.learning import Learning

print("--------- Data Mining ---------")
data = DataMining()

if not os.path.isfile("data/wikidump.xml") :
    raise Exception("Use the Makefile !")

if not os.path.isfile("data/wikilinks.bin") :
    data.build("data/wikidump.xml")
    data.export("data/wikilinks.bin")
else :
    data.load("data/wikilinks.bin")

print(data.get_corpus("Bar"))


print("--------- feature Extraction ---------")

s = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
       sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
feature = FeatureExtraction()
print(feature.extract(s, 3))


print("--------- Learning ---------")

learning = Learning()
