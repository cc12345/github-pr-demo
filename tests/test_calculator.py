#!/usr/bin/env python3
"""
计算器模块测试
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from calculator import Calculator


class TestCalculator:
    """计算器测试类"""
    
    def setup_method(self):
        """每个测试方法前的设置"""
        self.calc = Calculator()
    
    def test_add_integers(self):
        """测试整数加法"""
        assert self.calc.add(1, 2) == 3
        assert self.calc.add(10, 20) == 30
        assert self.calc.add(-5, 5) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_add_floats(self):
        """测试浮点数加法"""
        assert self.calc.add(1.5, 2.5) == 4.0
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)
        assert self.calc.add(-1.5, 1.5) == 0.0
    
    def test_add_mixed_types(self):
        """测试混合类型加法"""
        assert self.calc.add(1, 2.5) == 3.5
        assert self.calc.add(2.5, 1) == 3.5
        assert self.calc.add(-1, 1.5) == 0.5
    
    def test_subtract_integers(self):
        """测试整数减法"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 20) == -10
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(5, 0) == 5
    
    def test_subtract_floats(self):
        """测试浮点数减法"""
        assert self.calc.subtract(5.5, 2.3) == pytest.approx(3.2)
        assert self.calc.subtract(1.0, 0.5) == 0.5
        assert self.calc.subtract(0.3, 0.1) == pytest.approx(0.2)
    
    def test_subtract_mixed_types(self):
        """测试混合类型减法"""
        assert self.calc.subtract(5, 2.5) == 2.5
        assert self.calc.subtract(2.5, 1) == 1.5
        assert self.calc.subtract(1.5, 1) == 0.5
    
    def test_history_tracking(self):
        """测试历史记录功能"""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        
        history = self.calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history
    
    def test_clear_history(self):
        """测试清空历史记录"""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        
        assert len(self.calc.get_history()) == 2
        
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
    
    def test_history_immutability(self):
        """测试历史记录不可变性"""
        self.calc.add(1, 2)
        
        history1 = self.calc.get_history()
        history2 = self.calc.get_history()
        
        # 修改返回的历史记录不应影响原始记录
        history1.append("fake record")
        assert len(self.calc.get_history()) == 1
        assert len(history2) == 1
    
    def test_large_numbers(self):
        """测试大数运算"""
        large_num1 = 999999999999999
        large_num2 = 111111111111111
        
        result = self.calc.add(large_num1, large_num2)
        assert result == 1111111111111110
        
        result = self.calc.subtract(large_num1, large_num2)
        assert result == 888888888888888
    
    def test_negative_numbers(self):
        """测试负数运算"""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.add(-5, 3) == -2
        assert self.calc.subtract(-5, 3) == -8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])