import os

packages = {
    'Pacman': [
        'gtk3',
        'gtk4',
        'hyprpolkitagent',
        'qt5-wayland',
        'qt6-wayland',
        'gnome-themes-extra',
        'hyprland',
        'firefox',
        'go',
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
        'hyprpaper',
        'rofi',
        'kitty',
        'python-pywal',
        'celluloid',
        'pavucontrol',
        'noto-fonts',
        'ttf-jetbrains-mono',
        'ttf-jetbrains-mono-nerd',
        'fastfetch',
        'xdg-desktop-portal',
        'xdg-desktop-portal-gtk',
        'swaync',
        'pipewire',
        'pipewire-pulse',
        'wireplumber',
        'xdg-desktop-portal-hyprland',
        'iwd',
        'networkmanager',
        'network-manager-applet'
    ],

    'Aur': [
        'oh-my-posh-bin',
        'hyprpicker',
        'hyprshot',
        'pinta',
        'nwg-look',
        'papirus-icon-theme',
        'bibata-cursor-theme'
    ]
}

dialog = input('Install Nvidia drivers? [Y/n] ')

if dialog.lower() == 'y' or dialog == '':
    drivers = {
        'Pacman': [
            'nvidia',
            'nvidia-utils'
        ],

        'Aur': [

        ]
    }

    packages['Pacman'] += drivers['Pacman']
    packages['Aur'] += drivers['Aur']

pacman_parsed = ' '.join(packages['Pacman'])
aur_parsed = ' '.join(packages['Aur'])

os.system(f'sudo pacman -S --noconfirm --needed {pacman_parsed}')
os.system(f'paru -S --noconfirm {aur_parsed}')