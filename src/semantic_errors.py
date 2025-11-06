"""
Semantic error definitions for RoboLang.
"""
from typing import List, Optional


class SemanticError(Exception):
    """Base class for semantic errors."""
    def __init__(self, message: str, node=None):
        self.message = message
        self.node = node
        super().__init__(message)


class InvalidValueError(SemanticError):
    """Raised when a numeric value is invalid (e.g., negative when positive required)."""
    pass


class InvalidUnitError(SemanticError):
    """Raised when an invalid unit is used."""
    pass


class InvalidAngleError(SemanticError):
    """Raised when an angle is outside valid range."""
    pass


class InvalidRepeatCountError(SemanticError):
    """Raised when repeat count is invalid."""
    pass


class SemanticErrorCollector:
    """Collects multiple semantic errors during analysis."""
    def __init__(self):
        self.errors: List[SemanticError] = []
    
    def add_error(self, error: SemanticError):
        self.errors.append(error)
    
    def has_errors(self) -> bool:
        return len(self.errors) > 0
    
    def get_error_messages(self) -> List[str]:
        return [e.message for e in self.errors]
    
    def raise_if_errors(self):
        if self.has_errors():
            msg = "Semantic errors found:\n" + "\n".join(f"  - {e}" for e in self.get_error_messages())
            raise SemanticError(msg)
