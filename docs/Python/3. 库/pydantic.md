---
title: Pydantic
---
!!! quote
    用于数据验证和设置第三方库。它提供了一种简单且直观的方式来定义数据模型，并使用这些模型对数据进行验证和转换(to dict or json)。

### 特性
```text title="Pydantic 的一些主要特性"
    1. 类型注解：Pydantic 使用类型注解来定义模型的字段类型。你可以使用 Python 内置的类型、自定义类型或者其他 Pydantic 提供的验证类型。
    2. 数据验证：Pydantic 自动根据模型定义进行数据验证。它会检查字段的类型、长度、范围等，并自动报告验证错误。你可以使用 ValidationError 异常来捕获验证错误。
    3. 模型转换：Pydantic 提供了从各种数据格式（例如 JSON、字典）到模型实例的转换功能。它可以自动将输入数据解析成模型实例，并保留类型安全性和验证规则。
```

### 安装
```bash
pip install pydantic
```

### 使用

=== "Pydantic 基本操作"
    ```text
    使用 Pydantic，可以定义一个模型类，该类需要继承 pydantic 中的 BaseModel 类，
    模型类描述了数据的结构和类型，并指定验证规则; 然后，可以使用这个模型类来验证输入的数据是否符合预期，并以类型安全的方式访问和操作数据; 
    如果创建实例的数据不符合类型注解的要求，则会报 ValidationError 错误。
    ```
    ```py linenums="1"

    from pydantic import BaseModel, ValidationError
    
    class User(BaseModel):
        name: str
        age: int
        email: str
    
    try:
        user = User(name="Alice", age="30", email="alice@example.com") 
    except ValidationError as e:
        print(e.json())
    ```

=== "Pydantic 高级操作"
    ```text
    Pydantic 还可以结合 typing 模块，进行默认值，可选字段属性等验证的高级操作。
    甚至还可以通过 EmailStr 类来直接验证邮件正确性，但该类依赖一个第三方模块，在使用前需要使用 pip install email-validator 进行安装后才可以使用。
    ```
    ```py linenums="1"

    from typing import Optional
    from pydantic import BaseModel, EmailStr
    
    class User(BaseModel):
        name: str
        age: int
        email: EmailStr
        phone: Optional[str] = None
    
    
    user = User(name="Alice", age=30, email="alice@example.com")  # 有效
    user = User(name="Alice", age=30, email="invalid_email")  # 错误：无效的电子邮件
    ```

=== "Field 对象"
    ```markdown

    Pydantic 还提供了 Field 对象，用于定义字段的验证规则，例如默认值、最大长度、最小值等。
        - ...：表示该字段是必填项。
        - default：定义字段的默认值。如果未提供该值，则默认为None,不能与 ... 同时使用。
        - min_length 和 max_length：针对字符串类型的字段定义最小和最大长度限制。
        - gt、ge、lt 和 le：针对数值类型的字段定义大于 gt、大于等于 ge、小于 lt 和小于等于 le 的限制。
    ```
    ```py linenums="1"

    from pydantic import BaseModel, EmailStr, ValidationError, Field

    class User(BaseModel):
        name: str = Field(..., min_length=1, max_length=10)
        age: int = Field(..., ge=0, le=200)
        email: EmailStr
        phone: str = Field(default="13800138000", min_length=11, max_length=11)
    
    user = None
    try:
        user = User(name="Tom", age=22, email="alice@example.com")
    except ValidationError as e:
        a = eval(e.json())
        print(a[0]["msg"])
    finally:
        print(user)
    ```

=== "数据转换(dict)"
    ```text

    通过定义模型类，可以将通过网络传输或数据库查询的数据转换成模型类对象在程序中使用。
    反之，也可以将处理过后的模型类对象转换成对应的 dict 或 JSON 数据进行存储或传输。
    
    模型类转换为字典
    使用 模型类.model_dump() 方法可以将一个模型类实例对象转换为字典类型数据。
    ```
    ```python linenums="1"
    
    from pydantic import BaseModel, EmailStr, Field
    
    class User(BaseModel):
        name: str = Field(..., min_length=1, max_length=10)
        age: int = Field(..., ge=0, le=200)
        email: EmailStr
        phone: str = Field(default="13800138000", min_length=11, max_length=11)
    
    user = User(name="Tom", age=22, email="alice@example.com")
    data = User.model_dump(user)
    print(data)
    print(type(data))
    ```

=== "模型类转换为JSON"
    ```text
    使用 模型类.model_dump_json() 方法可以将一个模型类实例对象转换为 JSON 字符串。
    ```
    ```py linenums="1"
    
    from pydantic import BaseModel, EmailStr, Field
    
    class User(BaseModel):
        name: str = Field(..., min_length=1, max_length=10)
        age: int = Field(..., ge=0, le=200)
        email: EmailStr
        phone: str = Field(default="13800138000", min_length=11, max_length=11)
    
    user = User(name="Tom", age=22, email="alice@example.com")
    data = User.model_dump_json(user)
    print(data)
    print(type(data))
    ```