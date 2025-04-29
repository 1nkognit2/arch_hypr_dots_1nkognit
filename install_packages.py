import os

packages = {
    'Pacman': [
        'gtk3',
        'gtk4',
        'hyprland',
        'xdg-desktop-portal-hyprland',
        'hyprpicker',
        'hyprpaper',
        'qt5-wayland',
        'qt6-wayland',
        'gnome-themes-extra',
        'firefox',
        'nano',
        'flatpak',
        'nautilus',
        'polkit-gnome',
        'gnome-calculator',
        'gnome-disk-utility',
        'gnome-text-editor',
        'gnome-system-monitor',
        'gnome-music',
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
        'solaar',
        'discord',
        'telegram-desktop',
        'networkmanager',
        'network-manager-applet',
        'ntfs-3g',
        'dosfstools',
        'fuse',
        'nvidia',
        'nvidia-utils'
    ],

    'Aur': [
        'hyprshot',
        'oh-my-posh-bin',
        'nwg-look',
        'papirus-icon-theme',
        'bibata-cursor-theme-bin'
    ]
}

pacman_parsed = ' '.join(packages['Pacman'])
aur_parsed = ' '.join(packages['Aur'])

os.system(f'sudo pacman -S --noconfirm --needed {pacman_parsed}')
os.system(f'paru -Sy && paru -S --noconfirm {aur_parsed}')