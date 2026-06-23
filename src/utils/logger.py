import logging
import os


class Logger:

    @staticmethod
    def setup_logger():

        os.makedirs(
            "outputs/logs",
            exist_ok=True
        )

        logger = logging.getLogger(
            "AutoDeck"
        )

        logger.setLevel(
            logging.INFO
        )

        if not logger.handlers:

            file_handler = logging.FileHandler(
                "outputs/logs/autodeck.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

        return logger