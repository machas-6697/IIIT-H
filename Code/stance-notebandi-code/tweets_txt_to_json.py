import json

def convert_txt_to_json(txt_file, json_file):
    data = []
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            id_line = lines[i].strip()
            # Check if the line is not empty
            if id_line:
                try:
                    id = int(id_line)  # Convert id to integer
                except ValueError:
                    print(f"Invalid id '{id_line}' at line {i+1}")
                    i += 1
                    continue
                i += 1
                text = ""  # Initialize text as empty
                if i < len(lines):  # Check if there is a next line
                    text_line = lines[i].strip()
                    if text_line:  # Check if the next line is not empty
                        text = text_line
                        i += 1
                data.append({"id": id, "text": text})
            else:  # If the line is empty, skip it
                i += 1
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Call the function
convert_txt_to_json('path/directory/Notebandi_tweets.txt', 'path/directory//Notebandi_tweets.json')
