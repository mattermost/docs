#!/bin/bash

# Directory paths
SOURCE_SCSS_DIR="source/_static/scss"
SOURCE_CSS_DIR="source/_static/css"
BUILD_CSS_DIR="build/html/_static/css"

# Start sass --watch in the background
sass --watch $SOURCE_SCSS_DIR:$SOURCE_CSS_DIR &

SASS_PID=$!

# Function to kill sass when script exits
cleanup() {
  echo "Stopping sass watch..."
  kill $SASS_PID
}

trap cleanup EXIT

# Loop to sync CSS changes
while true; do
  rsync -r $SOURCE_CSS_DIR/ $BUILD_CSS_DIR
  sleep 1 # Wait for 1 second before syncing again
done
