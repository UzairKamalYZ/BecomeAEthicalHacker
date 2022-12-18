#!/bin/python3
#Imporinting
print("Importing is important guys")
import sys 
movie = ["A", "B","C"]
person = ["1", "2", "3"]
combine = zip(movie,person)
movie_dict= {key: value for key, value in combine}
print(movie_dict)
