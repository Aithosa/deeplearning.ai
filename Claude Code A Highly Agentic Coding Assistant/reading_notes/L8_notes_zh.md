# 第 8 课：基于 Figma 原型创建 Web 应用

## Figma 设计

这是 [Figma 设计原型](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/key-indicators.fig)，你可以使用 [Figma 桌面应用](https://www.figma.com/downloads/) 打开。

在终端中，使用以下命令初始化你的 `Next.js` 应用程序：
`npx create-next-app@latest .`

## Figma 官方 MCP 服务器 (Dev Mode MCP Server)

注意：Figma 提供的官方 MCP 服务器需要 [Professional、Organization 或 Enterprise 计划](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)中的 [Dev 或 Full 席位](https://help.figma.com/hc/en-us/articles/27468498501527-Updates-to-Figma-s-pricing-seats-and-billing-experience#h_01JCPBM8X2MBEXTABDM92HWZG4)。你可以查看[此指南](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server)了解更多细节。此外，还有一个由 Framelinks 提供的可以免费使用的 Figma MCP 服务器。详情请查看本笔记的最后一部分。

### 启用 MCP 服务器

- 在 Figma 桌面应用中打开 [Figma 设计文件](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/key-indicators.fig)。
- 在左上角打开 Figma 菜单。
- 在 Preferences（首选项）下，选择 Enable Dev Mode MCP Server（启用开发模式 MCP 服务器）。

你应该会在屏幕底部看到一条确认消息，告知你服务器已启用并在本地运行，地址为 `http://127.0.0.1:3845/mcp`（使用 HTTP 传输协议在本地运行的远程服务器）。

### 为 Claude Code 配置 MCP 服务器

- 在终端中输入：`claude mcp add --transport http figma-dev-mode-mcp-server http://127.0.0.1:3845/mcp`。

- 同时添加 Playwright MCP 服务器：`claude mcp add playwright npx @playwright/mcp@latest`。

- 启动 Claude Code 并（使用 `/mcp` 命令）验证你是否已连接到这两个 MCP 服务器。

## 提示词

- 要复制 Figma 设计链接，请在 Figma 桌面端选择该设计，然后按下 `Ctrl`+ `L` 或 `cmd` + `L`。

- 以下是提示词：

  ```
  使用以下 Figma 原型（粘贴链接），利用 Figma 开发模式 MCP 服务器分析该原型，并在此 Next.js 应用程序中构建底层代码。使用 recharts 库创建图表，使之成为一个 Web 应用程序。使用 Playwright MCP 服务器查看该应用程序的外观，并验证其外观是否尽可能接近原型。
  ```

- 后续请求：

  ```
  使用来自 FRED 的真实世界数据填充这些图表。
  ```

  如果你想将仪表盘连接到真实数据，你需要从 FRED 获取 API 密钥，点击[此处](https://fred.stlouisfed.org/docs/api/api_key_key.html)。

## Figma 官方 MCP 服务器的替代方案 - Framelink Figma MCP 服务器

这里有一份关于如何配置 Framelink Figma MCP 服务器的[指南](https://www.framelink.ai/docs/quickstart?utm_source=github&utm_medium=referral&utm_campaign=readme)（以及使用该服务器的一些[最佳实践](https://www.framelink.ai/docs/best-practices)）。

你可以使用以下命令为 Claude Code 配置它：

`claude mcp add "Framelink Figma MCP" -- npx -y figma-developer-mcp --figma-api-key=YOUR-KEY --stdio`

或者使用此命令：

`claude mcp add-json "Framelink-Figma-MCP" '{"command": "npx", "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY","--stdio"]}'`
