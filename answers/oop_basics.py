class Student:
    """
    学生类
    
    包含学生的基本信息(姓名、年龄、成绩)和相关方法
    """
    
    def __init__(self, name, age, grade):
        """
        初始化学生对象
        
        参数:
        - name: 学生姓名
        - age: 学生年龄
        - grade: 学生成绩
        """
        # 初始化学生属性
        self.name = name
        self.age = age
        self.grade = grade
    
    def print_info(self):
        """
        打印学生信息
        
        打印格式:
        姓名: [name], 年龄: [age], 成绩: [grade]
        
        返回:
        - 无返回值，直接打印信息
        """
        # 打印学生信息
        print(f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.grade}")
    
    def is_passing(self):
        """
        判断学生是否通过考试
        
        标准:
        - 成绩大于等于60分为通过
        
        返回:
        - 布尔值，表示是否通过考试
        """
        # 判断成绩是否达到及格标准
        return self.grade >= 60


def create_student_example():
    """
    创建一个Student类的实例并调用方法
    
    返回:
    - 创建的Student对象
    """
    # 创建一个Student对象，设置姓名为"张三"，年龄为18，成绩为85
    student = Student("张三", 18, 85)
    
    # 调用print_info()方法打印学生信息
    student.print_info()
    
    # 返回创建的Student对象
    return student 