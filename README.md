# GitHub PR 演示项目

这是一个用于演示 GitHub Pull Request 工作流程的项目。

## 项目结构

```
demo-project/
├── src/
│   ├── calculator.py      # 主要功能模块
│   └── utils.py          # 工具函数
├── tests/
│   ├── test_calculator.py # 测试文件
│   └── test_utils.py     # 工具测试
├── docs/
│   └── api.md            # API 文档
├── .github/
│   └── workflows/        # CI/CD 配置
├── requirements.txt      # 依赖管理
└── README.md            # 项目说明

```

## 功能特性

- [x] 基础计算器功能（加、减）
- [ ] 扩展功能（乘、除）
- [ ] 错误处理
- [ ] 单元测试
- [ ] CI/CD 集成
- [ ] 代码文档

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行程序

```bash
python src/calculator.py
```

### 运行测试

```bash
python -m pytest tests/
```

## 开发工作流程

### 1. 克隆项目

```bash
git clone https://github.com/your-username/demo-project.git
cd demo-project
```

### 2. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

### 3. 开发功能

编写代码，添加测试...

### 4. 提交更改

```bash
git add .
git commit -m "feat: add your feature"
```

### 5. 推送分支

```bash
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

```bash
gh pr create --title "feat: Your Feature" --body "描述你的功能"
```

## 代码规范

- 使用 PEP 8 Python 代码规范
- 提交消息遵循 [Conventional Commits](https://www.conventionalcommits.org/)
- 所有功能必须包含测试
- 代码覆盖率要求 > 80%

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交变更
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License