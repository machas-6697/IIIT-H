import pandas as pd
from datasets import Dataset, ClassLabel

dff=pd.read_csv('path/directory/file.csv', names=["id", "text", "label"])

dff['source'] = ["csv_file_name"] * dff.shape[0]

# dff is a pandas Dataframe
# Convert the dataframes to Hugging Face Datasets
def convert_to_dataset(df):
    dataset = Dataset.from_pandas(df)
    features = dataset.features.copy()
    # label column will be identified as ClassLabel type
    features["label"] = ClassLabel(names=['OAG', 'CAG', 'NAG'])
    dataset = dataset.cast(features)
    return dataset

daataset = convert_to_dataset(dff)
# now daataset is a hugging face dataset

print(dff.dtypes)
print(daataset.features['label'])

mapping = {0: 'OAG', 1: 'CAG', 2: 'NAG'} 
# replacing the numerical values in the label column of daataset with the real labels OAG, CAG and NAG

daataset_df = daataset.to_pandas()
# now daataset_df is a pandas DataFrame

# Replace the values in the label column using the mapping dictionary
# daataset_df label column now has this labels as OAG, CAG and NAG
daataset_df['label'] = daataset_df['label'].map(mapping)

# Save the updated dataset to a new CSV file
new_csv_path = 'path/directory/output_file.csv'
daataset_df.to_csv(new_csv_path, index=False)
print(f"Updated dataset saved to: {new_csv_path}")
