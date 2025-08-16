import json

segments = []

with open('path/directory/data.txt', 'r', encoding='utf-8') as f:
    # Initialize empty lists for the current segment
    words = []
    label1 = []
    label2 = []
    # Read the file line by line
    for line in f:
        # Strip the line to remove any leading or trailing whitespace
        stripped_line = line.strip()
        # If the line is not blank and contains a tab character
        if stripped_line and '\t' in stripped_line:
            parts = stripped_line.split('\t')
            # Ensure the line splits into exactly three parts
            if len(parts) == 3:
                word, lbl1, lbl2 = parts
                words.append(word)
                label1.append(lbl1)
                label2.append(lbl2)
        else:
            # If the line is blank, it means the current segment has ended
            if words or label1 or label2:
                # Add the current segment to the list of all segments
                segments.append({'words': words, 'label1': label1, 'label2': label2})
                # Reset the lists for the next segment
                words = []
                label1 = []
                label2 = []
    # Don't forget to add the last segment if the file doesn't end with a blank line
    if words or label1 or label2:
        segments.append({'words': words, 'label1': label1, 'label2': label2})

# Write the list of all segments to a JSON file
with open('path/directory/data.json', 'w', encoding='utf-8') as f:
    json.dump(segments, f, ensure_ascii=False, indent=4)
