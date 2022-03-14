import logging
import re


class MyErrors(Exception):
    def __init__(self, text):
        self.text = text


def get_errors_info_from_log(log):
    try:
        log_file = open(log, "r")
        log_list = log_file.readlines()
        log_file.close()
        if not log_list:
            raise Exception("File is empty")
    except Exception as e:
        log_list = []
        print(e)

    log_list_len = len(log_list)
    err_logger = logging.getLogger(__name__)
    err_logger.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    file_handler = logging.FileHandler("found_errors.log")
    file_handler.setLevel(logging.ERROR)
    err_logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)

    console.setFormatter(formatter)

    err_logger.addHandler(file_handler)
    err_logger.addHandler(console)

    error_length = 0
    cr_error_length = 0

    try:
        str = " ".join(log_list)
        if re.search("CRITICAL ERROR", str):
            raise MyErrors("\nAttention! Critical Error found {{{}}} times!\n".format(str.count("CRITICAL ERROR")))
    except MyErrors as e:
        print(e)

    for x in log_list:
        if re.search("ERROR", x, re.IGNORECASE) and not re.search("CRITICAL ERROR", x):
            error_length += 1
            err_logger.error(x)
        elif re.search("CRITICAL ERROR", x):
            cr_error_length += 1
            err_logger.critical(x)
    else:
        pass

    return log_list_len / (error_length + cr_error_length)


if __name__ == '__main__':
    try:
        file = "yupdate.log"
        er_log = get_errors_info_from_log(file)
    except FileNotFoundError as err1:
        print("Error:", err1)
    except ZeroDivisionError as err2:
        print("No errors were found:", err2)
    except Exception as err3:
        print("Error:", err3)
    else:
        print("Соотношение общего количества записей {{{}}} к количеству записей с ошибками: {}.".format(file, er_log))