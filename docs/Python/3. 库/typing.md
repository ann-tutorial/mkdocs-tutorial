---
title: Typing
---
!!! quote
    1. 从Python 3.5版本引入的标准库
    2. 提供了类型提示和类型注解的功能，用于对代码进行静态类型检查和类型推断
    3. 定义了多种类型和泛型，以帮助开发者代码的可读性、可维护性和可靠性


## typing 库导下常见的类型别名

=== "callable"
    ``` text
    callable ：表示一个可调用对象，如函数、方法、类等。callable可以用于定义一个函数的参数类型，该参数接受一个可调用对象
    ```
    ```py
    from typing import Callable

    def add(a:int, b:int) -> int:
        return a + b
    
    # Callable[[int, int], int]表示接受两个整数参数并返回一个整数.
    def test_callable(func:Callable[[int, int], str], a:int, b:int) ->int:
        return func(a,b)
    
    a = test_callable(add, 1, 2)
    print(a) # 3
    ```
=== "Dict"
    ```
    表示一个字典类型，其键和值的类型可以通过泛型参数指定
    ```
    ```py
    from typing import Dict

    # Dict[str, int] 是一个类型提示，键的类型为字符串 (str)，值的类型为整数 (int)。
    user_dict: Dict[str, int] = {"Alice": 30, "Bob": 25}
    
    print(user_dict["Alice"])  # 30
    ```

=== "List"
    ```
    表示一个列表类型，列表中的元素类型可以通过泛型参数指定
    ```
    ```py
    from typing import List
    
    numbers: List[int] = [1, 2, 3, 4, 5]
    ```
=== "Optional"
    ```
    Optional 是一个泛型类型提示，用于表示一个可选的值。
    它可以与其他类型提示一起使用，表示该类型可以是指定的类型或者 None
    ```
    ```py title="example1"
    from typing import Optional

    def greet(name: Optional[str]) -> str:
        if name is None:
            return "Hello, stranger!"
        else:
            return f"Hello, {name}!"
    
    print(greet("Alice"))  # 输出: Hello, Alice!
    print(greet(None))  # 输出: Hello, stranger!
    ```
    ``` py title="example2"
    from typing import Optional 
    def get_user_age(username: str) -> Optional[int]:
        ＃ 在这里查找用户年龄，如果找到则返回年龄，否则返回 None
    ```
=== "TypeVar"
    ```
    TypeVar 是一个泛型类型变量的工具，用于表示一个可变的类型。它通常与泛型类型提示一起使用，以在函数或类中引入灵活的类型参数
    使用 TypeVar，我们可以在函数或类中引入一个灵活的类型参数 T，从而使函数或类能够处理多种类型的输入，并保持类型安全性
    ```
    ```py
    from typing import TypeVar, List

    T = TypeVar('T')
    
    def reverse_list(items: List[T]) -> List[T]:
        return items[::-1]
    
    string_list = ["apple", "banana", "cherry"]
    reversed_string_list = reverse_list(string_list)
    print(reversed_string_list)  # 输出: ["cherry", "banana", "apple"]
    
    number_list = [1, 2, 3, 4, 5]
    reversed_number_list = reverse_list(number_list)
    print(reversed_number_list)  # 输出: [5, 4, 3, 2, 1]
    ```
=== "Union"
    ```
    Union 是一个泛型类型提示，用于表示多个可能的类型中的一个。它可以用于函数参数、返回值或变量的类型提示，表示该参数、返回值或变量可以是指定的多个类型中的任意一个
    ```
    ```py
    from typing import Union
    
    def square_or_concatenate(value: Union[int, str]) -> Union[int, str]:
        if isinstance(value, int):
            return value ** 2
        elif isinstance(value, str):
            return value + value
        else:
            raise TypeError("Unsupported type")
    
    result1 = square_or_concatenate(5)
    print(result1)  # 输出: 25
    
    result2 = square_or_concatenate("hello")
    print(result2)  # 输出: "hellohello"
    ```
=== "NewType"
    ```
    用于创建具有特定类型约束的新类型别名。它可以帮助在类型提示中引入更具意义的类型，并增加代码的可读性和可维护
    ```
    ```py
    from typing import NewType

    # 创建一个类型别名 Distance，约束为非负浮点数
    Distance = NewType('Distance', float)
    
    def calculate_distance(x: Distance, y: Distance) -> Distance:
        return abs(x - y)
    
    distance_a = Distance(5.8)
    distance_b = Distance(3.2)
    
    result = calculate_distance(distance_a, distance_b)
    print(result)  # 输出: 2.6
    ```
=== "Any"
    ```
    Any 是一个特殊的类型提示，表示任何类型都可以被接受。使用 Any 声明的变量或函数参数可以接受任意类型的值，而不进行类型检查
    ```
    ```py
    from typing import Any
    
    def print_value(value: Any) -> None:
        print(value)
    
    print_value(10)  # 输出: 10
    print_value("hello")  # 输出: "hello"
    print_value([1, 2, 3])  # 输出: [1, 2, 3]
    ```

## 类型别名

```
类型别名将声明两个类型是相互 等价 的, 所以当想要简化复杂的类型签名时会很有用处。
eg: Vector = list[float]
```

```py title="Vector 和 list[float] 将被静态类型检查器等同处理"
from typing import TypeAlias

# 方法一：
Vector: TypeAlias = list[float]
# 方法二：
# Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

# output = [2.0, -8.4, 10.8]
```

## NewType

```text
1. NewType 函数创建一个新的类型别名时，它实际上并没有在运行时引入新的类型。它只是在静态类型检查过程中提供了一种额外的类型标记，用于增强代码的可读性和类型安全性
2. NewType 声明把一种类型当作另一种类型的 子类型。

## 使用NewType的好处
1. 增加代码的可读性和可维护性
2. 提供类型约束和安全性（约束类型后，静态类型检查工具（如 Mypy）可以在编译时或运行时检测到类型错误，从而提供更好的类型安全性）
3. 代码重构的便利性（如果我们在代码中使用了多个地方需要表示距离的 float 类型，而后续决定使用其他类型（如 Decimal）来表示距离，那么我们只需要修改 NewType 创建的类型别名即可，而不必遍历整个代码库来修改每个使用 float 的地方）
```

```py title="NewType 并不会对输入参数类型进行限制或强制类型检查。它主要用于提高代码的可读性，让代码中的类型更加清晰易懂"
from typing import NewType

# 定义一个新的类型别名
UserId = NewType('UserId', int)

# 创建一个 UserId 类型的变量
user_id = UserId(54321)

# 使用类型别名进行操作
def get_user_by_id(user_id: UserId) -> str:
    return f"User with ID {user_id}"

# 调用函数并传入 UserId 类型的参数
result = get_user_by_id(user_id)
print(result)
```

```py 
# 由于 Derived 类型是 Original 类型的子类型，我们只能将 Derived 类型的值传递给期望 Derived 类型的参数。而不能将 Original 类型的值直接传递给 Derived 类型的参数，因为这会违反类型系统中的子类型关系
from typing import NewType

Original = NewType('Original', int)
Derived = NewType('Derived', Original)

def process_data(data: Derived) -> None:
    # 处理 Derived 类型的数据
    pass

value: Original = 10
process_data(value)
```
