import pandas as pd
from datasets import Dataset, ClassLabel

# Load JSON into pandas DataFrame
df = pd.read_json('path/directory/merged_output.json')

# Ensure 'id_str' is treated as a string
df['id_str'] = df['id_str'].astype(str)

# Convert pandas DataFrame to Hugging Face Dataset
def convert_to_dataset(df):
    dataset = Dataset.from_pandas(df)
    features = dataset.features.copy()
    # Define the label column as ClassLabel type
    features["label"] = ClassLabel(names=['Normal Speech', 'Hate Speech'])
    dataset = dataset.cast(features)
    return dataset

dataset = convert_to_dataset(df)

# Check data types and label feature
print(df.dtypes)
print(dataset.features['label'])

# Mapping dictionary for labels
mapping = {0: 'Normal Speech', 1: 'Hate Speech'}

# Convert Hugging Face Dataset back to pandas DataFrame
dataset_df = dataset.to_pandas()

# Ensure 'id_str' is treated as a string after conversion
# this is because when converting a pandas DataFrame to a JSON file, pandas tries to infer the best data types for each column, which can sometimes lead to unexpected type conversions. In this case, it’s converting your id_str (which should remain a string) into a number because the values are numeric strings.
dataset_df['id_str'] = dataset_df['id_str'].astype(str)

# Replace numerical labels with string labels
dataset_df['label'] = dataset_df['label'].map(mapping)

# Save the updated DataFrame to a new JSON file with the desired format
new_json_path = 'path/directory/hate_dataset.json'
dataset_df.to_json(new_json_path, orient='records', indent=4)
print(f"Updated dataset saved to: {new_json_path}")