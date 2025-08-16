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
dev_df_D = json_to_dataframe("path/directory/Devanagari/validation.json")
train_df_D = json_to_dataframe("path/directory/Devanagari/train.json")
test_df_D = json_to_dataframe("path/directory/Devanagari/test.json")

dev_df_R = json_to_dataframe("path/directory/Romanized/validation.json")
train_df_R = json_to_dataframe("path/directory/Romanized/train.json")
test_df_R = json_to_dataframe("path/directory/Romanized/test.json")

dev_dataset = Dataset.from_pandas(dev_df_D)
train_dataset = Dataset.from_pandas(train_df_D)
test_dataset = Dataset.from_pandas(test_df_D)

dev_daataset = Dataset.from_pandas(dev_df_R)
train_daataset = Dataset.from_pandas(train_df_R)
test_daataset = Dataset.from_pandas(test_df_R)


# Combine datasets into a DatasetDict
dataset_dict = DatasetDict({
    "dev_Devanagari": dev_dataset,
    "train_Devanagari": train_dataset,
    "test_Devanagari": test_dataset
})

daataset_dict = DatasetDict({
    "dev_Romanized": dev_daataset,
    "train_Romanized": train_daataset,
    "test_Romanized": test_daataset
})

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'yourHFtoken'
login('yourHFtoken', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=False)


upload_dataset(daataset_dict, "HFusername/HFreponame")

upload_dataset(dataset_dict, "HFusername/HFreponame")

