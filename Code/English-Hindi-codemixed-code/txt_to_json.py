import json

# File paths
t_en_path = 'path/directory/t-en.txt'
s_enhi_path = 'path/directory/s-enhi.txt'
output_json_path = 'path/directory/combined_output.json'

# Reading the contents of the files
with open(t_en_path, 'r', encoding='utf-8') as f:
    t_en_lines = f.readlines()

with open(s_enhi_path, 'r', encoding='utf-8') as f:
    s_enhi_lines = f.readlines()

# Combining the lines into a dictionary
combined_data = []
num_lines = min(len(t_en_lines), len(s_enhi_lines))  # Use the minimum number of lines
for i in range(num_lines):
    entry = {
        "english": t_en_lines[i].strip(),
        "hinglish": s_enhi_lines[i].strip()
    }
    combined_data.append(entry)

# Writing the combined data to a JSON file
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print(f"Data has been written to {output_json_path}")
