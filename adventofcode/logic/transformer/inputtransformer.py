""" Input transformer module"""
import logging
from typing import Any, List

from adventofcode.logic.transformer.transfomerstrategy import TransformerStrategy


class InputTransformer:
    """Class to execute different transformer strategies."""

    # pylint: disable=too-few-public-methods
    def __init__(self, strategy: List[TransformerStrategy]) -> None:
        self.strategy = strategy

    def do_transformations(self, raw_input: Any) -> Any:
        """Manage execution of transformation list

        This method executes and removes transformation strategies from the
        transformation list until all transformations are done. This is reached
        by recusrive calls to itself.

        Args:
            raw_input (Any): input objet

        Returns:
            raw_input: transformed object after all transformations are executed
        """

        if self.strategy:
            logging.debug(f"Executing transformer {self.strategy[0]}")
            transformed_result = self.strategy[0].do_transformation(raw_input)
            self.strategy.pop(0)
            return self.do_transformations(transformed_result)
        else:
            return raw_input
