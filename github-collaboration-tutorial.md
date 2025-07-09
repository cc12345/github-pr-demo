# GitHub 协同开发完整教程

## 目录

1. [GitHub 协同开发概述](#github-协同开发概述)
2. [Pull Request (PR) 工作流程详解](#pull-request-pr-工作流程详解)
3. [实战演示：创建第一个 PR](#实战演示创建第一个-pr)
4. [PR 操作详解](#pr-操作详解)
5. [CI/CD 集成实战](#cicd-集成实战)
6. [多人协作场景](#多人协作场景)
7. [最佳实践和高级技巧](#最佳实践和高级技巧)

## 📚 配套文档

- **[PR 分支管理最佳实践](./demo-project/pr-branch-management.md)** - 详细解释源分支与目标分支的管理
- **[分支合并演示](./demo-project/branch-merge-demo.md)** - 实际操作演示和常见问题解答
- **[协作开发实战指南](./collaboration-guide.md)** - 基于真实项目的协作经验
- **[CI/CD 集成实例](./demo-project/demo-cicd.md)** - 自动化流程配置和说明

---

## GitHub 协同开发概述

### 什么是 GitHub 协同开发？

GitHub 协同开发是一套基于 Git 版本控制系统的团队协作流程，主要包括：

- **Fork & Clone**：复制项目到个人仓库
- **Branch**：创建功能分支
- **Pull Request (PR)**：代码审查和合并流程
- **Code Review**：代码审查和反馈
- **Merge**：合并代码到主分支
- **CI/CD**：持续集成和部署

### 基本概念

#### Repository（仓库）
- **Origin**：你 fork 的远程仓库
- **Upstream**：原始项目仓库
- **Local**：本地仓库

#### Branch（分支）
- **main/master**：主分支，包含稳定代码
- **develop**：开发分支，包含最新开发代码
- **feature**：功能分支，用于开发新功能
- **hotfix**：热修复分支，用于紧急修复

#### Pull Request（拉取请求）
- 代码合并的正式请求
- 代码审查的平台
- 讨论和协作的空间

---

## Pull Request (PR) 工作流程详解

### PR 生命周期

```
开发者分支 → 创建 PR → 代码审查 → 修改完善 → 合并 → 删除分支
```

### 1. 创建 PR 的前提条件

#### 准备工作
```bash
# 克隆项目
git clone https://github.com/your-username/project.git
cd project

# 添加上游仓库
git remote add upstream https://github.com/original-owner/project.git

# 创建并切换到新分支
git checkout -b feature/new-feature

# 开发完成后提交
git add .
git commit -m "feat: add new feature"

# 推送到个人仓库
git push origin feature/new-feature
```

### 2. PR 分支关系详解 ⭐ 重要概念

#### 核心概念：源分支与目标分支

每个 PR 都有两个关键分支：

**源分支（Head Branch）**：您的功能分支，包含新代码
**目标分支（Base Branch）**：要合并到的分支，接收新代码

```bash
# PR 分支关系示例
功能分支 (feature/new-feature) ──合并──> 目标分支 (main/develop)
   源分支                                    目标分支
```

#### PR 创建时目标分支的确定

**方法 1：明确指定目标分支（推荐）**
```bash
# 合并到 main 分支
gh pr create --base main --head feature/new-feature --title "新功能"

# 合并到 develop 分支  
gh pr create --base develop --head feature/new-feature --title "新功能"

# 合并到 release 分支
gh pr create --base release/v2.0 --head hotfix/urgent-fix --title "紧急修复"
```

**方法 2：使用默认规则**
```bash
# 不指定 --base，GitHub 自动选择目标分支
gh pr create --title "新功能"

# 默认规则：
# 1. 如果当前在 main/master 分支 → 目标分支 = main/master  
# 2. 如果当前在其他分支 → 目标分支 = 当前分支的上游分支
# 3. 没有上游分支 → 目标分支 = 仓库默认分支
```

#### 查看 PR 的分支关系

```bash
# 查看 PR 的源分支和目标分支
gh pr view 1 --json baseRefName,headRefName

# 输出示例：
{
  "baseRefName": "main",                    # 目标分支
  "headRefName": "feature/multiply-function" # 源分支
}

# 查看详细信息
gh pr view 1
# 会显示：feature/multiply-function → main
```

#### ⚠️ 重要提醒：合并时无需手动切换分支

**常见误区**：
```bash
# ❌ 错误做法：以为需要手动切换到目标分支
git checkout main        # 不需要！
gh pr merge 1 --squash   # 然后合并

# ✅ 正确做法：直接合并
gh pr merge 1 --squash   # GitHub 自动处理一切
```

**GitHub 自动执行的操作**：
1. 📥 获取 PR 的分支信息（源分支 → 目标分支）
2. 🔄 自动切换到目标分支
3. 📝 执行合并操作（按指定策略）
4. 📤 推送更新到远程仓库
5. 🧹 清理源分支（如果指定 --delete-branch）

### 3. PR 状态详解

#### Open（开启）
- PR 创建后的初始状态
- 可以继续推送提交来更新 PR
- 团队成员可以进行代码审查

#### Draft（草稿）
- 工作进行中的 PR
- 不能被合并
- 可以转换为正式 PR

#### Review（审查中）
- 等待审查者审查
- 可能需要修改代码
- 审查通过后可以合并

#### Closed（关闭）
- PR 被手动关闭
- 代码未被合并
- 可以重新打开

#### Merged（已合并）
- PR 被成功合并到目标分支
- 不可逆操作
- 通常会自动删除源分支

### 4. PR 合并策略

#### Merge Commit（合并提交）
```bash
# 创建合并提交
git merge --no-ff feature/new-feature
```
- 保留完整的提交历史
- 创建合并节点
- 历史记录清晰但可能复杂

#### Squash and Merge（压缩合并）
```bash
# 压缩所有提交为一个
git merge --squash feature/new-feature
git commit -m "feat: add new feature"
```
- 将分支的所有提交压缩为一个
- 保持主分支历史简洁
- 丢失详细的提交历史

#### Rebase and Merge（变基合并）
```bash
# 变基到目标分支
git rebase main
git checkout main
git merge feature/new-feature
```
- 重写提交历史
- 保持线性历史
- 没有合并提交

---

## 实战演示：创建第一个 PR

### 场景设置

我们将创建一个实际的项目来演示完整的 PR 流程。

### 步骤 1：初始化项目

```bash
# 创建新的 GitHub 仓库
gh repo create github-pr-demo --public --description "GitHub PR 演示项目"

# 克隆到本地
git clone https://github.com/your-username/github-pr-demo.git
cd github-pr-demo
```

### 步骤 2：创建基础项目结构

```bash
# 创建项目文件
mkdir src tests docs
touch README.md
touch src/main.py
touch tests/test_main.py
touch .gitignore
```

### 步骤 3：添加初始代码

**README.md**
```markdown
# GitHub PR 演示项目

这是一个用于演示 GitHub Pull Request 工作流程的项目。

## 功能
- [ ] 基础计算器功能
- [ ] 单元测试
- [ ] CI/CD 集成

## 使用方法

```bash
python src/main.py
```

## 开发指南

1. Fork 项目
2. 创建功能分支
3. 提交 PR
4. 代码审查
5. 合并代码
```

**src/main.py**
```python
#!/usr/bin/env python3
"""
简单计算器演示
"""

def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def main():
    print("欢迎使用简单计算器")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", subtract(5, 3))

if __name__ == "__main__":
    main()
```

**tests/test_main.py**
```python
#!/usr/bin/env python3
"""
计算器测试
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import add, subtract

def test_add():
    """测试加法"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """测试减法"""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("所有测试通过!")
```

**.gitignore**
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
```

### 步骤 4：提交初始代码

```bash
git add .
git commit -m "chore: initial project setup with basic calculator"
git push origin main
```

---

## PR 操作详解

### 1. 创建 PR

#### 使用 GitHub CLI 创建 PR

```bash
# 创建新功能分支
git checkout -b feature/multiply-function

# 添加乘法功能
# 编辑 src/main.py 添加 multiply 函数
```

#### 实际演示：不同目标分支的 PR 创建

**场景 1：合并到默认分支（master）**
```bash
# 当前在 feature/multiply-function 分支
git checkout feature/multiply-function

# 创建 PR，不指定 --base（使用默认）
gh pr create --title "feat: 添加乘法功能"

# 结果：feature/multiply-function → master
# 查看验证：
gh pr view 1 --json baseRefName,headRefName
# 输出：{"baseRefName":"master","headRefName":"feature/multiply-function"}
```

**场景 2：合并到开发分支（develop）**
```bash
# 当前在 feature/power-function 分支
git checkout feature/power-function

# 创建 PR，明确指定目标分支为 develop
gh pr create --base develop --title "feat: 添加幂运算功能"

# 结果：feature/power-function → develop
# 查看验证：
gh pr view 3 --json baseRefName,headRefName
# 输出：{"baseRefName":"develop","headRefName":"feature/power-function"}
```

**场景 3：GitFlow 工作流示例**
```bash
# 功能开发 → develop 分支
gh pr create --base develop --title "feat: 用户认证功能"

# 发布准备 → master 分支
gh pr create --base master --title "release: v2.0.0"

# 紧急修复 → master 分支
gh pr create --base master --title "hotfix: 修复安全漏洞"
```

让我们添加乘法功能：

**更新 src/main.py**
```python
#!/usr/bin/env python3
"""
简单计算器演示
"""

def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def main():
    print("欢迎使用简单计算器")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 6 =", multiply(4, 6))

if __name__ == "__main__":
    main()
```

**更新 tests/test_main.py**
```python
#!/usr/bin/env python3
"""
计算器测试
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import add, subtract, multiply

def test_add():
    """测试加法"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """测试减法"""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    """测试乘法"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print("所有测试通过!")
```

#### 提交并创建 PR

```bash
# 提交更改
git add .
git commit -m "feat: add multiply function with tests"

# 推送到远程分支
git push origin feature/multiply-function

# 使用 gh 创建 PR
gh pr create --title "feat: 添加乘法功能" --body "$(cat <<'EOF'
## 功能描述
添加乘法功能到计算器中

## 变更内容
- 在 main.py 中添加 multiply() 函数
- 在 test_main.py 中添加对应的测试用例
- 更新 main() 函数以演示乘法功能

## 测试
- [x] 单元测试通过
- [x] 手动测试通过
- [x] 代码符合项目规范

## 相关问题
解决了基础计算器缺少乘法功能的问题
EOF
)"
```

### 2. 查看 PR 状态

```bash
# 查看所有 PR
gh pr list

# 查看特定 PR 详情
gh pr view 1

# 查看 PR 的 diff
gh pr diff 1

# 查看 PR 的检查状态
gh pr checks 1
```

### 3. 更新 PR

如果需要修改 PR：

```bash
# 在同一分支上继续修改
git checkout feature/multiply-function

# 做一些修改，比如添加除法功能
# 编辑文件...

git add .
git commit -m "feat: add divide function"
git push origin feature/multiply-function

# PR 会自动更新
```

### 4. 审查 PR

#### 作为审查者

```bash
# 检出 PR 分支进行本地测试
gh pr checkout 1

# 运行测试
python tests/test_main.py

# 添加审查评论
gh pr review 1 --comment --body "代码看起来不错，但建议添加错误处理"

# 请求修改
gh pr review 1 --request-changes --body "请添加除零错误处理"

# 批准 PR
gh pr review 1 --approve --body "代码质量良好，测试通过，可以合并"
```

### 5. 合并 PR

#### ⚠️ 合并前的重要检查

**步骤 1：确认 PR 的分支关系**
```bash
# 查看 PR 将要合并到哪个分支
gh pr view 1 --json baseRefName,headRefName

# 输出示例：
{
  "baseRefName": "master",                    # 目标分支
  "headRefName": "feature/multiply-function"  # 源分支
}

# 如果目标分支不正确，需要重新创建 PR
```

**步骤 2：查看将要合并的内容**
```bash
# 查看代码差异
gh pr diff 1

# 查看 PR 详细信息
gh pr view 1
```

#### 不同的合并选项

**合并到 master 分支示例**：
```bash
# 标准合并（创建合并提交）
gh pr merge 1 --merge --delete-branch
# 结果：feature/multiply-function 合并到 master

# 压缩合并（将所有提交压缩为一个）
gh pr merge 1 --squash --delete-branch
# 结果：feature/multiply-function 的所有提交压缩为一个提交并合并到 master

# 变基合并（重写历史为线性）
gh pr merge 1 --rebase --delete-branch
# 结果：feature/multiply-function 的提交重写并合并到 master
```

**合并到 develop 分支示例**：
```bash
# 场景：PR #3 的目标分支是 develop
gh pr view 3 --json baseRefName,headRefName
# 输出：{"baseRefName":"develop","headRefName":"feature/power-function"}

# 执行合并（自动合并到 develop 分支）
gh pr merge 3 --squash --delete-branch
# 结果：feature/power-function 合并到 develop，NOT master！
```

#### 🔍 合并后的验证

**验证合并结果**：
```bash
# 检查目标分支的提交历史
git log --oneline master -5    # 如果合并到 master
git log --oneline develop -5   # 如果合并到 develop

# 对比不同分支的状态
git log --oneline master develop --graph
```

**实际演示结果**：
```bash
# 演示项目中的实际情况：

# master 分支历史（没有幂运算功能）：
$ git log --oneline master -5
e5b3a65 docs: add comprehensive collaboration guide
3b34cab feat: add comprehensive CI/CD workflows
b9756da feat: add divide function with error handling
15be88d feat: add multiply function with comprehensive tests (#1)
7370208 chore: initial project setup

# develop 分支历史（包含幂运算功能）：
$ git log --oneline develop -5
4744bed feat: add power function for exponentiation (#3)  ← 新功能！
e5b3a65 docs: add comprehensive collaboration guide
3b34cab feat: add comprehensive CI/CD workflows
b9756da feat: add divide function with error handling
15be88d feat: add multiply function with comprehensive tests (#1)
```

#### 合并后的清理

```bash
# 切换到主分支
git checkout main

# 拉取最新代码
git pull origin main

# 删除本地功能分支
git branch -d feature/multiply-function

# 删除远程分支（如果使用 --delete-branch 选项会自动删除）
git push origin --delete feature/multiply-function
```

### 6. 关闭 PR

```bash
# 关闭 PR（不合并）
gh pr close 1 --comment "此功能暂时不需要"

# 重新打开 PR
gh pr reopen 1
```

---

## CI/CD 集成实战

### 1. GitHub Actions 配置

创建 `.github/workflows/ci.yml`：

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        python -m pytest tests/ -v --cov=src/
    
    - name: Run linting
      run: |
        pip install flake8
        flake8 src/ tests/ --max-line-length=88
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      if: matrix.python-version == '3.9'

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      run: |
        echo "部署到生产环境"
        # 这里添加实际的部署脚本
```

### 2. 分支保护规则

```bash
# 使用 GitHub CLI 设置分支保护
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["test"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1}' \
  --field restrictions=null
```

### 3. 自动化 PR 检查

创建 `.github/workflows/pr-check.yml`：

```yaml
name: PR Check

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  pr-check:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Check PR title
      run: |
        if [[ "${{ github.event.pull_request.title }}" =~ ^(feat|fix|docs|style|refactor|test|chore):.* ]]; then
          echo "PR title format is correct"
        else
          echo "PR title must start with: feat:, fix:, docs:, style:, refactor:, test:, or chore:"
          exit 1
        fi
    
    - name: Check for tests
      run: |
        if git diff --name-only HEAD~1 | grep -q "^src/"; then
          if ! git diff --name-only HEAD~1 | grep -q "^tests/"; then
            echo "Warning: Changes to src/ detected but no test files modified"
          fi
        fi
```

---

## 多人协作场景

### 1. Fork 工作流程

#### 贡献者流程

```bash
# 1. Fork 项目到个人账户
gh repo fork original-owner/project

# 2. 克隆个人 Fork
git clone https://github.com/your-username/project.git
cd project

# 3. 添加上游仓库
git remote add upstream https://github.com/original-owner/project.git

# 4. 创建功能分支
git checkout -b feature/new-feature

# 5. 开发和提交
git add .
git commit -m "feat: add new feature"

# 6. 推送到个人仓库
git push origin feature/new-feature

# 7. 创建 PR
gh pr create --repo original-owner/project --title "feat: 添加新功能" --body "功能描述"
```

#### 保持同步

```bash
# 定期同步上游更改
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# 更新功能分支
git checkout feature/new-feature
git rebase main
git push origin feature/new-feature --force-with-lease
```

### 2. 代码审查最佳实践

#### 审查者指南

```bash
# 检出 PR 进行本地测试
gh pr checkout 123

# 运行完整测试套件
python -m pytest tests/ -v

# 检查代码质量
flake8 src/ tests/

# 手动测试功能
python src/main.py
```

#### 审查评论模板

```markdown
## 代码审查清单

### 功能性
- [ ] 功能按预期工作
- [ ] 边界情况处理正确
- [ ] 错误处理完善

### 代码质量
- [ ] 代码可读性良好
- [ ] 遵循项目编码规范
- [ ] 没有重复代码

### 测试
- [ ] 包含充分的单元测试
- [ ] 测试覆盖率足够
- [ ] 测试用例命名清晰

### 文档
- [ ] 代码注释充分
- [ ] API 文档更新
- [ ] 变更日志更新

## 建议

1. 考虑重构 `function_name` 以提高可读性
2. 添加对 `edge_case` 的处理
3. 更新相关文档

## 总结

整体代码质量良好，建议修改上述问题后合并。
```

### 3. 冲突解决

#### 解决合并冲突

```bash
# 拉取最新主分支
git checkout main
git pull upstream main

# 变基功能分支
git checkout feature/new-feature
git rebase main

# 如果有冲突，解决冲突
git add .
git rebase --continue

# 强制推送更新的分支
git push origin feature/new-feature --force-with-lease
```

### 4. 发布工作流程

#### 语义化版本发布

```bash
# 创建发布分支
git checkout -b release/v1.1.0

# 更新版本号
echo "1.1.0" > VERSION

# 更新变更日志
cat >> CHANGELOG.md << 'EOF'
## [1.1.0] - 2024-01-15

### Added
- 乘法功能
- 除法功能
- 错误处理

### Fixed
- 除零错误处理

### Changed
- 改进测试覆盖率
EOF

# 提交发布准备
git add .
git commit -m "chore: prepare release v1.1.0"

# 创建发布 PR
gh pr create --title "chore: Release v1.1.0" --body "准备发布 v1.1.0 版本"

# 合并后创建标签
git checkout main
git pull origin main
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0

# 创建 GitHub 发布
gh release create v1.1.0 --title "v1.1.0" --notes "$(cat CHANGELOG.md)"
```

---

## 最佳实践和高级技巧

### 1. PR 最佳实践

#### PR 大小控制
- 保持 PR 小而专注
- 一个 PR 只做一件事
- 避免超过 400 行代码变更

#### 提交消息规范
```bash
# 使用约定式提交
feat: 添加新功能
fix: 修复bug
docs: 更新文档
style: 代码格式化
refactor: 重构代码
test: 添加测试
chore: 构建过程或辅助工具的变动
```

#### PR 描述模板

创建 `.github/pull_request_template.md`：

```markdown
## 变更类型
- [ ] 新功能
- [ ] Bug 修复
- [ ] 文档更新
- [ ] 性能优化
- [ ] 重构

## 描述
简要描述此 PR 的目的和变更内容。

## 测试
- [ ] 单元测试通过
- [ ] 手动测试通过
- [ ] 回归测试通过

## 检查清单
- [ ] 代码遵循项目规范
- [ ] 自测试通过
- [ ] 添加/更新了相关文档
- [ ] 添加/更新了测试用例

## 相关问题
关闭 #issue_number

## 截图（如适用）
粘贴相关截图

## 额外信息
任何其他相关信息
```

### 2. 高级 Git 技巧

#### 交互式变基
```bash
# 整理提交历史
git rebase -i HEAD~3

# 修改提交消息
git commit --amend

# 拆分提交
git reset HEAD~1
git add file1
git commit -m "feat: add file1"
git add file2
git commit -m "feat: add file2"
```

#### 使用 git hooks
```bash
# 创建 pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# 运行测试
python -m pytest tests/
if [ $? -ne 0 ]; then
    echo "测试失败，阻止提交"
    exit 1
fi

# 运行代码检查
flake8 src/ tests/
if [ $? -ne 0 ]; then
    echo "代码检查失败，阻止提交"
    exit 1
fi
EOF

chmod +x .git/hooks/pre-commit
```

### 3. 自动化工具

#### 使用 GitHub CLI 脚本

创建 `scripts/pr-workflow.sh`：

```bash
#!/bin/bash

# PR 工作流自动化脚本

set -e

FEATURE_NAME=$1
if [ -z "$FEATURE_NAME" ]; then
    echo "用法: $0 <feature-name>"
    exit 1
fi

echo "🚀 开始 PR 工作流程: $FEATURE_NAME"

# 1. 同步主分支
echo "📥 同步主分支..."
git checkout main
git pull upstream main
git push origin main

# 2. 创建功能分支
echo "🌿 创建功能分支..."
git checkout -b feature/$FEATURE_NAME

# 3. 开发完成后的提示
echo "✅ 功能分支已创建: feature/$FEATURE_NAME"
echo "📝 现在可以开始开发，完成后运行:"
echo "    git add ."
echo "    git commit -m 'feat: $FEATURE_NAME'"
echo "    git push origin feature/$FEATURE_NAME"
echo "    gh pr create --title 'feat: $FEATURE_NAME' --body 'Add $FEATURE_NAME feature'"
```

#### 使用 GitHub Actions 模板

创建 `.github/workflows/auto-label.yml`：

```yaml
name: Auto Label PR

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest
    
    steps:
    - name: Label PR based on files changed
      uses: actions/labeler@v4
      with:
        repo-token: "${{ secrets.GITHUB_TOKEN }}"
        configuration-path: .github/labeler.yml
    
    - name: Label PR based on title
      uses: actions/github-script@v6
      with:
        script: |
          const title = context.payload.pull_request.title.toLowerCase();
          const labels = [];
          
          if (title.includes('feat:')) labels.push('enhancement');
          if (title.includes('fix:')) labels.push('bug');
          if (title.includes('docs:')) labels.push('documentation');
          if (title.includes('test:')) labels.push('tests');
          
          if (labels.length > 0) {
            github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              labels: labels
            });
          }
```

### 4. 监控和度量

#### PR 度量指标

```bash
# 查看 PR 统计
gh pr list --state all --json number,title,state,createdAt,closedAt \
  | jq '.[] | select(.state == "MERGED") | {title, createdAt, closedAt}'

# 计算平均 PR 生命周期
gh pr list --state merged --limit 50 --json createdAt,closedAt \
  | jq -r '.[] | [.createdAt, .closedAt] | @csv' \
  | while IFS=, read -r created closed; do
      # 计算时间差
      echo "PR 生命周期分析"
    done
```

#### 代码审查度量

```bash
# 审查者活跃度
gh pr list --state all --json reviews \
  | jq -r '.[] | .reviews[]? | .author.login' \
  | sort | uniq -c | sort -nr
```

这个完整的教程涵盖了 GitHub 协同开发的各个方面，从基础概念到高级技巧，包含了丰富的实战示例。你可以按照教程逐步实践，掌握现代软件开发的协作流程。

需要我对某个特定部分进行更详细的演示吗？