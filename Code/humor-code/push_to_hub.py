import os
from huggingface_hub import HfApi, login
import pandas as pd
from datasets import Dataset

df = pd.read_csv("path/directory/final_file.csv")

dataset = Dataset.from_pandas(df)
# dataset is a hugging face dataset

# Set up Hugging Face API token and log in
os.environ['HF_TOKEN'] = 'your_HF_token'
login('your_HF_token', add_to_git_credential=True)

#Upload the dataset to Hugging Face Hub
def upload_dataset(dataset_dict, repo_name):
    api = HfApi()
    user_info = api.whoami(token=os.getenv('HF_TOKEN'))
    print(user_info)
    
    dataset_dict.push_to_hub(repo_name, private=False)

upload_dataset(dataset, "HF_username/HF_repo_name")
