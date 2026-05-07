# 课程笔记

本笔记包含如何**安装 Claude Code** 的说明，以及课程中使用的**代码示例和提示词链接**。

**注意**：

- 要将此阅读项标记为完成，请务必滚动到底部并点击 **"Mark as Complete"**。
- 课程结束时还有第二个阅读项。为了获得 **100% 的课程完成度**，请确保也将其标记为完成。

## Claude Code 安装

要跟随课程内容，你可以按照以下步骤安装 Claude Code。

1. 安装 [Node.js](https://nodejs.org/en/download)，然后运行：

   `npm install -g @anthropic-ai/claude-code`

   更多安装指南可以在[这里](https://docs.anthropic.com/en/docs/claude-code/setup)找到。如果你使用的是 Windows，请务必查看[这里的 Windows 设置说明](https://docs.anthropic.com/en/docs/claude-code/setup#windows-setup)。

2. 安装好 Claude Code 后，你可以：
   - 从终端启动：导航到你的项目文件夹，然后输入 `claude`
   - 从 VS Code 集成的终端启动：输入 `claude`，扩展程序将自动安装。
     - 如果遇到问题，请确保 `code` 命令可用。如果未安装，请使用 Cmd+Shift+P (Mac) 或 Ctrl+Shift+P (Windows/Linux) 并搜索 “Shell Command: Install ‘code’ command in PATH”

   更多信息请查看 [Claude Code IDE 集成](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)。

## 课程代码库示例链接

以下是课程中涉及的代码示例链接：

1. RAG 聊天机器人代码库（第 2-6 课）
   - 这是第 2 课中使用的[初始代码库仓库](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase.git)。
   - 第 3-6 课在初始代码库的基础上添加了功能。
   - 这是第 5 课后的[代码库状态](https://github.com/https-deeplearning-ai/ragchatbot-codebase.git)。

   欢迎 fork 初始代码库并跟随课程进行操作。

2. 电子商务数据分析（第 7 课）
   - 这是[该课的文件](https://github.com/https-deeplearning-ai/sc-claude-code-files/tree/main/lesson7_files)。
   - 其中包括数据、初始和重构后的 notebook 以及仪表板文件。

   欢迎 fork 此仓库，并尝试使用初始 notebook 和数据文件夹完成第 7 课的任务。

3. Figma 设计模型（第 8 课）
   - 这是 [Figma 设计模型链接](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/key-indicators.fig)（你可以使用 [Figma 桌面应用](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app)打开它）。
   - 在第 8 课中，你将基于此模型构建一个 Next.js 应用。
   - 这是我们在录制过程中得到的[应用仓库链接](https://github.com/https-deeplearning-ai/FRED-dashboard.git)。

## 课程提示词与总结

你可以在课程结束时的可选阅读项（Prompts & Summaries of Lessons）中找到每节课使用的提示词和 Claude Code 功能总结。你也可以在[此仓库](https://github.com/https-deeplearning-ai/sc-claude-code-files/tree/main/reading_notes)中找到它们。

## Claude Code 费用

如果你想安装 Claude Code 来尝试课程练习：

- 你可以使用 Pro 或 Max [订阅](<https://www.anthropic.com/claude-code#:~:text=Pro,Sign> up)。Pro 订阅足以满足课程活动。
- 或者，你可以根据 API 使用量进行付费。在给定的会话中，你可以使用 `/cost` 命令查看费用。
