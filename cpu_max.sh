#usage:
#$sudo bash ./cpu_max.sh "max(by def)/min" "any governors,ondemand by default"

#!/bin/bash
cd /sys/devices/system/cpu


if [ "$2" != "" ] ; then
	governor="$2"
else
	governor="ondemand"
fi

if [ "$1" == "min" ] ; then
	newSpeedTop=`awk '{print $1}' ./cpu0/cpufreq/cpuinfo_min_freq`
	newSpeedLow=$newSpeedTop
else
	newSpeedTop=`awk '{print $1}' ./cpu0/cpufreq/cpuinfo_max_freq`
        newSpeedLow=$newSpeedTop
fi

for c in ./cpu[0-63]* ; do
	echo $newSpeedTop | sudo tee ${c}/cpufreq/scaling_max_freq
	echo $newSpeedLow | sudo tee ${c}/cpufreq/scaling_min_freq
	echo $governor | sudo tee ${c}/cpufreq/scaling_governor
done
