#!/usr/bin/env python3
"""
工具模块测试
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from utils import (
    is_number, format_number, parse_expression, validate_input,
    get_operation_symbol, create_calculation_record
)


class TestUtils:
    """工具函数测试类"""
    
    def test_is_number(self):
        """测试数字检查函数"""
        # 有效数字
        assert is_number("123") == True
        assert is_number("123.45") == True
        assert is_number("-123") == True
        assert is_number("-123.45") == True
        assert is_number("0") == True
        assert is_number("0.0") == True
        assert is_number(".5") == True
        assert is_number("5.") == True
        
        # 无效数字
        assert is_number("abc") == False
        assert is_number("12a") == False
        assert is_number("") == False
        assert is_number("1.2.3") == False
        assert is_number("1+2") == False
    
    def test_format_number(self):
        """测试数字格式化函数"""
        # 整数
        assert format_number(123) == "123"
        assert format_number(0) == "0"
        assert format_number(-123) == "-123"
        
        # 浮点数
        assert format_number(123.45) == "123.45"
        assert format_number(123.00) == "123"
        assert format_number(123.10) == "123.1"
        assert format_number(0.5) == "0.5"
        
        # 指定小数位数
        assert format_number(123.456, 1) == "123.5"
        assert format_number(123.456, 3) == "123.456"
        assert format_number(123.000, 2) == "123"
    
    def test_parse_expression(self):
        """测试表达式解析函数"""
        # 基本表达式
        assert parse_expression("1+2") == ["1", "+", "2"]
        assert parse_expression("10 - 5") == ["10", "-", "5"]
        assert parse_expression("3.5*2.1") == ["3.5", "*", "2.1"]
        assert parse_expression("10/2") == ["10", "/", "2"]
        
        # 复杂表达式
        assert parse_expression("(1+2)*3") == ["(", "1", "+", "2", ")", "*", "3"]
        assert parse_expression("1.5 + 2.3 - 0.8") == ["1.5", "+", "2.3", "-", "0.8"]
        
        # 空白字符处理
        assert parse_expression(" 1 + 2 ") == ["1", "+", "2"]
        assert parse_expression("1+2") == ["1", "+", "2"]
    
    def test_validate_input(self):
        """测试输入验证函数"""
        # 有效输入
        assert validate_input("123") == 123.0
        assert validate_input("123.45") == 123.45
        assert validate_input("-123") == -123.0
        assert validate_input("0") == 0.0
        assert validate_input("  123  ") == 123.0
        
        # 无效输入
        assert validate_input("abc") is None
        assert validate_input("") is None
        assert validate_input("   ") is None
        assert validate_input("12a") is None
        assert validate_input("1.2.3") is None
    
    def test_get_operation_symbol(self):
        """测试运算符号获取函数"""
        assert get_operation_symbol("add") == "+"
        assert get_operation_symbol("subtract") == "-"
        assert get_operation_symbol("multiply") == "*"
        assert get_operation_symbol("divide") == "/"
        assert get_operation_symbol("power") == "^"
        assert get_operation_symbol("mod") == "%"
        
        # 大小写不敏感
        assert get_operation_symbol("ADD") == "+"
        assert get_operation_symbol("Subtract") == "-"
        
        # 未知操作
        assert get_operation_symbol("unknown") == "?"
        assert get_operation_symbol("") == "?"
    
    def test_create_calculation_record(self):
        """测试计算记录创建函数"""
        record = create_calculation_record(1.5, 2.5, "add", 4.0)
        
        assert record["operand1"] == 1.5
        assert record["operand2"] == 2.5
        assert record["operation"] == "add"
        assert record["symbol"] == "+"
        assert record["result"] == 4.0
        assert record["formatted_result"] == "4"
        assert record["expression"] == "1.5 + 2.5 = 4"
    
    def test_create_calculation_record_with_integers(self):
        """测试整数计算记录创建"""
        record = create_calculation_record(10, 3, "subtract", 7)
        
        assert record["operand1"] == 10
        assert record["operand2"] == 3
        assert record["operation"] == "subtract"
        assert record["symbol"] == "-"
        assert record["result"] == 7
        assert record["formatted_result"] == "7"
        assert record["expression"] == "10 - 3 = 7"
    
    def test_create_calculation_record_with_floats(self):
        """测试浮点数计算记录创建"""
        record = create_calculation_record(3.14, 2.86, "add", 6.0)
        
        assert record["operand1"] == 3.14
        assert record["operand2"] == 2.86
        assert record["operation"] == "add"
        assert record["symbol"] == "+"
        assert record["result"] == 6.0
        assert record["formatted_result"] == "6"
        assert record["expression"] == "3.14 + 2.86 = 6"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])