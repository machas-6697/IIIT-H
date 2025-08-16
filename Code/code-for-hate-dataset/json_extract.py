import json

def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    features = [{'id': item['id'], 'id_str': item['id_str'], 'full_text': item['full_text']} for item in data]
    return features

def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Example usage
input_file_path = "directorypath/inputfile.json"
output_file_path = "directorypath/outputfile.json"

# Parse the input JSON file to extract features
features = parse_json(input_file_path)

# Save the extracted features to a new JSON file
save_to_json(features, output_file_path)

print(f"Extracted features saved to {output_file_path}")

