#!/bin/bash

# Get the absolute path of the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if planes.py is running
if ! pgrep -f "${SCRIPT_DIR}/planes.py" > /dev/null; then
    echo "planes.py is not running. Restarting..."
    python3 "${SCRIPT_DIR}/planes.py" &
fi

# Check if planeconfig.py is running
if ! pgrep -f "${SCRIPT_DIR}/planeconfig.py" > /dev/null; then
    echo "planeconfig.py is not running. Restarting..."
    python3 "${SCRIPT_DIR}/planeconfig.py" &
fi
# make executible by running this from SSH: 
# chmod +x check_processes.sh
#then add the file below by running crontab -e and pasting this at the bottom 
#*/2 * * * * /path/to/planes/check_processes.sh >/dev/null 2>&1
