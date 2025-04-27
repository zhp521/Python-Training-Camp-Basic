# Python训练营基础部分

欢迎来到 Python 训练营的基础部分！本项目旨在通过一系列实践练习，帮助你巩固 Python 编程的基础知识。

你需要通过补全 `exercises` 目录下的 Python 代码，并通过运行提供的测试来验证你的实现。

## 练习内容

### 第1部分: 基础入门
1.  `exercises/hello_world.py`: `print` 输出语句。
2.  `exercises/data_types.py`: 变量和基本数据类型 (整数, 浮点数, 字符串等)。

### 第2部分: 控制结构
3.  `exercises/if_else.py`: `if-elif-else` 条件语句。
4.  `exercises/for_loop.py`: `for` 循环。
5.  `exercises/while_loop.py`: `while` 循环。
6.  `exercises/break_continue.py`: `break` 和 `continue` 语句。

### 第3部分: 函数和模块
7.  `exercises/function_params.py`: 函数定义和参数传递。
8.  `exercises/math_module.py`: 使用 `math` 模块进行计算。

### 第4部分: 数据结构
9.  `exercises/list_operations.py`: 列表常用操作。
10. `exercises/dict_operations.py`: 字典常用操作。
11. `exercises/set_operations.py`: 集合常用操作。

### 第5部分: 字符串操作
12. `exercises/string_formatting.py`: 字符串格式化 (f-strings)。
13. `exercises/string_split.py`: 字符串分割 (`split` 方法)。
14. `exercises/regex_match.py`: 正则表达式基础匹配。

### 第6部分: 文件操作和网络
15. `exercises/file_operations.py`: 文件读写基础。
16. `exercises/http_requests.py`: 发送 HTTP 请求和处理响应。

### 第7部分: 面向对象编程
17. `exercises/oop_basics.py`: 类和对象的基础。

## 操作流程

请按照以下步骤完成练习：

**1. 准备 GitHub 仓库**

*   **Fork**: 点击本仓库页面右上角的 "Fork" 按钮，将此仓库复制到你自己的 GitHub 账户下。
*   **Clone**: 在你的电脑上选择一个合适的位置，打开终端或 Git Bash，运行以下命令将你 Fork 的仓库克隆到本地：
    ```bash
    git clone https://github.com/YOUR_USERNAME/Python-Training-Camp-Basic.git
    cd Python-Training-Camp-Basic
    ```
    (请将 `YOUR_USERNAME` 替换为你的 GitHub 用户名)

**2. 设置本地开发环境**

*   **Python 版本**: 建议使用 Python 3.8, 3.9 或 3.10 (与 GitHub Actions 测试环境一致)。
*   **创建虚拟环境 (推荐)**:
    ```bash
    python -m venv .venv
    ```
*   **激活虚拟环境**:
    *   Linux / macOS: `source .venv/bin/activate`
    *   Windows: `.venv\Scripts\activate`
*   **安装依赖**: 激活虚拟环境后，安装必要的库：
    ```bash
    pip install -r requirements.txt
    ```
    主要依赖包括 `pytest`, `flake8`, `pytest-cov`, `requests`。

**3. 完成练习**

*   打开 `exercises/` 目录，根据 [建议学习顺序](#建议学习顺序) 或你感兴趣的主题选择一个 `.py` 文件。
*   仔细阅读文件顶部的说明和代码中的注释，理解需要实现的功能。
*   在标记为 `# TODO:` 或 `# 请在下方编写代码` 的地方编写你的 Python 代码。

**4. 本地测试 (可选但推荐)**

*   在提交前运行测试，检查代码是否通过：
    ```bash
    # 运行所有测试
    python -m pytest tests/ -v
    
    # 运行单个练习的测试 (例如 if_else.py)
    python -m pytest tests/test_if_else.py -v
    ```
*   根据测试结果 (`PASSED`/`FAILED`) 调试代码。

**5. 提交代码与自动评分**

*   **提交更改**: 
    ```bash
    git add exercises/your_modified_file.py
    git commit -m "完成 if_else.py 练习"
    git push origin main
    ```
    (修改 `your_modified_file.py` 和提交信息)
*   **查看评分**: 
    *   代码推送后，GitHub Actions 会自动运行测试并评分。
    *   访问你 Fork 仓库的 "Actions" 页面，点击名为 **"Python测试"** 的工作流查看运行状态。
    *   (如果 Actions 未自动运行，请手动启用或触发)
    *   工作流会运行所有测试。如果所有测试都通过，你将获得 100 分；只要有任何一个测试失败，则为 0 分。
    *   最终分数会自动发送到评分系统（用于课程排名）。
    *   你可以在 Actions 的 "Summary" 页面查看详细的测试报告和练习完成情况。

## 建议学习顺序

建议按照练习文件的编号顺序进行：

## 运行测试

## 运行测试 (本地)

```bash
# 确保已安装依赖
# pip install -r requirements.txt

# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_if_else.py -v
```

## 评分标准

GitHub Actions 会自动进行评分：
*   **100 分**: `tests/` 目录下的所有测试用例全部通过。
*   **0 分**: `tests/` 目录下至少有一个测试用例失败。

## 目录结构

```
Python-Training-camp/
├── exercises/             # 练习题目
│   ├── hello_world.py
│   ├── data_types.py
│   ├── if_else.py
│   ├── for_loop.py
│   ├── while_loop.py
│   ├── ...
│   ├── string_formatting.py
│   ├── string_split.py
│   ├── regex_match.py
│   ├── file_operations.py
│   ├── http_requests.py
│   └── oop_basics.py
├── tests/                 # 测试文件
│   ├── test_hello_world.py
│   ├── test_data_types.py
│   ├── ...
│   ├── test_string_split.py
│   ├── test_regex_match.py
│   ├── test_file_operations.py
│   ├── test_http_requests.py
│   └── test_oop_basics.py
└── requirements.txt       # 项目依赖
``` 
