#!/bin/bash
echo "Mounting NAS"
sudo mount -t cifs -o username=$NAS_USER,vers=3.0,iocharset=utf8,file_mode=0777,dir_mode=0777 //$NAS_IP/homes /mnt/samba && echo "NAS has been mounted :)"
# nitrogen --restore
