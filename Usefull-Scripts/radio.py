import time

import vlc

# pip install python-vlc

url = "https://stream6.megarockradio.net:80"
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(url)
player.set_media(media)
player.play()


try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("\nExiting nicely...")
