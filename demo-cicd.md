# CI/CD 集成演示

## 项目的 CI/CD 流程

### 1. 触发条件
- 推送到 `main` 或 `develop` 分支
- 创建 PR 到 `main` 或 `develop` 分支

### 2. 流水线阶段

#### Test 阶段
- **多版本测试**: Python 3.8, 3.9, 3.10, 3.11
- **代码检查**: 使用 flake8 进行代码规范检查
- **类型检查**: 使用 mypy 进行类型检查
- **单元测试**: 使用 pytest 运行测试套件
- **覆盖率报告**: 生成代码覆盖率报告

#### Security 阶段
- **安全扫描**: 使用 bandit 进行安全漏洞扫描
- **依赖检查**: 使用 safety 检查依赖安全性

#### Build 阶段
- **构建包**: 使用 Python build 工具构建分发包
- **上传构件**: 保存构建产物

#### Deploy 阶段
- **部署条件**: 仅在 main 分支且推送事件时触发
- **部署流程**: 下载构建产物并部署到预发布环境

### 3. 分支保护

建议设置以下分支保护规则：

```bash
# 设置分支保护
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["test"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1}' \
  --field restrictions=null
```

### 4. 自动化标签

PR 会根据以下规则自动打标签：
- `feat:` → `enhancement`
- `fix:` → `bug`
- `docs:` → `documentation`
- `test:` → `tests`

### 5. 质量标准

- 代码必须通过 linting
- 所有测试必须通过
- 代码覆盖率要求
- 安全扫描无高危漏洞

### 6. 监控和通知

- 构建失败时自动通知
- 部署成功时发送确认
- 安全扫描结果报告

## 使用示例

### 本地开发流程

```bash
# 1. 创建功能分支
git checkout -b feature/new-feature

# 2. 开发功能
# ... 编写代码 ...

# 3. 运行本地测试
pytest tests/ -v --cov=src/

# 4. 提交更改
git add .
git commit -m "feat: add new feature"

# 5. 推送并创建 PR
git push origin feature/new-feature
gh pr create --title "feat: Add new feature" --body "描述"
```

### CI/CD 自动化流程

1. **推送代码** → 触发 CI 流水线
2. **运行测试** → 多版本并行测试
3. **安全扫描** → 检查代码安全性
4. **构建验证** → 确保代码可以正确构建
5. **部署检查** → 验证部署流程

### 质量门控

- ✅ 所有测试通过
- ✅ 代码覆盖率 > 80%
- ✅ 安全扫描通过
- ✅ 代码审查通过
- ✅ 分支保护规则满足

只有满足所有条件的 PR 才能合并到主分支。