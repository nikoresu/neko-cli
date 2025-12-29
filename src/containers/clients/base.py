from typing import Any, Iterable


class ContainerClient:
    """Base class defining the container client interface.

    Concrete implementations should subclass this and implement the
    methods used by the rest of the application.
    """

    backend: str = "none"

    def __init__(self, client: Any = None):
        self.client = client

    def available(self) -> bool:
        return self.client is not None

    def list_containers(self, all: bool = True) -> Iterable:
        """Return an iterable of containers.

        Subclasses should implement this.
        """
        raise NotImplementedError()
