sudo raspi-config nonint do_hostname StratuxHud
# Sets to auto-login, commandline
sudo raspi-config nonint do_boot_behaviour B2
sudo raspi-config nonint do_ssh 1
sudo raspi-config nonint get_config_var gpu_mem_128 /boot/config.txt
sudo apt-get update && sudo apt-get dist-upgrade -y
sudo apt install vim -y
sudo apt-get install python3-dev -y
sudo apt-get install libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev -y

# Make sure that everything is rebooted after changing the HW and OS config
sudo reboot now