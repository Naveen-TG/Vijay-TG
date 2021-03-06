class Script(object):
    START_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..</b>"""

    HELP_TXT = """Hey {}

<b>Here Is The Help For My Commands.</b>

/start - Cğğ¾ğ¼ğ Wğğ¾ğğğ¾ğ ağ Oğğğğğ¾ 
/help - Gğ¾ğ Tğğğ Hğ¾ğğ Mğ¾ğğğºğğ¾
/about - Ağ»ğğğ Mğ¾"""

    ABOUT_TXT = """<b>â¥ ğğ® ğğğ¢ğ : {}

â¥ ğ¾ğ§ğğğ©ğ¤ğ§ : <a href='https://t.me/Y2say'>Dhanush-TG</a>

â¥ ğğğğ§ğğ§ğ® : <a href='https://docs.pyrogram.org/'>Pyrogram</a>

â¥ ğğğ£ğğªğğğ : Python ğ¹

â¥ ğ¿ğğ©ğ ğ½ğğ¨ğ : <a href='https://www.mongodb.com/'>MongoDB</a>

â¥ ğ½ğ¤ğ© ğğğ§ğ«ğğ§ : <a href='https://heroku.com'>Heroku</a>

â¥ ğ½ğªğğ¡ğ ğğ©ğğ©ğªğ¨ : v2.0.1 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>
Dhanush is not a Open source project.

ğ²ğ®ğ´ğ±ğ¢ğ¤ ğ¢ğ®ğ£ğ¤ ~ ğ­ğ®ğ³ ğ ğµğ ğ¨ğ«ğ ğ¡ğ«ğ¤ ğ±ğ¨ğ¦ğ§ğ³ ğ­ğ®ğ¶</b>

<b>ğ®ğ³ğ§ğ¤ğ± ğªğ¨ğ­ğ£ ğ¡ğ®ğ³ğ²:</b>
<b>ğ ğ´ğ³ğ® ğ¥ğ¨ğ«ğ³ğ¤ğ±</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>ğ¤ğğº ğ¬ğºğğğº</a>
<b>ğ²ğ®ğ­ğ¦</b> :  <a href='https://github.com/AsmSafone/RadioPlayerV2'>ğ ğğğ²ğºğ¿ğğğ¾</a>
<b>ğ¥ğ¨ğ«ğ³ğ¤ğ±</b> : <a href='https://github.com/TroJanzHEX/Unlimited-Filter-Bot'>ğ´ğğğğğğğ¾ğ½ ğ¥ğğğğ¾ğ ğ¡ğğ</a>
<b>PLUGINS</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>Eva Maria</a>

<b>DEVS:</b>
- <a href='https://t.me/Naveen_TG'>Naveen-TG</a>"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Dhamush should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - add a filter in chat.
â¢ /filters - list all the filters of a chat.
â¢ /del - delete a specific filter in chat.
â¢ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Dhanush Support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Dhanush supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code>{fullname}</code>: The user's full name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Message Text.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage:</b>
â¢ /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
 /connect  - connect a particular chat to your PM.
â¢ /disconnect  - disconnect from a chat.
â¢ /connections - list all your connections."""
    
    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage:</b>
â¢ /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
â¢ IMDb should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    COVID_TXT = """<b><u>ğ¢ğğğğ½ 19 ğğğ¿ğğğğºğğğğ</u><b/>

- It is Used to Find ğ¢ğğğğğº Iğğ¿ğğğğºğğğğ ğğ¿ Yğğğ Cğğğğğğ / ğ³ğ ğğğğ ğğğ¾ ğ¼ğğğğ½ ğğğ¿ğ ğğ¿ ğºğğ ğ¼ğğğğğğ            
- ğ¢ğğğğ½ get True and current details and cases
     
<b>NOTE:</b>

1. Users Can Use this to know the Current COVID Info
2. All Users of Dhanush can access this Feature

<b>ğ¢ğğğğºğğ½ and Usage</b>
â¢ /covid (country Name) - ğ¦ğ¾ğ ğğğ¿ğ ğºğ»ğğğ ğ¼ğğğğ½ ğ¼ğºğğ¾ğ ğğ ğğğğ ğ¼ğğğğğğ

<b>ğ´ğğºğğ¾</b>
- ğ¢ğğğğ½ ğ»ğ¾ ğğğ¾ğ½ ğğ ğğ ğºğğ½ ğğğğğğ."""

    STICKER_TXT ="""Help: <b>StickerID</b>

