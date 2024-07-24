from abc import ABC, abstractmethod

class RepositoryAbstract(ABC):
    """
    Abstract base class for a generic repository pattern.

    This class defines the basic CRUD (Create, Read, Update, Delete) operations 
    that a repository should implement for managing entities.

    Methods
    -------
    add(entity):
        Adds a new entity to the repository.

    get(entity_id):
        Retrieves an entity by its identifier from the repository.

    get_all():
        Retrieves all entities from the repository.

    update(entity):
        Updates an existing entity in the repository.

    delete(entity_id):
        Deletes an entity by its identifier from the repository.
    """
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass
