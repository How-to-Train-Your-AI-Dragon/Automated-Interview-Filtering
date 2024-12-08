"""Base class for LLM providers"""

from abc import abstractmethod
from typing import Dict, Optional


class BaseLLMProvider:
    @abstractmethod
    def __init__(self):
        """LLM provider initialization"""
        raise NotImplementedError

    @abstractmethod
    def complete(self, prompt: str = "") -> str:
        """LLM chat completion implementation by each provider"""
        raise NotImplementedError
