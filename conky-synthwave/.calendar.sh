#! /bin/bash
cal_var=`date +%_d`;
gcal --starting-day=1 | sed s/"\(^\|[^0-9]\)$cal_var"'\b'/'\1${font Luculent:bold:pixelsize=12}${color2}'"$cal_var"'${font}${color}'/ | sed ':a;N;$!ba;s/\n/\n /g'