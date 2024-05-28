
import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from ZelzalMusic import app
import random

chat = []


@app.on_message(filters.group, group = 768)
async def ad3iyar(c, msg):
  if msg.text == "تفعيل الادعيه":
    if msg.chat.id in chat:
      return await msg.reply_text("الادعيه مفعله من قبل 💘 ⋅")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الادعيه 💘 ⋅")
  elif msg.text == "تعطيل الادعيه":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الادعيه 💘 ⋅")
    else:
      return await msg.reply_text("الادعيه متعطله من قبل 💘 ⋅")
      


async def ad3iya():
   ad3iyal = [
   "‏اللهم اشفي من لا يعلم بوجعه إلا أنت\nوارح قلباً لا يعلم بهمّه إلا أنت .",
   "‏اللهم انت ربي لا اله الا انت خلقتني وانا عبدك وانا على عهدك ووعدك ما استطعت اعوذ بك من شر ما صنعت ابوء لك بنعمتك علي وابوء بذنبي فغفر لي فإنه لا يغفر الذنوب الا انت .",
   "اللهم ارضى عَنّا رضًا، لا نرى بعده إلا جمال نعيمَك.",
   "‏اللهّم إختر لنا ولاتُخيرنا فـ قد حصدنا ما يكفي من سوء اختيارنا",
   "‏اللهم شُعور الفَرح الذي لا يُوصَف بـِتِلكَ اللّحظة المُنتظرة في كُلِّ حِين.",
   "ربيّ اسألك ان ترشدني بنورك ،\nالذي ينقذني من أن اتوه عن إختيار\nمافيه خير لي ، ألهمني البصيرة التي\nتدفعني لإدراك رسائلك أينما كانت 💓 .",
   "اللهُمَّ قِني عذابك يوم تُبعث عبادك .",
   "اللهُم إن رأيتني ابتعدُ عَنك ، فردنِي إلَيك رداً جَميلاً ..",
   "اللهم اغفر لي في كُل امرًا اخطئ به دون قصد",
   "‏اللهم انزل على قبور من فقدناهم ضياءً يؤنس وحشتهم، وينور مضجعهم، وسعة في قبورهم و أرحمهم برحمتك يا ارحم الراحمين .",
   "اللهّم لا تدع حُزناً في قُلوبنا إلا بدلتَه فرحاً .",
   "‏اللهم اجعلني لك وبك وعلى نور منك حتى ألقاك",
   "اللهُم أغفر لي إن أذنبت و أعفُ عني إن مُت .",
   "‏ربِّ لا ترجعني إلى ضيقٍ أخرجتني يومًا منه .",
   "‏اللهم يُسراً ، اللهم تسهيلاً ، اللهم توفيقاً.",
   "يا سامعٓا صوتَ الضعيفِ اذا شكى\nما لى سواكَ لدمع قلبِي؛ فاستجب!🤍🍃",
   "اللهم قدرًا جميلًا، وخيرًا يتبعهُ الرِّضا .",
   "‏اللهُم أغفر لنا حتى نبلُغ جنتك و ثبتنا حتى نلقاك و أصلح حالنا فإننا لا حول لنا ولا قوة إلا بك.",
   "‏اللهُم اجعلنا ممن قلت عنهم\n﴿وُجُوهٌ يَوْمَئِذٍ مُّسْفِرَةٌ ضَاحِكَةٌ مُّسْتَبْشِرَة﴾",
   "اللهُّم الجنة لِموتانا دارًا ومقامًا ولقاء .",
   "صب علينا الصبر اذا ضاقت سبلنا يا الله .",
   "اللهم افتح لنا من خزائن رحمتك ما يرفع\nالوباء عنا وعن العالمين",
   "«اللَّهُمَّ إني أسألُكَ الهُدَى والتُّقَى والعَفَافَ والغِنَى» .",
   "‏اللهم أرحم أرواحًا كانت كالجنّة على الأرض اللهم أرحم أبي واجمعنا به في جنات النعيم",
   "اللهم إني وجهت قلبي إليك .. انت الذي لا يضام من كنتَ نصيراً له وجهت قلبي إليك أملاً، طمعاً، حبّا و رغبةً بخيرِ ما عندك",
   "اللّهم جُمعة تفيضُ بالراحَة لعِبادك.",
   "‏اللهُم في يوم الجمعه ارحم الأنفس الطيبه التي انتقلت إلى جوارك و اغفر لهم و وسع لهم بقبورهم و اجمعنا بهم بجناتك .\n\nــــــــــــــــــــــــــــــــــــ🍃🌸🍃",
   "اللهم اغفر للمؤمنين والمؤمنات، والمسلمين والمسلمات، الاحياء منهم والاموات",
   "‏ربِ لاتجعل للحُزن مكاناً في قلوبِنا وإن ضاقت\nبِنا الأحوال يوماً فأوسِعها برحمتك .",
   "اللهم طمأنينة ليس بعدها خوف .",
   "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً ، وَفِي الْآخِرَةِ ‏حَسَنَةً ، وَقِنَا عَذَابَ النَّارِ .",
   "اللهُم ارحم الراحلين من ديارنا ونوّر قبورهم وتجاوز عنهُم واجعل قبورهم روضةٍ من رياض الجنّة..",
   "‏اللهم اخرجني من ضيق تفكيري إلى سعة تدبيرك .",
   "اللَّهُمَّ اغْفِرْ لي ذَنْبِي كُلَّهُ دِقَّهُ وجِلَّهُ وأَوَّلَهُ وآخِرَهُ وعَلانِيَتَهُ وسِرَّهُ.",
   "‏اللهّم لاتُبدل لنا الحال إلا لأحسّنه.",
   "اسـتغفر الله، حتى يفيض القلب فرحاً",
   "يَارب عظُمَتِ ‌الأماني وأنتَ أعظم",
   "- اللهُم عافية تروي عروق المُتعبِين ورحمّة لمن استوقفت بهُم الحياة 🧡",
   "اللهم وارْزُق فُـؤادي مَـا ابْتَـغَىٰ\nأنْـتَ القَـديرُ وَلَيسَ شَيءٌ يُعجِـزُكَ.. )",
   "ونسألك اللهُم شغفًا متجددًا، وحبًا في البحث والمقاومة، وأن نجد دومًا سبيلاً لحُب الحياة",
   "اللهم أرزقني قوة الحفظ وسرعة الفهم وصفاء الذهن، اللهم أنعِم عليّ بفضلك وكرمك 💙",
   "اللهم أغرس في نبضّات كل مرِيض راحه، وَفي جسدهُ عافِيه لاتفارقهُ أبداً، اللهُم اشفِ مرضَانا ومرضىَ المُسلمين شفَاء ليس بعدهُ سقما ابداً",
   "يارب حُسن الحياة ، وحُسن الرحيل ، وحُسن الأثر",
   "اللهم لا تقبض ارواحنا الا وانتَ راضِِ عنا",
   "اللهم هون علينا الصعب، وعجل لنا بالخير، واِختر لنا ما يُرضيك عنّا، واجعل صدورنا خالية من الهم وقلوبنا مُطمئنة بذكرك يارب العالمين",
   "اللهُّم السعة التي تجعل كل شيءٍ هيّن، ليّن و سهل و مُطمئن",
   "يارب صحائِف مليئة بالعفو والمغفرة مُطّهره من الذنوب ،اللهُّم أعتِق رِقابنا من النَّار",
   "‏اللهم خفف عني ثقل هذه الإيام، وأرزقني قوة الصبر، وأشرح صدري، و إنزع منه ما استثقلته نفسي، وأرح قلبي و أرزقني، فأنت أعلم بما تحتاجه نفسي.",
   "الحمدلله الذي حفظ عافيتي وستر خطيئتي ومازال يعطيني، الحمدلله دائمًا وأبدًا.",
   "اللَّهُمَ مغفِرة الذنُوب، ونعيم الجنّـة.",
   "ربي أعوذ بك من شتات الأمر ومس الضر وضيق الصدر.",
   "اللهم اني وليتك قلبي فتولاه بعزتك ورحمتك\nاللهم اجعلني من المصطفين الأخيار\n‏اللهم إني أسألك قرة العين بك\n‏اللهم هب لي رحمة من رحمتك تغنيني بها عمن سواك 💜",
   "اللَّهُمَّ طريقَ الصَّالحين، وثَباتَ الصَّالحين، وخاتمةَ الصَّالحين .",
   ".اللهُم شيئًا لطيفًا ، مُفاجئ غير مُخطط له ، يأتي من دون توقع ، شيء جميل مُفتقد ، يكسر الروتين المُهلك ، و يُبعد الغمة ، شيئًا يُفرح القلب .. يارب\n🌸..",
   "اللهم و أعوذُ بك من تقلب القلوب ، ومن الجفاء بعد أعوام من المودّة ، ومن الخذلان بعد الثقة ، ومن غُربةِ الأشخاص بعد أُلفتهِم",
   "اللهمّ يا مُحوّل الحول والأحوال حوّل حالنا إلى أحسن حال🤍",
   "‏﴿إِنَّ اللَّهَ وَمَلَائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ\nيَا أَيُّهَا الَّذِينَ آَمَنُوا صَلُّوا عَلَيْهِ وَسَلِّمُوا تَسْلِيمًا﴾\n\nاللهم صلي على سيدنا محمد وعلى آله وصحبه اجمعين 💜",
   "الحمدُلله الذي أبعدنا عن دُروبٍ لا\nتَليقُ بنا وسخّر لنا مَن الأقدارِ أجملها.",
   "اللهُم حظاً من الدنيا، يُمهد لنا طريقاً للجنّة.",
   "اللهم إنا نعوذ بك من أن نسير في طريق أحلامنا فلا نحصد إلا وهماً ، نعوذ بك من ضياع الأمل وفراغ النفس وهشاشة القلوب ..",
   "وَفِي يوم الجُمعَة\nيَآرب اجعَلهَا جُمعَة تَتبدَل فِيهَا\nالذُنُوب إلى حسَنات، وَهُمومَنا إلى أفرَاح\nيا الله♥️ ..",
   "الحمدلله على عين تبصر وآذن تسمع\nوجسد معافى وقلب ينبض، لك الحمد\nربي على نعمك التي لاتعد ولا تحصى!.",
   "اللَّهُمّ لا تجعلنِي ساهِياً لاهِياً غافِلاً عن ذِكرك ❤.",
   "ياربّ وإن ضاقت فمنك المُتسع.",
   "اللّهم إنّي اعوذ بك من علمٍ لا ينفع، ومن قلب لا يخشع، ومن دعاء لا يُستجاب له يا ربّ العالمين🤍 .",
   "اللهم من أراد بي سوء فجعل كيده في نحره واشغله في نفسه",
   "- اللَّهُمَّ أَصْلِحْ لي دِينِي الذي هو عِصْمَةُ أَمْرِي .",
   "وإنَّك ياربّ يُسري عندما يُعسر كُل شيء.",
   "وقلبي بين يديك ياالله، فلا ترده الا مجبورآ .",
   "اللهم علق قلبيّ بالصلاه والقرآن .",
   "‏اللهُمَّ إنَّك عفوٌّ كريمٌ تُحبُّ العفوَ فأعفُ عنِّي 🌼",
   "-اللهُم كُن معي و زدنيّ قوةً و صبراً،اللهُم أزل الضيقه عني و أبعد عنيّ كُل ضيقه أشعر بها وكُل ما يشغل بالي،ربي أرح قلبي،اللهم أجبُر قلبيّ وهّون عليّ حُزنيّ،يارب أن في قلبي دعاء وأنت ياربي مجيب♥️.",
   "اللهُم إني أسألُك موجبات رحمتِك و عزائم مغفرتك و السلامةِ من كُل إثم و الغنيمةِ من كُل بر و الفوز بالجنة و النجاةِ مِن النار.",
   "‏اللهم ابعد عني كثرة التفكير والقلق، وارزقني راحة القلب والبال، ربي حقق لي ما صبرت لأجله وارزقني سعادة في الدنيا والآخرة.",
   "اللهم اجعل خير أعمالنا خواتمها، وخير أعمارنا أواخرها، وخير أيامنا يوم نلقاك وأنت راضٍ عنا.",
   "وَلَقَدْ نَدِمْتُ عَلَى ذُنُوبِي ڪلِّهَا\nفَاقْبَلْ إِلَهِي تَـــوْبَتِي وَتَـنْدُّمِي",
   "‏اللهم ارض عن آبائنا وأمهاتنا، اللهم من ڪان منهم حياً فارزقه الصحة والعافية، ومن ڪان منهم ميتًا فاغفر له وارحمه يا رحيم .",
   "‏اللهم أنَت ربِّي، لا يخفى عليك ما في قلبي، فاللهم طمأنينة منك.. يارب أعوذ بك من ضيقة القلب، وشعور لا يُشكى ولا يفهم .. اللهم أرِح قلبي بما أنت به أعلم، ولا تجعلني أشكي لمن لا يخشى عليّ من حزني .. اللهم إني أُفوض دنياي كلها إليك🤍",
   "اللهم اسعد قلوبنا بذكرك وألهمنا شكر نعمك ، واكفنا كل ذي شر ، وامنع عنا كل ضر ، وحقق أمنياتنا ، وسخر لنا قلوب عبادك ، وسدد أقوالنا وأفعالنا",
   "يا قاضي الحاجات ، يا كاشف الكربات ، يا مجيب الدعوات ، يا غافر الزلات\nعافنا واعفُ عنا ، فرج همومنا ، واشرح صدورنا ، واصلح احوالنا ، وحقق آمالنا ، واشف مرضانا ، وارحم موتانا ، وأسعد قلوبنا ، واجعلنا من المقبولين عندك في الدنيا والآخره ، برحمتك يا أرحم الراحمين .",
   "‏اللهم أستودعك نفسي من ذُل الحياة ومن ضجيج التفكير،عوضني عن كل شيء أحببته فخسرته، طابت له نفسي فذهب، صدقته فكذب،استأمّنته فغدر ، اللهٌم لا تشغلني ولا تعلقني بشيء لم تكتبه لي  وقدّر لي كل فرح لم أتوقعه، اللهم و إن ضلت نفسي طريقها فردها إليك ردا جميلًا.",
   "‏- اللهم بقوة تدبيرك وعظيم عفوك وسعة حلمك وفيض كرمك؛ اسألك أن تدبرني بأحسن التدابير وتلطف بي وتنجيني مما يخيفني ويهمني\n\n‏اللهم لا أُضام وأنت حسبي، ولا أفتقر وأنت ربي، فأصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين .. ولا حول ولا قوة إلا بك.",
   "اللهُم سخر لي جنود الأرض وملائكة السماء وكل من وليته امري وارزقني حظ الدنيا ونعيم الآخرة ويسّر لي كل امر عسير، وقُل لما اريد كُن ليكون بحولك وقوتك ورحمتك، يارب ايّام جميلة واخبار مفرحة وراحة بال وتوفيق من عندك انك على كل شيء قدير.",
   "اللهُم اجعلنا من أولئك الذين تُحبهم والذين لا خوفٌ عليهم ولا هُم يحزنون اللهُم قربنا إليك تقرباً يرضيك واعتق رقابنا من النار",
   "اللهُم اعطنا خير ما تُعطي السائلين ، واجمع لنا صلاح الدنيا والدِين ، اللهم زِدنا نوراً في القلب ، وضياءً في الوجه ، وسعة في الرزق ، ومحبة في قلوب العباد ، واغفر لنا ولوالدينا ولجميع المسلمين",
   "نفتقدهم يا الله ونحنّ إليهم ونشتاق لهم فاجعلهم بفضلك منعمين مكرمين، هنيئة أرواحهم بما يلقون عندك من نعيم، اللهم ارحمهم واغفر لهم اللهم اجعلهم من عبادك الذين باتوا في القبور سعداء، وممّن أضحكت مباسمهم يوم العرض واللقاء..🖤",
   "اللهُم اجبر خاطري جبرًا أنت وليّه، فإنه لايعجزك شيئً في الأرض ولا في السماء ، ربي أشرح صدري وأرح قلبي وأزح من قلبي كل خوف يسكنني وكل ضعف يكسرني وكل أمر يبكيني ، ولا تفجعني في مستقبلي ولا في نفسي ولا في باقيّ أهلي ولا تُعسر أمري وأفتح لي أبوابي المغلقه.",
   "ربي أوصيك بمستقبلي خيرًا وأنت خير من أُوصي، اللهم وفقني ويسّر لي أمري وانزل على أيامي القادمة توفيقك ورضاك وكن لي عونًا معينًا، اللهم وفقني في كل خطوة اخطيها",
   "اللهُم فرحة تزيل الهُموم وتبكي العيون وتمحي ما مضى من غموم الحياة ، اللهُم إلهمني إبتسامة لا تغيب ، وصبراً لا ينفذ وروحاً بِك متعلقه وحمداً لك لا ينقطِع ، نستودعك يا الله أدعية فاضت بها القلوب فأستجب لنا يا كريم يا علام الغيوب وبشرَّنا بما يفرح القلوب ",
   "اللهم إني أعوذ بك من حزن يطويني وذنب يحبس فرحتي، ومن هموم الدنيا وما فيها، اللهم أجبر خاطري جبراً أنت وليّه يا رب، اللهم البشارات التي نحب، والأيام التي تسر، والرحمات التي تتوالى، والعافية التي ننعم بها، واليقين الذي يريح القلوب",
   "‏اللهمَّ تقبَّل مِنّا صَالِحَ أعمالِنا، واجعل هذا الشَّهرَ مُهذِّبًا لأنفسنا، وارزقنا أجرَ صيامِنا واجعلنا منَ المقبُولين🤍🌙",
   "‏يارب اجعلها أيام جبر وخير، لنا بها في كل يوم قبولاً بالسماء، ومحبة بالأرض، وتوفيقًا يلازم الخطى، وبركة بالوقت والعمل، وهداية منك لكل ماتحب وترضى، وتسخيرا لكل مافيه خير لنا..",
   "اللهم اكفني بحلالك عن حرامك وأغنني بفضلك عمّن سواك\nاللهم إني أسألك الهُدى والتُقى والعفاف والغِنى\nاللهم ارزقني لذّة طاعتك وأبعد عنّي لذّة معصيتك",
   "اللهُم إني أسألك حُسنٌ الخَاتمة\nاللهُم ارزقنيِ توبه نصوحة قبل الموت\nاللهُم يا مُقلب القلوب ثبت قلبي على دينك\nاللَّهم إنَّك عفوٌ كريمٌ تحبُّ العفوَ فاعفُ عنّا",
   "ونعوذ بك يا الله من أن نُبحر أميالاً في إتجاهٍ خاطئ",
   "‏اللهم ليس لنا من الأمر إلاَّ ما قضيت ولا من الخيِّر إلا ما أعطيت فاجعل لنا يارب في كل لحظة حظاً من عبادتك ونصيباً من شكرك، اللهم إنك ترى ما لا نرى وتعلم ما لا نعلم فأكفنا شر ما في الغيب وأحفظنا بحفظك وأسترنا بسترك وأرحمنا برحمتك ويسر أمورنا وفرج همومنا واشف مرضانا ياحي ياقيوم.",
   "اللهم ارزقنا الراحة في قربك، والطمـأنينة في ذكرك، اجعل هوانا حيث ترضى، حبّب إلينا ما تحب، وكرّه إلينا ما تبغض، نتعلق بك وحدك، ونسألك وحدك، لا تحوجنا لأحد من خلقك.",
   "ربِّ لنا أفئدة مُعلّقة بك، متوكلة عليك، سائرة إليك، ففتح لنا أبواب مغفرتك ورحمتك وهدايتك، واغننا بفضلك عمَّن سواك، وانزل البركة في حياتنا، والسكينة في منازلنا، واجعل لنا نصيب من القبول والإجابة في كل دعوة رفعناها إليك .",
   "اللهم أنَت ربِّي، لا يخفى عليك ما في قلبي، فاللهم طمأنينة منك، وغنى بك .. يارب أعوذ بك من ضيقة القلب، وشعور لا يُشكى ولا يفهم .. اللهم أرِح قلبي بما أنت به أعلم، ولا تجعلني أشكي لمن لا يخشى عليّ من حزني .. اللهم إني أُفوض دنياي كلها إليك",
   "يارب في ليلة الجمعة إجعل لنا نصيباً من الرحَمة و المَغفرة والفرج والسعادة والرزق والهداية\nاللهم صل وسلم وبارك ع خير البريه وشفيعنا يوم القيامه سيدنا محمد   ﷺ",
   "اللهُم ارحم كل من عزَّ علينا فراقهم اللهم اغفر للراحلين وأروي ارواحهم من أنهار جنتك وهب لهم رضوانًا و نعيماً وأكرمهم بالفردوس الأعلى يارب العالمين",
   "اللهُم في هذا اليوم الفضيل أجعل كل ما يتمناهُ قلبي تراهُ عيني ، اللُهم أستجب لي كل ما أعجز عن قولهِ ، وإني يارب في انتظار عطاياك المبهجة وكلي ثقة بأنك الكريم الذي حاشاه أن يرد عبده ، اللهُم عليكَ بما في قلبي و أنتَ أعلم مابه",
   "اللهُم إنّا ندعوكَ وبابُ جودك واسع، جمّلْ أيامنا ولحظاتنا وأمنياتنا بالسُّرور والعافية .",
   "اللهم بشّرنا بفرحة تسرّ خواطرنا اللهم تحقيقاً لكل الأمنيات التي طال انتظارها اللهم التمام في كل أمورنا صغيرها وكبيرها ، ورضاك والجنة ❤️.",
   "﴿‏يارب بعدد قطرات المطر استودعتك أدعية في قلبي لا يعلمها سواك ،أدعوك دعاء لا أعرف كيف أرتبه، فأنت تبصر الفؤاد وتلمس حاجة قلبي بيدك فاللهم أيام كما أحب وهمًا لا يبقى قائمًا في صدري، وفرحة ليس لها إنتهاء، و أمنياتي التي أنتظرها، اللهم طوّق قلبي بعقودٍ من الرضا، والراحة🌧✨.﴾",
   "نسألك يارب البركة والرحابة ، وحظًا في توالي النِعم ، وعافيةً في ما اعطيتنا وما انعمت به علينا ، وعوضًا وفيرًا يفيض على ندوبنا بالبشائر والرضا",
   "اللهم اخرجني من ضيق تفكيري إلى سعة تدبيرك، اللهم جبرًا يليق بعظمتك ورحمتك، اللهم ارني عجائب قدرتك اليوم عاجلاً وليس اجلاً في تحقيق حلمي وحلم كل من قال لا حول ولا قوة إلا بالله.",
   "أسأل الله العظيم رب العرش العظيم أن ينظر إليك وهو يباهي بك ملائكته فيقول سبحانه وتعالى أحببته فأحبوه ..فيا رب سر خاطره ، وأرح قلبه ، واشرح صدره..\n\nاللهم يا واحد ويا أحد يا فرد يا صمد أسعد كل احبابنه بما هو خير لهم من أمنياتهم ومن دعواتهم..\n\nاللهم إني استودعتك قلبه فلا يمسه ضر ولا حزن ولا ألم يا من لا تضيع ودائعه ..\n\nاللهم استودعتك عينيه فلا يبكي إلا من خشيتك أو يبكي فرحاً لقربك ولطاعتك.\n\nاللهم يا حي يا قيوم بلغه وعائلته وأحبابه رمضان  وهم بصحة وعافية\nاللهم اجعله من العتقاء من النيران ومن الفائزين بالجنان برحمتك يا أرحم الراحمين\nاللهم آمين.",
   "‏يا الله ارزقني حُبك، وأرزقني عونك ورضاك، اللهم لُطفك، اللهم الحاجه كُل الحاجه إليك، اللهم هُداك وذكرك وتيسيراً لا يتبعه عُسر يارب العالمين.",
   "وفي لیلة الجمعة يارب طهر أيامنا من الهم و الحزن، و افتح لنا أبواب السعادة و اﻷمل، اللهم ﻻتجعل للحزن مكاناً في قلوبنا، و إن ضاقت بنا اﻷحوال و سعها لنا برحمتك ، اللهم اشفي مرضانا وارحم امواتنا واجعلهم في جناتك يا ارحم الراحمين.",
   "أدعوك ربي أن تُبعد عني شتات البال، نوبات القلق ، أن لا يكون في طريقي سوى كُل ماهو آمن وهادئ لي ولقلبي   ",
   "اللهم بشائر خير وفرج من عندك سبحانك، اللهم بشرنا بكل خير وادفع عنَّا كُل سوء اللهم نرجو رحمتك ونخشى عذابك اللهم لاتكلنا لأنفسنا طرفة عين ،اللهم اجعلنا أغنى خلقك بك وأفقر عبادك إليك",
   "‏اللهم أغفر لما رأته عيني وانت لاترضاه واللهم اغفر لما سمعته اذني وانت لاترضاه واللهم اغفر لما نطق به لساني وانت لاترضاه."
   "آستغفر الله العظيم وآتوب إليه",
   "‏اللهم بقوة تدبيرك وعظيم عفوك وسعة حلمك وفيض كرمك أسألك أن تدبرني بأحسن التدابير، وتلطف بي، وتنجّيني مما يخيفني ويهمني، اللهم لا أُضام وأنت حسبي، ولا أفتقر وأنت ربي، فأصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين، ولا حول ولا قوة إلاّ بك . .",
   "﴿وَسَيَجْزِي اللهُ الشَّاكِرِينَ﴾\n\n«اللَّهُمَّ لَكَ الحَمْدُ حَمْدًا كَثِيرًا طَيِّبًا مُبَارَكًا فِيهِ ، كَمَا يَنْبَغِي لجَلَالِ وَجْهِكَ وَعَظِيمِ سُلْطَانِكَ»..🌷🌸",
   "اللهُمَّ  نسألك في هذا اليوم\nأن تمسـح عنا أوجاعنا\n‏وتنير ظلمات ايامنا\n‏آللهُمَّ إسقنا فرحاً\n‏وارزقنا سعادة من كل مداخل الخير\n‏اللهُمَّ أَســعِد قلوبنــا\n‏بما أنتَ أعْــلــمُ بِهِ منــا\n‏اللهُــم صل وسَـلم علىْ نَبينا مُحَـمّد ﷺ وعلــى آلــه",
   "‏اللهم إنك أنت الله لا إله إلا أنت، اللهم ادفع عنا البلاء والبراكين والزلازل والمحن وجميع الفتن ما ظهر منها وما بطن، اللهم إني أستودعك جميع المسلمين والمسلمات في بلاد المسلمين، واجعل ما أصابهم خيرًا ونعمة عليهم، اللهم احفظهم وأنت خير الحافظين.",
   "اللهم اجعلنا شاكرين لنعمك راضين بقضائك متلذذين بذكرك و طامعين برضاك ، اللهم اني اسالك اياما مبشره و هموما راحلة و قلبا مطمئنا",
   "يارب انت وحدك تعلم بالذي أحمله بقلبي وأنت يالله تعلم صعوبة أن أُكمل هذا الطريق رغم ماحدث وتعلم مابقلبي من تعب وثُقل والله أحمل مالاطاقة لي به يارب ارحم ضعفي وضعف قلبي إني يالله التجأتُ إليك وقد ضاقت بي الدنيا بما رحِبت والله إنها أيام ثِقال تمضي كثِقل الجِبال يارب الطف بقلبي",
   "ربَّاه أحببنا رسولنا ﷺولم نشاهده، وصدّقنا به ولم نخالطه، واشتقنا إليه ولم نصاحبه، وقرأنا أحاديثه ولم نجالسه.\n‏اللهم كما أكرمتنا بحبِّه، وهديتنا لشرعه، وشرّفتنا بأن كنا من أُمتّه، احشرنا في زمرته، واجمعنا تحت لوائه، وارزقنا شفاعته، وأوردنا حوضه، وأسعدنا بلقائه في الفردوس من جنتك يا رب العالمين🤍",
   "اللهم نسألك بصفاتك العليا التي لا يقدر أحد على وصفها، وبأسمائك الحسنى التي لا يقدر أحد أن يحصيها، وأسألك بذاتك الجليلة ووجهك الكريم أن تشفي كل مريض، وتعافيه بحولك وقوتك يا رب العالمين يا أكرم الأكرمين يا أجود الأجودين إنك على كل شيء قدير فاستجب لنا ما دعوناك به.",
   "اللهم في هذا البرد القارس ، هون برد الشتاء ، وأنزل دفئك ورحمتك على عبادك المُستضعفين ، والفقراء الذين لا يسمع أنينهم إلا أنت.\nاللهم إنا نستودعُك من ﻻ مأوى لهم وﻻ لباس لهم ، وﻻ مُعيل لهم\n‏اللهم أنزل على قلوبهم الدفء والطمأنينة\nوأحفظهُم بحفظك وأرحمهُم برحمتك يا أرحم الراحمين.",
   "اللهُم اكتب لنا أيام جميلة وأخبار مفرحة\n‏ونفس قنوعة راضية بكل قدر كُتب لها",
   "‏اللهم في ليلة الجمعة  نسألك نفحة من نفحات رحمتِك تلك التي لا تُبقي بؤسًا ، و لا حزنًا ، و لا ضيقًا ، و لا يأسًا أتت عليه إلا جعلته فرجًا و فرحًا يا الله ...  يارب بك تطيبُ الخواطر و من عندك تتحقّق الأمنيات استودعناك شيئاً في خواطرنا ؛ فحققه لنا يا رب العالمين .",
   "اللهُم إجعلنا مِن الذين نالوا ما تمنّوا 💚.",
   "اللهم ارزقنا نجاحاً في كل امر ونيل لكل مقصد ورزقنا القمه في اعلى الدرجات اللهم اكتب لنا التوفيق والنجاح والفرح اللهم سهل علينا كل صعب ✨",
   "”يا من رحمته واسعة وخزائنه لا تنفذ، صُبّ علينا من رحمتك وخيرك ما يجعلنا في عيشٍ مطمئن، وسِعة لا يضيق لنا بها أمر، ونعيم دائم، وقرّة عين لا تنقطع“",
   "اللهم إنا نستودعك عبادك المسلمين في كل مكان، اللهم أرحم ضعفهم وفرج كربتهم وهّون عليهم مصابهم، اللهم برداً وسلاماً على أهلنا في تركيا وسوريا وجميع المدن المنكوبة",
   "اللهم إنك أنت الله لا إله إلا أنت الغني ونحن الفقراء نحن عبيدك بنو عبيدك نواصينا بيدك ماض ٍ فينا حكمك عدل فينا قضاؤك لا ملجأ ولا منجا منك إلا إليك اللهم ادفع عنا البلاء والبراكين والزلازل والمحن وجميع الفتن ما ظهر منها وما بطن",
   "اللهم سخر لي الارض ومن عليها والسماء ومن فيها وعبادك الصالحين وكل من وليته امري وارزقني من حظوظ الدنيا أجملها",
   " اللهم اجعلنا ممن عفوت عنهم ورضيت عنهم وغفرت لهم وكتبت لهم  الجنه وحرمتهم من  النار",
   "اسأل اللهَ أن يُبشرَك بفرحة لم تحسب لها حساب، وأنْ ينيرَ دربَك ويُسهلَ لك كلَّ أمراً ، ويحفظَك من كلِّ شر ، ومن كل تعبٍ ، ومن كل هَم ، وأن يجعل أيامك القادمة تفيض سعادةً وفرحًا ولا تغيب فيها ابتسامتك .",
   "ربي في ليلة الجمعة لك عبادٌ ينتظرون فرجاً فبشرهم و عبادٌ يسألون شفاءً فعافهم وعبادٌ يرجون رحمتك فأرحمهم وأمواتٌ ينتظرون دعاء لهم فأغفرلهم🌱🌧",
   "‏اللهم إني أسألُكَ الثباتَ في الأمرِ والعزيمةَ على الرُّشْدِ وأسألُكَ شُكْرَ نعمتِكَ وحُسْنَ عبادتِكَ وأسألُك قلبًا سليمًا ولسانًا صادقًا وأسألُكَ من خيرِ ما تَعْلَمُ وأعوذُ بك من شرِّ ما تعلمُ وأستغفرُك لما تعلمُ",
   "يا قاضي الحاجات ، يا كاشف الكربات ، يا مجيب الدعوات ، يا غافر الزلات عافنا واعفو عنا ، فرج همومنا ، واشرح صدورنا ، واصلح احوالنا ، وحقق آمالنا ، واشف مرضانا ، وارحم موتانا ، وأسعد قلوبنا ، واجعلنا من المقبولين عندك تشملهم رحمتك في الدنيا والآخره\nبرحمتك يا أرحم الراحمين",
   "اللهم اجعل لنا نصيباً في سعة الأرزاق\nوتيسير الأحوال وقضاء الحاجات وإجابة الدعوات ..",
   "اللهم …..\n\n‏متعنا براحة البال وصلاح الحال وقبول الأعمال وأنعم علينا بصحة الأبدان وإكفنا شر الإنس والجان وأسألك أللَّهُم فرجاً لكل مهموم وعطاءً لكل محروم وشفاءً لكل مريض ورحمة لكل ميت ورزقاً لكل محتاج وإستجابة لكل دعاء.",
   "‏اللهُم اجعلنا أسعد خلقك وأقرب عبادك إليك، اللهم ارزقنا سعادة القلب وطمأنينة النفس وسكينة الروح، اللهُم إغفر لنا ما مضى وأصلح لنا ما بقى واكتب لنا اللهم رضاك وعفوك والجنّة برحمتك يا ارحم الراحمين",
   "للهُم أجبُر خواطرنا وارزق قلوبنا العوض الجميل عن كل ما فقدناه وقر أعُيننا بما ننتظره منك وقدِّر لنا الخير حيث كان ثم رَضّنا به وبكل شيءٍ كتبته لنا وحوِّل أحوالنا إلى أحسنها ولا تفجعنا في أحبابنا يارب.",
   "‏اللهُم عوضاً عن ما مضى وعافية \n‏فيما يجري وكَرماً فيما سيأتي🤎",
   "‏اللهم انت ربي لا اله الا انت خلقتني وانا عبدك وانا على عهدك ووعدك ما استطعت اعوذ بك من شر ما صنعت ابوء لك بنعمتك علي وابوء بذنبي فغفر لي فإنه لا يغفر الذنوب الا انت .",
   "اللهم يا مسبب الأسباب، يا مفتح الأبواب، ويا سامع الأصوات، ويا مجيب الدعوات، ويا قاضيَ الحاجات، اكفنى بحلالك عن حرامك، وأغنني بفضلك عمن سواك",
   "ياربّ كل الأمر عندك، وكل الجند طوعك، وكل أمورنا بحكمتك؛ فيسّر وسهّل واقضِ قضاءً يرضي القلب الذي عقد رجاءه إيمانًا بقدرتك، وتسليمًا لحكمك، ويقينًا بعدلك",
   "‏اللهم اجعل هذه الجمعة حاملة لنا من الخير فوق ما نرجو واشرح صدورنا ، ويسر أمورنا\n‏وأرحم موتانا وأشف مرضانا وأجعلها جمعة خير لأمورنا كلها يارب",
   "اللهُم اعطنا خير ما تُعطي السائلين ، واجمع لنا صلاح الدنيا والدِين ، اللهم زِدنا نوراً في القلب ، وضياءً في الوجه ، وسعة في الرزق ، ومحبة في قلوب العباد ، واغفر لنا ولوالدينا ولجميع المسلمين💛.",
   "اللهم اجعلنا نمشي في رياض جنتك، وتجمعنا مع أحبتك، ونحيا على ذكرك، ونستقيم يا الله على كتابك العظيم، ونموت على شهادتك، وبارك لنا يا الله ولوالدينا في جمعتك هذه، وارحمنا برحمتك الواسعة التي وسعت كل شيء،  واللهم ارحم امواتنا وأجعل مثواهم الجنة ،جمعة مباركة.",
   "‏اللهم ارزقنا حلو الحياة وخير العطاء وسعة الرزق وراحة البال ولباس العافية وحسن الخاتمة.",
   "اللهم إني اسألك حسن الخاتمة اللهم ارزقني توبةً نصوحاً قبل الموت اللهم يا مقلب القلوب ثبت قلبي على دينك",
   "اللهُم وسع قبور من رحلوا إليك بجنةٍ لا يفنى نعيمها",
   "اللهم اسقنا الغيث ولا تجعلنا من القانطين\nأللهم اجعلها سقيا رحمة لا سقيا عذاب 🤲🏻♥️",
   "يارب وكَّلتك أمري وحيرتي وشتاتي وقلة علمي، وكلتك الأبواب المُغلقة التي مفاتيحها بين يديك، والأمور الصعبة التي تيسيرها هينٌ عليك، وكلتك الطرق التي لا أعلم نهايتها والمسافات التي لا أعلم حجمها، وكلتك سعادتي فلا تجعل همًا يشقيني ولا خوفًا يرهقني، استودعتك حياتي فإنك خير المُستودعين.",
   "في الأيام الأخيرة من هذا العام، أشهدك يا الله أنك سبحانك أكرمتني وسترتني وأعطيتني من فضلك الواسع، وأنعمت عليّ بكرمك وجودك، وأحمدك على كل مرض غفر ذنب، وكل ابتلاء رفع مقام، وكل عسر جاء معه يسر، وكل منع كان هو نفسه عين العطاء.. وأسألك يا رب في العام الجديد سترًا وعفوًا وقربًا إليك.. وأسألك العوض.. العوض عن كل سوءٍ رأيته، وأسألك يا رب أن تجعلني لكَ كما تحب أنت.",
   "اللهُمَّ إنَّا  نسألك البركة في يومنا والتيسير في أمورنا والتسهيل في شؤوننا والتثبيت في قلوبنا والبهجة على وجوهنا والعافية في أبداننا وزيادة الرزق في أموالنا والصلاح في أولادنا والأجر والثواب في طاعتنا والقبول في عباداتنا .\nوان تشافي مرضانا ، وترحم امواتنا\n‏اللهم آمين يارب العالمين",
   "اللهم امنحنا في هذا اليوم من رحمتك وفضلك ماتُسعِدُ به قلوبنا، وتَشرح به صدورنا، وتُيَسّر به دروبنا، وتُنَفّس به كروبنا، وتغفر به ذنوبنا، ياربّ العالمين",
   "اللهم انك أكرمتني فلك الحمد ، وسترتني فلك الحمد ، ورزقتني فلك الحمد ، وعافيتني فلك الحمد .. لك الحمد حبًا وشكرًا ، ولك الحمد يومًا وعمرًا ، ولك الحمد دائمًا وأبدًا .",
   "ربي إنا طرقنا بابك راجين جودك\n‏فافتح لنا ولأحبتنا ابواب سمائك.\n‏واغمرنا برحمتك ..واجرنا من عظيم بلائك وسخر لنا الطيبين من عبادك\n‏إلهي .. إلى من نقصد وأنت المقصود ومن ذا الذي يسأل وأنت رب الوجود ..اللهم اقض حوائجنا ، واغفر ذنوبنا.\n‏اللهم اشف مرضانا. وارحم موتانا",
   "اللهمّ يا مسهّل الشّديد، ويا مليّن الحديد، ويا منجز الوعيد، ويا من هو كلّ يومٍ في أمرٍ جديد، أخرجني من حلق الضّيق الى أوسع الطّريق، بك أدفع ما لا أطيق، ولا حول ولا قوّة إلّا بالله العليّ العظيم🌱",
   "‏إليك يا الله نبث كل مايهمّنا ويقلقنا ويتعبنا، ومنك يا الله وحدك نرجو الفرج والتيسير والفرح.. اللهم غيثًا من رحمتك ولطفك وكرمك وفضلك على قلوبنا وأرواحنا وحياتنا🤲🏼💜",
   "اللهم أصلح لنا أمورنا، واكتب لنا من خفايا القدر أجملها، اللهم اجعل لنا نصيبًا في سعة الأرزاق وقضاء الحاجات وإجابة الدعوات، اللهم لطفك بقلوبنا وأحوالنا وأيامنا، اللهم تولّنا بسِعتك وعظيم فضلك، وارزقنا لذة الوصول بعد السعي، وحاوط قلوبنا برحمتك يا رحيم فإنك على كل شيءٍ قدير.",
   "‏اللهم هب لنا من جلالك عزاً ، ومن خزائنك رزقآ\nاللهم اجعلنا من اصحاب الحمد عند العطاء و الصبر عند البلاء و هب لنا نفوسا راضية و صدورا من الهموم خالية و قلوبا بحبك صافية و اتمم علينا الصحة و العافية اللهم أعتق رقابنا ورقاب آبائنا وأمهاتناوإخواننا وأخواتنا وأزواجنا",
   "ياربِّ وإن كُنا مُقصرين؛ فِي الدُعاء للأموات فأنتَ الكريم الذي لاتنسى هب لهم نعيمًا ورضوانًا وسرورًا اللهُمَّ ارحم موتانا واغفر لهم ونوّر قبورهم",
   "‏اللهم ارزقنا سعادة القلب وطمأنينة\n‏النفس وسكينة الروح، اللهم اجعلنا أسعد\n‏خلقك وأقرب عبادك إليك ،\n‏اللهم إغفر لنا ما مضى وأصلح لنا\n‏ما بقى واكتب لنا رضاك وعفوك والجنة\n‏برحمتك يا أرحم الراحمين",
   "‏اللهم أجبر خاطر كل مكسور\nو فرج هم كل مهموم  و أدخل السعادة\nفي قلب كل حزين\nو إشفِ برحمتك كل من يتألم.\n‏و إقضِ\nبكرمك كل حوائجنا\nوارحم جميع امواتنا\nو إستجب كل دعواتنا و إغفر ذنوبنا\n‏وأرزق نفوسنا الراحة و الطمأنينه\nو احفظنا بعينك التي لا تنام  🖤",
   "اللهم يا من وسعت رحمته كل شيء يا مالك الملك لا تجعلنا من الذين ضَل سعيهم في الدنياوهم يحسبون انهم يحسنون صنعاً اللهم اهدينا واغفر لنا وارحمنا واجعلنا من الفائزين برضاك يالله",
   "اللّهمّ فرّج أُموراً ضَاقت بها صُدورنا . وعجزت بها حيلتنا وقلّ بها صَبرنا... الّلهمّ أَسعِد قلوبنا بما أنتَ أعْلَمُ بِهِ مِنّا ... اللّهمّ اجْعَل مانُريدُه في حياتِنا قريباً لِناظِرنَا سَعيداً لخواطِرنَا .اللّهمّ أسْعدنَا سعادتين : الدّنْيا بِخيرِها والجنّةِ بِفردَوسها♥️",
   "‏يا الله، أنت أكبر من الحظ، وأكبر من هذا التعجيز، وأكبر من هذا التعقيد، وأكبر من هذه البعثرة، اختَرْ لي ولا تخيرني، واكفني شتات العقل، وحزن القلب، وحيرة النفس، وارزقني طاقة بها أعيش وأتحمل، وأرضى ، وأتأقلم، وأتقبل، واتجاهل ، وأسعى ، واصبر، فعليك توكلت وأنت خير وكيل",
   "ونسألك يالله ألا نرتخي أمام جراحنا، وألا تتمكن منا الهواجس، وألا يغدر بنا الأمل، وألا نكون سببًا في تدمير أرواحنا آمين",
   "‏اللهم أمسح على قلبي براحة تُسِّر بها نفسي يارب أشرح لي صدري و يسر لِي أمري وطمّن قلبي و أكفني ما أهمّني وارزقني راحة البال",
   "‏اللهم أشرح الصدور وبارك في الأجور\n‏ويسر الأمور وأرحم أهل القبور وأنقلهم\n‏من الضيق إلى أنس وسرور يا رحيم يا غفور ..",
   "اللهم أنت الوآهب لآ سوآك .. والمعطي لمن دعآك .. يآمن ترآنا ولآ نرآك .. وتعطينآ ولآنبلغ ثنآك .. اجعل كل أيآمنآ في حسن عبآدتك وطآعتك ورضآك .. وبارك لنآ فيمآ رزقتنا وقنآ عذآب النآر .. وأكرمنآ بخير هذه الدآر ونعيم تلك الدآر",
   "اللهم أذق من رحلوا الى جوارك حلاوة الجنة ونعيمها..\nيارب وسع على موتانا قبورهم وگفر سيئاتهم وعاملهم برحمتك وعفوك ي غفور...\nاللهم آنس وحشتهم واجعلهم من اهل جنات النعيم..",
   "ربي أرزقني تسابق أمنياتي علي بتسخير منك\nيا مجيب الدعوات وياقاضي الحاجات ..",
   "‏اللهم أبعد عني كل ما يُدمع عيني وأبعد عني الضيق الذي يخفي ابتسامتي اللهم ارح قلبي وعوضني عن كل أمر أحزنني❤️‍🩹",
   "اللهم لك أسلَمتُ، وبك آمَنت، وعليك توكَّلت، وإليك أنَبت، وبك خاصَمت، وإليك حاكَمت، فاغفِرْ لي ما قدَّمتُ وما أخَّرت، وما أسرَرتُ وما أعلَنت، أنت إلهي، لا إله إلا أنت",
   "‏اللهم فوضت أمري وأنت خير مُعين \n‏و سألتك خيراً وجبراً لقلبي وتوفيقاً في كل حين\nاللهم اكتب لنا من خيرك و أتم علينا فضلك وتقبل منا صلاتنا\n‏وارزقنا طاعتك واجعل خير أعمالنا خواتيمها وارزقنا راحة البال",
   "عوضني يارب عن كل ألم حاصر روحي وعن كل كدرٍ عكر صفو حياتي ولا أرجو غير جبرك وعوضك شيء يارحيم .",
   "‏اللهم إنا نسألك في سفرنا هذا البرّ والتقوى، ومن العمل ما ترضى، اللهم هون علينا سفرنا هذا واطو عنا بعده، اللهم أنت الصاحب في السفر، والخليفة في الأهل، اللهم إني أعوذ بك من وعثاء السفر، وكآبة المنظر وسوء المنقلب في المال والأهل",
   "رباه أنا هنا، حيث وضعتني أقاوم لمستقبل لا أعرف عنه شيء، ولكنك تعلمه، اللهم أيامًا كما أحب وحالًا  إلى ما هو أفضل، يارب السعة أخرجنا من كل ضيق .",
   "اللهم أجبر خوآطرنا جبراً أنت وليه وإعطنا سؤلنا وأسعد قلوبنآ فإنه لآ يعجزك شيء\nفي الأرض ولآ في السمآء\nاللهم إنا نسألك فرجا تقر به الأعين وتصح\nبه الأبدان وتسمو به الروح فحقق لنا كل\nالأمنيات وعلق قلوبنآ بجميل الطاعآت\nواغمرنا بعفوك ومغفرتك وأمطرنا\nبكرمك ولاتحرمنا رحمتك يارب",
   "اللهم أصلح لنا أمورنا، واكتب لنا من خفايا القدر أجملها، اللهم اجعل لنا نصيبًا في سعة الأرزاق وقضاء الحاجات وإجابة الدعوات، اللهم لطفك بقلوبنا وأحوالنا وأيامنا، اللهم تولّنا بسِعتك وعظيم فضلك، وارزقنا لذة الوصول بعد السعي، وحاوط قلوبنا برحمتك يا رحيم فإنك على كل شيءٍ قدير",

   ]
   while not await asyncio.sleep(1800):
     for i in chat:
       try:
         await app.send_message(i, random.choice(ad3iyal))
       except:
         pass
    
     
