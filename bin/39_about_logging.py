"""
logging library: to capture the logs in text file

Logging Level
INFO
DEBUG
WARNING
CRITICAL
ERROR
"""
print("Configure logger")
print("-"*20)
# ---------------

import logging
logging.basicConfig(filename="mylog.log", filemode="w", level=logging.DEBUG,
                    format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s"
                    )

my_logger = logging.getLogger(__name__)

print("Configuration is DONE")

print("#"*40, end="\n\n")
###########################

print("Testing my_logger")
print("-"*20)
# ---------------

my_logger.info("This is info")
my_logger.debug("This message is for debug")
my_logger.critical("This is critical")
my_logger.warning("This is warning")
my_logger.error("This is error")

print("Testing my_logger DONE")
print("Please check mylog.log file")

print("#"*40, end="\n\n")
###########################


print("using my_logger in program")
print("-"*20)
# ---------------

try:
    my_logger.info("Reached try block")
    my_logger.info("Opening File")
    my_file_handle = open("D:/sffdsfs/ejwje.txt", "w")
    my_logger.info("Opening file Done")
except Exception as e:
    my_logger.info("Reached except block")
    my_logger.error(f"Got Error and Details: {e}")
    my_logger.info("End of except block")

print("Please check mylog.log file")

print("#"*40, end="\n\n")
###########################