"""
# @File: ku.py
# @CreateDate: 2024/2/26 09:25
# @Author: ann
"""

# -*- coding: utf-8 -*-

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str

if __name__ == '__main__':
    try:
        user = User(name="Alice", age="123", email="alice@example.com")
    except ValidationError as e:
        print(e.json())