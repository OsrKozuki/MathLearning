import os

### Consider that the 

# This will print the absolute path of the current file, in this case testing.py
base = os.path.abspath(__file__)
print("The current file path is", base, "\n")

# Now I will print working directory
print("The current directory is ", os.path.abspath("."), "\n")

# Print the parent working directory
print("Idk what is this, seems to be the parent directory, probably due to environment variable", os.path.abspath(".."))

# Combination of both
print("This... ", os.path.dirname(base))
print("This... ", os.path.dirname(__file__)) # <<<<< This is the one that I need. 
print("This... ", os.path.join(os.path.dirname(__file__), "tempFiles"))  # <<< And this was the relative function that should work in ALL machines, I do not care if it is Linux, Mac or Windows. 

