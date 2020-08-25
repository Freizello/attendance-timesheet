import datetime


def get_today(format_str: str = "%B %Y"):  # "%m-%D-%Y
    return datetime.date.today().strftime(format_str)


def get_delta_time(time_start, time_end):
    delta_time = datetime.datetime.strptime(time_end, "%H:%M") - datetime.datetime.strptime(time_start, "%H:%M")
    return delta_time  # TODO : Find a way to format delta_time to %H:%M


def generate_holiday(date):
    # TODO : check holiday to generate report
    pass
