import subprocess

def execute_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    # List of script paths
    script_paths = [
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\modify.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\music_writer.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\1.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\2.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\modify.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\curr.py", 
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\modify_data_to_clips_control.py",
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\transfer.py",
        # Add more script paths as needed
    ]

    # Execute each script
    for path in script_paths:
        execute_python_script(path)
