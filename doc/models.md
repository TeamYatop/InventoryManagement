## Models

### Inventory
| Name     | Value                    | Type     | options         |
| -------- | ------------------------ | -------- | --------------- |
| name     | name of the product      | string   |                 |
| color    | color of the product     | string   |                 |
| size     | type of the event        | string   | choice(SIZE)    |
| option   | size of the event        | string   | choice(OPTIONS) |
| quantity | quantity of the product  | int(>=0) | default(0)      |

### Task
| Name     | Value                | Type     | options         |
| -------- |--------------------- | -------- | --------------- |
| date     | date of the task     | datetime | default(NOW)    |
| action   | type of the task     | string   | choice(ACTIONS) |
| name     | name of the product  | string   |                 |
| color    | color of the product | string   |                 |
| type     | type of the product  | string   | choice(COLOR)   |
| size     | size of the product  | string   | choice(OPTIONS) |
| quantity | quantity of the task | int(>=0) | default(0)      |

## CHOICES

### SIZE
| Name | Value              |
| ---- | ------------------ |
| XXS  | double extra small |
| XS   | extra small        |
| S    | small              |
| M    | medium             |
| L    | large              |
| XL   | extra large        |
| XXL  | double extra large |

### OPTIONS
| Name | Value       |
| ---- | ----------- |
| NA   | None at All |
| L1   | l1          |
| L2   | l2          |

### ACTIONS
| Name | Value           |
| ---- | --------------- |
| ADD  | add products    |
| DEL  | delete products |
