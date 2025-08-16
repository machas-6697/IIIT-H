import json

def parse_conll(filename):
    segments = []
    current_segment = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("# sent_enum ="):
                if current_segment:
                    segments.append(current_segment)
                segment_id = line
                current_segment = {'id': segment_id, 'text': [], 'label1': [], 'label2': []}
            elif line:
                parts = line.split()
                if len(parts) == 3:
                    current_segment['text'].append(parts[0])
                    current_segment['label1'].append(parts[1])
                    current_segment['label2'].append(parts[2])
                elif len(parts) == 2:
                    current_segment['text'].append(parts[0])
                    current_segment['label2'].append(parts[1])

    if current_segment:
        segments.append(current_segment)

    return segments

def parse_test_conll(filename):
    segments = []
    current_segment = {'text': [], 'label': []}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                if current_segment['text'] or current_segment['label']:
                    segments.append(current_segment)
                current_segment = {'text': [], 'label': []}
            else:
                parts = line.split()
                if len(parts) == 2:
                    current_segment['text'].append(parts[0])
                    current_segment['label'].append(parts[1])

    if current_segment['text'] or current_segment['label']:
        segments.append(current_segment)

    return segments

def convert_to_json(input_filename, output_filename, is_test=False):
    if is_test:
        segments = parse_test_conll(input_filename)
    else:
        segments = parse_conll(input_filename)
    
    with open(output_filename, 'w') as json_file:
        json.dump(segments, json_file, indent=4)

# Convert dev.conll and train.conll
convert_to_json('path/directory/dev.conll', 'path/directory/dev.json')
convert_to_json('path/directory/train.conll', 'path/directory/train.json')

# Convert test.conll
convert_to_json('path/directory/test.conll', 'path/directory/test.json', is_test=True)
