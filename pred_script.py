import json

input_file = "output/baseline-llama-3-8b-instruct.jsonl"
output_file = "output/predictions.jsonl"
predictions = []

with open(input_file, "r") as f:
    for line in f:
        try:
            entry = json.loads(line.strip())
            
            subject_entity = entry["SubjectEntity"]
            relation = entry["Relation"]
            object_entities_id = entry["ObjectEntitiesID"]
            
            prediction = {
                "SubjectEntity": subject_entity,
                "Relation": relation,
                "ObjectEntitiesID": object_entities_id
            }
            
            predictions.append(prediction)
        
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON on line: {line.strip()}. Error: {e}")
        except KeyError as e:
            print(f"Missing required field in JSON on line: {line.strip()}. Key Error: {e}")

with open(output_file, "w") as f:
    for pred in predictions:
        f.write(json.dumps(pred) + "\n")

print(f"Predictions written to {output_file}")
