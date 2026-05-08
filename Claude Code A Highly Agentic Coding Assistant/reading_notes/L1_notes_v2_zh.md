# 课程笔记

你可以在这里找到如何安装 Claude Code 的说明，以及课程中使用的代码示例和提示词的链接。

**注意**：要将此阅读项标记为完成，请务必滚动到底部并点击“标记为完成”。

## Claude Code 安装

要跟随课程进行操作，你可以按照以下步骤安装 Claude Code。

1. 运行以下命令：

   `npm install -g @anthropic-ai/claude-code`

   更多安装指南，请参阅[此处](https://docs.anthropic.com/en/docs/claude-code/setup)。

2. 安装 Claude Code 后，你可以：
   - 从终端启动：导航到你的项目文件夹，然后输入 `claude`
   - 从 VS Code 的集成终端启动：输入 `claude`，扩展程序将自动安装。
     - 如果遇到问题，请确保 `code` 命令可用。如果未安装，请使用 Cmd+Shift+P (Mac) 或 Ctrl+Shift+P (Windows/Linux) 并搜索 “Shell Command: Install ‘code’ command in PATH”
   更多信息，请查看 [Claude Code IDE 集成](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)。

## 课程代码库示例链接

以下是课程中涉及的代码示例链接：

1. RAG 聊天机器人代码库（第 2-6 课）
   - 这是第 2 课中使用的[初始代码库仓库](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase.git)。
   - 第 3-6 课在初始代码库的基础上添加了功能。
   - 这是第 5 课之后代码库的[状态](https://github.com/https-deeplearning-ai/ragchatbot-codebase.git)。

   欢迎 fork 初始代码库并跟随课程活动进行操作。

2. 电子商务数据分析（第 7 课）
   - 这是[课程文件](https://github.com/https-deeplearning-ai/sc-claude-code-files/tree/main/lesson7_files)。
   - 其中包括数据、初始和重构后的 notebook，以及仪表板文件。

   欢迎 fork 此仓库，并使用初始 notebook 和数据文件夹尝试第 7 课的任务。

3. Figma 设计稿（第 8 课）
   - 这是 [Figma 设计稿链接](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/key-indicators.fig)（你可以使用 [Figma 桌面应用](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app)打开它）。
   - 在第 8 课中，你将基于此设计稿构建一个 Next.js 应用。
   - 这是我们在拍摄期间得到的[应用仓库链接](https://github.com/https-deeplearning-ai/FRED-dashboard.git)。

## 课程提示词与总结

你可以在课程结束时的可选阅读项（课程提示词与总结）中找到每节课使用的提示词以及 Claude Code 功能的总结。你也可以在这个[仓库](https://github.com/https-deeplearning-ai/sc-claude-code-files/tree/main/reading_notes)中找到它们。

## Claude Code 成本

如果你想安装 Claude Code 来尝试课程：

- 你可以使用 Pro 或 Max [订阅](https://www.anthropic.com/claude-code#:~:text=Pro,Sign%20up)。Pro 订阅足以满足课程活动。
- 或者，你可以根据 API 使用量进行计费。对于给定的会话，你可以 use `/cost` 命令查看成本。
