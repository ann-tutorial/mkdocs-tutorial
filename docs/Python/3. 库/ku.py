"""
# @File: ku.py
# @CreateDate: 2024/2/26 09:25
# @Author: ann
"""
import copy

a = [1,2,3,4]
b = copy.copy(a)
# b = a

if id(a) == id(b):
    print("id相同")
else:
    print("id不同")


b[0] = 4
print(a[0]) # a[0] = 4
if id(a) == id(b):
    print("id相同")
else:
    print("id不同")

b.append(5)
if id(a) == id(b):
    print("id相同")
else:
    print("id不同")



# from typing import Optional
# from pydantic import BaseModel, EmailStr
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#     phone: Optional[str] = None
#
#
# user = User(name="Alice", age=30, email="alice@example.com")  # 有效
# user = User(name="Alice", age=30, email="invalid_email")  # 错误：无效的电子邮件


# -*- coding: utf-8 -*-

# from pydantic import BaseModel, ValidationError
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
# try:
#     user = User(name="Alice", age="30", email="alice@example.com")
# except ValidationError as e:
#     print(e.json())