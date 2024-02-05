# Flatten JSON
*python-based CLI tool for 'flattening' nasty, nested json.*

> [!NOTE]
> **ATTENTION:** please let me know if there is a (better) way to do this with native shell commands

## Example

### json input:
```console
user@shell:~$ cat example.json
{
  "data": {
    "object": { 
      "user": {
        "id":1,
        "range": [-255,0,255],
        "notation":"big-O",
        "details": {
          "lat":0.000,"long":0.000,"time":42
        }
      },
      "groups":[
        {"id":2,"name": "foo"},
        {"id":3,"name": "bar"}
      ]
    },
    "metdata": {
      "list": [
        [ [1,42],[3.14, 98.6] ], 
        [ 3, 6, 9, "low" ],
        [{"x":1,"y":-1}]
      ],
      "ugly_nest": {"depth":{"test": true} }
    }
  },
  "log":"123abc"
}

```

### flattened output:

```console
user@shell:~$ python flatten.py $(cat example.json)
data.object.user.id=1
data.object.user.range[0]=-255
data.object.user.range[1]=0
data.object.user.range[2]=255
data.object.user.notation=big-O
data.object.user.details.lat=0.0
data.object.user.details.long=0.0
data.object.user.details.time=42
data.object.groups[0].id=2
data.object.groups[0].name=foo
data.object.groups[1].id=3
data.object.groups[1].name=bar
data.metdata.list[0][0][0]=1
data.metdata.list[0][0][1]=42
data.metdata.list[0][0][1][0]=3.14
data.metdata.list[0][0][1][1]=98.6
data.metdata.list[1][0]=3
data.metdata.list[1][1]=6
data.metdata.list[1][2]=9
data.metdata.list[1][3]=low
data.metdata.list[2][].x=1
data.metdata.list[2][].y=-1
data.metdata.ugly_nest.depth.test=True
log=123abc
```

### Usage
Pass a JSON string via stdin: 

```
python flatten.py $(cat example.json)
```

or
```
cat example.json | python flatten.py
```

**USE CASE**: pipe to `grep` to find path.to.value:\
```console
user@shell:~$ python flatten.py $(cat example.json) | grep foo
data.object.groups[0].name=foo
```

or, find all find values for a path:\

```console
user@shell:~$ python flatten.py $(cat example.json) | grep user.details
data.object.user.details.lat=0.0
data.object.user.details.long=0.0
data.object.user.details.time=42
```

> [!TIP] 
> Each line returned by `flatten.py` is (read: "should be") a valid `jq` query! Use this tool to flatten JSON output to help find path.to.value for complex queries.

```console
user@shell:~$ python flatten.py $(cat example.json) | grep user.details
data.object.user.details.lat=0.0
data.object.user.details.long=0.0
data.object.user.details.time=42

user@shell:~$cat example.json | jq .data.object.user.details.time
42
```

### Getting Started
`git clone https://github.com/tmprender/flatten_json`

`python path/to/flatten.py $some_json_string`

Create an ALIAS for easy use:
```
# ADD FOLLOWING LINE IN YOUR ~/.bash_profile
alias fj="python /path/to/flatten.py"
```
Now you can more simply run... \
`fj $(cat example.json)`\
or\
`cat example.json | fj`

 