asyncio.create_task(ad3iya())


@app.on_message(filters.group, group = 770)
async def azkarr(c, msg):
  if msg.text == "تفعيل الاذكار":
    if msg.chat.id in chat:
      return await msg.reply_text("الاذكار مفعله من قبل 💘 ⋅")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذكار 💘 ⋅")
  elif msg.text == "تعطيل الاذكار":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذكار 💘 ⋅")
    else:
      return await msg.reply_text("الاذكار معطله من قبل 💘 ⋅")
      


async def azkar():
   azkarl = [
   "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
   "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
   "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
   "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "سبحان الله وبحمده سبحان الله العظيم🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
   "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
   "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
   "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
   "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
   "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
   "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
   "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
   "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
   "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
   "استغفر الله العظيم وأتوبُ إليه.",
   "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
   " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
   "ماتستغفر ربنا كده🥺❤️",
   "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
   "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
   "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
   "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
   "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
   "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
   "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
   "أصبحنا وأصبح الملك لله ولا اله الا الله.",
   "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
   "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
   "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
   "- اللهم القبول الذي لا يزول ❤️🍀.",
   "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
   "سبحان الله وبحمده ،سبحان الله العظيم.",
   "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
   " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
   "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
   "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
   "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
   "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
   "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
   "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
   "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
   "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
   "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
   "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
   "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
   "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
   "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
   "صلي على النبي بنيه الفرج❤️",
   "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
   "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
   "لا اله الا الله سيدنا محمد رسول الله🌿💜",
   "قول معايا - استغفر الله استفر الله استغفر الله -",
   "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
   "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
   "صلي على اشرف الخلق سيدنا محمد صلاةً الله عليه وسلم تسليما كثيرا ❤️",
   "ربي اجعلني مقيم الصلاة ومن ذريتي ربنا وتقبل دعاءنا . ربنا تقبل منا إنك أنت السميع العليم وتب علينا إنك أنت التواب الرحيم",
   "رب اغفر لي خطيئتي يوم الدين❤️",
   "اللهم اهدني فيمن هديت، وعافني فيمن عافيت، وتولني فيمن توليت، وبارك لي فيما أعطيت، وقني شرما قضيت، إنه لا يذل من واليت، تباركت ربنا وتعاليت",
   "اللهم إني أعوذ بك من عذاب النار، وأعوذ بك من عذاب القبر، وأعوذ بك من الفتن ما ظهر منها وما بطن، وأعوذ بك من فتنة الدجال",
   "اللهم إني أعوذ بك من علم لا ينفع وعمل لا يرفع وقلب لا يخشع وقول لا يسمع",
   "اللهم لا تخزني يوم القيامة",
   "اللهم إني أعوذ بك من صلاة لا تنفع",
   "اللهم إني أسألك الفردوس أعلى الجنة",
   "أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ. مرة واحدة",
   "اللهم يا رحمن يا حنان يا منان استودعك يا رب قلبي فلا تجعل فيه أحدا سواك واستودعتك شهادة لا إله إلا الله فألهمني بها يا رب عند الممات واستودعك اللهم نفسي فلا تجعلني أخطو خطوة واحدة إلا في مرضاتك واستودعك روقي وعافيتي فاحفظها لي.",
   "اللهم يا كريم يا ودود يا رحيم يا عظيم انك قادر على كل شيء انك تقول للشيء كن فيكون ارحم اهلي رحمة دائمة واجعلهم من أهل الجنه في الفردوس لأعلي اللهم تقبلهم إليك واسعدهم بلقائك",
   "اللهم يا رحمن يارحيم ارحمني برحمتك الواسعه يارب ونقني من زنوبي مثل نقاء الثوب الأبيض من الدنس",
   "رَبَّنَا اغفِر لي وَلِوالِدَيَّ وَلِلمُؤمِنينَ يَومَ يَقومُ الحِسابُ",
   "رَّبِّ اغْفِرْ لِي وَلِوَالِدَيَّ وَلِمَن دَخَلَ بَيْتِيَ مُؤْمِنًا وَلِلْمُؤْمِنِينَ وَالْمُؤْمِنَاتِ وَلَا تَزِدِ الظَّالِمِينَ إِلَّا تَبَارًا",
   "اللهمَّ اغفر لوالدي وارحمهما كما ربّياني صغيراً، اللهمّ يا باسط اليدين بالعطايا ابسط على والدي من فضلك العظيم وجودك الواسع ما تشرح به صدرهما لعبادتك وطاعتك، والأنس بك والعمل بما يُرضيك، وبارك لهما في عُمرها، واغنهما من فضلك، وأعنهما في حلّهما وترحالهما وذهابهما وإيابهما، وأطل في عمرهما مع العافية في صحتهما ودِينهما، واجعل اللهمَّ آخر كلامهما من الدنيا لا إله إلّا الله محمدٌ رسول الله",
   "(اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ فِي الدُّنْيَا وَالآخِرَةِ، اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ: فِي دِينِي وَدُنْيَايَ وَأَهْلِي، وَمَالِي، اللَّهُمَّ اسْتُرْ عَوْرَاتِي، وَآمِنْ رَوْعَاتِي، اللَّهُمَّ احْفَظْنِي مِنْ بَينِ يَدَيَّ، وَمِنْ خَلْفِي، وَعَنْ يَمِينِي، وَعَنْ شِمَالِي، وَمِنْ فَوْقِي، وَأَعُوذُ بِعَظَمَتِكَ أَنْ أُغْتَالَ مِنْ تَحْتِي)).",
   "يا حيّ يا قيّوم برحمتك أستغيث أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عينٍ أبداً ...",
   "‏﴿ وَاذْكُر ربّكَ إِذَا نَسِيتَ ﴾ ",
   "- اللهم صلِ وسلم على نبينآ محمد ❥⇣",
   "((اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبَيِّنَا مُحَمَّدٍ)) (عشرَ مرَّاتٍ).",
   "اللهم يا عزيز يا جبار اجعل قلوبنا تخشع من تقواك واجعل عيوننا تدمع من خشياك واجعلنا يا رب من أهل التقوى وأهل المغفر",
   "استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب الي",
   "اللهم إنك عفو تُحب العفو فاعفُ عن",
   "اللهم إني أسألك الثبات في الامر والعزيمة على الرشد واسالك قلبا سليما ولسانا صادقا واسالك شكر نعمتك و حسن عبادت",
   "اللهم إني أسألك العافية في الدنيا والآخرة، اللهم إني أسألك العفو والعافية في ديني ودنياي، وأهلي ومالي، اللهم استُر عوراتي، وآمِن رَوعاتي، اللهم احفظني من بين يدي ومن خلفي، وعن يميني وعن شمالي، ومن فوقي، وأعوذ بعظمتك أن أُغتال من تحتي",
   "((اللَّهُمَّ قِنِي عَذَابَكَ يَوْمَ تَبْعَثُ عِبَادَكَ)).",
   "((لاَ إِلَهَ إِلاَّ اللَّهُ، وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ)) (مائةَ مرَّةٍ).",
   "((اللَّهُمَّ عَالِمَ الغَيْبِ وَالشَّهَادَةِ فَاطِرَ السَّمَوَاتِ وَالْأَرْضِ، رَبَّ كُلِّ شَيْءٍ وَمَلِيكَهُ، أَشْهَدُ أَنْ لاَ إِلَهَ إِلاَّ أَنْتَ، أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ شَرِّ الشَّيْطانِ وَشِرْكِهِ، وَأَنْ أَقْتَرِفَ عَلَى نَفْسِي سُوءاً، أَوْ أَجُرَّهُ إِلَى مُسْلِمٍ))",
   "اللهم اكفني بحلالك عن حرامك، وأغنني بفضلك عمن سواك",
   "(بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَاَ حَوْلَ وَلَا قُوَّةَ إِلاَّ بِاللَّهِ)",
   "((أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ)) (مِائَةَ مَرَّةٍ فِي الْيَوْمِ).",
   "اللهم نشكوا إليك ضعفنا وقلة حيلتنا من امرنا فأغثنا وارحمنا واغفرلنا ولا تكل امرنا لمن لايخافك ولا يرحمنا ولا تؤخذنا بما فعل السفهاء منا",
   "مَنْ كَانَ آخِرُ كَلاَمِهِ لاَ إِلَهَ إِلاَّ اللَّهُ دَخَلَ الْجَنَّة"
   "االلَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞 ",
"من الأدعية النبوية المأثورة:اللهمَّ زَيِّنا بزينة الإيمان",
"اااللهم يا من رويت الأرض مطرا أمطر قلوبنا فرحا 🍂 ",
"اا‏اللَّهُـمَّ لَڪَ الحَمْـدُ مِنْ قَـا؏ِ الفُـؤَادِ إلىٰ ؏َـرشِڪَ المُقـدَّس حَمْـدَاً يُوَافِي نِـ؏ـمَڪ 💙🌸",
"﴿وَاذْكُرِ اسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًا﴾🌿✨",
"﴿وَمَن يَتَّقِ اللهَ يُكَفِّرْ عَنْهُ سَيِّئَاتِهِ وَيُعْظِمْ لَهُ أَجْرًا﴾",
"«سُبْحَانَ اللهِ ، وَالحَمْدُ للهِ ، وَلَا إلَهَ إلَّا اللهُ ، وَاللهُ أكْبَرُ ، وَلَا حَوْلَ وَلَا قُوَّةَ إلَّا بِاللهِ»🍃",
"وذُنُوبًا شوَّهتْ طُهْرَ قُلوبِنا؛ اغفِرها يا ربّ واعفُ عنَّا ❤️",
"«اللَّهُمَّ اتِ نُفُوسَنَا تَقْوَاهَا ، وَزَكِّهَا أنْتَ خَيْرُ مَنْ زَكَّاهَا ، أنْتَ وَلِيُّهَا وَمَوْلَاهَا»🌹",
"۝‏﷽إن اللَّه وملائكته يُصلُّون على النبي ياأيُّها الذين امنوا صلُّوا عليه وسلِّموا تسليما۝",
"فُسِبًحً بًحًمًدٍ ربًکْ وٌکْنِ مًنِ الَسِاجّدٍيَنِ 🌿✨",
"اأقُمً الَصّلَاةّ لَدٍلَوٌکْ الَشُمًسِ إلَيَ غُسِقُ الَلَيَلَ🥀🌺",
"نِسِتٌغُفُرکْ ربًيَ حًيَتٌ تٌلَهّيَنِا الَدٍنِيَا عٌنِ ذِکْرکْ🥺😢",
"وٌمًنِ أعٌرض عٌنِ ذِکْريَ فُإنِ لَهّ مًعٌيَشُةّ ضنِکْا 😢",
"وٌقُرأنِ الَفُجّر إنِ قُرانِ الَفُجّر کْانِ مًشُهّوٌدٍا🎀🌲",
"اأّذّأّ أّلَدِنِيِّأّ نَِّستّګوِ أّصٌلَګوِ زِّوِروِ أّلَمَقِأّبِر💔",
"حًتٌيَ لَوٌ لَمًتٌتٌقُنِ الَخِفُظُ فُمًصّاحًبًتٌ لَلَقُرانِ تٌجّعٌلَکْ مًنِ اهّلَ الَلَهّ وٌخِاصّتٌهّ❤🌱",
"وٌإذِا رضيَتٌ وٌصّبًرتٌ فُهّوٌ إرتٌقُاء وٌنِعٌمًةّ✨??",
"«ربً اجّعٌلَنِيَ مًقُيَمً الَصّلَاةّ وٌمًنِ ذِريَتٌيَ ربًنِا وٌتٌقُبًلَ دٍعٌاء 🤲",
"ااعٌلَمً انِ رحًلَةّ صّبًرکْ لَهّا نِهّايَهّ عٌظُيَمًهّ مًحًمًلَهّ بًجّوٌائزٍ ربًانِيَهّ مًدٍهّشُهّ🌚☺️",
"اإيَاکْ وٌدٍعٌوٌةّ الَمًظُلَوٌمً فُ إنِهّا تٌصّعٌدٍ الَيَ الَلَهّ کْأنِهّا شُرارهّ مًنِ نِار 🔥🥺",
"االَلَهّمً انِقُذِ صّدٍوٌرنِا مًنِ هّيَمًنِهّ الَقُلَقُ وٌصّبً عٌلَيَهّا فُيَضا مًنِ الَطِمًأنِيَنِهّ✨🌺",
"يَابًنِيَ إنِ صّلَاح الَحًيَاةّ فُ أتٌجّاهّ الَقُبًلَهّ 🥀🌿",
"الَلَهّمً ردٍنِا إلَيَکْ ردٍا جّمًيَلَا💔🥺"
   ]
   while not await asyncio.sleep(1900):
     for i in chat: 
       try:
         await app.send_message(i, random.choice(azkarl))
       except:
         pass
    
     
asyncio.create_task(azkar())
