# 课程提示词与总结

本笔记包含课程中使用的提示词链接、其他资源以及 Claude Code 功能的总结。

**注意**：要将此阅读项标记为完成，请务必滚动到底部并点击“标记为完成”。

## 提示词

以下是各课笔记和提示词的链接：

- [第 2 课提示词：设置与代码库理解](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L2_notes.md)
- [第 3 课提示词：添加功能](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L3_notes.md)
- [第 4 课提示词：测试、错误调试与代码重构](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L4_notes.md)
- [第 5 课提示词：同时添加多个功能 - 使用 Git Worktrees](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L5_notes.md)
- [第 6 课笔记：GitHub 集成与 Hooks 引用](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L6_notes.md)
- [第 7 课提示词：重构 Jupyter Notebook 并创建仪表板](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L7_notes.md)
- [第 8 课提示词：基于 Figma 设计稿创建 Web 应用](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L8_notes.md)

## 其他资源

要了解有关这些功能以及其他功能的更多信息，你可以查看：

- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 常用工作流](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
- [Claude Code 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code 使用案例](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

Anthropic Academy 上还有一门很棒的课程，你可以查看更多 Claude Code 的示例：

- [行动中的 Claude Code](https://anthropic.skilljar.com/claude-code-in-action)

## Claude Code 功能总结

### 管理项目记忆

- `/init`：Claude Code 扫描你的代码库并在项目目录中创建 CLAUDE.md 文件。
  - CLAUDE.md 引导 Claude 了解你的代码库，指出重要的命令、架构和编码风格。每次启动 Claude Code 时，它都会自动包含在上下文中。
  - 这是为 RAG 聊天机器人示例通过 `init` 生成的 [CLAUDE.md 文件示例](https://github.com/https-deeplearning-ai/ragchatbot-codebase/blob/main/CLAUDE.md)。

- `#`：使用 `#` 快速添加记忆。当你发现 Claude Code 重复出现错误时非常有用。
  - **示例 1**：由于该项目是一个 `uv` 项目，我们使用 `#` 将以下内容添加到 CLAUDE.md 文件中：
    - `#`使用 uv 运行 python 文件或添加任何依赖项
  - **示例 2**：你可以向 Claude Code 提供数据库架构信息，例如，如果你有一个向量数据库，可以告知其存储在其中的集合：
    - `#`向量数据库有两个集合：
      - `course_catalog`：
        - 存储用于名称解析的课程标题
        - 每个课程的元数据：标题、讲师、课程链接、课时数、课程 JSON（课程列表：课号、课名、课链接）
      - `course_content`：
        - 存储用于语义搜索的文本块
        - 每个块的元数据：课程标题、课号、块索引

### Claude Code 命令总结

| 命令       | 描述                                                                                                                             |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `/clear`   | 清除当前对话历史                                                                                                                 |
| `/compact` | 总结当前对话历史                                                                                                                 |
| `ESC`      | 中断 Claude 以进行重定向或纠正                                                                                                   |
| `ESC ESC`  | 将对话回滚到较早的时间点                                                                                                         |
| `@`        | 使用 `@` 提及文件，将其内容包含在你的请求中                                                                                      |
| `/mcp`     | 管理 MCP 连接并检查可用的 MCP 服务器及其提供的工具（[Claude Code 中的 MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)） |

你可以在 Claude Code 中使用常规 bash 命令，但需要以 `!` 开头（例如：`!pwd`）。你可以输入 `exit` 退出 Claude Code。

| 快捷键        | 描述                                                                  |
| ------------- | --------------------------------------------------------------------- |
| `shift`+`tab` | 在计划模式和自动接受模式之间切换                                      |
| 截图          | `cmd`+ `shift`+ `ctrl` + `4` (Mac) 或 `Win` + `Shift` + `S` (Windows) |
| 粘贴截图      | `Ctrl` + `V`（在 Windows 上可能不起作用）                             |

### 其他 Claude 功能

- **扩展思考模式 (Extended Thinking Mode)**

  对于复杂任务（例如，复杂的架构更改、调试复杂问题），你可以使用“think”一词来触发[扩展思考模式](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)。思考有多个级别：“think” < “think hard” < “think harder” < “ultrathink”。每个级别都会为 Claude 分配更多的思考预算。

- **子代理的使用 (Use of subagents)**

  你已经了解到，Claude Code 的开箱即用工具之一是 **Task**，Claude Code 可以使用它启动子代理来处理复杂的多步骤任务。你可以明确要求 Claude Code 使用子代理来集思广益，或调查你想要解决的问题或疑问的多个方面。这些内置代理是通用的。

  你也可以创建自定义的专业子代理。每个子代理都有自己的上下文窗口，你可以为每个子代理定义自定义系统提示词和特定工具。本课程不涵盖此部分，但你可以查看[此处](https://docs.anthropic.com/en/docs/claude-code/sub-agents)文档中的详细信息。
