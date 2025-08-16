import pandas as pd
from datasets import Dataset, ClassLabel
import json

# Load JSON into pandas DataFrame
df = pd.read_json('path/directory/merged_file.json')

# Convert pandas DataFrame to Hugging Face Dataset
def convert_to_dataset(df):
    dataset = Dataset.from_pandas(df)
    features = dataset.features.copy()
    # Define the label column as ClassLabel type
    features["label"] = ClassLabel(names=['NONE', 'FAVOR', 'AGAINST'])
    dataset = dataset.cast(features)
    return dataset

dataset = convert_to_dataset(df)

# Check data types and label feature
print(df.dtypes)
print(dataset.features['label'])

# Mapping dictionary for labels
mapping = {0: 'NONE', 1: 'FAVOR', 2: 'AGAINST'}

# Convert Hugging Face Dataset back to pandas DataFrame
dataset_df = dataset.to_pandas()

# Replace numerical labels with string labels
dataset_df['label'] = dataset_df['label'].map(mapping)

# Save the updated DataFrame to a new JSON file with the desired format
new_json_path = 'path/directory/stance_dataset.json'
dataset_df.to_json(new_json_path, orient='records', indent=4)
print(f"Updated dataset saved to: {new_json_path}")

def add_id_str_to_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
        updated_data = []
        for item in data:
            item["id_str"] = str(item["id"])  # Add "id_str" key with string value of "id"
            updated_item = {
                "id": item["id"],
                "id_str": item["id_str"],
                "text": item["text"],
                "label": item["label"],
                "langid": item["langid"]
            }
            updated_data.append(updated_item)
    
    with open(output_file, 'w') as f:
        json.dump(updated_data, f, indent=4)

# Example usage:
input_file = 'path/directory/stance_dataset.json'
output_file = 'path/directory/final_stance_dataset.json'
add_id_str_to_json(input_file, output_file)




