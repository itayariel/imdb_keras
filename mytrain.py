import os
from time import sleep, time
from datetime import datetime

# Create 'output' folder if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')
file_name = f"output/file_50000.txt"
with open(file_name, 'w') as file:
    file.write(f"content")
print("finished writing")
