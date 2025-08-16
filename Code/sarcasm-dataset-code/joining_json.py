import json

# Function to merge dictionaries based on a common key
def merge_json_files(files, common_key):
    merged_data = {}

    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            for item in data:
                key_value = item[common_key]
                if key_value not in merged_data:
                    merged_data[key_value] = {}
                merged_data[key_value].update(item)

    # Convert the merged data back to a list for final JSON output
    merged_list = list(merged_data.values())

    return merged_list

# List of JSON files to merge
json_files = ['path/directory/tweets.json', 'path/directory/tweet_truth.json', 'path/directory/tweets_with_language.json']
common_key = 'id'

# Merge the files
merged_data = merge_json_files(json_files, common_key)

# Write the merged data to a new JSON file
with open('path/directory/merged_file.json', 'w') as f:
    json.dump(merged_data, f, indent=4)

print("Merged JSON file created successfully.")
