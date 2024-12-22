#!/bin/bash

# TODO, https://github.com/mendableai/firecrawl.git
# # # # This tool is a crawler, scrapper, that can get a lot of content converted into markdown, perfect to train LLMs

# # # set -e

# # # # Import logging functions and constants
# # # source "$(dirname "$0")/logs.sh"
# # # source "$(dirname "$0")/constants.sh"

# # # # Variables
# # # FIRECRAWL_DIR="$HOME/.firecrawl"
# # # FIRECRAWL_ENV="$FIRECRAWL_DIR/apps/api/.env"

# # # sudo -v # Ensure sudo privileges upfront

# # # # Step 1: Clone Firecrawl repository
# # # log "[MAI] Checking if Firecrawl is already installed..."
# # # if [ -d "$FIRECRAWL_DIR" ]; then
# # #     warn "[MAI] Firecrawl is already installed at $FIRECRAWL_DIR."
# # # else
# # #     log "[MAI] Cloning Firecrawl repository to $FIRECRAWL_DIR..."
# # #     git clone https://github.com/mendableai/firecrawl.git "$FIRECRAWL_DIR" || error "[ERROR] Failed to clone Firecrawl repository."
# # # fi

# # # # Step 2: Install or update Node.js
# # # log "[MAI] Installing or updating Node.js..."
# # # if ! command -v node &> /dev/null || [[ "$(node -v)" < "v18.12.0" ]]; then
# # #     sudo apt-get install -y curl
# # #     curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n
# # #     sudo bash n lts || error "[ERROR] Failed to install Node.js."
# # #     rm n
# # #     log "[MAI] Node.js updated to version: $(node -v)."
# # # else
# # #     log "[MAI] Node.js is already up to date ($(node -v))."
# # # fi

# # # # Step 3: Install PNPM
# # # log "[MAI] Installing PNPM..."
# # # if ! command -v pnpm &> /dev/null; then
# # #     npm install -g pnpm@9 || sudo npm install -g pnpm@9 || error "[ERROR] Failed to install PNPM."
# # #     log "[MAI] PNPM installed successfully."
# # # else
# # #     log "[MAI] PNPM is already installed ($(pnpm -v))."
# # # fi

# # # # Step 4: Install Redis
# # # log "[MAI] Installing Redis..."
# # # if ! command -v redis-server &> /dev/null; then
# # #     sudo apt update
# # #     sudo apt install -y redis || error "[ERROR] Failed to install Redis."
# # #     log "[MAI] Redis installed successfully."
# # # else
# # #     log "[MAI] Redis is already installed."
# # # fi

# # # # Step 5: Install Firecrawl dependencies
# # # log "[MAI] Installing Firecrawl dependencies..."
# # # cd "$FIRECRAWL_DIR/apps/api"
# # # pnpm install || error "[ERROR] Failed to install Firecrawl dependencies."

# # # # Step 6: Configure environment variables
# # # log "[MAI] Configuring environment variables..."
# # # if [ ! -f "$FIRECRAWL_ENV" ]; then
# # #     cp "$FIRECRAWL_DIR/apps/api/.env.example" "$FIRECRAWL_ENV"
# # #     sed -i 's/^NUM_WORKERS_PER_QUEUE=.*/NUM_WORKERS_PER_QUEUE=8/' "$FIRECRAWL_ENV"
# # #     sed -i 's/^PORT=.*/PORT=3002/' "$FIRECRAWL_ENV"
# # #     sed -i 's/^HOST=.*/HOST=0.0.0.0/' "$FIRECRAWL_ENV"
# # #     sed -i 's/^REDIS_URL=.*/REDIS_URL=redis:\/\/localhost:6379/' "$FIRECRAWL_ENV"
# # #     sed -i 's/^REDIS_RATE_LIMIT_URL=.*/REDIS_RATE_LIMIT_URL=redis:\/\/localhost:6379/' "$FIRECRAWL_ENV"
# # #     log "[MAI] Environment variables configured in $FIRECRAWL_ENV."
# # # else
# # #     warn "[MAI] .env file already exists at $FIRECRAWL_ENV."
# # # fi

# # # # Step 7: Start Redis server
# # # log "[MAI] Checking Redis server status..."
# # # if ! systemctl is-active --quiet redis-server; then
# # #     sudo systemctl enable redis-server
# # #     sudo systemctl start redis-server || error "[ERROR] Failed to start Redis server."
# # #     log "[MAI] Redis server started successfully."
# # # else
# # #     log "[MAI] Redis server is already running."
# # # fi

# # # # Step 8: Test the installation
# # # log "[MAI] Running Firecrawl tests..."
# # # if pnpm run test:local-no-auth; then
# # #     log "[MAI] Firecrawl tests passed successfully."
# # # else
# # #     warn "[MAI] Firecrawl tests failed. Please check the logs for details."
# # # fi

# # # # Completion
# # # log "[MAI] Firecrawl setup completed successfully!"
# # # log "Run the following commands to start Firecrawl services:"
# # # echo "1. Redis:      redis-server"
# # # echo "2. Workers:    cd $FIRECRAWL_DIR/apps/api && pnpm run workers"
# # # echo "3. Server:     cd $FIRECRAWL_DIR/apps/api && pnpm run start"
