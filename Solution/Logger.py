from datetime import datetime

class Logger:
    path: str = "results/api_download.log"

    def log(message: str, logLevel: str = "INFO"):
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.path, "a") as log_file:
            log_file.write(f"{currentTime}:{logLevel}: {message}\n")