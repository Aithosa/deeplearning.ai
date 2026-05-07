# 课程讲义：第七节 - 探索 GitHub 集成与钩子

## 1. 恢复对话 (Resuming Conversations)

- **场景**：当你需要回到之前的任务（如移除合并后的 worktrees）时。
- **命令**：使用 `claude --resume` 标志。
- **功能**：允许你继续之前的对话上下文，而无需重新解释背景。

## 2. GitHub 集成 (GitHub Integration)

Claude Code 不仅在终端运行，还可以作为 GitHub 的“虚拟队友”存在。

- **安装**：使用 `/install-GitHub-app` 命令。
- **核心组件**：
  - **GitHub App**：连接仓库。
  - **SDK**：允许在终端之外运行 Claude Code。
  - **GitHub Actions**：通过 YAML 文件定义自动化工作流。
- **主要用途**：
  - **代码审查 (Code Review)**：自动分析 PR 中的代码质量、安全性和最佳实践。
  - **议题修复 (Issue Fixing)**：通过在 Issue 中标记 Claude (@claude)，让它自动生成 PR 修复问题。

## 3. 自我审查 (Self-Review)

- **机制**：当 Claude 提交代码并生成 PR 后，另一个 Claude 实例（通过 GitHub Action）会对其工作进行双重检查。
- **价值**：增加了代码的安全性和可靠性。

## 4. Claude Code 钩子 (Hooks)

钩子允许你在 Claude Code 的生命周期事件中注入自定义代码。

- **管理命令**：`/hooks`。
- **配置文件**：存储在 `.claude/settings.local.json` 中。
- **常见事件**：
  - `BeforeToolUse`：工具执行前（可阻止执行）。
  - `PostToolUse`：工具执行后。
  - `UserPrompt`：用户提交提示词时。
  - `AgentConclusion`：代理完成任务前。
- **匹配器 (Matcher)**：可以指定钩子仅对特定工具（如 `read`, `grep`, `edit`）生效。

## 5. 实战技巧：使用钩子自动化任务

- **自动化测试**：在编辑文件后自动运行测试。
- **Linting**：在提交前自动格式化代码。
- **通知系统**：任务完成后通过系统语音或弹窗提醒。

---

**下一节预告**：我们将探索如何在 Jupyter notebooks 中使用 Claude Code 进行数据科学任务、代码重构和可视化。
