#!/bin/bash
# Program:
#       This program is get host Disk status
# Using:
#       watch -n 0.1 bash getDISK.sh
# History:
# 2016/06/18 Ellis Wu Release
#

CPULOG_1=$(cat /proc/stat | grep 'cpu ' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}')
SYS_IDLE_1=$(echo $CPULOG_1 | awk '{print $4+$5}')
Total_1=$(echo $CPULOG_1 | awk '{print $1+$2+$3+$4+$5+$6+$7}')

sleep 1

CPULOG_2=$(cat /proc/stat | grep 'cpu ' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}')
SYS_IDLE_2=$(echo $CPULOG_2 | awk '{print $4+$5}')
Total_2=$(echo $CPULOG_2 | awk '{print $1+$2+$3+$4+$5+$6+$7}')

SYS_IDLE=`expr $SYS_IDLE_2 - $SYS_IDLE_1`
Total=`expr $Total_2 - $Total_1`
SYS_USAGE=`expr $SYS_IDLE/$Total*100 |bc -l`
SYS_Rate=`expr 100-$SYS_USAGE |bc -l`
Disp_SYS_Rate=`expr "scale=3; $SYS_Rate/1" |bc`

echo $Disp_SYS_Rate%

