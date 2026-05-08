# 第 6 课：GitHub 集成与钩子 (Hooks) 参考

## GitHub 集成

Claude Code GitHub Actions 将 Claude 引入你的 GitHub 工作流。设置完成后，你可以在任何 Pull Request (PR) 或 Issue 中提及 `@claude`。它可以实现代码、创建 PR 并审查代码。最简单的设置方法是在终端中运行 `/install-github-app`。

你可以查看[此处文档](https://docs.anthropic.com/en/docs/claude-code/github-actions)，了解有关如何使用此集成的更多信息。

## 钩子 (Hooks)

Claude Code 钩子是你可以定义的 Shell 命令，可以在 Claude Code 生命周期的各个阶段执行（工具执行前、工具执行后、子代理完成任务时、Claude 完成响应时）。

我们在本课中展示了一个关于钩子的简短示例。如果你想了解更多关于钩子的信息并查看更多示例，建议查看：

- Anthropic Academy 课程 [Claude Code In action](https://anthropic.skilljar.com/claude-code-in-action/312000) 中的 “Hooks” 部分。
- 文档：[钩子指南 (Hooks guide)](https://docs.anthropic.com/en/docs/claude-code/hooks-guide) 和 [钩子参考 (Hooks reference)](https://docs.anthropic.com/en/docs/claude-code/hooks)。
