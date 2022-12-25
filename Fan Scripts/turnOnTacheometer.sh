#/bin/bash
{
sudo sh -c 'echo 1 > /sys/class/hwmon/hwmon1/tach_enable' &&
echo "Turned on the tacheometer, here's the reading:"
bash ./speed.sh
} || {
echo "An error occurred"
}
