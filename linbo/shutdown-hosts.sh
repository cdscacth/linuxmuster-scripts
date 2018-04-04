#!/bin/bash
# wake hosts if they are in S4 / Suspend-Mode
echo "Shutdown all hosts in Linbo..."
linbo-remote -r a103 -c halt
linbo-remote -g compaq -c halt
echo "Wake hosts that are in suspend mode..."
linbo-remote -r a103 -w 0
# wait for hosts to get an IP
echo "Waiting 40s..."
sleep 40
# shutdown hosts
echo "Shutdown all other hosts, that are online..."
for HOST in $(cat /etc/linuxmuster/workstations | grep -v -E 'admin|rpi|printer|aps|teacher|staff' | cut -d ";" -f 5)
do
  if ping -c 1 $HOST -w1 >/dev/null
    then
      ssh -o StrictHostKeyChecking=no $HOST shutdown -h now >/dev/null
  fi
done
# Shutdown all hosts we accidently waked up to Linbo
linbo-remote -r a103 -c halt
echo "Done"
