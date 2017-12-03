## InventoryRetrieve
> 재고 조회를 위한 API

## Request
### URL
```ROOT/api/inventory/```

### Method
```GET```

### URL Params
| Name  | Value                | Type   |
| ----- |--------------------- | ------ |
| name  | name of the product  | string |
| color | color of the product | string |

### Data Params
```None```

## Response

### Success Response
- Code: 201
- Content:


```
{
    "pk": 1,
    "name": "ghost",
    "color": "black",

    "quantities":
    {
        "xxs": 0,
        "xs": 0,
        "s": 55,
        "m": 60,
        "l": 140,
        "xl": 0,
        "xxl": 0,
    }
}
```

### Error Response
- Code: 400
- Reason: 키(name or color)가 없는 경우
- Content:


```
{
    "name": [
        "This field is required."
    ],
    "color": [
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
        name: 'ghost',
        color: 'black'
    }
})
.done(function(response) {
    console.log(response);
})
.fail(function(response) {
    console.log(response);
});
```
