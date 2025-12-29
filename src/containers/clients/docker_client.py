try:
    import docker
except Exception:
    docker = None

from .base import ContainerClient
from typing import Iterable


class DockerClient(ContainerClient):
    backend = "docker"

    def __init__(self, client=None):
        super().__init__(client=client)

    @classmethod
    def create_from_env(cls):
        if docker is None:
            return cls(client=None)
        try:
            client = docker.from_env()
            return cls(client=client)
        except Exception:
            return cls(client=None)

    def list_containers(self, all: bool = True) -> Iterable:
        if not self.available():
            raise RuntimeError("Docker client not available")
        return self.client.containers.list(all=all)
