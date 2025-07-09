#!/bin/bash

# Air-Gap Docker Registry Setup for Mattermost Calls Offloader
# This script sets up a local Docker registry and pre-loads required images
# for air-gapped network deployments
#
# Usage: ./air-gap-docker-registry-setup.sh <recorder-version> <transcriber-version>
# Example: ./air-gap-docker-registry-setup.sh v0.8.5 v0.6.3

set -e

# Function to display usage
usage() {
    echo "Usage: $0 <recorder-version> <transcriber-version>"
    echo ""
    echo "Arguments:"
    echo "  recorder-version    Version of mattermost/calls-recorder image (e.g., v0.8.5)"
    echo "  transcriber-version Version of mattermost/calls-transcriber image (e.g., v0.6.3)"
    echo ""
    echo "Examples:"
    echo "  $0 v0.8.5 v0.6.3"
    echo "  $0 v0.9.0 v0.7.0"
    echo ""
    echo "To find the correct versions for your Calls plugin:"
    echo "1. Check your Calls plugin version in System Console > Plugins > Plugin Management"
    echo "2. Visit: https://github.com/mattermost/mattermost-plugin-calls/blob/v<YOUR_VERSION>/plugin.json"
    echo "3. Look for 'RecorderImage' and 'TranscriberImage' entries (near the bottom)"
    echo ""
    echo "Environment variables (optional):"
    echo "  REGISTRY_HOST       Docker registry host (default: localhost)"
    echo "  REGISTRY_PORT       Docker registry port (default: 5000)"
    echo "  REGISTRY_DATA_DIR   Registry data directory (default: /opt/docker-registry/data)"
    exit 1
}

