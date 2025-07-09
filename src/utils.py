#!/usr/bin/env python3
"""
工具函数模块
提供通用的辅助功能
"""

import re
from typing import Union, List


def is_number(value: str) -> bool:
    """
    检查字符串是否为有效数字
    
    Args:
        value: 要检查的字符串
        
    Returns:
        如果是有效数字返回 True，否则返回 False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def format_number(num: Union[int, float], decimal_places: int = 2) -> str:
    """
    格式化数字显示
    
    Args:
        num: 要格式化的数字
        decimal_places: 小数位数
        
    Returns:
        格式化后的数字字符串
    """
    if isinstance(num, int):
        return str(num)
    else:
        return f"{num:.{decimal_places}f}".rstrip('0').rstrip('.')


def parse_expression(expression: str) -> List[str]:
    """
    解析数学表达式
    
    Args:
        expression: 数学表达式字符串
        
    Returns:
        解析后的标记列表
    """
    # 简单的表达式解析，支持基本的四则运算
    pattern = r'(\d+\.?\d*|[+\-*/()])'
    tokens = re.findall(pattern, expression.replace(' ', ''))
    return tokens


def validate_input(value: str) -> Union[float, None]:
    """
    验证并转换输入值
    
    Args:
        value: 输入字符串
        
    Returns:
        转换后的数字或 None（如果无效）
    """
    if not value.strip():
        return None
    
    if is_number(value):
        return float(value)
    
    return None


def get_operation_symbol(operation: str) -> str:
    """
    获取运算符号
    
    Args:
        operation: 运算名称
        
    Returns:
        对应的运算符号
    """
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/',
        'power': '^',
        'mod': '%'
    }
    return symbols.get(operation.lower(), '?')


def create_calculation_record(a: float, b: float, operation: str, result: float) -> dict:
    """
    创建计算记录
    
    Args:
        a: 第一个操作数
        b: 第二个操作数
        operation: 运算类型
        result: 计算结果
        
    Returns:
        包含计算信息的字典
    """
    return {
        'operand1': a,
        'operand2': b,
        'operation': operation,
        'symbol': get_operation_symbol(operation),
        'result': result,
        'formatted_result': format_number(result),
        'expression': f"{format_number(a)} {get_operation_symbol(operation)} {format_number(b)} = {format_number(result)}"
    }