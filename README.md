# dex_bot

Discord bot with the following functions:

- prefix '$'
-----------
- play [youtube link]    -> Joins Lobby and plays the link
- play [own search term] -> Joins Lobby, searched the given term on youtube, finds the first Video, copies the link and then plays it
- pause                  -> Pauses the song being played
- resume                 -> Resumes the song that got paused
- join                   -> Joins the Voice chat, from which the user called the bot. Does not work if the user is not in VC
- leave                  -> Leaves the Voice chat
- greet                  -> Greets the user with a message
-----------
Bot is hosted on a Raspi4b and being accessed through RDP on Windows/Remmina on Linux
