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
| Name      | Value                   | Type    |
| --------- |------------------------ | ------- |
| action    | action type of the task | string  |
| inventory | target inventory        | string  |
| value     | value of the task       | int(>0) |

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
- Reason: missing required filed(s)(action, inventory, quantity)
- Content:
```
{
    "action": [
        "This field is required."
    ],
    "inventory": [
        "This field is required."
    ],
    "value": [
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
        'inventory': 2,
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
