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
| Name      | Value             | Type     | options           |
| --------- |------------------ | -------- | ----------------- |
| date      | date of the task  | datetime | auto_add_now=True |
| action    | type of the task  | string   | choice(ACTIONS)   |
| inventory | target inventory  | fk       |                   |
| value     | value of the task | int(>=0) | default(0)        |

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
| Name | Value              |
| ---- | ------------------ |
| ADD  | task inventory add |
| SUB  | task inventory sub |
