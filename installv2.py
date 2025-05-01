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

drivers = {
    'Nvidia': [
        'nvidia-dkms',
        'nvidia-utils',
        'lib32-nvidia-utils',
        'vulkan-icd-loader',
        'lib32-vulkan-icd-loader'
    ],

    'AMD' : [
        'mesa',
        'lib32-mesa',
        'vulkan-radeon',
        'lib32-vulkan-radeon',
        'libva-mesa-driver',
        'lib32-libva-mesa-driver',
        'mesa-vdpau',
        'lib32-mesa-vdpau'
    ],

    'Intel': [
        'mesa',
        'lib32-mesa',
        'vulkan-intel',
        'lib32-vulkan-intel',
        'intel-media-sdk',
        'libva-intel-driver',
        'lib32-libva-intel-driver'
    ],
    
    'Do not install GPU driver': [

    ]
}

for i, x in enumerate(drivers):
    print(f'{i+1}: {x}')

while 1:
    try:
        gpu_type = int(input('Enter your GPU manifacturer to install drivers: '))
        if gpu_type-1 in [i for i, x in enumerate(drivers)]:
            selected_drivers = drivers[[x for i, x in enumerate(drivers)][gpu_type-1]]
            break
    except:
        pass

do_ly_dm = dialog('Do you want to install Ly DM?', True)
do_reboot = dialog('Do you want to reboot after install?', True)



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
        'noto-fonts-extra'
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
        'ufw',
        'grim',
        'slurp',
        'swappy',
        'playerctl',
        'libnotify'
    ],

    'Aur': [
        'oh-my-posh-bin',
        'pinta',
        'nwg-look',
        'papirus-icon-theme',
        'bibata-cursor-theme-bin',
        'emote'
    ]
}

packages['Pacman'] += selected_drivers

if do_ly_dm:
    packages['Pacman'].append('ly')

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
home = os.getenv('HOME')

waybar_css = f'{home}/.config/waybar/style.css'
wallpapers_conf = f'{home}/.config/hypr/wallpapers.conf'
hyprpaper_conf = f'{home}/.config/hypr/hyprpaper.conf'
multilib_conf = '/etc/pacman.conf'

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



# Ly dm

if do_ly_dm:
    os.system('sudo systemctl enable ly')



# Reboot
if do_reboot:
    print('zzz')
    os.system('sudo reboot')