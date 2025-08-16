import csv
import pickle
import pandas as pd
from datasets import Dataset, ClassLabel

# Load the data from the .pkl file
filename = "path/directory/data.pkl"
with open(filename, "rb") as f:
    data = pickle.load(f)

print(type(data))

# Open the CSV file in write mode
with open('humor_output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["Text", "Lang", "Label"])
    
    # Iterate over the data
    for sublist in data:
        words = ' '.join([tup[0] for tup in sublist if isinstance(tup, tuple)])
        labels = ' '.join([tup[1] for tup in sublist if isinstance(tup, tuple)])
        number = sublist[-1] if isinstance(sublist[-1], int) else 'N/A'
        
        # Write the row to the CSV
        writer.writerow([words, labels, number])



dff=pd.read_csv('path/directory/humor_output.csv')

# dff is a pandas Dataframe
# Convert the dataframes to Hugging Face Datasets
def convert_to_dataset(df):
    dataset = Dataset.from_pandas(df)
    features = dataset.features.copy()
    # label column will be identified as ClassLabel type
    features["Label"] = ClassLabel(names=['0', '1'])
    dataset = dataset.cast(features)
    return dataset

daataset = convert_to_dataset(dff)
# now daataset is a hugging face dataset

print(dff.dtypes)
print(daataset.features['Label'])

mapping = {0: '0', 1: '1'} 

daataset_df = daataset.to_pandas()
# now daataset_df is a pandas DataFrame

# Replace the values in the label column using the mapping dictionary
# daataset_df label column now has this labels as OAG, CAG and NAG
daataset_df['Label'] = daataset_df['Label'].map(mapping)

# Save the updated dataset to a new CSV file
new_csv_path = 'path/directory/final_file.csv'
daataset_df.to_csv(new_csv_path, index=False)
print(f"Updated dataset saved to: {new_csv_path}")