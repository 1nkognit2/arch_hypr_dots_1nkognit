import os

home = os.getenv("HOME")
wal_colors = f"{home}/.cache/wal/colors-universal.css"

image = input('Drag & drop wallpaper image: ')
os.system(f'wal -i {image}')
file = open(f'{home}/.config/hypr/wallpapers.conf','wb')
file.write(f'$wallpaper = {image}'.encode())
file.close()
os.system(f'')
os.system(f'killall hyprpaper || true')
os.system(f'killall waybar || true')
os.system(f'waybar & disown')
os.system(f'hyprpaper & disown')