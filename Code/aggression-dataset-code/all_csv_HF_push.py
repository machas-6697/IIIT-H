import os
from huggingface_hub import HfApi, login
import pandas as pd
from datasets import Dataset
import glob

# Get a list of all CSV files
csv_files = glob.glob('path/directory/*.csv')

# Initialize an empty list to hold dataframes
dataframes = []

# Load each CSV file into a dataframe and append to the list
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Convert the combined dataframe to a Hugging Face dataset
dataset = Dataset.from_pandas(combined_df)

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'yourtoken'
login('yourtoken', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=True)

upload_dataset(dataset, "yourHFusername/HF-repo-name")
