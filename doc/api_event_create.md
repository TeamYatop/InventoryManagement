## EventCreate
> API for event create

## Request
### URL
```ROOT/api/event```

### Method
```POST```

### URL Params
```None```

### Data Params
| Name        | Value                | Type   |
| ----------- |--------------------- | ------ |
| title       | title of the event   | string |
| description | description of event | string |
| events      | detailed sub events  | list   |

## Response

### Success Response
- Code: 201
- Content:
```
{
    "title": "sample product stock event",
    "description": "detailed description for event",
    "date": "2017.12.03",
    "events": [
        {
            "action": "ADD",
            "name": "ghost",
            "color": "black",
            "size": "S",
            "option": "NA",
            "quntity": 45
        },
        {
            "action": "ADD",
            "name": "ghost",
            "color": "black",
            "size": "M",
            "option": "NA",
            "quntity": 100
        },
        {
            "action": "ADD",
            "name": "ghost",
            "color": "black",
            "size": "XL",
            "option": "NA",
            "quntity": 75
        }
    ]
}
```

### Error Response
- Code: 400
- Reason: missing required filed(s)(title, description, events)
- Content:
```
{
    "title": [
        "This field is required."
    ],
    "description": [
        "This field is required."
    ],
    "events": [
        "This field is required."
    ]
}
```

## Sample Call
```
$.ajax({
    url: 'ROOT/api/event/',
    type: 'POST',
    dataType: 'json',
    data: {
        "title": "sample product stock event",
        "description": "detailed description for event",
        "events": [
            {
                "action": "ADD",
                "name": "ghost",
                "color": "black",
                "size": "S",
                "option": "NA",
                "quntity": 45
            },
            {
                "action": "ADD",
                "name": "ghost",
                "color": "black",
                "size": "M",
                "option": "NA",
                "quntity": 100
            },
            {
                "action": "ADD",
                "name": "ghost",
                "color": "black",
                "size": "XL",
                "option": "NA",
                "quntity": 75
            }
        ]
    }
})
.done(function(response) {
    console.log(response);
})
.fail(function(response) {
    console.log(response);
});
```
