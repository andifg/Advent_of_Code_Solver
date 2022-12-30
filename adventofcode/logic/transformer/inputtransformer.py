""" Input transformer module"""
from typing import Any

from adventofcode.logic.transformer.transfomerstrategy import TransformerStrategy


class InputTransformer:
    """Class to execute different transformer strategies."""

    # pylint: disable=too-few-public-methods
    def __init__(self, strategy: TransformerStrategy) -> None:
        self.strategy = strategy

    def do_transformation(self, raw_input: Any) -> Any:
        """_summary_

        Args:
            raw_input (Any): input objet

        Returns:
            transformed_input: transformed object
        """

        transformed_input = self.strategy.do_transformation(raw_input)
        return transformed_input
