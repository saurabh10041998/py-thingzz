import datetime


def close_kitchen():
    pass


def closing_time():
    return datetime.datetime.now()

def log_closing_time(*args):
    pass


class CustomDateTime:
    def __init__(self, text: str) -> None:
       self.text = text


# CustomDateTime provides all the features of
# datetime.datetime, we're using it here because
# of additional logging facilities
close_kitchen_if_past_close(CustomDateTime("now")) # no error

def close_kitchen_if_past_close(point_in_time: datetime.datetime):
    if point_in_time > closing_time():
        close_kitchen()
        log_closing_time(point_in_time)
