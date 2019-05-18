# ライブラリインポート
import discord

# ディスコードへの接続
client = discord.Client()

# 人狼アプリのトークン設定
BOT_TOKEN = "NTc5MzEyMTA3NDk4MjQyMDY1.XOAoRQ.bA4hvCmxwWYQ1KhspbksrNQRLW0"

# イベント設定
@client.event
async def on_ready():

#   あいさつ
    print('人狼ゲーム')

# イベント設定（ログイン）
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('OK')

#   bot終了
    if message.content.startswith('$bye'):
        await client.logout()

#bot形成
client.run(BOT_TOKEN)
