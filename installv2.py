import os
import pathlib
import shutil

def dialog(text: str, default_true: bool):
    dialog = input(f'{text} ({'Y/n' if default_true else 'y/N'}): ')
    if dialog.lower() == 'y':
        return True
    elif dialog == '':
        if default_true:
            return True
        else:
            return False
    else:
        return False

do_nvidia_drivers = dialog('Install NVidia drivers?', False)
do_reboot = dialog('Reboot after install?', True)




print(r'''
          ___         _        _ _ _                           _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ __| |____ _ __ _ ___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` / _| / / _` / _` / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_\__|_\_\__,_\__, \___/__/
                                         |___/  |_|                    |___/
''')

packages = {
    'Pacman': [
        'gtk3',
        'gtk4',
        'hyprland',
        'xdg-desktop-portal-hyprland',
        'hyprpicker',
        'hyprpolkitagent',
        'hyprpaper',
        'hyprlock',
        'qt5-wayland',
        'qt6-wayland',
        'gnome-themes-extra',
        'firefox',
        'nano',
        'flatpak',
        'nautilus',
        'vim',
        'gnome-calculator',
        'gnome-disk-utility',
        'gnome-text-editor',
        'gnome-system-monitor',
        'gnome-music',
        'eog',
        'waybar',
        'cliphist',
        'wl-clipboard',
        'rofi',
        'kitty',
        'python-pywal',
        'celluloid',
        'pavucontrol',
        'noto-fonts',
        'noto-fonts-emoji',
        'ttf-liberation',
        'ttf-jetbrains-mono',
        'ttf-jetbrains-mono-nerd',
        'fastfetch',
        'xdg-desktop-portal',
        'xdg-desktop-portal-gtk',
        'swaync',
        'pipewire',
        'pipewire-pulse',
        'wireplumber',
        'iwd',
        'networkmanager',
        'network-manager-applet',
        'ntfs-3g',
        'dosfstools',
        'fuse',
        'ufw'
    ],

    'Aur': [
        'hyprshot',
        'oh-my-posh-bin',
        'pinta',
        'nwg-look',
        'papirus-icon-theme',
        'bibata-cursor-theme-bin',
        'emote'
    ]
}

if do_nvidia_drivers:
    drivers = {
        'Pacman': [
            'nvidia',
            'nvidia-utils'
        ],

        'Aur': [

        ]
    }

    print('z')

    packages['Pacman'] += drivers['Pacman']
    packages['Aur'] += drivers['Aur']

pacman_parsed = ' '.join(packages['Pacman'])
aur_parsed = ' '.join(packages['Aur'])

os.system(f'sudo pacman -S --noconfirm --needed {pacman_parsed}')
os.system(f'paru -Sy && paru -S --noconfirm {aur_parsed}')


print(r'''
          ___         _        _ _ _                _     _    __ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   __| |___| |_ / _(_) |___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | / _` / _ \  _|  _| | / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \__,_\___/\__|_| |_|_\___/__/
                                         |___/
''' )

file_dir = pathlib.Path(__file__).parent.resolve()
home = pathlib.Path(os.path.expanduser('~')).resolve()
source_dir = file_dir / 'home'

def copy_with_replace(src, dst):
    try:
        if src.is_dir():
            if not dst.exists():
                dst.mkdir(parents=True)
            for item in src.iterdir():
                copy_with_replace(item, dst / item.name)
        else:
            shutil.copy2(src, dst, follow_symlinks=False)
    except Exception as e:
        pass

if source_dir.exists():
    for item in source_dir.iterdir():
        copy_with_replace(item, home / item.name)
    
    shutil.rmtree(source_dir, ignore_errors=True)


print(r'''
          ___        _     _         _        _ _                           _
         | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _ _ ___  __ ___ __| |_  _ _ _ ___ ___
         |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ '_/ _ \/ _/ -_) _` | || | '_/ -_|_-<
         |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/_| \___/\__\___\__,_|\_,_|_| \___/__/
                                                   |_|
''')

file_dir = pathlib.Path(__file__).parent.resolve()
home = os.getenv("HOME")

waybar_css = f'{home}/.config/waybar/style.css'
wallpapers_conf = f'{home}/.config/hypr/wallpapers.conf'
hyprpaper_conf = f'{home}/.config/hypr/hyprpaper.conf'
multilib_conf = '/etc/pacman.conf'

def numtobool(str):
    if str == '1':
        return True
    else:
        return False

# Waybar config
if not os.access(waybar_css, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {waybar_css} && chmod 644 {waybar_css}')

file = open(waybar_css, 'rb')
content = file.read().decode()
file.close()
file = open(waybar_css, 'wb')
file.write(content.replace('$HOME',home).encode())
file.close()



# Walpaper set
image = f'{home}/Wallpapers/wallpaper.jpg'

os.system(f'wal -i {image}')

if not os.access(wallpapers_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {wallpapers_conf} && chmod 644 {wallpapers_conf}')

file = open(wallpapers_conf,'wb')
file.write(f'$wallpaper = {image}'.encode())
file.close()

if not os.access(hyprpaper_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {hyprpaper_conf} && chmod 644 {hyprpaper_conf}')

file = open(hyprpaper_conf,'wb')
file.write(f'preload = {image}\nwallpaper = , {image}'.encode())
file.close()



# Multilib enable
try:
    if not os.access(multilib_conf, os.R_OK | os.W_OK):
        os.system(f'sudo chown $USER:$USER {multilib_conf} && chmod 644 {multilib_conf}')

    file = open(multilib_conf, 'rb')
    content = file.read().decode()
    file.close()
    file = open(multilib_conf, 'wb')
    file.write(content.replace('#[multilib]\n#Include = /etc/pacman.d/mirrorlist','[multilib]\nInclude = /etc/pacman.d/mirrorlist').encode())
    file.close()
except:
    pass



# Screenshare
os.system('sudo systemctl --user enable --now pipewire pipewire-pulse wireplumber')



# Network manager
os.system('sudo systemctl enable NetworkManager.service')



# Default dark mode
os.system("gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark")
os.system("gsettings set org.gnome.desktop.interface color-scheme prefer-dark")
os.system("gsettings set org.gnome.desktop.interface icon-theme Papirus")
os.system("gsettings set org.gnome.desktop.interface font-name 'Noto Sans Regular 11'")



# Reboot
if do_reboot:
    print('zzz')
    os.system('sudo reboot')