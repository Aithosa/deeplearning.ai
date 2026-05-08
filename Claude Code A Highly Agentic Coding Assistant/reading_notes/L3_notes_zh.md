# 第 3 课：添加功能

## 每个功能所使用的提示词

### 功能 1 - 在来源引用中嵌入链接

对于每个响应，聊天机器人会返回其用于回答查询的章节。向量存储有两个集合：一个用于章节分块，另一个用于课程元数据（其中包括每个章节的链接）。假设你想在 UI 中嵌入返回来源的链接，并希望 Claude Code 提供帮助：

以下是示例提示词（配合计划模式使用）：

```
聊天界面显示带有来源引用的查询响应。我需要修改它，以便每个来源都变成一个可点击的链接，在新标签页中打开相应的章节视频：
- 当课程在 @backend/document_processor.py 中被处理成块时，每个章节的链接都存储在 course_catalog 集合中。
- 修改 @backend/search_tools.py 中的 _format_results，以便同时也返回章节链接。
- 链接应以不可见的方式嵌入（不显示可见的 URL 文本）。
```

后续请求：

```
[Ctrl + V 粘贴截图] 这些链接很难看清。让它们更具视觉吸引力。
```

### 功能 2 - 添加“+ New Chat”功能

以下是提示词：

```
在左侧边栏的课程部分上方添加一个“+ NEW CHAT”按钮。点击时，它应该：
- 清除聊天窗口中的当前对话
- 在不刷新页面的情况下开始新会话
- 处理 @frontend 和 @backend 的适当清理工作
- 匹配现有部分（Courses, Try asking）的样式——相同的字体大小、颜色和全大写格式
```

[Playwright MCP 服务器](https://github.com/microsoft/playwright-mcp) 的配置：

- 退出 Claude Code
- 在终端中输入：`claude mcp add playwright npx @playwright/mcp@latest`
- 再次打开 Claude Code，并使用 `/mcp` 命令验证是否已连接到 MCP 服务器

以下是后续请求：

```
使用 Playwright MCP 服务器，访问 127.0.0.1:8000 并查看“+ New Chat”按钮。我希望该按钮的外观与下方 Courses 和 Try Asking 的其他链接一致。确保其左对齐并移除边框。
```

_旁注_：默认情况下，Claude Code 会请求你授权使用 Playwright 的“take a screenshot”（截屏）工具。你可以选择在 Claude Code 询问时始终允许，也可以手动配置此设置：输入 `/permissions` 命令 -> 添加新规则（确保突出显示“Allow”）-> 然后指定工具的全名。要输入截屏工具的全名，可以在 Claude Code 终端输入 `/mcp` -> 选择你的 MCP 服务器（在本例中为 Playwright） -> view tools -> 14. Take a screenshot -> 你将看到全名 "mcp**playwright**browser_take_screenshot"。

### 功能 3 - 为聊天机器人添加工具

如果你查看起始代码库中的 [search_tools.py](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase/blob/main/backend/search_tools.py)，你会看到为 RAG 聊天机器人定义了一个工具。假设你现在想为 RAG 聊天机器人定义另一个工具来处理与大纲相关的问题。这样，你就不再依赖接收到的内容来回答大纲问题，而是返回准确的大纲（每个章节的标题、课程链接、课程标题）。向量数据库中的 course_metadata 集合包含这些信息。你可以要求 Claude Code 为你实现这个工具：

以下是所使用的提示词：

```
在 @backend/search_tools.py 中，在现有内容相关工具的基础上添加第二个工具。这个新工具应该处理课程大纲查询。
- 功能：
   - 输入：课程标题
   - 输出：课程标题、课程链接和完整的章节列表
   - 对于每个章节：章节编号、章节标题
- 数据源：向量存储的课程元数据集合
- 更新 @backend/ai_generator 中的系统提示词，以便返回课程标题、课程链接、每个章节的编号和标题，以解决与大纲相关的查询。
- 确保新工具已在系统中注册。
```

## Claude 功能 / 命令摘要

| 命令   | 描述                                                                                                                          |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `@`    | 使用 `@` 提及文件，将其内容包含在你的请求中                                                                                   |
| `/mcp` | 管理 MCP 连接并检查可用的 MCP 服务器及其提供的工具 ([Claude Code 与 MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)) |

| 快捷键        | 描述                                                                  |
| ------------- | --------------------------------------------------------------------- |
| `shift`+`tab` | 在计划模式 (Planning) 和自动接受模式 (Auto-accept) 之间切换           |
| 截屏          | `cmd`+ `shift`+ `ctrl` + `4` (Mac) 或 `Win` + `Shift` + `S` (Windows) |
| 粘贴截图      | `Ctrl` + `V`（在 Windows 上可能无法直接工作）                         |
