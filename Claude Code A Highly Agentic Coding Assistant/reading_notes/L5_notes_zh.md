# 第 5 课：同时添加多个功能 - 使用 Git 工作树 (Worktrees)

## 自定义斜杠命令 (Custom Slash Commands)

- 在项目目录的 `.claude` 文件夹内，创建一个名为 `commands` 的文件夹。
- 在 `commands` 文件夹内，创建一个 Markdown 文件：`implement-feature.md`。
- 将以下内容复制到该 Markdown 文件中：

```
You will be implementing a new feature in this codebase

$ARGUMENTS

IMPORTANT: Only do this for front-end features.
Once this feature is built, make sure to write the changes you made to file called frontend-changes.md
Do not ask for permissions to modify this file, assume you can always do it.
```

- 重新启动 Claude Code，你现在就可以像使用其他内置命令一样使用该自定义命令了。

## 什么是 Git 工作树 (Worktrees)？

Git 工作树允许你将同一个代码仓库的多个分支检出到不同的目录中。每个工作树代表工作目录的一个副本，文件相互隔离，但共享同一个 Git 历史记录。

## 工作流程

- 首先确保你已经添加并提交了代码库之前的任何更改。
- 创建 .trees 文件夹：`mkdir .trees`。
- 为你要实现的每个功能创建一个工作树：
  - `git worktree add .trees/ui_feature`
  - `git worktree add .trees/testing_feature`
  - `git worktree add .trees/quality_feature`
- 在每个工作树中打开集成终端，在每个终端中启动 Claude Code，并要求它实现相应的功能。
- 在每个工作树中，添加并提交各自的更改。
- 关闭 Claude 终端。
- 在主终端中：要求 Claude Code 执行 `git merge` 合并工作树并解决任何合并冲突（提示词示例：`使用 git merge 命令将 .trees 文件夹中的所有工作树合并到 main 分支中，并修复任何冲突（如果有的话）`）。

## 每个功能所使用的提示词

### UI 功能

```
添加一个切换按钮，允许用户在深色和浅色主题之间切换。

1. 切换按钮设计
    - 创建一个符合现有设计美学的切换按钮
    - 将其放置在右上角
    - 使用基于图标的设计（太阳/月亮图标或类似图标）
    - 切换时有平滑的过渡动画
    - 按钮应该是无障碍的，并且支持键盘导航

2. 浅色主题 CSS 变量
    添加带有适当颜色的浅色主题变体：
    - 浅色背景色
    - 深色文本以获得良好的对比度
    - 调整主色和辅助色
    - 适当的边框和表面颜色
    - 保持良好的无障碍标准

3. JavaScript 功能
    - 点击按钮时在主题之间切换
    - 主题之间平滑过渡

4. 实现细节
    - 使用 CSS 自定义属性（CSS 变量）进行主题切换
    - 在 body 或 html 元素上添加 data-theme 属性
    - 确保所有现有元素在两种主题下都能良好运行
    - 保持当前的视觉层次结构和设计语言
```

### 测试功能

```
增强 @backend/tests 中现有的 RAG 系统测试框架。当前的测试涵盖了单元组件，但缺少必要的 API 测试基础设施：

- API 端点测试 - 测试 FastAPI 端点（/api/query, /api/courses, /）的正确请求/响应处理
- pytest 配置 - 在 pyproject.toml 中添加 pytest.ini_options 以实现更简洁的测试执行
- 测试固件 (Fixtures) - 创建 conftest.py，包含用于 Mock 和测试数据设置的共享固件

backend/app.py 中的 FastAPI 应用挂载了在测试环境中不存在的静态文件。要么创建一个独立的测试应用，要么在测试文件中内联定义 API 端点，以避免导入问题。
```

### 质量功能

```
在开发工作流中添加基本的代码质量工具。设置 black 进行代码自动格式化。在整个代码库中保持格式的一致性，并创建用于运行质量检查的开发脚本。
```

## Claude Code 功能摘要

**自定义斜杠命令 (Custom Slash Commands)**

- 在项目目录的 `.claude` 文件夹内，创建一个名为 `commands` 的文件夹。
- 在 `commands` 文件夹内，创建一个 Markdown 文件：`implement-feature.md`。
- 将以下内容复制到该 Markdown 文件中：

  ```
  You will be implementing a new feature in this codebase

  $ARGUMENTS

  IMPORTANT: Only do this for front-end features.
  Once this feature is built, make sure to write the changes you made to file called frontend-changes.md
  Do not ask for permissions to modify this file, assume you can always do it.
  ```

- 重新启动 Claude Code，你现在就可以像使用其他内置命令一样使用该命令了。
