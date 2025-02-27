import yaml

from src.llm.enums import OPENAI_LLM, NVIDIA_LLM
from src.llm.base_llm_provider import BaseLLMProvider
from src.llm.openai_llm import OpenAILLM
from src.llm.nvidia_llm import NvidiaLLM


def get_llm(config_file_path: str = "config.yaml") -> BaseLLMProvider:
    """
    Initiates LLM client from config file
    """

    # load config
    with open(config_file_path, "r") as f:
        config = yaml.safe_load(f)

    # init & return llm
    if config["PROVIDER"] == OPENAI_LLM:
        return OpenAILLM(
            model=config["MODEL"],
            temperature=config["TEMPERATURE"],
            base_url=config["BASE_URL"],
        )
    elif config["PROVIDER"] == NVIDIA_LLM:
        return NvidiaLLM(
            model=config["MODEL"],
            temperature=config["TEMPERATURE"],
            base_url=config["BASE_URL"],
        )
    else:
        raise ValueError(config["MODEL"])
