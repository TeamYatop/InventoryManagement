## TaskCreate
> API for inventory update task create

## Request
### URL
```ROOT/api/task```

### Method
```POST```

### URL Params
```None```

### Data Params
| Name     | Value                        | Type    |
| -------- |----------------------------- | ------- |
| action   | action type of the task      | string  |
| name     | name of the target product   | string  |
| color    | color of the target product  | string  |
| type     | type of the target product   | string  |
| size     | size of the target product   | string  |
| option   | option of the target product | string  |
| quantity | quantity of the task         | int(>0) |

## Response

### Success Response
- Code: 201
- Content:
```
{
    "date": "2017-12-03"
    "action": "ADD",
    "name": "ghost",
    "color": "black",
    "size": "XS",
    "option": "NA",
    "quntity": 50
}
```

### Error Response
- Code: 400
- Reason: missing required filed(s)(action, name, color, size, option, quantity)
- Content:
```
{
    "action": [
        "This field is required."
    ],
    "name": [
        "This field is required."
    ],
    "color": [
        "This field is required."
    ],
    "type": [
        "This field is required."
    ],
    "size": [
        "This field is required."
    ],
    "quantity": [
        "This field is required."
    ],
}
```

## Sample Call
```
$.ajax({
    url: 'ROOT/api/task/',
    type: 'POST',
    dataType: 'json',
    data: {
        'action': 'ADD',
        'name': 'ghost',
        'color': 'back',
        'size': 'XS',
        'option': 'NA',
        'quntity': 55
    }
})
.done(function(response) {
    console.log(response);
})
.fail(function(response) {
    console.log(response);
});
```
