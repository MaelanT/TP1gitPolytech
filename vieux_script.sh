#!/bin/sh
# Script de sauvegarde ameliore : archive horodatee
DATE=$(date +%Y%m%d)
tar czf "backup-$DATE.tar.gz" menu.txt config.ini src/
echo "sauvegarde $DATE terminee"
