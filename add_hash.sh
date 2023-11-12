#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
    echo "File not found: $file"
    exit 1
fi

# Prompt for start and end line numbers
read -p "Start line (press Enter for the beginning): " start
read -p "End line (press Enter for the end): " end

# If no start and end values are provided, add "#" to every line
if [ -z "$start" ]; then
    sed -i 's/^/#/' "$file"
else
    # Add "#" only to the specified range of lines
    sed -i "${start},${end}s/^/#/" "$file"
fi

echo "Hash symbols added to specified lines in $file"
