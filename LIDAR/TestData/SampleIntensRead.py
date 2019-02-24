#This is how we can pretend the .txt files are LIDAR readings

import numpy as np

def sampleIntensRead(fileName):
    #This function will read the text files generated by "GenerateSampleIntens.py" and put them in a 
    #   numpy array as if they had just been read from the LIDAR

    rocks = []
    elements = []

    with open(fileName, 'r') as file:
        for line in file:
            elements = line.split(",")
            rocks.append(float(elements[0]), float(elements[1]), float(elements[2]))      

    return np.array(rocks)        #turn into a numpy array before return