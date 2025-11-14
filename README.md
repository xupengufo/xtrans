# Discord 翻译机器人

这是一个简单的 Discord 机器人，可以自动将非中文消息翻译成中文。

## 功能特性

- 自动检测消息语言
- 将非中文消息翻译成中文
- 可以指定需要翻译的频道
- 免费且易于部署

## 部署步骤

### 1. 创建 Discord 机器人

1. 访问 [Discord 开发者门户](https://discord.com/developers/applications)
2. 点击 "New Application" 创建新应用
3. 在 "Bot" 选项卡下，点击 "Add Bot" 创建机器人
4. 复制 "Token" 并保存（稍后会用到）
5. 在 "OAuth2" -> "URL Generator" 中：
   - 勾选 "bot" 和 "applications.commands"
   - 在 "Bot Permissions" 中勾选所需权限（建议：Administrator）
   - 复制生成的 URL 并在浏览器中打开，邀请机器人加入你的服务器

### 2. 获取项目代码

下载或克隆此项目到本地：

```bash
git clone <项目地址>
```

或者直接下载代码文件：
- [main.py](main.py)
- [requirements.txt](requirements.txt)

### 3. 安装依赖

确保你已经安装了 Python 3.8 或更高版本，然后运行：

```bash
pip install -r requirements.txt
```

### 4. 设置环境变量

在运行机器人之前，需要设置 Discord 机器人的 Token 作为环境变量：

**Windows (CMD):**
```cmd
set DISCORD_BOT_TOKEN=你的机器人token
```

**Windows (PowerShell):**
```powershell
$env:DISCORD_BOT_TOKEN="你的机器人token"
```

**macOS/Linux:**
```bash
export DISCORD_BOT_TOKEN=你的机器人token
```

### 5. 运行机器人

```bash
python main.py
```

看到显示机器人用户名的信息表示机器人已成功启动。

### 6. 使用机器人

在 Discord 中使用以下命令：

- `!translate_channel` - 将当前频道添加到翻译列表
- `!untranslate_channel` - 将当前频道从翻译列表中移除

添加到翻译列表的频道中，所有非中文消息都会被自动翻译成中文。

## 免费托管选项

如果你希望机器人 24/7 运行，可以考虑以下免费托管服务：

1. [Render](https://render.com/) - 提供免费的 Web Service 托管
2. [Replit](https://replit.com/) - 在线编程环境，支持运行机器人
3. [Pella](https://www.pella.app/) - 专门用于 Discord 机器人的免费托管服务

注意：免费托管服务通常有资源限制，对于高流量的服务器可能不够用。

## 技术说明

- 使用 [discord.py](https://github.com/Rapptz/discord.py) 库实现 Discord 机器人功能
- 使用 [googletrans](https://github.com/ssut/py-googletrans) 库实现翻译功能
- 支持自动语言检测和翻译

## 注意事项

- googletrans 是非官方的 Google 翻译 API，可能会有速率限制
- 对于生产环境，建议使用官方翻译 API（如 Google Cloud Translation）
- 请遵守 Discord 的使用条款和服务协议