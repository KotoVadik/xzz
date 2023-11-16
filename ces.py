from hikkatl.types import Message
from .. import loader

@loader.tds
class ChannelEchoModule(loader.Module):
    """Создание отзывов"""
    strings = {"name": "OtzviCreat", "forwarded": "#⃣ | Сделка № {deal_number}\nℹ | {deal_text}\n💬 | Отзыв ниже!\n\n🔗 | {deal_pruf}",
               "success": "💞 | Спасибо за ваш отзыв!\n☑️ | Отзыв уже выложен в канал!\nПосмотреть отзывы - @inPROshop_reviews"}

    @loader.command(aliases=["ces"])
    async def ces(self, message: Message):
        """Создать отзыв 📚"""
        # Replace CHANNEL_ID with your channel ID
        channel_id = -1001986859647  # Replace with your channel ID
        replied_message = await message.get_reply_message()

        if replied_message:
            # Extracting deal number, deal pruf, and deal text from the command
            args = message.text.split(maxsplit=3)
            deal_number = args[1] if len(args) > 1 else "N/A"
            deal_pruf = args[2] if len(args) > 2 else "N/A"
            deal_text = args[3] if len(args) > 3 else "N/A"

            # Create the message to send to the channel
            forward_text = self.strings["forwarded"].format(deal_number=deal_number, deal_pruf=deal_pruf, deal_text=deal_text)

            # Forward the replied message and the new message to the channel
            await self._client.send_message(channel_id, forward_text)
            await replied_message.forward_to(channel_id)

            # Respond with success message and delete the original command message
            await message.respond(self.strings["success"])
            await message.delete()
        else:
            await message.respond("❌ Что-то неправильно указано!")
