import json

def read_conll_file(file_path, output_path):
    data = []
    current_sentence = []
    current_labels = []
    current_id = None

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("# sent_enum"):
                if current_sentence:  # Save the previous sentence and labels
                    data.append({
                        "id": current_id,
                        "sentence": current_sentence,
                        "labels": current_labels
                    })
                    current_sentence = []
                    current_labels = []
                current_id = line  # Save the current id
            elif line:
                word, label = line.split()
                current_sentence.append(word)
                current_labels.append(label)
        
        if current_sentence:  # Save the last sentence and labels
            data.append({
                "id": current_id,
                "sentence": current_sentence,
                "labels": current_labels
            })

    with open(output_path, 'w', encoding='utf-8') as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=4)

def read_test_conll_file(file_path, output_path):
    data = []
    current_sentence = []
    current_id = None
    sent_enum_counter = 1  # Counter for generating ids for test set

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                current_sentence.append(line)
            else:
                if current_sentence:
                    current_id = f"# sent_enum = {sent_enum_counter}"
                    data.append({
                        "id": current_id,
                        "sentence": current_sentence
                    })
                    current_sentence = []
                    sent_enum_counter += 1
        
        if current_sentence:  # Save the last sentence
            current_id = f"# sent_enum = {sent_enum_counter}"
            data.append({
                "id": current_id,
                "sentence": current_sentence
            })

    with open(output_path, 'w', encoding='utf-8') as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=4)

# Paths to the CoNLL files and output JSON files
dev_file_path = 'path/directory/dev.conll'
test_file_path = 'path/directory/test.conll'
train_file_path = 'path/directory/train.conll'

dev_output_path = 'path/directory/dev.json'
test_output_path = 'path/directory/test.json'
train_output_path = 'path/directory/train.json'

# Convert files
read_conll_file(train_file_path, train_output_path)
read_conll_file(dev_file_path, dev_output_path)
read_test_conll_file(test_file_path, test_output_path)
