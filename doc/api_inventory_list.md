## InventoryRetrieve
> API for inventory search

## Request
### URL
```ROOT/api/inventory/```

### Method
```GET```

### URL Params
| Name   | Value                 | Type   |
| ------ |---------------------- | ------ |
| name   | name of the product   | string |
| color  | color of the product  | string | 
| size   | size of the product   | string |
| option | option of the product | string |

### Data Params
```None```

## Response

### Success Response
- Code: 201
- Content:
```
{
    "inventories": [
        {
            "name": "ghost",
            "color": "black",
            "size": "XS",
            "option": "NA",
            "quntity": 55
        },
        {
            "name": "ghost",
            "color": "black",
            "size": "S",
            "option": "NA",
            "quntity": 60
        },
        {
            "name": "ghost",
            "color": "black",
            "size": "L",
            "option": "NA",
            "quntity": 74
        },
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
