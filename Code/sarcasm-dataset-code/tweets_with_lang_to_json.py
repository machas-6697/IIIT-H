import json

def convert_txt_to_json(txt_file, json_file):
    data = []
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            id_line = lines[i].strip()
            try:
                # Try to convert the line to an integer
                id = int(id_line)
                langid = [[], []]
                i += 1
                while i < len(lines) and not lines[i].strip().isdigit():  # Continue until the next ID or the end of the file
                    words = lines[i].split()
                    if len(words) == 2:  # Check if the line contains two words
                        langid[0].append(words[0])
                        langid[1].append(words[1])
                    i += 1
                data.append({"id": id, "langid": langid})  # Use id instead of id_line
            except ValueError:
                # If the line cannot be converted to an integer, skip it
                i += 1
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Call the function
convert_txt_to_json('path/directory/tweets_with_language.txt', 'path/directory/tweets_with_language.json')
