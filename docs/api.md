# API 文档

## Calculator 类

### 概述
`Calculator` 类提供基础的数学运算功能，包括加法、减法等操作，并支持计算历史记录。

### 构造函数

#### `__init__()`
创建一个新的计算器实例。

**示例:**
```python
calc = Calculator()
```

### 方法

#### `add(a: Number, b: Number) -> Number`
执行加法运算。

**参数:**
- `a` (Number): 第一个操作数
- `b` (Number): 第二个操作数

**返回值:**
- `Number`: 两数之和

**示例:**
```python
result = calc.add(5, 3)  # 返回 8
result = calc.add(2.5, 1.5)  # 返回 4.0
```

#### `subtract(a: Number, b: Number) -> Number`
执行减法运算。

**参数:**
- `a` (Number): 被减数
- `b` (Number): 减数

**返回值:**
- `Number`: 两数之差

**示例:**
```python
result = calc.subtract(10, 4)  # 返回 6
result = calc.subtract(5.5, 2.5)  # 返回 3.0
```

#### `get_history() -> List[str]`
获取计算历史记录。

**返回值:**
- `List[str]`: 包含所有计算记录的列表

**示例:**
```python
calc.add(1, 2)
calc.subtract(5, 3)
history = calc.get_history()
# 返回: ['1 + 2 = 3', '5 - 3 = 2']
```

#### `clear_history() -> None`
清空计算历史记录。

**示例:**
```python
calc.clear_history()
```

## Utils 模块

### 函数

#### `is_number(value: str) -> bool`
检查字符串是否为有效数字。

**参数:**
- `value` (str): 要检查的字符串

**返回值:**
- `bool`: 如果是有效数字返回 True，否则返回 False

**示例:**
```python
is_number("123")     # True
is_number("12.34")   # True
is_number("abc")     # False
```

#### `format_number(num: Union[int, float], decimal_places: int = 2) -> str`
格式化数字显示。

**参数:**
- `num` (Union[int, float]): 要格式化的数字
- `decimal_places` (int, optional): 小数位数，默认为 2

**返回值:**
- `str`: 格式化后的数字字符串

**示例:**
```python
format_number(123)      # "123"
format_number(123.45)   # "123.45"
format_number(123.00)   # "123"
```

#### `parse_expression(expression: str) -> List[str]`
解析数学表达式。

**参数:**
- `expression` (str): 数学表达式字符串

**返回值:**
- `List[str]`: 解析后的标记列表

**示例:**
```python
parse_expression("1+2")     # ["1", "+", "2"]
parse_expression("(1+2)*3") # ["(", "1", "+", "2", ")", "*", "3"]
```

#### `validate_input(value: str) -> Union[float, None]`
验证并转换输入值。

**参数:**
- `value` (str): 输入字符串

**返回值:**
- `Union[float, None]`: 转换后的数字或 None（如果无效）

**示例:**
```python
validate_input("123")   # 123.0
validate_input("abc")   # None
```

#### `get_operation_symbol(operation: str) -> str`
获取运算符号。

**参数:**
- `operation` (str): 运算名称

**返回值:**
- `str`: 对应的运算符号

**示例:**
```python
get_operation_symbol("add")      # "+"
get_operation_symbol("subtract") # "-"
```

#### `create_calculation_record(a: float, b: float, operation: str, result: float) -> dict`
创建计算记录。

**参数:**
- `a` (float): 第一个操作数
- `b` (float): 第二个操作数
- `operation` (str): 运算类型
- `result` (float): 计算结果

**返回值:**
- `dict`: 包含计算信息的字典

**示例:**
```python
record = create_calculation_record(1.5, 2.5, "add", 4.0)
# 返回:
# {
#     'operand1': 1.5,
#     'operand2': 2.5,
#     'operation': 'add',
#     'symbol': '+',
#     'result': 4.0,
#     'formatted_result': '4',
#     'expression': '1.5 + 2.5 = 4'
# }
```

## 类型定义

### `Number`
```python
Number = Union[int, float]
```

数字类型的联合类型，可以是整数或浮点数。

## 错误处理

目前的实现没有特殊的错误处理机制。计划在未来版本中添加：

- 除零错误检查
- 输入验证
- 溢出检查
- 类型错误处理

## 使用示例

### 基本用法
```python
from calculator import Calculator

# 创建计算器实例
calc = Calculator()

# 执行计算
result1 = calc.add(10, 5)      # 15
result2 = calc.subtract(20, 8)  # 12

# 查看历史记录
history = calc.get_history()
print(history)  # ['10 + 5 = 15', '20 - 8 = 12']

# 清空历史
calc.clear_history()
```

### 配合工具函数使用
```python
from calculator import Calculator
from utils import format_number, validate_input

calc = Calculator()

# 验证用户输入
user_input1 = "15.5"
user_input2 = "7.2"

if validate_input(user_input1) and validate_input(user_input2):
    a = float(user_input1)
    b = float(user_input2)
    result = calc.add(a, b)
    formatted_result = format_number(result)
    print(f"结果: {formatted_result}")
```

## 版本信息

- 当前版本: 1.0.0
- 最后更新: 2024-01-15
- 作者: Demo Team

## 未来计划

- [ ] 添加乘法和除法运算
- [ ] 实现错误处理机制
- [ ] 支持更复杂的数学表达式
- [ ] 添加科学计算功能
- [ ] 实现计算历史的持久化存储