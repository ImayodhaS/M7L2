import discord
from discord.ext import commands
import requests
import os
from ai import predict

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def cekharga(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("⚠️ Kirim gambar bersama perintah ini, contoh:\n`$saveing` + upload gambar.")
        return

    for attachment in ctx.message.attachments:
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Download gambar
            img_data = requests.get(attachment.url).content

            # Pastikan folder 'saved_images' ada
            os.makedirs("saved_images", exist_ok=True)

            # Simpan file
            file_path = os.path.join("saved_images", attachment.filename)
            with open(file_path, "wb") as f:
                f.write(img_data)

            hasil = predict(file_path)
            if hasil == 'Apel Merah':
                await ctx.send('Ini Apel Merah, harga Rp. 1.250 per buah')
            elif hasil == 'Pisang':
                await ctx.send('Ini Pisang, harga Rp. 1.500 per buah')
            elif hasil == 'Apel Busuk':
                await ctx.send('Ow kamu menemukan buah apel yang busuk, buang saja di tong sampah seberang toko')
            elif hasil == 'Pisang Busuk':
                await ctx.send('Ow kamu menemukan buah apel yang busuk, buang saja di tong sampah seberang toko')
            elif hasil == 'Apel Hijau':
                await ctx.send('Ini Apel Hijau, harga Rp. 1.250 per buah')
            elif hasil == 'Pisang Hijau':
                await ctx.send('Ini Pisang Hijau, harga Rp. 1.500 per buah')

            await ctx.send(f"✅ Gambar **{attachment.filename}** berhasil disimpan!")
        else:
            await ctx.send(f"❌ File **{attachment.filename}** bukan gambar yang didukung (.png, .jpg, .jpeg, .gif).")
        

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ai(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

bot.run("MTM4MjM0MDAyODgxNzk5Nzk2NA.GE-1G9.W3SPekAy4PQfzIjL_qWzqPw3ED3OKgruqDhdZQ")