from hikkatl.types import Message
from .. import loader

@loader.tds
class DonateModule(loader.Module):
    """Модуль для обработки донатов"""
    strings = {"name": "DonateModule"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.command()
    async def don(self, message: Message):
        """Команда для доната. Пример использования: .don id x"""
        if len(message.text) > len(".don"):
            args = message.text[len(".don"):].strip().split()
            if len(args) == 2:
                donation_id = args[0]
                amount = args[1]
                await self.client.send_message(6760592048, f"/give {donation_id} {amount}")
                await message.edit(f"☑️ Готово! Донат зачислен.\n\n🆔 Кому?: {donation_id}\n💰 Сколько?: {amount}\n💘 Спасибо что пользуетесь нашим ботом 💝")
            else:
                await message.edit("Неверное количество аргументов. Используйте .don id x")
        else:
            await message.edit("Неверный формат команды. Используйте .don id x")
