"""
测试练习: 面向对象编程基础
"""
import pytest
import sys
import os
import io
from contextlib import redirect_stdout

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的类和函数
from exercises.oop_basics import Student, create_student_example

def test_student_init():
    """测试Student类初始化"""
    student = Student("李明", 20, 85)
    
    # 检查属性是否被正确设置
    assert hasattr(student, 'name'), "Student对象应该有name属性"
    assert hasattr(student, 'age'), "Student对象应该有age属性"
    assert hasattr(student, 'grade'), "Student对象应该有grade属性"
    
    assert student.name == "李明", "name属性应该正确设置"
    assert student.age == 20, "age属性应该正确设置"
    assert student.grade == 85, "grade属性应该正确设置"

def test_student_print_info():
    """测试print_info方法"""
    student = Student("王芳", 19, 92)
    
    # 捕获标准输出
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        student.print_info()
    
    output = captured_output.getvalue().strip()
    
    # 检查输出是否包含学生信息
    assert "姓名: 王芳" in output, "输出应该包含学生姓名"
    assert "年龄: 19" in output, "输出应该包含学生年龄"
    assert "成绩: 92" in output, "输出应该包含学生成绩"

def test_student_is_passing():
    """测试is_passing方法"""
    # 测试及格情况
    passing_student = Student("赵六", 21, 60)
    assert passing_student.is_passing() is True, "60分应该被判定为及格"
    
    passing_student2 = Student("钱七", 22, 75)
    assert passing_student2.is_passing() is True, "75分应该被判定为及格"
    
    # 测试不及格情况
    failing_student = Student("孙八", 20, 59)
    assert failing_student.is_passing() is False, "59分应该被判定为不及格"
    
    failing_student2 = Student("周九", 18, 45)
    assert failing_student2.is_passing() is False, "45分应该被判定为不及格"

def test_create_student_example():
    """测试create_student_example函数"""
    # 捕获标准输出
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        student = create_student_example()
    
    output = captured_output.getvalue().strip()
    
    # 检查返回值是否为Student对象
    assert isinstance(student, Student), "函数应该返回Student对象"
    
    # 检查学生属性是否符合要求
    assert student.name == "张三", "学生姓名应该是'张三'"
    assert student.age == 18, "学生年龄应该是18"
    assert student.grade == 85, "学生成绩应该是85"
    
    # 检查是否正确调用了print_info方法
    assert "姓名: 张三" in output, "应该打印学生姓名"
    assert "年龄: 18" in output, "应该打印学生年龄"
    assert "成绩: 85" in output, "应该打印学生成绩" 