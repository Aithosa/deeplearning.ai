# 课程讲义：第九节 - 基于 Figma 原型图创建 Web 应用程序

## 1. 核心流程：从设计到代码 (Design to Code)

本节课展示了如何利用 Claude Code 结合 MCP 服务器，将静态的 UI 设计快速转化为功能齐全的 Web 应用。

- **Figma MCP 服务器**：允许 Claude 读取 Figma 文件中的图层、样式和属性。
- **Playwright MCP 服务器**：允许 Claude 在浏览器中测试生成的代码，并通过截图验证视觉一致性。

## 2. 环境准备与配置

- **技术栈**：使用 **Next.js** (React) 构建现代前端应用。
- **Figma 设置**：
  - 在 Figma 偏好设置中开启 **"Enable dev mode MCP server"**。
  - 复制需要开发的特定图层 ID。
- **Claude 配置**：
  - 使用 `/mcp add <name> <cmd>` 命令连接 Figma 和 Playwright 服务器。
  - _最佳实践_：采用**项目级配置**，配置保存在 `.claude/settings.local.json` 中。
  - 针对复杂的前端生成任务，建议使用 **Claude 3 Opus** 模型以获得更高质量的代码。

## 3. 迭代开发模式

1. **初步生成**：Claude 根据 Figma 数据生成 HTML/CSS 结构。
2. **依赖安装**：Claude 自动识别并安装所需的库（如用于图表的 `recharts`）。
3. **视觉验证**：
   - 运行本地开发服务器 (`npm run dev`)。
   - 使用 Playwright 截取 `localhost:3000` 的快照。
   - Claude 根据截图与原型的差异进行自动调整（如侧边栏布局、柱状图样式）。

## 4. 接入真实世界数据 (Real-World Data)

将静态原型转化为动态应用的关键步骤：

- **API 搜索**：利用 Claude 的 Web 搜索功能查找相关的 API 文档（如 FRED 经济数据）。
- **服务编写**：编写异步函数来获取实时数据（如失业率、CPI、国债收益率）。
- **安全处理**：配置 API Key。
- **数据绑定**：将获取的真实数据注入到 UI 组件（如 Recharts 图表）中。

## 5. 总结与愿景

- **效率提升**：原本需要数天的工作量（从设计稿到对接 API 的仪表盘）现在可以在几分钟内完成。
- **应用场景**：快速原型验证、内部工具构建、数据可视化面板。

---

**课程总结**：我们已经学习了 Claude Code 从基础命令、Git 工作流、GitHub 集成、Jupyter notebook 处理到复杂前端生成的全过程。现在，轮到你去构建属于你的强大工具了！
