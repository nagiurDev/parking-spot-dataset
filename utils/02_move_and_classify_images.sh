#!/bin/bash

# Directory paths
base_dir="../data/extracted_frames"
target_dir="../data/annotations/ready_to_annotate"


read -p "Enter the directories: " -a selected_directories


for cur_dir in "${selected_directories[@]}"; do
    
    cur_target_dir="$target_dir/$cur_dir"

    # Check if the current directory already exists in the target directory
    if [ -d "$cur_target_dir" ]; then
        read -p "Directory $cur_dir already exists. Do you want to delete old images and move new images? (y/n): " response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            rm -rf "$cur_target_dir/to_manual/" "$cur_target_dir/to_model/"
            echo "Old images deleted."
        else
            echo "Skipping $cur_dir."
            continue  
        fi
    else
        # Create the directories if they do not exist
        mkdir -p "$cur_target_dir/to_manual"
        mkdir -p "$cur_target_dir/to_model"
    fi

    # Create necessary directories
    mkdir -p "$cur_target_dir/to_manual"
    mkdir -p "$cur_target_dir/to_model"

    image_files=("$base_dir/$cur_dir"/*.jpg) 
    total_files=${#image_files[@]}

    echo
    echo "Directory: $cur_dir"
    echo "--------------"
    echo "Total: $total_files images"

    read -p "Percentage(%) for manual-annotation: " percentage_manual
    num_manual=$((total_files * $percentage_manual/100))

    echo "Manual: $num_manual images"
    echo "Model: $((total_files - num_manual)) images"
    echo 

    # Shuffle the list of images
    shuffled_images=($(printf "%s\n" "${image_files[@]}" | sort -R))

    count=0
    for file in "${shuffled_images[@]}"; do
        if (( count < num_manual )); then
            cp "$file" "$target_dir/$cur_dir/to_manual/"
        else
            cp "$file" "$target_dir/$cur_dir/to_model/"
        fi
        count=$((count + 1))
    done

done

