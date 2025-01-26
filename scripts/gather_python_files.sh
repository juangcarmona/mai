#!/bin/bash

# Check if folder path is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <folder_path>"
    exit 1
fi

# Define the folder to search and the output file
FOLDER_PATH="$1"
OUTPUT_FILE="python_files_content.txt"

# Clear the output file if it exists
> "$OUTPUT_FILE"

# Check if .gitignore exists and create an exclusion list
EXCLUDE_LIST=()
if [ -f "$FOLDER_PATH/.gitignore" ]; then
    while IFS= read -r line; do
        # Skip empty lines and comments
        if [[ -n "$line" && ! "$line" =~ ^\# ]]; then
            # Remove trailing slashes for directories
            line="${line%/}"
            EXCLUDE_LIST+=("$line")
        fi
    done < "$FOLDER_PATH/.gitignore"
fi

# Build the find command with exclusions
FIND_CMD="find '$FOLDER_PATH' -type f -name '*.py'"
for pattern in "${EXCLUDE_LIST[@]}"; do
    # Exclude both files and directories matching the pattern
    FIND_CMD+=" -not -path '$FOLDER_PATH/$pattern'"
    FIND_CMD+=" -not -path '$FOLDER_PATH/$pattern/*'"
done

# Execute the find command and process files
eval "$FIND_CMD" | while read -r file; do
    echo "=== $file ===" >> "$OUTPUT_FILE"
    cat "$file" >> "$OUTPUT_FILE"
    echo -e "\n\n" >> "$OUTPUT_FILE"
done

echo "Content of all Python files in '$FOLDER_PATH' (excluding .gitignore patterns) has been written to $OUTPUT_FILE"