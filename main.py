import logging
import logging.handlers
import os
import csv
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=london&country=GB')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in London: {temperature}')

        # Adicionar a temperatura ao arquivo CSV sem perder informações anteriores
        with open("temperatures.csv", "a", newline="") as csvfile:
            fieldnames = ["timestamp", "temperature"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Verifica se o arquivo CSV já existe e escreve cabeçalhos se necessário
            if os.path.getsize("temperatures.csv") == 0:
                writer.writeheader()

            writer.writerow({"timestamp": logger_file_handler.formatTime(), "temperature": temperature})

    logger.info(f"testando")



# import logging
# import logging.handlers
# import os

# import requests

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger_file_handler = logging.handlers.RotatingFileHandler(
#     "status.log",
#     maxBytes=1024 * 1024,
#     backupCount=1,
#     encoding="utf8",
# )
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger_file_handler.setFormatter(formatter)
# logger.addHandler(logger_file_handler)

# try:
#     SOME_SECRET = os.environ["SOME_SECRET"]
# except KeyError:
#     SOME_SECRET = "Token not available!"

# if __name__ == "__main__":
#     logger.info(f"Token value: {SOME_SECRET}")

#     r = requests.get('https://weather.talkpython.fm/api/weather/?city=london&country=GB')
#     if r.status_code == 200:
#         data = r.json()
#         temperature = data["forecast"]["temp"]
#         logger.info(f'Weather in London: {temperature}')
    
#     logger.info(f"testando")