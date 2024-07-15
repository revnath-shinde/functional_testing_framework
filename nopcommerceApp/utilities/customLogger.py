import logging
import os

def setup_logging():
    log_dir = r"C:\Users\REVNATH\PycharmProjects\nopcommerceApp\Logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "automation.log")
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG
    )

    logger = logging.getLogger('urbanGUI')
    return logger

7


