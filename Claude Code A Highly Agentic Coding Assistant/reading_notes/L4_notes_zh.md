# 第 4 课：测试、错误调试与代码重构

## 错误调试

为了制造错误，我们故意在 backend/config.py 中设置了 `MAX_RESULTS: int = 0`。

以下是配合计划模式 (Plan mode) 使用的提示词：

```
RAG 聊天机器人对于任何与内容相关的问题都返回“query failed”（查询失败）。我需要你：
1. 编写测试来评估 @backend/search_tools.py 中 CourseSearchTool 的 execute 方法的输出。
2. 编写测试来评估 @backend/ai_generator.py 是否正确调用了 CourseSearchTool。
3. 编写测试来评估 RAG 系统如何处理与内容查询相关的问题。

将测试保存在 @backend 内的 tests 文件夹中。针对当前系统运行这些测试，以识别哪些组件出现了故障。根据测试揭示的损坏部分提出修复建议。

Think.
```

## 代码重构

在起始代码库的 backend/ai_generator.py 中，聊天机器人被设计为每个查询仅使用一次工具调用。为了处理更复杂的查询，你可以要求 Claude Code 对其进行重构，以便能够处理连续的工具调用。

提示词：

```
重构 @backend/ai_generator.py 以支持连续工具调用，使 Claude 可以在不同的 API 轮次中进行最多 2 次工具调用。

当前行为：
- Claude 进行 1 次工具调用 → 工具从 API 参数中移除 → 给出最终响应。
- 如果 Claude 在看到结果后想再次进行工具调用，它无法实现（会得到空响应）。

期望行为：
- 每次工具调用都应该是一个独立的 API 请求，Claude 可以在其中根据之前的结果进行推理。
- 支持复杂的查询，例如需要进行多次搜索以进行比较、处理多部分问题，或者需要来自不同课程/章节的信息时。

示例流程：
1. 用户：“搜索一门讨论与课程 X 的第 4 课相同主题的课程。”
2. Claude：获取课程 X 的课程大纲 → 得到第 4 课的标题。
3. Claude：使用该标题搜索讨论相同主题的课程 → 返回课程信息。
4. Claude：提供完整的答案。

要求：
- 每个用户查询最多支持 2 轮连续调用。
- 在以下情况终止：(a) 完成 2 轮调用，(b) Claude 的响应中没有 tool_use 块，或 (c) 工具调用失败。
- 在各轮次之间保留对话上下文。
- 优雅地处理工具执行错误。

注意：
- 更新 @backend/ai_generator.py 中的系统提示词。
- 更新测试文件 @backend/tests/test_ai_generator.py。
- 编写测试以验证外部行为（发出的 API 调用、执行的工具、返回的结果），而不是内部状态细节。

使用两个并行的子代理 (subagents) 来集思广益可能的计划。不要实现任何代码。
```

## Claude 功能摘要

- **深度思考模式 (Extended Thinking Mode)**

  对于复杂的任务（例如：复杂的架构变更、调试复杂的问题），你可以使用“think”一词来触发[深度思考模式](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-extended-thinking)。思考有多个级别：“think” < “think hard” < “think harder” < “ultrathink”。每个级别都会为 Claude 分配更多的思考预算。

- **使用子代理 (Subagents)**

  你已经了解到，Claude Code 的开箱即用工具之一是 **Task**，Claude Code 可以使用它启动子代理来处理复杂的多步任务。你可以明确要求 Claude Code 使用子代理来集思广益，或者调查你想要解决的问题或疑问的多个方面。这些内置代理是通用型的。

  你也可以创建自定义的专业化子代理。每个子代理都有自己的上下文窗口，你可以为每个子代理定义自定义系统提示词和特定工具。本课程不涵盖此部分，但你可以在文档中查看详细信息：[此处](https://docs.anthropic.com/en/docs/claude-code/sub-agents)。
