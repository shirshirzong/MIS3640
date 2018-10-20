import os
# print(os.getcwd())
# fout = open('session14/output.txt','a')

# line1 = 'How many roads must a man walk down \n'
# fout.write(line1)

# line2 = 'Before you call him a man?\n'
# fout.write(line2)
# fout.close()

# print(os.path.abspath('session14/output.txt'))
# print(os.path.exists('session14/output.txt'))

import pickle

t2 = pickle.load(open('save.p','rb'))
print(t2)