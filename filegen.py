import os
import time

# Specify the directory where you want to create the files
directory = "output"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Loop to create 1000 files
for i in range(1, 10001):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(directory, file_name)
    
    # Create an empty file
    with open(file_path, 'w') as f:
        f.write(f"This is file number {i}\n")
    if i % 1000 == 0:
        print(f"I is {i} going to sleep for 20 minutes.")
        print(f"1000 files have been created in '{directory}'.")
        # Sleep for 20 minutes (1200 seconds)
        time.sleep(1200)
