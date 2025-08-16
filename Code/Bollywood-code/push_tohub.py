import json
import os
from huggingface_hub import HfApi, login
import pandas as pd
from datasets import Dataset

def json_to_dataframe(file_path):
      with open(file_path, "r", encoding="utf-8") as file:
           data = json.load(file)
      df = pd.DataFrame(data)
      return df

# Convert JSON files to Hugging Face Datasets
df = json_to_dataframe("path/directory/Updated_Final_Key.json")
df_1 = json_to_dataframe("path/directory/Dialogue_Key.json")

dataset = Dataset.from_pandas(df)
dataset_1 = Dataset.from_pandas(df_1)

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'your-HF-token'
login('your-HF-token', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=False)

upload_dataset(dataset, "HFusername/HFreponame")

upload_dataset(dataset_1, "HFusername/HFreponame")
