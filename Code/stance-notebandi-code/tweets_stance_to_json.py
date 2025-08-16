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
                i += 1
                if i < len(lines):  # Check if there is a next line
                    label_line = lines[i].strip()
                    data.append({"id": id, "label": label_line})  # Use id instead of id_line
                i += 1
            except ValueError:
                # If the line cannot be converted to an integer, skip it
                i += 1
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Call the function
convert_txt_to_json('path/directory/Notebandi_tweets_stance.txt', 'path/directory/Notebandi_tweets_stance.json')
