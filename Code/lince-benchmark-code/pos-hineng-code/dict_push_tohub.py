import json
import os
from huggingface_hub import HfApi, login
import pandas as pd
from datasets import Dataset, DatasetDict

def json_to_dataframe(file_path):
      with open(file_path, "r", encoding="utf-8") as file:
           data = json.load(file)
      df = pd.DataFrame(data)
      return df

# Convert JSON files to Hugging Face Datasets
dev_df = json_to_dataframe("path/directory/dev.json")
train_df = json_to_dataframe("path/directory/train.json")
test_df = json_to_dataframe("path/directory/test.json")

dev_dataset = Dataset.from_pandas(dev_df)
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# Combine datasets into a DatasetDict
dataset_dict = DatasetDict({
    "dev": dev_dataset,
    "train": train_dataset
})

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'your-HF-token'
login('your-HF-token', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=False)

upload_dataset(dataset_dict, "HF-username/HF-repo-name")

daataset_dict = DatasetDict({
    "test": test_dataset
})

upload_dataset(daataset_dict, "HF-username/HF-repo-name")
