import discord
from discord.ext import commands
from googletrans import Translator
import os
from keep_alive import keep_alive

# 初始化机器人和翻译器
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator()

# 存储需要翻译的频道ID
translation_channels = set()

@bot.event
async def on_ready():
    print(f'{bot.user} 已上线!')

@bot.command()
async def translate_channel(ctx):
    """添加当前频道到翻译列表"""
    translation_channels.add(ctx.channel.id)
    await ctx.send(f"已将 {ctx.channel.mention} 添加到翻译频道列表!")

@bot.command()
async def untranslate_channel(ctx):
    """从翻译列表中移除当前频道"""
    translation_channels.discard(ctx.channel.id)
    await ctx.send(f"已将 {ctx.channel.mention} 从翻译频道列表中移除!")

@bot.event
async def on_message(message):
    # 避免机器人回复自己
    if message.author == bot.user:
        return
        
    # 检查是否在翻译频道中且消息不是命令
    if message.channel.id in translation_channels and not message.content.startswith('!'):
        # 检测语言
        detected_lang = translator.detect(message.content)
        
        # 如果不是中文，则翻译成中文
        if detected_lang.lang != 'zh':
            try:
                translated = translator.translate(message.content, dest='zh')
                # 发送翻译结果
                await message.channel.send(f"翻译结果: {translated.text}")
            except Exception as e:
                print(f"翻译出错: {e}")
    
    # 确保命令仍然可以正常工作
    await bot.process_commands(message)

# 启动保持活动的服务器
keep_alive()

# 运行机器人
if __name__ == "__main__":
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        print("错误: 请设置 DISCORD_BOT_TOKEN 环境变量")
    else:
        bot.run(token)