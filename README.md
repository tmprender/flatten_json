# Example

### json input:
```
{
  "data": {
    "object": { 
      "user": {
        "id":2,
        "range": [-255,0,255],
        "notation":"big-O",
        "details": {
          "lat":0.000,"long":0.000,"time":42
        }
      },
      "groups":[
        {"id":1,"name": "foo"},
        {"id":3,"name": "bar"}
      ]
    },
    "metdata": {
      "list":[ 
        [ [1,42],[3.14,98.6] ], 
        [ 3,6,9, "low" ],
        [{"x":1,"y":-1}]  # this can not be fully parsed by jq
      ],
      "ugly_nest": {"depth":{"test": true} }
    }
  },
  "log":"123abc"
}

```
### flattened output:
```
data.object.user.id=2
data.object.user.range[0]=-255
data.object.user.range[0]=0
data.object.user.range[0]=255
data.object.user.notation=big-O
data.object.user.details.lat=0.0
data.object.user.details.long=0.0
data.object.user.details.time=42
data.object.groups[0].id=1
data.object.groups[0].name=foo
data.object.groups[1].id=3
data.object.groups[1].name=bar
data.metdata.list[0][0]=1
data.metdata.list[0][0]=42
data.metdata.list[0][0]=3.14
data.metdata.list[0][0]=98.6
data.metdata.list[0][1]=3
data.metdata.list[0][1]=6
data.metdata.list[0][1]=9
data.metdata.list[0][1]=low
data.metdata.list[0]x=1       # does not correspond to a valid jq query
data.metdata.list[0]y=-1      # ^^
data.metdata.ugly_nest.depth.test=True
log=123abc
```

### Usage
`python flatten_json.py filename`

pipe to grep (find path to value, or all values for a path):\
`python flatten_json.py filename | grep foo`\
`python flatten_json.py filename | grep user.details`


convert to other file formats (csv, LEEF), using different delimiter

### To-Do:
- allow for custom delimiter
 
