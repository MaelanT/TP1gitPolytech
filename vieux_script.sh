#!/bin/sh
# Ancien script de sauvegarde, a remplacer un jour
tar czf backup.tar.gz menu.txt config.ini || exit 1
echo "sauvegarde terminee"
