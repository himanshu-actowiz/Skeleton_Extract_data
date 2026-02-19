import json
#Read a json file 
def input_file(json_file):
    with open(json_file, 'rb') as f:
        data = json.loads(f.read().decode())
        
        return data
#Extract Json data and Find out Each of Key's Datatype 
def skeleton(json_data):

    if isinstance(json_data, dict):
        skeleton_dict = {}
        for key, value in json_data.items():
            skeleton_dict[key] = skeleton(value)
        return skeleton_dict
    
    elif isinstance(json_data, list):
        return [skeleton(item) for item in json_data]
    
    else:
        return type(json_data).__name__

#Convert a python to json file
def convert_datatype_json_file(processed_data):
    with open("Zomato_skeleton.json" , "w") as file:
        json.dump(processed_data,file,indent=4)


file=input("enter file name: ")
data_file_input=input_file(file)
extracted=skeleton(data_file_input)
convert_datatype_json_file(extracted)