import json
#Read a json file 
def input_file(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data
#Extract Json data and Find out Each of Key's Datatype 
def skeleton(json_data):
    skeleton_dict = dict()
    for key,value in json_data.items():
        #isinstance() method use of find out current object type..
        if isinstance(value,list):
            empty_list = []
            for v in value:
                if isinstance(v,dict):
                    empty_list.append(skeleton(v))
                else:
                    empty_list.append(type(v).__name__)
            skeleton_dict[key] = empty_list
        elif isinstance(value,dict):
            skeleton_dict[key] = skeleton(value)
        else:
            skeleton_dict[key] = type(value).__name__

    return skeleton_dict
#Convert a python to json file
def convert_datatype_json_file(processed_data):
    with open("Zomato_skeleton.json" , "w") as file:
        json.dump(processed_data,file,indent=4)


file=input("enter file name: ")
data_file_input=input_file(file)
extracted=skeleton(data_file_input)
convert_datatype_json_file(extracted)