- It is Used to get the id of the stickers
- Can get instant and unexpirable ids

<b>Commands and Usages</b>
â¢ /stickerid - Reply to a Sticker to get the ids 

<b>Usages</b>
ğ¨ğ¿ ğ¸ğğ ğ­ğ¾ğ¾ğ½ ğ³ğ¾ğğ¾ğğğºğ ğ²ğğğ¼ğğ¾ğ ğ¨ğ½ Use Commands ğ³ğ ğ¦ğ¾ğ ğ²ğğğ¼ğğ¾ğ ğ¨ğ½ (ğ±ğ¾ğğğ ğ¶ğğğ ğ²ğğğ¼ğğ¾ğ)</b>"""
     
    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
â¢ /paste [text] - paste the given text on Pasty
â¢ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
â¢ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
â¢ Dhansuh should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
â¢ /id - get id of a specified user.
â¢ /info  - get information about a user.
â¢ /json - get the json details of a message.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    IMAGE_TXT = """Help: <b>Image</b>

ğğğğ ğğğğğğğ ğğğğğ ğ¢ğğ ğğ ğğğğ a ğğğğğ ğğğğ¢ ğğğğğğ¢ 

â¤ ğğ¨ğ¦ğ¦ğğ§ğğ¬ ğğ§ğ ğğ¬ğğ ğ:

âª ğ©ğğğ ğğ¾ğğ½ ğğ¾ ğº ğğğºğğ¾ ğğ ğ¾ğ½ğğ â¨"""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
â¢ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ Dhanush can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
â¢ /imdb  - get the film information from IMDb source.
â¢ /search  - get the film information from various sources.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ More search tools can be found on inline.
â¢ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
â¢ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on group.
â¢ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
â¢ /ban - ban a user.
â¢ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
â¢ /mute - mute a user.
â¢ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
â¢ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on group.
â¢ These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
â¢ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
â¢ /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works only group.
â¢ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - to get the rescent errors.
â¢ /stats - to get status of files in db.
â¢ /delete - to delete a specific file from db.
â¢ /users - to get list of my users and ids.
â¢ /chats - to get list of the my chats and ids.
â¢ /leave - to leave from a chat.
â¢ /disable - do disable a chat.
â¢ /ban_users - to ban a user.
â¢ /unban_users - to unban a user.
â¢ /channel - to get list of total connected channels.
â¢ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>ğ ğğ¤ğ©ğğ¡ ğğğ¡ğğ¨ : </b> <code>{}</code>

<b>ğ¤ ğğ¤ğ©ğğ¡ ğğ¨ğğ§ğ¨ : </b> <code>{}</code>

<b>ğ¥ ğğ¤ğ©ğğ¡ ğ¾ğğğ©ğ¨ : </b> <code>{}</code>

<b>âï¸ ğğ¨ğğ ğğ©ğ¤ğ§ğğğ : </b> <code>{}</code> MiB

<b>ğ ğğ¤ğ©ğğ¡ ğğ©ğ¤ğğğ : </b> <code>{}</code> MiB


ğğ® ğğğ§ğ«ğğ§ ğğ©ğğ©ğªğ¨ ğ

ğ» ğ¾ğğ ğğ¨ğğğ :</b> {}%
âï¸ ğğ¼ğ ğğ¨ğğğ :</b> {}%"""

    FORCESUB_TXT = """**â¦ï¸ READ THIS INSTRUCTION â¦ï¸**

__ğ£ In Order To Get The Movie Requested By You in Our Groups, You Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately ğ__

**ğ JOIN THIS CHANNEL & TRY AGAIN ğ**"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
â¢ /throw or /dart - tğ mğºğğ¾ drat 
â¢ /roll or /dice - roll the dice 
â¢ /goal or /shoot - to make a goal or shoot
â¢ /luck or /cownd - Spin the Lucky
â¢ /runs strings

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
â¢ /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
â¢ Dhamush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
â¢ /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
â¢ /song or /mp3 (songname) - download song from yt servers.
â¢ /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
â¢ /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
â¢ /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
â¢ Only Digits Are Allowed
â¢ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
â¢ Dhanush should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

A bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
â¢ /share (text or reply to message)

<b>NOTE:</b>
â¢ Dhansuh should have admin privillage.
â¢ These commands works on both pm and group.
â¢ These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
â¢ /inkick - command with required arguments and i will kick members from group.
â¢ /instatus - to check current status of chat member from group.
â¢ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
â¢ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
â¢ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """âYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âï¸ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """ğ® Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """âI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """âï¸ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
