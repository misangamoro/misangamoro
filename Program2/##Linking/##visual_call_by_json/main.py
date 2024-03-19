import json

def merge_data(file1, file2, file3):
    # Read data from file1.json
    with open(file1, 'r') as f1:
        data1 = json.load(f1)["animations"]

    # Read data from file2.json
    with open(file2, 'r') as f2:
        data2 = json.load(f2)["animations"]

    # Read data from file3.json
    with open(file3, 'r') as f3:
        data3 = json.load(f3)["animations"]

    # Default constants for missing data
    default_data = {
        "image_path": "C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Image\\Charectes\\comment.png",
        "text1": "Hello Animation 1",
        "text2": "Hello2 Animation 1",
        "delay_text_duration": 2,
        "text_display_duration": 3,
        "font_size1": 80,
        "font_size2": 80,
        "font_color1": [86, 86, 86, 255],
        "font_color2": [255, 0, 0, 255], #red
        # "font_color2": [59, 62, 128, 255],  #defalut blue
        # "font_color2": [44, 31, 98, 255],
        # "font_path": "C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Font\\Mentimun.ttf",
        # "font_path": "C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Font\\Om Botak.ttf",  
        "font_path": "C:\\Users\\Sumit\\Desktop\\Online\\Visuals Production\\Assest\\Font\\Tealand.ttf",
        "text1_position": [350, 290],
        "text2_position": [350, 420]
    }

    # Merge data from all three files
    merged_data = []
    for d1, d2, d3 in zip(data1, data2, data3):
        merged_entry = {**default_data, **d1, **d2, **d3}
        merged_data.append(merged_entry)

    # Write the merged data to output.json
    output_data = {"animations": merged_data}
    with open(r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\##visual_call_by_json\brighed\output.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=2)

if __name__ == "__main__":
    file1 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\size_with_position_data_bridge\out\file.json'
    file2 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\text_with_image_data_bridge\out\file.json'
    file3 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\time_with_visuals_data_bridge\out\output.json'
    merge_data(file1, file2, file3)
