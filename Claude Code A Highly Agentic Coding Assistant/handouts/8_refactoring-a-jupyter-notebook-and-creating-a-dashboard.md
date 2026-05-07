# 课程讲义：第八节 - 重构 Jupyter Notebook 并创建仪表盘

## 1. 处理 Jupyter Notebook 的工具 (Notebook Tools)

- **核心命令**：Claude Code 拥有专门用于处理 `.ipynb` 文件的工具。
- **功能**：能够读取 notebook 中的单元格（Cell）、分析代码结构，并对内容进行编辑或重构。

## 2. 关注点分离 (Separation of Concerns)

重构混乱代码的关键原则：

- **逻辑剥离**：将核心业务逻辑从 notebook 的展示层中提取出来。
- **模块化**：
  - `data_loader.py`：负责数据的读取、清理和预处理。
  - `metrics.py`：负责业务指标（如 Revenue, AOV）的计算逻辑。
- **价值**：代码更易于测试、重用和维护。

## 3. 面向对象重构 (Object-Oriented Refactoring)

- **实践**：通过将零散的 pandas 操作封装成类和方法，使代码结构更清晰。
- **错误处理**：利用 Claude Code 快速修复常见的 notebook 错误（如 `KeyError`），通过提供完整的代码上下文来提高修复准确率。

## 4. 从 Notebook 迁移到仪表盘 (Streamlit)

**Streamlit** 是数据科学领域常用的快速开发 Web 界面的工具。

- **迁移流程**：
  1. **定义需求**：明确标题、KPI 卡片、图表类型（收入、地理分布、满意度等）。
  2. **编写代码**：利用 Claude 将 notebook 中的逻辑映射到 Streamlit 的 `st` 组件中。
  3. **环境准备**：更新 `requirements.txt` 并安装依赖（`pip install streamlit plotly`）。
  4. **运行服务**：使用 `streamlit run dashboard.py` 启动。

## 5. 交互式功能增强

- **动态过滤器**：添加按“年份”或“月份”过滤的功能。
- **可视化库**：利用 **Plotly** 创建交互式图表（如悬停显示各州详细数据）。
- **迭代开发**：通过向 Claude 提供反馈（如“移除空卡片”、“修改默认年份”），快速打磨 UI/UX 细节。

---

**下一节预告**：我们将探索如何利用 MCP 服务器连接 Figma 和 Playwright，通过 UI 原型图直接构建现代化的 Next.js Web 应用程序。
