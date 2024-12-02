"""OpenAI LLM Implementation"""

from llama_index.llms.openai import OpenAI

from src.llm.base_llm_provider import BaseLLMProvider
from src.llm.enums import DEFAULT_LLM_API_BASE


class OpenAILLM(BaseLLMProvider):
    def __init__(
        self,
        model: str = "gpt-4o-mini",
        temperature: float = 0.0,
        base_url: str = DEFAULT_LLM_API_BASE,
    ):
        """Initiate OpenAI client"""

        if base_url == DEFAULT_LLM_API_BASE:
            self._client = OpenAI(
                model=model,
                temperature=temperature,
            )
        else:
            self._client = OpenAI(
                model=model, temperature=temperature, base_url=base_url
            )

    def complete(self, prompt: str = "") -> str:
        return str(self._client.complete(prompt))
