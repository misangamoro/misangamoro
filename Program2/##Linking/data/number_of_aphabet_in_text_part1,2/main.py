import os
import string

def count_alphabets(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        alphabet_count = sum(c.isalpha() or c.isspace() or c in string.punctuation for c in content)
    return alphabet_count

def process_folder():
    input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data\out"  # Replace this with the actual folder path
    output_folder = os.path.join(input_folder, r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\number_of_aphabet_in_text_part1,2\no_of_words')
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)

            alphabet_count = count_alphabets(file_path)

            with open(output_file_path, 'w') as output_file:
                output_file.write(str(alphabet_count))

if __name__ == "__main__":
    process_folder()
    print("Process completed. Check the 'output' folder for the result.")
