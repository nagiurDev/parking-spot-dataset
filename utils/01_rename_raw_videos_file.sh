#!/bin/bash

directory="../data/raw_videos"

cd "$directory" || exit

for i in $(seq -f "%02g" 1 76); do

    for file in ${i}_*.mp4; do 

        if [[ -f "$file" ]]; then
            # Rename the file
            mv "$file" "${i}.mp4"
            echo "Renamed: $file to ${i}.mp4"
        fi
    done
done