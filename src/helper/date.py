import datetime


def get_today(format_str: str = "%B %Y"):  # "%m-%D-%Y
    return datetime.date.today().strftime(format_str)
