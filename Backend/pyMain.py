import os

# Initial information
base_dir = os.path.dirname(os.path.abspath(__file__))


print("Starting Python Code")
### Just in case something went wrong during the pulling
f = open(os.path.join(os.path.dirname(__file__), "tempFiles/tempText.txt"), "w")
f.write("Hello Team, this is just the beginning!!!! \n");
f.close()