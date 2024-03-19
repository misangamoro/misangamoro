def calculate_cumulative_sum(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            data = [float(line.strip()) for line in input_file.readlines()]

        cumulative_sum = [str(sum(data[:i + 1])) for i in range(len(data))]

        with open(output_filename, 'w') as output_file:
            output_file.write(','.join(cumulative_sum))

        print(f"Cumulative sum successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File {input_filename} not found.")


# Example usage:
input_file = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\openned_data\out\combined_values.txt'
output_file = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\p_individual_sum\out\output.txt'
calculate_cumulative_sum(input_file, output_file)
