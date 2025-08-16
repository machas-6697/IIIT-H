import json
import os
from huggingface_hub import HfApi, login
import pandas as pd
from datasets import Dataset

with open("path/directory/combined_output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def json_to_dataframe():
      df = pd.DataFrame(data)
      return df

datafr = json_to_dataframe()
# Convert the dataframes to Hugging Face Datasets
hf_dataset = Dataset.from_pandas(datafr)

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'yourHFtoken'
login('yourHFtoken', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=False)

upload_dataset(hf_dataset, "HFusername/HFreponame")