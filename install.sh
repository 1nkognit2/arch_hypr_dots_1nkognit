script_dir=$(dirname "$(realpath "$0")")

echo "~~~INSTALL SCRIPT~~~"
sleep 1

echo "    Installing paru"
cd ~
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ~
sudo rm -rf paru
echo "    Paru installed"
sleep 1
echo ""

echo "    Installing python"
sudo pacman -S --noconfirm python
echo "    Python installed"
sleep 1
echo ""

echo "    Installing Packages"
python "$script_dir/install_packages.py"
echo "    Packages installed"
sleep 1
echo ""

echo "    Installing configs"
python "$script_dir/install_homefiles.py"
echo "    Configs installed"
sleep 1
echo ""

echo "    Post-installing"
python "$script_dir/post_install.py"