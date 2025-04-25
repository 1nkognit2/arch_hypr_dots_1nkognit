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
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ~
sudo rm -rf paru
sleep 1

sudo pacman -S --noconfirm python
sleep 1

sudo python "$script_dir/install_packages.py"
python "$script_dir/install_homefiles.py"
sudo python "$script_dir/post_install.py"

kill $PID