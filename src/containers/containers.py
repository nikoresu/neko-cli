from .clients.docker_client import DockerClient
from .clients.podman_client import PodmanClient


def get_container_client():
    """Try to initialize Docker, otherwise Podman.

    Returns a concrete `DockerClient` or `PodmanClient`. If neither
    backend initializes, returns an instance with `client=None`.
    """
    # Prefer Docker
    docker_adapter = DockerClient.create_from_env()
    if docker_adapter.available():
        return docker_adapter

    # Fallback to Podman
    podman_adapter = PodmanClient.create_from_env()
    if podman_adapter.available():
        return podman_adapter

    # Neither available — return empty DockerClient (or could return None)
    return docker_adapter


def list():
    """List all available containers"""
    
    print("Initializing container client...")
    adapter = get_container_client()

    if not adapter.available():
        print("No container environment found (docker or podman not available)")
        return adapter

    print("Initialized client:", True, "-", adapter.backend.capitalize())
    print(adapter.list_containers())
