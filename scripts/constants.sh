#!/bin/bash

# Shared constants
export MAI_DIR="$HOME/.mai"
export VENV_DIR="$MAI_DIR/venv"
export MAI_TEMP="$HOME/.mai_temp"
export ZSHRC="$HOME/.zshrc"

# Ensure directories exist
mkdir -p "$MAI_DIR" "$MAI_TEMP"