# Check if required arguments are provided
if [ $# -ne 2 ]; then
    echo "ERROR: Missing required arguments"
    echo ""
    usage
fi

# Validate version format (should start with 'v' followed by semantic version)
validate_version() {
    local version=$1
    local image_name=$2
    
    if [[ ! $version =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "ERROR: Invalid version format for $image_name: $version"
        echo "Expected format: vX.Y.Z (e.g., v0.8.5)"
        exit 1
    fi
}

# Parse and validate arguments
CALLS_RECORDER_VERSION="$1"
CALLS_TRANSCRIBER_VERSION="$2"

validate_version "$CALLS_RECORDER_VERSION" "calls-recorder"
validate_version "$CALLS_TRANSCRIBER_VERSION" "calls-transcriber"

# Configuration variables
REGISTRY_HOST="${REGISTRY_HOST:-localhost}"
REGISTRY_PORT="${REGISTRY_PORT:-5000}"
REGISTRY_DATA_DIR="${REGISTRY_DATA_DIR:-/opt/docker-registry/data}"
REGISTRY_CONFIG_DIR="${REGISTRY_CONFIG_DIR:-/opt/docker-registry/config}"

LOG_FILE=/tmp/air-gap-registry-setup.log

echo "Setting up Air-Gap Docker Registry for Mattermost Calls" | tee $LOG_FILE
echo "Recorder version: $CALLS_RECORDER_VERSION" | tee -a $LOG_FILE
echo "Transcriber version: $CALLS_TRANSCRIBER_VERSION" | tee -a $LOG_FILE

# Function to check if running with internet access (for image pulling phase)
check_internet() {
    if ! curl -s --connect-timeout 5 https://hub.docker.com > /dev/null 2>&1; then
        echo "ERROR: This script requires internet access during the image preparation phase." | tee -a $LOG_FILE
        echo "Please run this script on a machine with internet access first, then transfer the images." | tee -a $LOG_FILE
        return 1
    fi
}

# Function to setup local Docker registry
setup_registry() {
    echo "Setting up local Docker registry..." | tee -a $LOG_FILE
    
    # Create directories
    sudo mkdir -p $REGISTRY_DATA_DIR
    sudo mkdir -p $REGISTRY_CONFIG_DIR
    
    # Create registry configuration
    cat > /tmp/registry-config.yml << EOF
version: 0.1
log:
  level: info
storage:
  filesystem:
    rootdirectory: /var/lib/registry
http:
  addr: 0.0.0.0:5000
  headers:
    X-Content-Type-Options: [nosniff]
EOF
    
    sudo mv /tmp/registry-config.yml $REGISTRY_CONFIG_DIR/config.yml
    
    # Pull and run registry container
    echo "Starting Docker registry container..." | tee -a $LOG_FILE
    docker pull registry:2 >> $LOG_FILE 2>&1
    
    # Stop existing registry if running
    docker stop local-registry 2>/dev/null || true
    docker rm local-registry 2>/dev/null || true
    
    # Start registry container
    docker run -d \
        --name local-registry \
        --restart=always \
        -p $REGISTRY_PORT:5000 \
        -v $REGISTRY_DATA_DIR:/var/lib/registry \
        -v $REGISTRY_CONFIG_DIR/config.yml:/etc/docker/registry/config.yml \
        registry:2 >> $LOG_FILE 2>&1
    
    # Wait for registry to be ready
    echo "Waiting for registry to be ready..." | tee -a $LOG_FILE
    sleep 10
    
    # Test registry
    if curl -s http://$REGISTRY_HOST:$REGISTRY_PORT/v2/ > /dev/null; then
        echo "Local Docker registry is running at $REGISTRY_HOST:$REGISTRY_PORT" | tee -a $LOG_FILE
    else
        echo "ERROR: Failed to start local Docker registry" | tee -a $LOG_FILE
        return 1
    fi
}

# Function to download and push Mattermost images
setup_mattermost_images() {
    echo "Downloading and pushing Mattermost Calls images..." | tee -a $LOG_FILE
    
    # Images to process
    declare -A IMAGES=(
        ["mattermost/calls-recorder"]="$CALLS_RECORDER_VERSION"
        ["mattermost/calls-transcriber"]="$CALLS_TRANSCRIBER_VERSION"
    )
    
    for image in "${!IMAGES[@]}"; do
        version="${IMAGES[$image]}"
        echo "Processing $image:$version..." | tee -a $LOG_FILE
        
        # Pull from Docker Hub
        echo "  Pulling $image:$version from Docker Hub..." | tee -a $LOG_FILE
        docker pull $image:$version >> $LOG_FILE 2>&1
        
        # Tag for local registry
        local_tag="$REGISTRY_HOST:$REGISTRY_PORT/$image:$version"
        echo "  Tagging as $local_tag..." | tee -a $LOG_FILE
        docker tag $image:$version $local_tag >> $LOG_FILE 2>&1
        
        # Push to local registry
        echo "  Pushing to local registry..." | tee -a $LOG_FILE
        docker push $local_tag >> $LOG_FILE 2>&1
        
        # Also tag as 'latest' for convenience
        if [ "$version" != "latest" ]; then
            latest_tag="$REGISTRY_HOST:$REGISTRY_PORT/$image:latest"
            docker tag $image:$version $latest_tag >> $LOG_FILE 2>&1
            docker push $latest_tag >> $LOG_FILE 2>&1
        fi
        
        echo "  Successfully pushed $image:$version to local registry" | tee -a $LOG_FILE
    done
    
    # Create registry data archive for transfer
    echo "Creating registry data archive..." | tee -a $LOG_FILE
    sudo tar -czf docker-registry-data.tar.gz -C $REGISTRY_DATA_DIR .
    
    # Create registry container image archive
    echo "Creating registry container image archive..." | tee -a $LOG_FILE
    docker save -o registry-image.tar registry:2
    gzip registry-image.tar
    
    echo "Created archives for air-gap transfer:" | tee -a $LOG_FILE
    echo "  - docker-registry-data.tar.gz" | tee -a $LOG_FILE
    echo "  - registry-image.tar.gz" | tee -a $LOG_FILE
}

# Function to configure calls-offloader for local registry
configure_calls_offloader() {
    echo "Configuring calls-offloader for local registry..." | tee -a $LOG_FILE
    
    # Create a modified calls-offloader config
    if [ -f "/opt/calls-offloader/calls-offloader.toml" ]; then
        sudo cp /opt/calls-offloader/calls-offloader.toml /opt/calls-offloader/calls-offloader.toml.backup
        
        # Update image_registry setting
        sudo sed -i "s/image_registry = \"mattermost\"/image_registry = \"$REGISTRY_HOST:$REGISTRY_PORT\/mattermost\"/" /opt/calls-offloader/calls-offloader.toml
        
        echo "Updated calls-offloader configuration to use local registry" | tee -a $LOG_FILE
        echo "Backup created at /opt/calls-offloader/calls-offloader.toml.backup" | tee -a $LOG_FILE
    else
        echo "Warning: calls-offloader.toml not found. You'll need to manually configure:" | tee -a $LOG_FILE
        echo "  image_registry = \"$REGISTRY_HOST:$REGISTRY_PORT/mattermost\"" | tee -a $LOG_FILE
    fi
}

# Function to create docker daemon configuration for insecure registry
configure_docker_daemon() {
    echo "Configuring Docker daemon for insecure registry..." | tee -a $LOG_FILE
    
    # Create or update Docker daemon configuration
    sudo mkdir -p /etc/docker
    
    # Check if daemon.json exists
    if [ -f "/etc/docker/daemon.json" ]; then
        sudo cp /etc/docker/daemon.json /etc/docker/daemon.json.backup
        echo "Backed up existing daemon.json" | tee -a $LOG_FILE
    fi
    
    # Create new daemon.json with insecure registry configuration
    cat > /tmp/daemon.json << EOF
{
    "insecure-registries": ["$REGISTRY_HOST:$REGISTRY_PORT"]
}
EOF
    
    sudo mv /tmp/daemon.json /etc/docker/daemon.json
    
    # Restart Docker daemon
    echo "Restarting Docker daemon..." | tee -a $LOG_FILE
    sudo systemctl restart docker >> $LOG_FILE 2>&1
    
    # Wait for Docker to restart
    sleep 10
    
    echo "Docker daemon configured for insecure registry access" | tee -a $LOG_FILE
}

# Function to verify setup
verify_setup() {
    echo "Verifying air-gap setup..." | tee -a $LOG_FILE
    
    # Check registry is accessible
    if curl -s http://$REGISTRY_HOST:$REGISTRY_PORT/v2/_catalog | grep -q repositories; then
        echo "✓ Local registry is accessible" | tee -a $LOG_FILE
    else
        echo "✗ Local registry is not accessible" | tee -a $LOG_FILE
        return 1
    fi
    
    # List available images
    echo "Available images in local registry:" | tee -a $LOG_FILE
    curl -s http://$REGISTRY_HOST:$REGISTRY_PORT/v2/_catalog | jq '.repositories[]' 2>/dev/null || echo "Could not list repositories (jq not available)" | tee -a $LOG_FILE
    
    # Test pulling from local registry
    test_image="$REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-offloader:latest"
    echo "Testing pull from local registry: $test_image" | tee -a $LOG_FILE
    if docker pull $test_image >> $LOG_FILE 2>&1; then
        echo "✓ Successfully pulled test image from local registry" | tee -a $LOG_FILE
    else
        echo "✗ Failed to pull test image from local registry" | tee -a $LOG_FILE
        return 1
    fi
}

# Function to create air-gap deployment script
create_airgap_deployment_script() {
    echo "Creating air-gap deployment script..." | tee -a $LOG_FILE
    
    cat > /tmp/deploy-airgap-calls.sh << 'EOF'
#!/bin/bash

# Air-Gap Calls Deployment Script
# Run this script on the air-gapped network after setting up the local registry

REGISTRY_HOST="${REGISTRY_HOST:-localhost}"
REGISTRY_PORT="${REGISTRY_PORT:-5000}"

echo "Deploying Mattermost Calls in air-gapped environment..."

# Configure Docker for local registry
sudo mkdir -p /etc/docker
cat > /tmp/daemon.json << EOD
{
    "insecure-registries": ["$REGISTRY_HOST:$REGISTRY_PORT"]
}
EOD
sudo mv /tmp/daemon.json /etc/docker/daemon.json
sudo systemctl restart docker
sleep 10

# Update calls-offloader configuration
if [ -f "/opt/calls-offloader/calls-offloader.toml" ]; then
    sudo sed -i "s/image_registry = \"mattermost\"/image_registry = \"$REGISTRY_HOST:$REGISTRY_PORT\/mattermost\"/" /opt/calls-offloader/calls-offloader.toml
    
    # Restart calls-offloader service
    sudo systemctl restart calls-offloader
    
    echo "Calls-offloader configured for air-gap deployment"
else
    echo "Warning: /opt/calls-offloader/calls-offloader.toml not found"
    echo "Please manually configure image_registry = \"$REGISTRY_HOST:$REGISTRY_PORT/mattermost\""
fi

echo "Air-gap deployment configuration complete"
echo ""
echo "IMPORTANT: Additional configuration required on Mattermost server:"
echo "On your Mattermost server, add this environment variable:"
echo "  MM_CALLS_JOB_SERVICE_IMAGE_REGISTRY=\"$REGISTRY_HOST:$REGISTRY_PORT/mattermost\""
echo ""
echo "Add it to /opt/mattermost/config/mattermost.environment and restart Mattermost:"
echo "  echo 'MM_CALLS_JOB_SERVICE_IMAGE_REGISTRY=\"$REGISTRY_HOST:$REGISTRY_PORT/mattermost\"' | sudo tee -a /opt/mattermost/config/mattermost.environment"
echo "  sudo systemctl restart mattermost"
EOF
    
    chmod +x /tmp/deploy-airgap-calls.sh
    mv /tmp/deploy-airgap-calls.sh ./deploy-airgap-calls.sh
    
    echo "Air-gap deployment script created at ./deploy-airgap-calls.sh" | tee -a $LOG_FILE
}

# Main execution
main() {
    echo "Starting air-gap Docker registry setup..." | tee -a $LOG_FILE
    
    # Check if we have internet access for image pulling
    if ! check_internet; then
        echo "Skipping image download phase - run this script with internet access first" | tee -a $LOG_FILE
    else
        # Setup local registry
        setup_registry
        
        # Download and push images
        setup_mattermost_images
    fi
    
    # Configure Docker daemon
    configure_docker_daemon
    
    # Configure calls-offloader
    configure_calls_offloader
    
    # Verify setup
    verify_setup
    
    # Create air-gap deployment script
    create_airgap_deployment_script
    
    echo "" | tee -a $LOG_FILE
    echo "=== Air-Gap Setup Complete ===" | tee -a $LOG_FILE
    echo "Local registry running at: http://$REGISTRY_HOST:$REGISTRY_PORT" | tee -a $LOG_FILE
    echo "Registry data stored at: $REGISTRY_DATA_DIR" | tee -a $LOG_FILE
    echo "" | tee -a $LOG_FILE
    echo "Next steps for air-gapped deployment:" | tee -a $LOG_FILE
    echo "1. Transfer these files to your air-gapped network:" | tee -a $LOG_FILE
    echo "   - docker-registry-data.tar.gz" | tee -a $LOG_FILE
    echo "   - registry-image.tar.gz" | tee -a $LOG_FILE
    echo "   - deploy-airgap-calls.sh" | tee -a $LOG_FILE
    echo "2. Run the local registry container in the air-gapped network" | tee -a $LOG_FILE
    echo "3. Execute ./deploy-airgap-calls.sh on the air-gapped systems" | tee -a $LOG_FILE
    echo "" | tee -a $LOG_FILE
    echo "Log file: $LOG_FILE" | tee -a $LOG_FILE
}

# Run main function
main "$@"