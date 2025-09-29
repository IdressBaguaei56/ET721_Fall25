"""
Idress Baguaei 
Lab 7, accessing data in a file 
Sep 29, 2025
"""
def testing():
    print("Idress Baguaei")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line  with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser 
    for each in fileuser:
        print(each)

