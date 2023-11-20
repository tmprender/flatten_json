import sys
import json

GLOBAL_STRING = ""
#DELIMITER = .

def parse_json_to_string(json_data, path, depth=0):
    global GLOBAL_STRING

    ### DEBUG ####
    #print("DATA: " + str(json_data) + "\nPATH: " + path)

    # handle json {}
    if type(json_data) is dict:
        # base case: no (more) keys to parse
        if len(json_data.keys()) < 1:
            return GLOBAL_STRING

        # store path for current run before updating
        parent = path
        
        for key in json_data.keys():
            # check for nested json block
            if type(json_data[key]) is dict:
                # build path.to.key=value as string
                path += key + "."
                # recurse until value is non-dict
                parse_json_to_string(json_data[key], path)
                # reset path for this loop now that method has returned
                path = parent

            # check for list
            elif type(json_data[key]) is list:
                # iterate thru elements - multiple counters
                #outter = 0
                for idx, i in enumerate(json_data[key]):
                    # check if nested as dict
                    if type(i) is dict:
                        # update path indicating list element
                        path +=  key + "[" + str(idx) + "]."
                        parse_json_to_string(i, path)
                        path = parent
                    # nested list
                    elif type(i) is list:
                        #depth = 0
                        path += key + "[" + str(depth) + "]"
                        parse_json_to_string(i, path, depth+1)
                        path = parent
                    # value within a list    
                    else:
                        
                        GLOBAL_STRING += path + key + "[" + str(depth) + "]="
                        GLOBAL_STRING += str(i) + "\n"
                        

            # not nested, write path.to.key=value pair(s) for this block
            else:
                GLOBAL_STRING += path + key + "="
                GLOBAL_STRING += str(json_data[key]) + "\n"

    # flatten list []
    elif type(json_data) is list:
        for i in json_data:
            if type(i) is dict or type(i) is list: 
                parse_json_to_string(i, path)
            else:
                GLOBAL_STRING += path + "[" + str(depth) + "]=" + str(i) + "\n"
                
                
    # return to caller
    return GLOBAL_STRING


if __name__ == "__main__":
    # is stdin a terminal? i.e. was last stdout piped here?
    if not sys.stdin.isatty():
        s = sys.stdin.read()

    # No, this script was called explicitly and passed a json string (hopefully). 
    # This should probably be an elif on len(argv) 
    # and another else for errors. Oh well.
    else:
        s = ''.join(sys.argv[1::]) # format args as string

    j = json.loads(s)  # oh the irony
    result = parse_json_to_string(j, "")
    print(result)
