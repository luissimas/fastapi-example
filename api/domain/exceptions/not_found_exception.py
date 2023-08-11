class NotFoundException(Exception):
    def __init__(self, entity_name: str = "Entity"):
        super().__init__(f"{entity_name} not found")
