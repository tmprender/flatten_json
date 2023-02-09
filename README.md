# Example

### json input:
```
{
  "data": {
    "stuff": {
      "type1":[
            {"id":1,"name": "foo"},
            {"id":2,"name": "bar"}
          ],
      "type2": {
        "id":2,
        "xyz": [-255,0,255],
        "notation":"big-O",
        "details": {
          "lat":0.000,"long":0.000,"time":42
        }
      }
    },
    "otherstuff": {
      "list":[
        [1,42],[2,2]
      ]
    }
  }
}
```
### flattened output:
```
data.stuff.type1=[{u'id': 1, u'name': u'foo'}, {u'id': 2, u'name': u'bar'}]
data.stuff.type2.xyz=[-255, 0, 255]
data.stuff.type2.id=2
data.stuff.type2.notation=big-O
data.stuff.type2.details.lat=0.0
data.stuff.type2.details.long=0.0
data.stuff.type2.details.time=42
data.otherstuff.list=[[1, 42], [2, 2]]
```

### to-do:
- implement lists
- un-reverse output
- remove continuous print as it recurses

