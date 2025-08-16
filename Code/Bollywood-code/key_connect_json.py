import json

# Load the JSON data from the first file
file_path = 'path/directory/Final_Key.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Movie name mapping from the second JSON file
movie_names = {
    "M_0": "ankhon-dekhi",
    "M_1": "d-day",
    "M_2": "dedh-ishqiya",
    "M_3": "dum-laga-ke-haisha",
    "M_4": "ek-main-aur-ekk-tu",
    "M_5": "kapoor-sons",
    "M_6": "koi-po-che",
    "M_7": "lootera",
    "M_8": "masaan",
    "M_9": "neerja",
    "M_10": "nh10",
    "M_11": "pink",
    "M_12": "queen",
    "M_13": "raman-raghavan-2-0",
    "M_14": "shahid",
    "M_15": "talvar",
    "M_16": "titli",
    "M_17": "udaan"
}

# Add the Movie_name key to each dictionary in the list
for entry in data:
    movie_key = entry.get("Movie")
    if movie_key in movie_names:
        entry["Movie_name"] = movie_names[movie_key]

# Save the updated JSON data to a new file
output_file = 'path/directory/Updated_Final_Key.json'
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Updated JSON file saved to: {output_file}")
