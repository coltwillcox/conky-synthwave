if [ "$XDG_CURRENT_DESKTOP" = "XFCE" ]; then
	while ! pidof xfdesktop >>/dev/null;
		do
			sleep 1
		done
fi
if [ ! -e "/home/$USER/.cache/fontconfig" ]; then
	fc-cache -r /usr/share/fonts/extra
fi
sleep 5
killall conky
conky -c /home/user/.conky/conky-synthwave/.conkyrc & conky -c /home/user/.conky/conky-synthwave/.conky_cal & conky -c /home/user/.conky/conky-synthwave/.conky_clock & conky -c /home/user/.conky/conky-synthwave/.conky_gmail & conky -c /home/user/.conky/conky-synthwave/.conky_mpd & conky -c /home/user/.conky/conky-synthwave/.conky_rss & conky -c /home/user/.conky/conky-synthwave/.conky_speed & conky -c /home/user/.conky/conky-synthwave/.conky_stod & conky -c /home/user/.conky/conky-synthwave/.conky_tor & conky -c /home/user/.conky/conky-synthwave/.conky_weather
