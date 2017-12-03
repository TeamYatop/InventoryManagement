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
| Name  | Value                | Type   |
| ----- |--------------------- | ------ |
| name  | name of the product  | string |
| color | color of the product | string |

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
        "s": 0,
        "m": 0,
        "l": 0,
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
    name: name,
    color: color
  }
})
.done(function(response) {
  console.log(response);
})
.fail(function(response) {
  console.log(response);
});
```
