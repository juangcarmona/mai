#!/bin/bash

set -e

# Import logging functions and shared constants
source "$(dirname "$0")/logs.sh"
source "$(dirname "$0")/constants.sh"

# Function to install NVIDIA CUDA Toolkit
install_cuda() {
    log "Updating package list..."
    sudo apt-get update -y

    log "Installing prerequisites..."
    sudo apt-get install -y build-essential dkms || error "Failed to install prerequisites."

    log "Adding NVIDIA package repository..."
    TEMP_FILE="$MAI_TEMP/cuda-keyring_1.1-1_all.deb"
    wget -O "$TEMP_FILE" https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb || error "Failed to download NVIDIA package repository."
    sudo dpkg -i "$TEMP_FILE" || error "Failed to add NVIDIA package repository."

    log "Installing CUDA Toolkit..."
    sudo apt-get update -y
    sudo apt-get install -y cuda-toolkit-12-5 || error "Failed to install CUDA Toolkit."

    log "CUDA Toolkit installed successfully."
}

install_cuda