## InventoryUpdate
> 재고 변경을 이벤트 생성을 위한 API

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
    "datetime": "2017.12.03 14:55:56",
    "events": [
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "S",
            "quantity": 45
        },
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "M",
            "quantity": 100
        },
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "L",
            "quantity": 75
        },
    ]
}
```

### Error Response
- Code: 400
- Reason: 키가 없는 경우
- Content:


```
{
    "name": [
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
    url: 'ROOT/api/inventory/',
    type: 'POST',
    dataType: 'json',
    data: {
    "title": "sample product stock event",
    "description": "detailed description for event",
    "events": [
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "S",
            "quantity": 45
        },
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "M",
            "quantity": 100
        },
        {
            "name": "ghost",
            "color": "black",
            "type": "ADD",
            "size": "L",
            "quantity": 75
        },
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
