import asyncioimport randomfrom ZelzalMusic import appfrom pyrogram.types import (InlineKeyboardButton,                            InlineKeyboardMarkup, Message)from pyrogram import filters, Clienttxt = [" كيف تعرفتو ؟","‏ أكثر اكله يحبها الطرف الثاني ؟"," اللون المفضل للطرف الثاني ؟️"," لو كان الطرف الثاني حيوان وش رح يكون ؟","‏لقبك عند الطرف الثاني ؟"," اكثر كلمه يحكيها الطرف الثاني ؟"," اوصف علاقتكم بكلمه وحده فقط ؟"," كم الكم مع بعض ؟"," اكثر وقت تحكو فيه ؟","الهوايه المفضله للطرف الثاني ؟"," هات 5 صفات ممكن تكون سبب حب الطرف الثاني لك ؟","اكثر شي يتسوا فيك ؟"," اكثر كلمه غبيه طلعت منك و انتم تحكو ؟"," موقف مستحيل تنساه حصل بينكم ؟"," جمله اثرت فيك قالها الطرف الثاني ؟"," انت صريح من ناحية شعورك ؟"," كيف تتعاملو مع العتاب ؟"," حبيت قبل الحين ؟"," كيف كانت حياتك قبل الطرف الثاتي - بدون محن بالله ؟"," مين الرومنسي فيكم اكثر ؟"," مين الحنون فيكم ؟"," مين متحمل الثاني ؟"," مين الي يسوي مصايب ؟"," الطباخ فيكم ؟"," لمن تتزوجو مين رح يطبخ و مين رح يغسل الصحون ؟"," اسماء اطفالكم المستقبليين ؟"," اكثر طريقه يعبر فيها الطرف الثاني عن حنانه و حبه فيها ؟"," لو تزاعلتم مين الي يراضي الثاني ؟"," مين النكدي ؟","اغنيه كل ما تسمعها تذكر حبيب/تك ؟",        ]        @app.on_message(filters.command(["مربوطين","مر"], ""))async def ktbat(client: Client, message: Message):      a = random.choice(txt)      await message.reply(        f"{a}")