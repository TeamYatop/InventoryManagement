## InventoryUpdate
> 재고 변경을 위한 API

## Request
### URL
```ROOT/api/inventory```

### Method
```UPDATE```

### URL Params
```None```

### Data Params
| Name     | Value                | Type    |
| -------- |--------------------- | ------- |
| name     | name of the product  | string  |
| color    | color of the product | string  |
| type     | type of the event    | string  |
| size     | size of the event    | string  |
| quantity | size of the product  | int(>0) |


## Response

### Success Response
- Code: 201
- Content:


```
{
    "pk": 1,
    "name": "ghost",
    "color": "black",
    "type": "ADD",
    "size": "XS",
    "quantity": 10
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
    url: 'ROOT/api/inventory/',
    type: 'POST',
    dataType: 'json',
    data: {
        name: 'ghost',
        color: 'black',
        type: 'ADD',
        size: 'XS',
        quntity: 10,
    }
})
.done(function(response) {
    console.log(response);
})
.fail(function(response) {
    console.log(response);
});
```
