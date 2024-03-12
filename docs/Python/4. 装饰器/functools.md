---
title: functools高阶函数
---


### lru_cache
```text
https://zhuanlan.zhihu.com/p/640954732
https://docs.python.org/zh-cn/3/library/functools.html
```
### cached_property

```text title="定义"
1. 将一个类的方法转换为只读的属性，并且只在第一次访问时计算属性值，然后将其缓存起来，以后再次访问该属性时直接返回缓存的值，而不再重新计算
2. 缓存的值只在对象的生命周期内有效

```

```text title="什么时候使用"
这个装饰器通常用于那些计算开销较大且不经常变化的属性，以提高代码的性能
```

```python
from functools import cached_property

class MyClass:
    def __init__(self):
        self._data = [1, 2, 3]

    @cached_property
    def calculated_property(self):
        print("Calculating...")
        return sum(self._data)

# 创建实例
obj = MyClass()

# 第一次访问属性，进行计算并缓存
result1 = obj.calculated_property  # 输出 "Calculating..."

# 第二次访问属性，直接返回缓存的值，不再计算
result2 = obj.calculated_property  # 无输出

print(result1)  # 输出计算结果：6
print(result2)  # 输出计算结果：6
```