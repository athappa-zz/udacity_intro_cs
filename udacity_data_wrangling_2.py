#Udacity Data Wrangling
#Lesson 2

import os
os.getcwd()


import pandas
baseball_data = pandas.read_csv("master.csv")
print baseball_data['name First']

baseball_data['height_plus_weight']