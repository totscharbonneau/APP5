# from extract import extractData
#
# authorDict = extractData()
#
# print('hi')

from markov_CIP1_CIP2 import *

test1 = markov()
test1.set_aut_dir('resources')
test1.set_ponc(False)
test1.analyze()
