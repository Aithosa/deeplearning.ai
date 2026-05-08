# 课程介绍

欢迎参加“Claude Code：高度代理化的编程助手”课程！在开始学习之前，建议你阅读本说明，以了解课程大纲以及如何最好地进行学习。

**注意**：要将此阅读项标记为完成，请务必滚动到底部并点击“Mark as Complete”（标记为完成）。

## 课程形式

本课程涵盖了使用 Claude Code 进行代理化编程的最佳实践和技巧。你将通过 3 个示例学习这些技巧：

- RAG 聊天机器人代码库（第 2-6 课）
- 电子商务数据分析（第 7 课）
- Figma 设计原型（第 8 课）

课程仅包含视频。你可以选择只看视频，但如果你想查看代码示例，可以在下方找到相应的链接。如果你想尝试课程中的任务，你需要安装 Claude Code 并直接在终端或 IDE 中使用它（例如本课程使用的 IDE 是 VS Code）。每节课后都附有一份阅读笔记，其中包括所使用的提示词（Prompts）、课程中涵盖的 Claude Code 功能摘要以及一些补充说明。

## 课程大纲

- **第 1 课：什么是 Claude Code？**
  - 笔记 1：安装 Claude Code

- **第 2 课：环境搭建与代码库理解**
  - 笔记 2：摘要与提示词

- **第 3 课：添加功能**
  - 笔记 3：摘要与提示词

- **第 4 课：测试、错误调试与代码重构**
  - 笔记 4：摘要与提示词

- **第 5 课：同时添加多个功能**
  - 笔记 5：摘要与提示词

- **第 6 课：探索 GitHub 集成与钩子（Hooks）**
  - 笔记 6：提示词与摘要

- **第 7 课：重构 Jupyter Notebook 并创建仪表盘**
  - 笔记 7：摘要与提示词

- **第 8 课：基于 Figma 原型创建 Web 应用**
  - 笔记 8：摘要与提示词

- **总结**

## 课程代码库示例链接

1. RAG 聊天机器人代码库（第 2-6 课）
   - 这是第 2 课使用的起始代码库的 [GitHub 仓库](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase.git)。
   - 第 3-6 课在起始代码库的基础上添加功能。
   - 这是第 5 课之后代码库的 [状态](https://github.com/https-deeplearning-ai/ragchatbot-codebase.git)。

   欢迎 Fork 起始代码库并跟随课程活动进行操作。

2. 电子商务数据分析（第 7 课）
   - 这是 [课程文件](https://github.com/https-deeplearning-ai/sc-claude-code-files/tree/main/lesson7_files)。
   - 其中包括数据、起始和重构后的 Notebook，以及仪表盘文件。

   欢迎 Fork 该仓库，并使用起始 Notebook 和数据文件夹尝试第 7 课的任务。

3. Figma 设计原型（第 8 课）
   - 这是 Figma 原型设计的 [链接](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/key-indicators.fig)（你可以使用 [Figma 桌面应用](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app) 打开）。
   - 在第 8 课中，你将基于此原型构建一个 Next.js 应用。
   - 这是我们在拍摄期间得到的应用的 [代码仓库链接](https://github.com/https-deeplearning-ai/FRED-dashboard.git)。

## 课程活动 - 成本可见性

如果你想安装 Claude Code 来尝试课程：

- 你可以订阅 Pro（20 美元/月）或 Max（100 美元/月）[计划](https://www.anthropic.com/claude-code#:~:text=Pro,Sign%20up)。Pro 订阅足以完成课程活动，但不包括 Opus 模型。
- 或者，你可以根据 API 使用量付费（如果你在所有课程活动中仅使用 Sonnet，则所有课程的总成本约为 12 到 20 美元）。在给定的会话中，你可以使用 `/cost` 命令监控成本。

## 课程先决条件

无论你是开发人员、数据科学家/分析师，甚至是由于非技术背景的人员，都可以参加本课程。但为了充分利用本课程并理解所用提示词的细节：

- 第 2-7 课需要基本的 Python 知识。
- 对于第 8 课，你将构建的是 Next.js 应用，因此如果你想查看生成的代码，可能需要熟悉该框架。但如果你不熟悉也不用担心，你仍然可以尝试最后一课，学习如何使用 Figma MCP 服务器将模拟设计导入 Claude 的上下文。
- 了解基本的终端命令也会有所帮助。
- 熟悉基本的 Git 命令会更好（`git add, commit, pull, push`）。

## 资源

本课程涵盖了 Claude Code 许多常用的功能。要了解有关这些功能以及其他功能的更多信息，可以查看：

- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 常见工作流](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
- [Claude Code 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code 使用案例](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

Anthropic Academy 上也有一门很棒的课程，你可以查看更多关于 Claude Code 的示例：

- [Claude Code 实战](https://anthropic.skilljar.com/claude-code-in-action)
