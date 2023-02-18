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
        [
          {"ugly_nest": true}, 
          {"depth":{"test": true} } 
        ]
      ]
    }
  },
  "log":"123abc"
}
```
### flattened output:
```
data.object.user.id=2
data.object.user.range[]=-255
data.object.user.range[]=0
data.object.user.range[]=255
data.object.user.notation=big-O
data.object.user.details.lat=0.0
data.object.user.details.long=0.0
data.object.user.details.time=42
data.object.groups[].id=1
data.object.groups[].name=foo
data.object.groups[].id=3
data.object.groups[].name=bar
data.metdata.list[][]=1
data.metdata.list[][]=42
data.metdata.list[][]=3.14
data.metdata.list[][]=98.6
data.metdata.list[]ugly_nest=True
data.metdata.list[]depth.test=True
log=123abc
```

### use
`python flatten_json.py filename`

- pipe to grep (find path to value, or all values for a path):
`python flatten_json.py filename | grep foo`
`python flatten_json.py filename | grep user.details`

- convert to other file formats (csv), using different delimiter

### to-do:
- allow for custom delimiter
 
