"""
Semantic Analyzer for RoboLang AST.

Validates:
- Numeric values are positive where required
- Units are valid (cm, m)
- Angles are within valid range (0-360 degrees)
- Velocities are positive
- Wait durations are positive
- Repeat counts are >= 1
- Program has valid name
"""
from typing import List
from .ast import Program, Move, Turn, Speed, Wait, Repeat, Command
from .semantic_errors import (
    SemanticErrorCollector,
    InvalidValueError,
    InvalidUnitError,
    InvalidAngleError,
    InvalidRepeatCountError
)


class SemanticAnalyzer:
    """Performs semantic analysis on RoboLang AST."""
    
    def __init__(self, collect_all_errors: bool = True):
        """
        Args:
            collect_all_errors: If True, collects all errors before raising.
                               If False, raises on first error.
        """
        self.collect_all_errors = collect_all_errors
        self.errors = SemanticErrorCollector()
    
    def analyze(self, program: Program) -> bool:
        """
        Analyze the program AST.
        
        Returns:
            True if no errors, False otherwise (when collect_all_errors=True)
        
        Raises:
            SemanticError: When errors are found (depending on collect_all_errors)
        """
        self.errors = SemanticErrorCollector()  # Reset errors
        
        # Validate program name
        if not program.name or not program.name.strip():
            self._add_error(InvalidValueError("O nome do programa não pode ser vazio", program))
        
        # Validate commands
        self._analyze_commands(program.commands)
        
        if self.errors.has_errors():
            if self.collect_all_errors:
                return False
            else:
                self.errors.raise_if_errors()
        
        return True
    
    def _add_error(self, error):
        if self.collect_all_errors:
            self.errors.add_error(error)
        else:
            raise error
    
    def _analyze_commands(self, commands: List[Command]):
        """Analyze a list of commands."""
        for cmd in commands:
            if isinstance(cmd, Move):
                self._analyze_move(cmd)
            elif isinstance(cmd, Turn):
                self._analyze_turn(cmd)
            elif isinstance(cmd, Speed):
                self._analyze_speed(cmd)
            elif isinstance(cmd, Wait):
                self._analyze_wait(cmd)
            elif isinstance(cmd, Repeat):
                self._analyze_repeat(cmd)
    
    def _analyze_move(self, move: Move):
        """Validate Move command."""
        # Check distance is positive
        if move.distance <= 0:
            self._add_error(InvalidValueError(
                f"Distancia de movimento deve ser positiva, obteve {move.distance}",
                move
            ))
        
        # Check unit is valid
        if move.unit not in ['cm', 'm']:
            self._add_error(InvalidUnitError(
                f"Unidade inválida: '{move.unit}', deve ser 'cm' ou 'm'",
                move
            ))
        
        # Check axis is valid
        if move.axis not in ['x', 'y', 'z']:
            self._add_error(InvalidValueError(
                f"Eixo inválido: '{move.axis}', deve ser 'x', 'y' ou 'z'",
                move
            ))
    
    def _analyze_turn(self, turn: Turn):
        """Validate Turn command."""
        # Check angle is within valid range
        if turn.degrees < 0 or turn.degrees > 360:
            self._add_error(InvalidAngleError(
                f"Ângulo deve estar entre 0 e 360 graus, obteve {turn.degrees}",
                turn
            ))
    
    def _analyze_speed(self, speed: Speed):
        """Validate Speed command."""
        # Check speed is positive
        if speed.value <= 0:
            self._add_error(InvalidValueError(
                f"Velocidade deve ser positiva, obteve {speed.value}",
                speed
            ))
    
    def _analyze_wait(self, wait: Wait):
        """Validate Wait command."""
        # Check duration is positive
        if wait.duration <= 0:
            self._add_error(InvalidValueError(
                f"Espera deve ser positiva, obteve {wait.duration}",
                wait
            ))
    
    def _analyze_repeat(self, repeat: Repeat):
        """Validate Repeat command."""
        # Check count is >= 1
        if repeat.count < 1:
            self._add_error(InvalidRepeatCountError(
                f"Contagem de repetição deve ser pelo menos 1, obteve {repeat.count}",
                repeat
            ))
        
        # Recursively analyze nested commands
        self._analyze_commands(repeat.commands)
    
    def get_errors(self) -> List[str]:
        """Get list of error messages."""
        return self.errors.get_error_messages()
