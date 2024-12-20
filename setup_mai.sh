#!/bin/bash

set -e

# Determine the root directory of the project
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$ROOT_DIR/scripts"

# Import logging functions and shared constants
source "$SCRIPTS_DIR/logs.sh"
source "$SCRIPTS_DIR/constants.sh"

# Function to execute a script and check for errors
run_script() {
    local script_path=$1
    log "Executing: $script_path..."
    if bash "$script_path"; then
        log "$script_path executed successfully."
    else
        error "Error occurred while executing $script_path. Exiting."
    fi
}

# Define script paths
INSTALL_ZSH="$SCRIPTS_DIR/install_zsh.sh"
INSTALL_CUDA="$SCRIPTS_DIR/install_cuda.sh"
INSTALL_LLAMA_CPP="$SCRIPTS_DIR/install_llama_cpp.sh"
INSTALL_LLAMA_CPP_PYTHON="$SCRIPTS_DIR/install_llama_cpp_python.sh"
CONFIGURE_ENVIRONMENT="$SCRIPTS_DIR/configure_environment.sh"

# Print banner
print_banner() {
    echo -e "${BLUE}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║               MAI Installer               ║"
    echo "║         My Artificial Intelligence        ║"
    echo "╚═══════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Main execution
main() {
    print_banner

    log "Starting MAI setup..."
    run_script "$INSTALL_ZSH"
    run_script "$INSTALL_CUDA"
    run_script "$INSTALL_LLAMA_CPP"
    run_script "$INSTALL_LLAMA_CPP_PYTHON"
    run_script "$CONFIGURE_ENVIRONMENT"

    echo -e "${BLUE}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║       MAI setup completed successfully!   ║"
    echo "╚═══════════════════════════════════════════╝"
    echo -e "${NC}"

    warn "Please restart your terminal or run 'source ~/.zshrc' to apply environment changes."
}

main
