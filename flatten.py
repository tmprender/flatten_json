import sys
import json

GLOBAL_STRING = ""
DELIM = "."
# enable FORMAT_JQ to output valid JQ query if DELIM (default=.) is in a key
FORMAT_JQ = True  

def parse_json_to_string(json_data, path):
    global GLOBAL_STRING

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
                path += f"{key}{DELIM}"
                # recurse until value is non-dict
                parse_json_to_string(json_data[key], path)
                # reset path for this loop now that method has returned
                path = parent

            # check for list
            elif type(json_data[key]) is list:
                # iterate thru elements - multiple counters
                for idx, i in enumerate(json_data[key]):
                    # check if nested as dict
                    if type(i) is dict:
                        # update path indicating list element
                        path += f"{key}[{idx}]{DELIM}"
                        parse_json_to_string(i, path)
                        path = parent
                    # nested list
                    elif type(i) is list:
                        
                        path += f"{key}[{idx}]"
                        parse_json_to_string(i, path)
                        path = parent
                    # value within a list    
                    else:
                        GLOBAL_STRING += f"{path}{key}[{idx}]={i}\n"
                        

            # not nested, write path.to.key=value pair(s) for this block
            else:
                # handle escpaing for DELIM in key
                value = json_data[key]
                if DELIM in key and FORMAT_JQ:
                    key = str(key).replace(DELIM, f"\{DELIM}")
                    key = f'\\"{key}\\"'
                
                GLOBAL_STRING += f"{path}{key}={value}\n"

    # flatten list []
    elif type(json_data) is list:
        for idx, i in enumerate(json_data):
            if type(i) is dict: 
                path += f"[]{DELIM}"
                parse_json_to_string(i, path)
            elif type(i) is list:
                path += f"[{idx}]"
                parse_json_to_string(i, path)
                
            else:
                GLOBAL_STRING += f"{path}[{idx}]={i}\n"
                
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
