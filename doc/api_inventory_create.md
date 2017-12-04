## InventoryCreate
> 재고 생성을 위한 API

## Request
### URL
```ROOT/api/inventory/```

### Method
```POST```

### URL Params
```None```

### Data Params
| Name   | Value                 | Type   |
| ------ |---------------------- | ------ |
| name   | name of the product   | string |
| color  | color of the product  | string |
| size   | size of the product   | string |
| option | option of the product | string |

## Response

### Success Response
- Code: 201
- Content:
```
{
    "name": "ghost",
    "color": "black",
    "size": "XS",
    "option": "NA",
    "quntity": 0
}
```

### Error Response
- Code: 400
- Reason: missing required filed(s)(name, color, size, option)
- Content:
```
{
    "name": [
        "This field is required."
    ],
    "color": [
        "This field is required."
    ],
    "size": [
        "This field is required."
    ],
    "option": [
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
        'name': 'ghost',
        'color': 'back',
        'size': 'XS',
        'option': 'NA',
    }
})
.done(function(response) {
    console.log(response);
})
.fail(function(response) {
    console.log(response);
});
```
