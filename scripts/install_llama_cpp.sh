#!/bin/bash

set -e

# Import logging functions and shared constants
source "$(dirname "$0")/logs.sh"
source "$(dirname "$0")/constants.sh"

install_llama_cpp() {
    local LLAMA_DIR="$MAI_DIR/llama.cpp"

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

    # Crear un directorio build y usar CMake
    mkdir -p build
    cd build

    log "Configuring build with CMake..."
    if command -v nvidia-smi &>/dev/null; then
        log "NVIDIA GPU detected, building with CUDA support..."
        cmake .. -DLLAMA_CUBLAS=off -DGGML_CUDA=on || error "CMake configuration failed for CUDA."
    else
        warn "No NVIDIA GPU detected. Building without CUDA support."
        cmake .. || error "CMake configuration failed."
    fi

    log "Compiling llama.cpp..."
    make || error "Failed to compile llama.cpp."

    log "llama.cpp compiled successfully. CLI and server binaries are available in $LLAMA_DIR/build."
}

install_llama_cpp
