#!/usr/bin/env python3
"""
简单计算器模块
提供基础的数学运算功能
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """简单计算器类"""
    
    def __init__(self):
        """初始化计算器"""
        self.history = []
    
    def add(self, a: Number, b: Number) -> Number:
        """
        加法运算
        
        Args:
            a: 第一个数字
            b: 第二个数字
            
        Returns:
            两数之和
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        减法运算
        
        Args:
            a: 被减数
            b: 减数
            
        Returns:
            两数之差
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        乘法运算
        
        Args:
            a: 第一个数字
            b: 第二个数字
            
        Returns:
            两数之积
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Number, b: Number) -> Number:
        """
        除法运算
        
        Args:
            a: 被除数
            b: 除数
            
        Returns:
            两数之商
            
        Raises:
            ZeroDivisionError: 当除数为零时抛出
        """
        if b == 0:
            raise ZeroDivisionError("不能除以零")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        获取计算历史
        
        Returns:
            计算历史记录列表
        """
        return self.history.copy()
    
    def clear_history(self):
        """清空计算历史"""
        self.history.clear()


def main():
    """主程序入口"""
    calc = Calculator()
    
    print("🧮 欢迎使用简单计算器")
    print("=" * 30)
    
    # 演示基础功能
    print("📊 基础运算演示：")
    print(f"1 + 2 = {calc.add(1, 2)}")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"4 * 6 = {calc.multiply(4, 6)}")
    print(f"12 / 3 = {calc.divide(12, 3)}")
    print(f"5.5 + 2.3 = {calc.add(5.5, 2.3)}")
    print(f"15 - 7.5 = {calc.subtract(15, 7.5)}")
    print(f"3.5 * 2.0 = {calc.multiply(3.5, 2.0)}")
    print(f"7.5 / 2.5 = {calc.divide(7.5, 2.5)}")
    
    print("\n📝 计算历史：")
    for record in calc.get_history():
        print(f"  {record}")
    
    print("\n✨ 更多功能正在开发中...")
    print("  - 高级数学函数")
    print("  - 表达式解析")
    print("  - 科学计算")
    print("  - 数据可视化")


if __name__ == "__main__":
    main()