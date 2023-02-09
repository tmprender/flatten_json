import sys
import json

GLOBAL_STRING = ""

def parse_json_to_string(json_data, path):
    global GLOBAL_STRING
    # base case
    if len(json_data.keys()) < 1:
        return GLOBAL_STRING

    # full path to key-value pair
    parent = ""
    
    for key in json_data.keys():
        # check for nested json block
        if type(json_data[key]) is dict:
            # store path to this nested block as its parent
            parent = path
            # build path.to.key=values as string
            path += key + "."

            ### for debugging.. ###
            #print("TMP PATH: ", path)
            #print("SENDING -> ", json_data[key])
            ### --------------- ###

            # recurse until value is non-dict
            parse_json_to_string(json_data[key], path)
            # reset path for this loop now that method has returned
            path = parent

        # not nested, write path.to.key=value pair(s) for this block
        else:
            #print("ADDING TO STRING ::: ", path, key, json_data[key], "\n")
            GLOBAL_STRING += path + key + "="
            GLOBAL_STRING += str(json_data[key]) + "\n"

    # return to caller
    #print("parent: ", parent, "path: ", path)
    print("RESULT:")
    print(GLOBAL_STRING)
    return GLOBAL_STRING

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        s = f.read()

    j = json.loads(s)  # oh the irony
    parse_json_to_string(j, "")
