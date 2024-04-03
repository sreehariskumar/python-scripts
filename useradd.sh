#!/bin/bash

# Check if the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 
    exit 1
fi

# Prompt for username
echo "Enter Username:"
read username

# Check if the username already exists
if id "$username" &>/dev/null; then
    echo "User $username already exists."
    exit 1
fi

# Add the user
useradd -m -s /bin/bash "$username"
if [ $? -ne 0 ]; then
    echo "Failed to create user $username."
    exit 1
fi

# Set password for the user
echo "Enter password for the user $username:"
passwd "$username"
if [ $? -ne 0 ]; then
    echo "Failed to set password for user $username."
    exit 1
fi

echo "User $username created successfully."
