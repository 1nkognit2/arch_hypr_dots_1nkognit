import os

home = os.getenv("HOME")
wal_colors = f"{home}/.cache/wal/colors-universal.css"

while 1:
    image = input('Drag & drop wallpaper image (without spaces): ')
    if image.count(' ') > 0:
        print('Please, enter image without spaces')
    else:
        break

os.system(f'wal -i {image}')
file = open(f'{home}/.config/hypr/wallpapers.conf','wb')
file.write(f'$wallpaper = {image}'.encode())
file.close()
file = open(f'{home}/.config/hypr/hyprpaper.conf','wb')
file.write(f'preload = {image}\nwallpaper = , {image}'.encode())
file.close()
os.system(f'')
os.system(f'killall hyprpaper || true')
os.system(f'killall waybar || true')
os.system(f'waybar & disown')
os.system(f'hyprpaper & disown')