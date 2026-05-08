# 笔记

## 命令摘要

### 管理项目记忆

- `/init`：Claude Code 扫描你的代码库并在项目目录中创建 CLAUDE.md 文件。
  - CLAUDE.md 指导 Claude 了解你的代码库，指出重要的命令、架构和编码风格。每次启动 Claude Code 时，它都会自动包含在上下文中。
  - 这是为 RAG 聊天机器人示例生成的 CLAUDE.md 文件的 [示例](https://github.com/https-deeplearning-ai/ragchatbot-codebase/blob/main/CLAUDE.md)。

- `#`：使用 `#` 快速添加记忆。当发现 Claude Code 重复出现错误时非常有用。
  - **示例 1**：由于本项目是一个 `uv` 项目，我们使用 `#` 将以下内容添加到 CLAUDE.md 文件中：
    - `#` 使用 uv 运行 python 文件或添加任何依赖项
  - **示例 2**：你可以向 Claude Code 提供数据库架构信息，在本例中，由于你有一个向量数据库，你可以告知 Claude Code 向量数据库中存储的集合信息：
    - `#` 向量数据库有两个集合：
      - `course_catalog`：
        - 存储课程标题用于名称解析
        - 每个课程的元数据：title, instructor, course_link, lesson_count, lessons_json（课程列表：lesson_number, lesson_title, lesson_link）
      - `course_content`：
        - 存储文本块用于语义搜索
        - 每个分块的元数据：course_title, lesson_number, chunk_index

### 管理 Claude Code 的上下文

| 命令       | 描述                                                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `/clear`   | 清除当前对话历史                                                                                                              |
| `/compact` | 压缩（总结）当前对话历史                                                                                                      |
| `ESC`      | 中断 Claude 以重新引导或纠正它                                                                                                |
| `ESC ESC`  | 将对话回溯到较早的时间点                                                                                                      |
| `@`        | 使用 `@` 提及文件，将其内容包含在你的请求中                                                                                   |
| `/mcp`     | 管理 MCP 连接并检查可用的 MCP 服务器及其提供的工具 ([Claude Code 与 MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)) |

你可以在 Claude Code 中使用常规 bash 命令，但需要以 ! 开头（例如：`!pwd`）。你可以输入 exit 退出 Claude Code。

---

| 快捷键        | 描述                                                                  |
| ------------- | --------------------------------------------------------------------- |
| `shift`+`tab` | 在计划模式 (Planning) 和自动接受模式 (Auto-accept) 之间切换           |
| 截屏          | `cmd`+ `shift`+ `ctrl` + `4` (Mac) 或 `Win` + `Shift` + `S` (Windows) |
| 粘贴截图      | `Ctrl` + `V`（在 Windows 上可能无法直接工作）                         |

## Claude 功能摘要

### 深度思考模式 (Extended Thinking Mode)

对于复杂的任务（例如：复杂的架构变更、调试复杂的问题），你可以使用“think”一词来触发[深度思考模式](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)。思考有多个级别：**“think” < “think hard” < “think harder” < “ultrathink”**。每个级别都会为 Claude 分配更多的思考预算。

> 直接用自然语言描述，比如在末尾加上 **think**

### 使用子代理 (Subagents)

你已经了解到，Claude Code 的开箱即用工具之一是 **Task**，Claude Code 可以使用它启动子代理来处理复杂的多步任务。你可以明确要求 Claude Code 使用子代理来集思广益，或者调查你想要解决的问题或疑问的多个方面。这些内置代理是通用型的。

你也可以创建自定义的专业化子代理。每个子代理都有自己的上下文窗口，你可以为每个子代理定义自定义系统提示词和特定工具。本课程不涵盖此部分，但你可以在文档中查看详细信息：[此处](https://docs.anthropic.com/en/docs/claude-code/sub-agents)。

> 可以用自然语言描述；可以用命令 /agent 管理和运行。

### 自定义斜杠命令 (Custom Slash Commands)

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

## 课程体会

虽然Claude Code的强大功能使得阅读和开发有了很大的帮助，但是看课程里所有例子的提示词都写得非常详细，每一次输入都包含了甚至细到文件以及函数级别的说明。

这说明好的开发范式一直都没有变过，更没有因为CC的出现而大幅简化：

- 如果你读不懂代码可以借助CC快速读懂
- 如果还不确定如何修改，就通过paln模式讨论明白：当你需要进行较大规模的更改时，我们始终建议先进入计划模式
- 如果想要开发新功能，要提供详细的需求说明、更改范围、更改方式：Claude Code 的表现取决于你提供给它的上下文

只有对代码和需求有高度的掌控，才能开发出符合需求、可持续迭代的项目。课程里每一次的提示词都不是一两句话就说完的，需要使用者也深度思考。

那种每次仅一句话描述就开始新功能开发的方式，会让项目逐渐失控。

对CC的使用：

- 真正动手之前通过`/plan`模式讨论方案
- 一个小问题解决后`/clear`及时清空对话上下文
- 需要固化的流程固化到项目中或者全局
