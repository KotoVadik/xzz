from hikkatl.types import Message
from .. import loader

@loader.tds
class SilModule(loader.Module):
    """Модуль Sil"""
    strings = {"name": "SilModule", "sil": "t.me/{}\n\n<code>{}</code>"}

    @loader.command(
        ru_doc="Отвечает ссылкой на номер",
        es_doc="Responde con un enlace al número",
        de_doc="Antwortet mit einem Link zur Nummer",
        # Добавьте больше переводов на языки при необходимости
    )
    async def sil(self, message: Message):
        """Отвечает ссылкой на номер"""
        args = message.text.split(" ", 1)
        if len(args) == 1:
            await message.edit("Укажите номер после .sil")
            return
        cleaned_args = args[1].replace(" ", "").replace("-", "")
        await message.edit(self.strings("sil").format(cleaned_args, cleaned_args))
