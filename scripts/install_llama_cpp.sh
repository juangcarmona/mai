#!/bin/bash

set -e

# Import logging functions and shared constants
source "$(dirname "$0")/logs.sh"
source "$(dirname "$0")/constants.sh"

# Function to install llama.cpp
install_llama_cpp() {
    local LLAMA_DIR="$MAI_DIR/llama.cpp"

    # Ensure cmake is installed
    log "Ensuring cmake is installed..."
    if ! command -v cmake &>/dev/null; then
        log "cmake not found. Installing..."
        sudo apt-get update
        sudo apt-get install -y cmake build-essential || error "Failed to install cmake."
    else
        log "cmake is already installed."
    fi

    log "Cloning llama.cpp repository to $LLAMA_DIR..."
    if [ -d "$LLAMA_DIR" ]; then
        warn "llama.cpp repository already exists at $LLAMA_DIR. Pulling latest changes..."
        cd "$LLAMA_DIR"
        git pull || error "Failed to update llama.cpp repository."
    else
        git clone https://github.com/ggerganov/llama.cpp.git "$LLAMA_DIR" || error "Failed to clone llama.cpp repository."
    fi

    log "Building llama.cpp..."
    cd "$LLAMA_DIR"
    mkdir -p build
    cd build
    if command -v nvidia-smi &>/dev/null; then
        log "NVIDIA GPU detected, building with CUDA support..."
        cmake .. -DGGML_CUDA=on || error "CMake configuration failed for CUDA."
    else
        warn "No NVIDIA GPU detected, building without CUDA support..."
        cmake .. || error "CMake configuration failed."
    fi
    make || error "Failed to build llama.cpp."

    log "llama.cpp installed successfully at $LLAMA_DIR."
}

install_llama_cpp
