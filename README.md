# Example

### json input:
```
{
  "data": {
    "object": {
      "A":[
            {"id":1,"name": "foo"},
            {"id":2,"name": "bar"}
          ],
      "B": {
        "id":2,
        "xyz": [-255,0,255],
        "notation":"big-O",
        "details": {
          "lat":0.000,"long":0.000,"time":42
        }
      }
    },
    "metdata": {
      "listOfLists":[
        [1,42],[2,2]
      ]
    }
  }
}
```
### flattened output:
```
data.object.A[].id=1
data.object.A[].name=foo
data.object.A[].id=2
data.object.A[].name=bar
data.object.B.xyz[]=-255
data.object.B.xyz[]=0
data.object.B.xyz[]=255
data.object.B.id=2
data.object.B.notation=big-O
data.object.B.details.lat=0.0
data.object.B.details.long=0.0
data.object.B.details.time=42
data.metdata.listOfLists[]=[1, 42]
data.metdata.listOfLists[]=[2, 2]
```

### to-do:
- nested lists, refactor
- un-reverse output
 
