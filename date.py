import datetime

def splitDate(date):
    """Split the date and return the year
       Add your conversion rules as needed"""
    # See here for a suitable format string: https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-strptime-behavior
    retdate = datetime.datetime(1,1,1)
    try:
        retdate = datetime.datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        try:
            retdate = datetime.datetime.strptime(date, "%Y")
        except ValueError:
            pass
    return retdate.year
