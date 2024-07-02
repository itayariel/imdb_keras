import os
from time import sleep, time
from datetime import datetime

# Create 'output' folder if it doesn't exist
if not os.path.exists('output2'):
    os.makedirs('output2')
file_name = f"output2/file_50000.txt"
with open(file_name, 'w') as file:
    file.write(f"content")
print("finished writing")
