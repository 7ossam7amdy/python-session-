import os
filename =input ("Enter the file name: ")
targetRowCount = int(input("Enter the target row count: ")) 
while targetRowCount < 1:
    print("Target row count must be greater than 0.") 
    status = input("Do you want to enter the target row count again? (y/n): ")
    if status.lower() == 'n':
        exit()
    targetRowCount = int(input("Enter the target row count again: ")) 
for (i) in range(targetRowCount):
    print(f"Processing row {i+1}/{targetRowCount} ")
    
print("Processing complete.")