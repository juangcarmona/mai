#!/bin/bash

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[38;5;214m'
BLUE='\033[38;5;31m'
NC='\033[0m'

MAGENTA='\033[0;35m'
CYAN='\033[0;36m'

# Logging functions
log() {
    echo -e "${GREEN}[MAI]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}
