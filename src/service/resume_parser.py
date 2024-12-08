import yaml
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

from src.template.parser_prompt import PARSE_RESUME_PROMPT


class ResumeParser:
    def __init__(self, config_file_path: str = "config.yaml"):
        """
        Initiates a resume parser client
        """

        # load config
        with open(config_file_path, "r") as f:
            config = yaml.safe_load(f)

        # set bbox size
        bbox_margin = config["PAGE_ROC_BBOX"]
        bbox = f"{bbox_margin['TOP']},{bbox_margin['RIGHT']},{bbox_margin['BOTTOM']},{bbox_margin['LEFT']}"

        self._parser = LlamaParse(
            language=config["LANGUAGE"],
            disable_ocr=config["DISABLE_OCR"],
            bounding_box=bbox,
            result_type="markdown",
            parsing_instruction=PARSE_RESUME_PROMPT,
            is_formatting_instruction=False,
        )

    def parse_resume_to_markdown(self, resume_path: str = "") -> str:
        """
        Parses the resume into markdown text.

        Supported filetypes:
        - .pdf
        """
        document = SimpleDirectoryReader(
            input_files=[resume_path], file_extractor={".pdf": self._parser}
        ).load_data()

        return "\n".join([str(d.text) for d in document])
