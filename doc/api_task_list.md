## TaskCreate
> API for inventory update task search

## Request
### URL
```ROOT/api/task```

### Method
```GET```

### URL Params
| Name     | Value                        | Type    |
| -------- |----------------------------- | ------- |
| action   | action type of the task      | string  |
| name     | name of the target product   | string  |
| color    | color of the target product  | string  |
| type     | type of the target product   | string  |
| size     | size of the target product   | string  |
| option   | option of the target product | string  |

### Data Params
```None```

## Response

### Success Response
- Code: 201
- Content:
```
{
    "tasks": [
        {
            "date": "2017-12-03"
            "action": "ADD",
            "name": "ghost",
            "color": "black",
            "size": "XS",
            "option": "NA",
            "quntity": 50
        },
        {
            "date": "2017-12-03"
            "action": "DEL",
            "name": "ghost",
            "color": "navy",
            "size": "L",
            "option": "NA",
            "quntity": 5
        },
        {
            "date": "2017-12-03"
            "action": "DEL",
            "name": "ghost",
            "color": "navy",
            "size": "M",
            "option": "NA",
            "quntity": 5
        }
    ]
}
```

### Error Response
- Code: 400
- Reason: none of the field was provided
- Content:
```
{
   "error": "at least one of the search field need to be provided"
}
```
