# from extract import extractData
#
# authorDict = extractData()
#
# print('hi')

from markov_CIP1_CIP2 import *

test1 = markov()
test1.set_aut_dir('resources')
# test1.set_auteurs()
test1.ngram = 1
test1.set_ponc(False)
test1.analyze()
test1.get_nth_element('Voltaire',4)

test1.gen_text("Balzac",100,"texttry.txt")

print("test")