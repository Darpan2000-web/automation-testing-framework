import logging

def get_logger():
    logging.basicConfig(
        filename="reports/log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()