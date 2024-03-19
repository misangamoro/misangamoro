import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_to_tuples(obj):
    if isinstance(obj, list):
        return tuple(obj)
    elif isinstance(obj, dict):
        return {key: convert_to_tuples(value) for key, value in obj.items()}
    return obj

def compare_and_generate_output(text1, text2, input_data):
    output = {"animations": []}
    unique_items = set()

    for entry in input_data["text_duration"]:
        for key, duration in entry.items():
            output_item = {}
            
            if "part1" in key:
                # Compare against text1 for part1
                for range_key, values in text1.items():
                    range_start, range_end = map(int, range_key.split('-'))
                    if range_start <= duration <= range_end:
                        output_item["font_size1"] = values[0]["font_size1"]
                        output_item["text1_position"] = values[0]["text1_position"]
                        break
            elif "part2" in key:
                # Compare against text2 for part2
                for range_key, values in text2.items():
                    range_start, range_end = map(int, range_key.split('-'))
                    if range_start <= duration <= range_end:
                        if "font_size2" not in output_item:
                            output_item["font_size2"] = values[0]["font_size2"]
                            output_item["text2_position"] = values[0]["text2_position"]
                        else:
                            # Update font_size2 and text2_position if part2 has a different font size
                            if values[0]["font_size2"] != output_item["font_size2"]:
                                output_item["font_size2"] = values[0]["font_size2"]
                                output_item["text2_position"] = values[0]["text2_position"]
                        break

            # Convert the dictionary to a frozenset to check for uniqueness
            unique_item_set = frozenset(convert_to_tuples(output_item).items())

            # Append unique items only
            unique_items.add(unique_item_set)
            output["animations"].append(output_item)

    return output

# Read the input JSON files
text1_constant = read_json(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\data_on_animation\text1_constant.json")
text2_constant = read_json(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\data_on_animation\text2_constant.json")
input_data = read_json(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\data_on_words\input.json")

# Compare and generate the output
result = compare_and_generate_output(text1_constant, text2_constant, input_data)

# Remove empty values from the list
result["animations"] = [item for item in result["animations"] if item]

# Specify the location to save the output JSON file
output_file_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\out\output.json"

# Write the result to the output JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(result, output_file, indent=2)

print(f"Result has been saved to {output_file_path}")
