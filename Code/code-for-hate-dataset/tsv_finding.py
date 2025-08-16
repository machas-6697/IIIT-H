import csv

def find_row_by_id(file_path, search_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for line_number, row in enumerate(reader, start=1):
            if row[0].strip() == search_id.strip():
                return {'line_number': line_number, 'id': row[0], 'label': row[1]}
    return None

# Example usage
file_path = 'path/directory/tsvfile.tsv'
search_id = 'id'  # Replace with the ID you're searching for
# take an id from the json file and input here so you will understand where that id is present in this tsv file

row_content = find_row_by_id(file_path, search_id)
if row_content:
    print(f"Row content for ID {search_id} at line {row_content['line_number']}: {row_content}")
else:
    print(f"No row found with ID {search_id}")
