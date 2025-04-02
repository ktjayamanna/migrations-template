#!/bin/bash

# Warn the user before proceeding
echo "WARNING: This script will remove all Docker containers, images, volumes, and networks from your system."
echo "Are you sure you want to proceed? (yes/no)"
read confirmation

if [ "$confirmation" != "yes" ]; then
    echo "Operation aborted."
    exit 1
fi

# Stop all running containers
echo "Stopping all running containers..."
docker stop $(docker ps -q) 2>/dev/null

# Remove all containers
echo "Removing all containers..."
docker rm $(docker ps -aq) 2>/dev/null

# Remove all images
echo "Removing all images..."
docker rmi $(docker images -q) -f 2>/dev/null

# Remove all volumes
echo "Removing all volumes..."
docker volume rm $(docker volume ls -q) 2>/dev/null

# Remove all networks
echo "Removing all networks..."
docker network rm $(docker network ls -q) 2>/dev/null

# Prune everything
echo "Pruning system..."
docker system prune -a --volumes -f

# Optionally, remove Docker's storage directory
echo "Removing Docker storage directories..."
sudo rm -rf /var/lib/docker /var/lib/containerd

# Restart Docker service
echo "Restarting Docker service..."
sudo systemctl restart docker

echo "Docker cleanup complete!"
