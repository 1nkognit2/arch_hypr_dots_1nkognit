cat << "EOF"
  _____           _        _ _           
 |_   _|         | |      | | |          
   | |  _ __  ___| |_ __ _| | | ___ _ __ 
   | | | '_ \/ __| __/ _` | | |/ _ \ '__|
  _| |_| | | \__ \ || (_| | | |  __/ |   
 |_____|_| |_|___/\__\__,_|_|_|\___|_|   

        Made by Vova_4104
EOF

script_dir=$(dirname "$(realpath "$0")")

sudo -v

(
    while true; do
        sleep 600
        sudo -v
    done
) &
PID=$!

sleep 1



cat << "EOF"
          ___         _        _ _ _                                 
         |_ _|_ _  __| |_ __ _| | (_)_ _  __ _   _ __  __ _ _ _ _  _ 
          | || ' \(_-<  _/ _` | | | | ' \/ _` | | '_ \/ _` | '_| || |
         |___|_||_/__/\__\__,_|_|_|_|_||_\__, | | .__/\__,_|_|  \_,_|
                                         |___/  |_|                  
EOF
cd ~
git clone --depth 1 https://aur.archlinux.org/paru-bin.git
cd paru-bin
makepkg -si --noconfirm
cd ~
sudo rm -rf paru-bin
sleep 1

cat << "EOF"
  ___        _     _         _        _ _             _   _             
 | _ \___ __| |_  (_)_ _  __| |_ __ _| | |  _ __ _  _| |_| |_  ___ _ _  
 |  _/ _ (_-<  _| | | ' \(_-<  _/ _` | | | | '_ \ || |  _| ' \/ _ \ ' \ 
 |_| \___/__/\__| |_|_||_/__/\__\__,_|_|_| | .__/\_, |\__|_||_\___/_||_|
                                           |_|   |__/                   
EOF
sudo pacman -S --noconfirm python
sleep 1

python "$script_dir/installv2.py"