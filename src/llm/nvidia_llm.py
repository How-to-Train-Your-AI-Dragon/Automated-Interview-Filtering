"""NVIDIA LLM Implementation"""

from llama_index.llms.nvidia import NVIDIA

from src.llm.base_llm_provider import BaseLLMProvider
from src.llm.enums import AUTO_LLM_API_BASE


class NvidiaLLM(BaseLLMProvider):
    def __init__(
        self,
        model: str = "nvidia/llama-3.1-nemotron-70b-instruct",
        temperature: float = 0.0,
        base_url: str = "https://integrate.api.nvidia.com/v1",
    ):
        """Initiate NVIDIA client"""

        if base_url == AUTO_LLM_API_BASE:
            self._client = NVIDIA(
                model=model,
                temperature=temperature,
            )
        else:
            self._client = NVIDIA(
                model=model, temperature=temperature, base_url=base_url
            )

    def complete(self, prompt: str = "") -> str:
        return str(self._client.complete(prompt))
