---
title: dataclass
---

## 定义
!!! quote
    这个模块提供了一个装饰器和一些函数, 用于自动为用户自定义的类添加生成的, 例如 __init__() 和 __repr__()。

```py
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

if __name__ == '__main__':
    print(InventoryItem("张三", 14.0,2).total_cost())
```

```py title="@dataclass将__init__方法会自动添加到类中, 此代码可省略"
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```

## 模块内容
```text
https://docs.python.org/zh-cn/3/library/dataclasses.html#dataclasses.dataclass
```
```bash
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)
```
