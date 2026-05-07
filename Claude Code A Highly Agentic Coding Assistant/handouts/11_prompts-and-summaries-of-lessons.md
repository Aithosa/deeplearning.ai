# 课程提示词与总结

本笔记包含了课程中使用的提示词链接、额外资源以及 Claude Code 功能总结。

**注意**：要将此阅读项标记为完成，请务必向下滚动到最后并点击“标记为完成”。

## 提示词 (Prompts)

以下是课程笔记和提示词的链接：

- [第 2 课提示词：环境搭建与代码库理解](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L2_notes.md)
- [第 3 课提示词：添加功能](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L3_notes.md)
- [第 4 课提示词：测试、错误调试与代码重构](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L4_notes.md)
- [第 5 课提示词：同时添加多个功能 - 使用 Git 工作树 (Git Worktrees)](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L5_notes.md)
- [第 6 课笔记：GitHub 集成与钩子 (Hooks) 引用](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L6_notes.md)
- [第 7 课提示词：重构 Jupyter Notebook 并创建仪表盘](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L7_notes.md)
- [第 8 课提示词：基于 Figma 设计稿创建 Web 应用](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/reading_notes/L8_notes.md)

## 额外资源 (Additional Resources)

要了解有关这些功能以及其他功能的更多信息，您可以查看：

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 常用工作流](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
- [Claude Code 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code 使用案例](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

在 Anthropic Academy 上还有一门非常棒的课程，您可以查看以了解更多 Claude Code 的示例：

- [Claude Code 实战 (Claude Code in Action)](https://anthropic.skilljar.com/claude-code-in-action)

## Claude Code 功能总结 (Summary of Claude Code Features)

### 管理项目记忆 (Managing Project Memory)

- `/init`：Claude Code 会扫描您的代码库，并在您的项目目录中创建 `CLAUDE.md` 文件。
  - `CLAUDE.md` 指导 Claude 了解您的代码库，指出重要的命令、架构和编码风格。每次启动 Claude Code 时，它都会自动包含在上下文中。
  - 这里有一个由 `init` 为 RAG 聊天机器人示例生成的 [CLAUDE.md 文件示例](https://github.com/https-deeplearning-ai/ragchatbot-codebase/blob/main/CLAUDE.md)。
- `#`：使用 `#` 快速添加记忆。当您看到 Claude Code 重复出现错误时非常有用。
  - **示例 1**：由于本项目是一个 `uv` 项目，我们使用 `#` 将以下内容添加到 `CLAUDE.md` 文件中：
    - `#` 使用 uv 运行 Python 文件或添加任何依赖项
  - **示例 2**：您可以向 Claude Code 提供数据库架构信息。在本例中，由于您有一个向量数据库，您可以告诉 Claude Code 存储在向量数据库中的集合信息：
    - `#` 向量数据库有两个集合：
      - `course_catalog`：
        - 存储用于名称解析的课程标题
        - 每门课程的元数据：标题 (title)、讲师 (instructor)、课程链接 (course_link)、课程数量 (lesson_count)、课程 JSON (lessons_json，包含课程编号、标题、链接的列表)
      - `course_content`：
        - 存储用于语义搜索的文本块
        - 每个块的元数据：课程标题 (course_title)、课程编号 (lesson_number)、块索引 (chunk_index)

### Claude Code 命令总结 (Summary of Claude Code Commands)

| 命令       | 描述                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/clear`   | 清除当前对话历史记录                                                                                                                 |
| `/compact` | 总结当前对话历史记录                                                                                                                 |
| `ESC`      | 中断 Claude 以进行重定向或纠正                                                                                                       |
| `ESC ESC`  | 将对话回退到之前的时间点                                                                                                             |
| `@`        | 使用 `@` 提及文件，将其内容包含在您的请求中                                                                                          |
| `/mcp`     | 管理 MCP 连接并检查可用的 MCP 服务器及其提供的工具 ([在 Claude Code 中使用 MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)) |

您可以在 Claude Code 中使用常规的 Bash 命令，但需要以 `!` 开头（例如：`!pwd`）。您可以输入 `exit` 退出 Claude Code。

| 快捷键        | 描述                                                                  |
| ------------- | --------------------------------------------------------------------- |
| `Shift`+`Tab` | 在规划 (Planning) 和自动接受 (Auto-accept) 模式之间切换               |
| 截屏          | `Cmd`+ `Shift`+ `Ctrl` + `4` (Mac) 或 `Win` + `Shift` + `S` (Windows) |
| 粘贴截图      | `Ctrl` + `V` (在 Windows 上可能无法正常工作)                          |

### 更多 Claude 功能 (Additional Claude Features)

- **扩展思考模式 (Extended Thinking Mode)**

  对于复杂的任务（例如：复杂的架构变更、调试复杂问题），您可以使用单词 "think" 来触发 [扩展思考模式](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)。思考有几个级别："think" < "think hard" < "think harder" < "ultrathink"。每个级别都会为 Claude 分配更多的思考额度。

- **使用子智能体 (Use of subagents)**

  您已经了解到 Claude Code 的开箱即用工具之一是 **Task**，Claude Code 可以使用它来启动子智能体 (subagents) 以执行复杂的、多步骤的任务。您可以明确要求 Claude Code 使用子智能体来构思方案，或者调查您想要解决的问题或疑问的多个方面。这些内置智能体是通用型的。

  您还可以创建自定义的专业子智能体。每个子智能体都有自己的上下文窗口，您可以为每个子智能体定义自定义系统提示词和特定工具。本课程不涵盖这部分内容，但您可以查看[此处](https://docs.anthropic.com/en/docs/claude-code/sub-agents)的文档了解详情。
