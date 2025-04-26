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

cd ~
git clone --depth 1 https://aur.archlinux.org/paru-bin.git
cd paru-bin
makepkg -si --noconfirm
cd ~
sudo rm -rf paru-bin
sleep 1

sudo pacman -S --noconfirm python
sleep 1

python "$script_dir/install_packages.py"
python "$script_dir/install_homefiles.py"
python "$script_dir/post_install.py"