def replace_word_in_file(file_path):
    replacement_word = "happy"
    words_to_check = ["happy", "sad", "realization", "fear", "sadxx", "nani", "happyaa", "byby", "anger", "ahhh"]

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            line_modified = False
            for word in words_to_check:
                if word in line:
                    line_modified = True
                    break
            if not line_modified:
                line = replacement_word + '\n'
            file.write(line)



file_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\inputsoundmodify.txt" 
replace_word_in_file(file_path)
