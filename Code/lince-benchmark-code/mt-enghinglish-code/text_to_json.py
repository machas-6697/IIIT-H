import json

# Function to convert dev.txt and train.txt to JSON format
def convert_dev_train_to_json(file_path, output_file):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english, hinglish = line.strip().split('\t')
            data.append({"english": english, "hinglish": hinglish})
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Function to convert test.txt to JSON format
def convert_test_to_json(file_path, output_file):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english = line.strip()
            data.append({"english": english})
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Convert the files
convert_dev_train_to_json('path/directory/dev.txt', 'path/directory/dev.json')
convert_dev_train_to_json('path/directory/train.txt', 'path/directory/train.json')
convert_test_to_json('path/directory/test.txt', 'path/directory/test.json')
