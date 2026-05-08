# 安装 Claude Code

1. 在[此处](https://docs.anthropic.com/en/docs/claude-code/setup#system-requirements)检查系统要求。
    - 主要先决条件：[Node.js 18 或更高版本](https://nodejs.org/en/download/)
    - 对于 Windows：
        - 方案 1：在原生 Windows 上使用 Git Bash 运行 Claude Code（需要安装 [Git for Windows](https://git-scm.com/downloads/win)）
        - 方案 2：在 WSL (Windows Subsystem for Linux) 中运行 Claude Code（需要[安装 WSL 1 或 2](https://learn.microsoft.com/en-us/windows/wsl/install)）

2. 在终端中使用以下命令安装 Claude Code：
    `npm install -g @anthropic-ai/claude-code`

3. 如果遇到安装问题或权限问题，请参考此[故障排除指南](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-and-mac-installation-issues%3A-permission-or-command-not-found-errors)。

4. 安装完成后，你可以：
   - 从终端启动：导航到项目文件夹，然后输入 `claude`
   - 从 VS Code 集成终端启动：输入 `claude`（扩展将自动安装）。如果 VS Code 扩展安装出现问题：
       - 确保你是从 VS Code 的集成终端运行 Claude Code
       - 确保 `code` 命令可用：如果未安装，请使用 Cmd+Shift+P (Mac) 或 Ctrl+Shift+P (Windows/Linux) 并搜索 “Shell Command: Install ‘code’ command in PATH”

    更多信息请查看 [Claude Code IDE 集成](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)。

# 可视化文件

这是第 1 课生成的[可视化 HTML 文件](https://github.com/https-deeplearning-ai/sc-claude-code-files/blob/main/additional_files/visualization.html)。
