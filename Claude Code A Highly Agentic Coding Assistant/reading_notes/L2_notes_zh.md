# 第 2 课：环境搭建与代码库理解

## 如何运行 RAG 聊天机器人应用？

- Fork 此 [代码仓库](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase.git)
- 将 Fork 后的仓库克隆到本地机器
- 按照 [README.md 文件](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase/blob/main/README.md) 中的说明进行操作：
  - 如果你使用的是 Windows，请使用 Git Bash 运行 Readme 文件中的所有命令（需要安装 [Git for Windows](https://git-scm.com/downloads/win)）。在 VS Code 中打开终端时，请务必选择 `Git Bash`。
  - RAG 聊天机器人应用由 Claude Sonnet 3.5 驱动，你需要指定 Anthropic API 密钥（[Anthropic Console](https://console.anthropic.com/login?returnTo=%2F%3F)）。你可以选择输入一个虚假密钥来运行应用并查看其外观，但查询请求将会失败。
- 在学习课程的过程中，你可以让应用在后台运行。

## 代码库探索

这里有一些建议可以向 Claude Code 提问：

<details>
<summary>给我一个该代码库的概览</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

课程资料 RAG 系统概览

这是一个检索增强生成 (RAG) 系统，旨在通过语义搜索和 AI 驱动的响应来查询课程资料。

架构

后端 (Python/FastAPI)：

- app.py - 带有 CORS/代理支持的 FastAPI 服务器，负责提供前端界面和 API 端点
- rag_system.py - 协调所有组件的主编排器
- vector_store.py - 用于语义搜索的 ChromaDB 集成
- ai_generator.py - 用于响应生成的 Anthropic Claude 集成
- document_processor.py - 文本处理和分块
- search_tools.py - 基于工具的搜索功能
- session_manager.py - 对话历史管理
- models.py - Pydantic 模型（Course, Lesson, CourseChunk）

前端 (HTML/CSS/JavaScript)：

- 带有聊天功能的现代 Web 界面
- 课程统计侧边栏
- 建议问题
- Markdown 响应渲染

数据存储：

- ChromaDB 向量数据库 (/chroma_db/)
- /docs/ 文件夹中的课程文档（支持 txt, pdf, docx）

核心功能

- 使用 Sentence Transformers 对课程资料进行跨语义搜索
- 使用 Claude Sonnet 3.5 提供 AI 驱动的响应
- 基于会话的对话历史记录
- 基于工具的搜索架构
- 课程分析和统计
- 自动文档处理和分块
- 具有实时聊天功能的 Web 界面

依赖项

Python 3.13+, ChromaDB, Anthropic API, FastAPI, sentence-transformers, uvicorn

系统在启动时加载课程文档，并提供 API 端点 (/api/query, /api/courses) 和位于 <http://localhost:8000> 的 Web 界面。

</div>
</details>

<details>
<summary>关键数据模型有哪些？</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

关键数据模型使用 Pydantic 定义：

1. Course (models.py:10-15)

- title: 课程名称（用作唯一标识符）
- course_link: 可选的课程链接 URL
- instructor: 可选的讲师姓名
- lessons: Lesson 对象列表
  1. Lesson (models.py:4-8)

- lesson_number: 序号 (0, 1, 2...)
- title: 章节标题
- lesson_link: 可选的具体章节 URL
  1. CourseChunk (models.py:17-22)

- content: 分块的文本内容
- course_title: 父课程标识符
- lesson_number: 可选的章节关联
- chunk_index: 在文档中的位置
  1. SearchResults (vector_store.py:8-32)

- documents: 检索到的文本块列表
- metadata: 每个分块关联的元数据
- distances: 相似度得分
- error: 可选的错误信息

  这些模型创建了一个层次结构：Course → Lessons → CourseChunks，实现了对教育内容的结构化存储和检索，并保留了适当的上下文。

</div>
</details>

<details>
<summary>解释一下文档是如何处理的</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

该代码库中的文档处理系统通过几个关键组件工作：

文档处理流程

1. 文档读取与结构解析 (document_processor.py:13-21)

- 使用 UTF-8 编码读取文件，必要时回退到忽略错误模式
- 期望结构化格式，前 3 行包含课程元数据：
  - 第 1 行：课程标题
  - 第 2 行：课程链接
  - 第 3 行：课程讲师

1. 文本分块 (document_processor.py:25-91)

- 将文档拆分为基于句子的块，具有可配置的大小和重叠度
- 使用正则表达式检测句子边界，同时处理缩写
- 保持块之间的上下文重叠，以便更好地进行检索

1. 课程结构提取 (document_processor.py:97-259)

- 解析章节标记（例如 "Lesson 0: Introduction"）
- 提取章节标题和可选的章节链接
- 创建结构化的 Course 和 Lesson 对象
- 生成带有章节上下文的 CourseChunk 对象

1. 向量存储 (vector_store.py:34-267)

- 使用带有 Sentence Transformer 嵌入的 ChromaDB
- 维护两个集合：
  - course_catalog：用于语义搜索的课程元数据
  - course_content：用于检索的实际分块内容
- 支持按课程名称和章节编号进行过滤搜索

核心功能：

- 保留章节结构并在分块中添加上下文信息
- 处理边缘情况，如没有章节标记的文件
- 支持跨课程和特定章节内的语义搜索
- 维护元数据以便链接回原始内容

该系统将原始课程文稿转换为可搜索、具有上下文感知的块，存储在向量数据库中以供 RAG 应用使用。

</div>
</details>

<details>
<summary>document_processor 期望的文档格式是什么？</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

根据 document_processor.py 代码，期望的文档格式为：

必须结构：
Course Title: [标题]
Course Link: [链接]
Course Instructor: [讲师]

Lesson 0: [章节标题]
Lesson Link: [可选章节链接]
[章节内容...]

Lesson 1: [章节标题]
Lesson Link: [可选章节链接]
[章节内容...]

核心格式规则：

- 第 1-3 行：课程元数据（标题、链接、讲师）
- 章节标记：必须以 "Lesson [数字]: [标题]" 开头（不区分大小写）
- 章节链接：紧跟在章节标记后的可选 "Lesson Link: [链接]"
- 内容：其他所有内容都成为章节内容，直到下一个章节标记

  示例：
  Course Title: Python 入门
  Course Link: <https://example.com/python-course>
  Course Instructor: 张三

  Lesson 0: 开始学习
  Lesson Link: <https://example.com/lesson0>
  欢迎学习 Python 编程。在本节课中我们将涵盖...

  Lesson 1: 变量和数据类型
  Python 中的基本数据类型包括字符串、整数...

  回退行为：

- 如果未找到章节标记，则将第 3 行之后的全部内容视为一个文档
- 缺失的元数据行将使用默认值（标题使用文件名，讲师使用 "Unknown"）
- 空行和空格将被妥善处理

  处理器将此结构提取为 Course/Lesson 对象，并创建用于向量存储的上下文分块。

</div>
</details>

<details>
<summary>课程分块是如何加载到数据库中的？</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

课程分块通过以下过程加载到数据库中：

1. 文档处理 (rag_system.py:39)
   course, course_chunks = self.document_processor.process_course_document(file_path)

- DocumentProcessor 读取文件并创建包含内容、元数据和章节上下文的 CourseChunk 对象
  1. 向量存储添加 (rag_system.py:45, vector_store.py:162-180)
     self.vector_store.add_course_content(course_chunks)

- 从每个分块中提取内容
- 创建包含课程标题、章节编号和分块索引的元数据
- 生成唯一 ID：{course*title}*{chunk_index}
- 将带有嵌入的块添加到 ChromaDB 的 course_content 集合中
  1. 加载触发器：

  启动加载 (app.py:88-98)

- 服务器启动时自动从 ../docs 文件夹加载所有文档
- 调用 rag_system.add_course_folder()

  批量文件夹处理 (rag_system.py:52-94)

- 处理文件夹中的所有 .txt, .pdf, .docx 文件
- 检查现有课程以避免重复
- 可选先清除现有数据

  ChromaDB 存储中的关键步骤：
  1. Documents → 分块内容字符串
  2. Metadata → 课程/章节/分块信息
  3. IDs → 每个分块的唯一标识符
  4. Embeddings → 由 Sentence Transformer 自动生成

  系统确保没有重复课程，并保持课程元数据与内容之间的引用完整性。

</div>
</details>

<details>
<summary>追踪从前端到后端的处理用户查询的过程</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

前端 → 后端流程

1. 前端用户交互 (script.js:45-96)

- 用户输入查询并点击发送或按回车键
- sendMessage() 禁用输入，将用户消息添加到聊天界面
- 向 /api/query 发送包含查询内容和 session_id 的 POST 请求
  1. FastAPI 端点 (app.py:56-74)

- 接收带有 QueryRequest 模型的 /api/query POST 请求
- 如果未提供则创建新会话：rag_system.session_manager.create_session()
- 调用 rag_system.query(request.query, session_id)
  1. RAG 系统处理 (rag_system.py:102-140)

- 将查询格式化为提示词：“Answer this question about course materials: {query}”
- 从会话管理器检索对话历史
- 使用工具和对话上下文调用 AI 生成器
- AI 完成后从工具管理器获取来源
- 使用问答对更新对话历史
  1. AI 生成 (ai_generator.py:43-80)

- 使用系统提示词和对话历史创建 Claude API 调用
- 如果可用，包含搜索工具
- 将查询发送给 Anthropic Claude API
- 如果 AI 决定使用工具，则处理工具调用（搜索）
  1. 工具执行（当 AI 调用搜索时）

- AI 可以使用特定的课程/章节过滤器调用搜索工具
- 工具管理器执行向量存储搜索
- 将相关的课程分块返回给 AI
- AI 将结果综合成最终响应
  1. 响应返回路径

- AI 生成器返回响应字符串
- RAG 系统返回 (response, sources) 元组
- FastAPI 格式化为 QueryResponse JSON
- 前端接收 JSON，如果是新的则更新 session_id
- 在聊天界面显示响应及可选的来源

核心功能：

- 会话管理保持对话上下文
- 基于工具的架构允许 AI 在需要时进行搜索
- 向量存储实现了跨课程内容的语义搜索
- 每一层都有错误处理和优雅的降级方案

</div>
</details>

<details>
<summary>画一张图来说明这个流程</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

# RAG 系统查询流程图

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│     前端         │    │     FASTAPI      │    │   RAG 系统       │
│   (script.js)   │    │    (app.py)      │    │ (rag_system.py) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │ 1. POST /api/query    │                       │
         │ {query, session_id}   │                       │
         ├──────────────────────▶│                       │
         │                       │ 2. rag_system.query() │
         │                       ├──────────────────────▶│
         │                       │                       │
         │                       │                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   会话管理器     │    │    AI 生成器     │    │    工具管理器    │
│(session_mgr.py) │    │ (ai_generator.py)│    │(search_tools.py)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
         ▲                       ▲                       │
         │ 3. get_history()      │ 4. generate_response() │
         │                       │    + 工具              │
         └───────────────────────┼───────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CLAUDE SONNET 3.5                            │
│  系统提示词: "你是一个拥有课程搜索工具的 AI 助手..."              │
│  工具: [CourseSearchTool]                                       │
│  查询: "回答关于课程资料的问题: ..."                             │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 │ 5. 工具调用决策
                                 ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│    课程搜索      │    │    向量存储      │    │    CHROMADB     │
│      工具        │    │ (vector_store.py)│    │                 │
│(search_tools.py)│    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │ 6. execute(query,     │                       │
         │    course_name,       │                       │
         │    lesson_number)     │                       │
         ├──────────────────────▶│ 7. search()           │
         │                       ├──────────────────────▶│
         │                       │                       │
         │                       │                       │
         │                       │ ┌─────────────────────┤
         │                       │ │ course_catalog      │
         │                       │ │ - 课程解析          │
         │                       │ │                     │
         │                       │ │ course_content      │
         │                       │ │ - 语义搜索          │
         │                       │ └─────────────────────┤
         │                       │                       │
         │                       │ 8. SearchResults      │
         │ 9. 格式化的结果        │◀──────────────────────┤
         │◀──────────────────────┤                       │
         │                       │                       │

         │ 10. 工具结果返回给 Claude
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CLAUDE SONNET 3.5                            │
│  将工具结果综合为最终答案                                        │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 │ 11. 最终响应
                                 ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   RAG 系统       │    │     FASTAPI      │    │      前端       │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │ 12. (response,        │                       │
         │     sources)          │                       │
         ├──────────────────────▶│ 13. QueryResponse     │
         │                       │ {answer, sources,     │
         │                       │  session_id}          │
         │                       ├──────────────────────▶│
         │                       │                       │
         │                       │                       │ 14. 更新 UI
         │                       │                       │ - 添加消息
         │                       │                       │ - 显示来源
         │                       │                       │ - 存储会话

流程摘要：
1. 用户查询 → FastAPI 端点
2. RAG 系统获取对话历史
3. AI 生成器携带工具调用 Claude
4. Claude 决定使用 CourseSearchTool
5. 工具搜索 ChromaDB 集合
6. 结果格式化并返回给 Claude
7. Claude 综合最终答案
8. 响应通过各层返回
9. 前端显示答案及来源
```

# 架构关键点

**双 ChromaDB 集合**：

- `course_catalog` 用于名称解析
- `course_content` 用于语义搜索

**基于工具的搜索**：

- Claude 决定何时搜索，何时使用通用知识

**会话连续性**：

- 在多个查询之间维护对话历史

**错误处理**：

- 每一层都能妥善处理故障

**来源追踪**：

- 搜索结果包含用于 UI 显示的课程/章节上下文

# 详细组件说明

前端 (script.js)：

- 处理用户输入并显示响应
- 管理会话状态和加载动画
- 渲染来源和 Markdown 内容

FastAPI (app.py)：

- 提供 REST API 端点
- 处理请求/响应序列化
- 管理 CORS 和静态文件服务

RAG 系统 (rag_system.py)：

- 协调所有组件的主编排器
- 管理会话创建和对话历史
- 通过带有工具的 AI 生成器路由查询

AI 生成器 (ai_generator.py)：

- 接口对接 Claude Sonnet 3.5 API
- 处理工具调用工作流
- 管理对话上下文和系统提示词

搜索工具 (search_tools.py)：

- 实现用于语义搜索的 CourseSearchTool
- 格式化带有课程/章节上下文的搜索结果
- 追踪用于 UI 显示的来源

向量存储 (vector_store.py)：

- 采用双集合策略的 ChromaDB 封装
- 提供课程名称解析和内容搜索
- 使用 Sentence-Transformers 生成嵌入

会话管理器 (session_manager.py)：

- 维护每个会话的对话历史
- 为后续问题提供上下文

</div>
</details>

<details>
<summary>解释文本是如何转换为块的？每个块的大小是多少？</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**
查看 document_processor.py:25-91 中的分块过程：

文本分块过程

1. 文本预处理 (第 28-29 行)

- 标准化空格：re.sub(r'\s+', ' ', text.strip())
- 移除多余的空格和换行符
  1. 句子分割 (第 31-38 行)

- 使用正则表达式分割句子边界：(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\!|\?)\s+(?=[A-Z])
- 处理缩写（避免在 "Mr.", "Dr." 等处分割）
- 在跟随大写字母的句号、感叹号、问号处分割
  1. 分块构建算法 (第 40-91 行)

- 基于句子的分块：通过添加完整的句子来构建块
- 大小限制：当 current_size + sentence_length > chunk_size 时停止添加句子
- 重叠计算：在块之间使用可配置的重叠以保留上下文

  分块大小配置

  分块大小来自 config.py 设置：

⏺ 读取(backend/config.py)
⎿ 读取 30 行

⏺ 分块配置

- 分块大小 (Chunk Size)：800 字符 (config.py:19)
- 分块重叠 (Chunk Overlap)：100 字符 (config.py:20)

  分块策略

  智能句子边界：

- 绝不在句中分割 —— 始终保持句子完整
- 如果单条句子超过 800 字符，它将独立成为一块
- 保持可读性和上下文

  重叠实现 (第 67-83 行)：

- 从当前块的末尾向前计数
- 包含最多 100 字符的前序句子
- 确保块之间的上下文连续性
- 防止分块边界处的信息丢失

  上下文增强 (第 184-188, 232-234 行)：

- 每个章节的第一块："Lesson {N} content: {chunk}"
- 其他块："Course {title} Lesson {N} content: {chunk}"
- 添加章节/课程上下文以便更好地检索

  过程示例：
  输入："这是第一句。这是第二句。这是第三句。"
  ↓
  800 字符限制、100 字符重叠的分块：

- 块 1："Lesson 1 content: 这是第一句。这是第二句。"
- 块 2："这是第二句。这是第三句。"（重叠部分）

  这种方法在分块大小（为了嵌入效率）与保留语义及上下文之间取得了平衡。

</div>
</details>

<details>
<summary>描述 API 端点</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

根据 app.py，该 API 具有以下端点：

API 端点

POST /api/query

用途：处理用户查询并返回 AI 生成的响应

请求模型 (app.py:38-41)：
{
"query": "string",
"session_id": "string" // 可选
}

响应模型 (app.py:43-47)：
{
"answer": "string",
"sources": ["string"],
"session_id": "string"
}

过程 (app.py:56-74)：

- 如果未提供则创建新会话
- 调用 RAG 系统处理查询
- 返回带有来源和会话 ID 的 AI 响应
- 使用 500 状态码处理错误

  GET /api/courses

  用途：获取课程分析和统计数据

  响应模型 (app.py:49-52)：
  {
  "total_courses": 0,
  "course_titles": ["string"]
  }

  过程 (app.py:76-86)：

- 调用 rag_system.get_course_analytics()
- 返回课程总数和所有课程标题列表
- 由前端用于显示可用课程

  静态文件服务

  挂载： "/" → ../frontend/ (app.py:119)

- 提供前端 HTML, CSS, JS 文件
- 在开发过程中使用自定义的 DevStaticFiles 类及无缓存请求头
- 支持 HTML=True 的单页应用 (SPA) 路由

  中间件配置

  CORS (app.py:24-32)：

- 允许所有来源 (allow_origins=["*"])
- 允许凭据以及所有方法/请求头
- 前后端通信所需

  TrustedHost (app.py:18-22)：

- 允许所有主机 (allowed_hosts=["*"])
- 处理代理配置

  启动事件 (app.py:88-98)

- 自动从 ../docs 文件夹加载文档
- 将课程文件处理到向量数据库中
- 记录加载进度和错误

  该 API 遵循 REST 原则，具有清晰的请求/响应模型和适当的错误处理。
  </div>
  </details>

<details>
<summary>我该如何运行这个应用？</summary>

<div style="margin-left: 20px;">

**来自 Claude Code 的参考回答**

根据代码库，运行应用的方式如下：

**快速启动（推荐）**

chmod +x run.sh
./run.sh

**手动启动**

cd backend
uv run uvicorn app:app --reload --port 8000

**先决条件**

1. 确保已安装 uv
2. 安装依赖：uv sync
3. 创建包含 Anthropic API 密钥的 .env 文件：
   ANTHROPIC_API_KEY=your_anthropic_api_key_here

应用将运行在：

- Web 界面：<http://localhost:8000>
- API 文档：<http://localhost:8000/docs>

</div>
</details>

## Claude Code 命令摘要

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

| 命令       | 描述                           |
| ---------- | ------------------------------ |
| `/clear`   | 清除当前对话历史               |
| `/compact` | 压缩（总结）当前对话历史       |
| `ESC`      | 中断 Claude 以重新引导或纠正它 |
| `ESC ESC`  | 将对话回溯到较早的时间点       |

你可以在 Claude Code 中使用常规的 Bash 命令，但命令需要以 `!` 开头（例如：`!pwd`）。你可以输入 `exit` 退出 Claude Code。
