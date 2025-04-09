# Python训练营

本项目包含一系列Python编程练习，涵盖了Python基础知识的各个方面。学生需要补全缺失的代码，并通过测试来验证自己的实现是否正确。

## 练习内容

### 第1部分: 基础入门
1. **hello_world.py**: print 输出语句
2. **data_types.py**: 变量和数据类型（整数、浮点数、字符串等）
3. **python_environment.py**: Python环境配置与检查

### 第2部分: 控制结构
4. **if_else.py**: if-elif-else条件语句
5. **for_loop.py**: for循环
6. **while_loop.py**: while循环
7. **break_continue.py**: break和continue语句

### 第3部分: 函数和模块
8. **function_params.py**: 函数定义和参数
9. **math_module.py**: 使用math模块

### 第4部分: 数据结构
10. **list_operations.py**: 列表操作
11. **dict_operations.py**: 字典操作 
12. **set_operations.py**: 集合操作

### 第5部分: 字符串操作
13. **string_formatting.py**: 字符串格式化

## 使用方法

1. 打开对应的练习文件（如`exercises/if_else.py`）
2. 阅读文件顶部的说明，了解需要实现的功能
3. 在标记为`# 请在下方编写代码`的位置编写你的代码
4. 使用pytest运行测试，检查你的实现是否正确

## 建议学习顺序

建议按照上述编号顺序学习，从基础逐步深入：
1. 先掌握基础入门部分（输出、数据类型、环境配置）
2. 学习控制结构（条件、循环）
3. 掌握函数定义与使用
4. 学习数据结构操作
5. 最后学习字符串格式化

## 运行测试

可以使用以下命令运行测试：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_if_else.py
```

## 参考答案

在`answers/`目录下提供了所有练习的参考答案实现。如果你遇到困难或想要检查自己的解决方案，可以参考这些文件。建议先尝试自己解决，只有在需要帮助时才查看参考答案。

## 评分标准

测试结果只有通过和不通过两种状态：
- 通过：所有测试用例都符合预期
- 不通过：至少有一个测试用例失败

## 目录结构

```
Python-Training-camp/
├── exercises/             # 练习题目
│   ├── hello_world.py
│   ├── data_types.py
│   ├── python_environment.py
│   ├── if_else.py
│   └── ...
├── tests/                 # 测试文件
│   ├── test_hello_world.py
│   ├── test_data_types.py
│   ├── test_python_environment.py
│   └── ...
├── answers/               # 参考答案
│   ├── hello_world.py
│   ├── data_types.py
│   ├── python_environment.py
│   └── ...
└── requirements.txt       # 项目依赖
``` 