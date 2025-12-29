try:
    import podman
except Exception:
    podman = None

from .base import ContainerClient
from typing import Iterable


class PodmanClient(ContainerClient):
    backend = "podman"

    def __init__(self, client=None):
        super().__init__(client=client)

    @classmethod
    def create_from_env(cls):
        if podman is None:
            return cls(client=None)
        try:
            client = podman.PodmanClient()
            return cls(client=client)
        except Exception:
            return cls(client=None)

    def list_containers(self, all: bool = True) -> Iterable:
        if not self.available():
            raise RuntimeError("Podman client not available")
        try:
            return self.client.containers.list(all=all)
        except TypeError:
            return self.client.containers.list()
