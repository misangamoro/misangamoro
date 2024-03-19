def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    values = eval(data)  # Assuming the input format is valid and can be safely evaluated as a Python expression

    with open(output_file, 'w') as file:
        for i in range(0, len(values), 4):
            value_set = values[i:i+4]
            
            file.write("open: {},".format(value_set[0]))
            file.write("\ntext: {}, {},".format(value_set[1], value_set[2]))
            file.write("\nclose: {},".format(value_set[3]))
            
            if i + 4 >= len(values):
                file.write("\ntotal: {}".format(values[-1]))
            else:
                file.write("\n\n")

if __name__ == "__main__":
    input_filename = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\p_individual_sum\out\output.txt"
    output_filename = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\z_created\out\output.txt"
    process_data(input_filename, output_filename)
