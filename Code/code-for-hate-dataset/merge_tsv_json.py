import json
import csv

# Function to load the JSON file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Function to load the TSV file and create a mapping of id_str to labels
def load_tsv(file_path):
    id_to_label = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            id_str, label = row
            id_to_label[id_str.strip()] = label.strip()
    return id_to_label

# Function to merge JSON data with labels from TSV
def merge_data(json_data, id_to_label):
    for item in json_data:
        id_str = item['id_str']
        if id_str in id_to_label:
            item['label'] = id_to_label[id_str]
        else:
            item['label'] = None  # or any other default value if not found
    return json_data

# Function to save the merged data back to a JSON file
def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# File paths
json_file_path = 'path/directory/extractedjsonfile.json'
tsv_file_path = 'path/directory/tsvfile.tsv'
output_json_file_path = 'path/directory/merged_output.json'

# Load the files
json_data = load_json(json_file_path)
id_to_label = load_tsv(tsv_file_path)

# Merge the data
merged_data = merge_data(json_data, id_to_label)

# Save the merged data to a new JSON file
save_json(merged_data, output_json_file_path)

print(f"Merged data has been saved to {output_json_file_path}")
