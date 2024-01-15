from datetime import datetime


class Writer:
    @staticmethod
    def write(text: str):
        with open("text_writer.txt", "a") as file:
            file.write(f"{text}\n")


class Logger:
    _exception_number = 0

    @classmethod
    def write(cls, exception: object):
        cls._exception_number += 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        exception_class_name = exception.__class__.__name__
        exception_msg = exception
        log = f"{cls._exception_number}\t{date}\t{exception_class_name}\t{exception_msg}"
        Writer.write(log)


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            Logger.write(e)

    return wrapper
