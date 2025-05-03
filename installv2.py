import os
import pathlib
import shutil
from modules.install_packages import install_packages
from modules.install_homefiles import install_homefiles
from modules.post_install import post_install

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

selected_drivers = drivers['Nvidia']

do_ly_dm = False
do_reboot = True 



print(r'''
          ___         _        _ _ _                           _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ __| |____ _ __ _ ___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` / _| / / _` / _` / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_\__|_\_\__,_\__, \___/__/
                                         |___/  |_|                    |___/
''')

install_packages(selected_drivers, do_ly_dm)

print(r'''
          ___         _        _ _ _                _     _    __ _ _
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   __| |___| |_ / _(_) |___ ___
          | || ' \(_-<  _/ _` | | | | ' \/ _` | / _` / _ \  _|  _| | / -_|_-<
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | \__,_\___/\__|_| |_|_\___/__/
                                         |___/
''' )

install_homefiles()

print(r'''
          ___        _     _         _        _ _                           _
         | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _ _ ___  __ ___ __| |_  _ _ _ ___ ___
         |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ '_/ _ \/ _/ -_) _` | || | '_/ -_|_-<
         |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/_| \___/\__\___\__,_|\_,_|_| \___/__/
                                                   |_|
''')

post_install(do_reboot, do_ly_dm)