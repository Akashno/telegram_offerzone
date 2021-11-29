from telethon import TelegramClient, events

api_id = *********
api_hash = *******


offermukk_bot_id = *******
hot_deals = ********

ignore_keywords = ['subscribe','Over.','Register','milega','karoge','Registration', 'Thanks', 'Offerzone_deals', 'Invite Your Friends', 'Ozians', 'Giveaway', 'Over Now', 'Scan above' ]
client = TelegramClient('no',api_id,api_hash)

@client.on(events.NewMessage)
async def handler(event):
     chat_id = event.chat_id
     if chat_id == hot_deals:
        msg = event.raw_text or 'New offers coming in  5 minute'
        if not any(word in msg for word in ignore_keywords):  
          msg = msg.replace('@hotdealsofficials', '@offerMukk')
          msg = msg.replace('@hot_deals_bot', '@offermukk_bot')
          await client.send_message(offermukk_bot_id,msg)

client.start()
client.run_until_disconnected()
