# import os
# import subprocess
# import threading
# import tkinter as tk
# from tkinter import messagebox

# # Function to execute a Python script
# def run_script(script_path):
#     try:
#         subprocess.run(["python", script_path], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running script {script_path}: {e}")
#         # Handle error as needed

# # Function to read the number of cycles from a text file
# def read_cycle_count(file_path):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             return int(file.read().strip())
#     else:
#         return 1  # Default to running scripts once if the file doesn't exist

# # List of script paths in the order you want to execute them
# script_paths = [
#     r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Delete_component.py',
#     r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\main.py",
#     r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#No._of_rep\main.py"
# ]

# # Function to run scripts sequentially for a given number of cycles
# def run_scripts_cyclically(cycles):
#     for _ in range(cycles):
#         for script_path in script_paths:
#             run_script(script_path)

#     # Display a message when all scripts are executed
#     messagebox.showinfo("Scripts Completed", f"All scripts have been executed {cycles} times.")

# # Function to run scripts in the background using threads
# def run_scripts_in_background(cycle_count):
#     background_thread = threading.Thread(target=run_scripts_cyclically, args=(cycle_count,))
#     background_thread.start()

# # Create a tkinter root window (this will be hidden)
# root = tk.Tk()
# root.geometry("1x1")  # Set the window size to 1x1 pixel
# root.withdraw()  # Hide the window

# # Specify the path to the text file containing the cycle count
# cycle_count_file_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#No._of_rep\out\count.txt'

# # Read the cycle count from the text file
# cycle_count = read_cycle_count(cycle_count_file_path)

# # Run scripts in the background for the specified number of cycles
# run_scripts_in_background(cycle_count)

# # Start the tkinter event loop (this keeps the program running in the background)
# root.mainloop()


import subprocess

def execute_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    # List of script paths
    script_paths = [
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Delete_component.py',
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\main.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#No._of_rep\main.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Sound_define\1.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Sound_define\2.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Sound_define\3.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Sound_define\4.py",
    ]

    # Execute each script
    for path in script_paths:
        execute_python_script(path)
