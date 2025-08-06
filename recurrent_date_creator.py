
from datetime import timedelta
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY, YEARLY
from dateutil.relativedelta import relativedelta

FREQ_MAP = {
    "daily": DAILY,
    "weekly": WEEKLY,
    "monthly": MONTHLY,
    "yearly": YEARLY,
}

class RecurrentDateCreator:
    
    def __init__(self, recurrence):
        self.recurrent_type = FREQ_MAP.get(recurrence["recurrent_type"])
        self.count = recurrence["count"]
    
    def generate_recurrent_dates(self, start_dt, freq):
        dates = []

        if freq == 1: # '1' is for 'MONTHLY'
            if start_dt.day in (29, 30, 31):
                day = int(start_dt.day)
                for _ in range(self.count):
                    dates.append(start_dt)
                    start_dt += timedelta(days=4)
                    start_dt = start_dt + relativedelta(day=day)

            else:
                dates = list(rrule(dtstart=start_dt, freq=freq, count=self.count))

        elif freq == 0:  # '0' is for 'YEARLY'
            if start_dt.month == 2 and start_dt.day == 29:
                for i in range(self.count):
                    dates.append(start_dt)
                    start_dt = start_dt + relativedelta(day=31, years=1)

            else:
                dates = list(rrule(dtstart=start_dt, freq=freq, count=self.count))
        
        else:
            dates = list(rrule(dtstart=start_dt, freq=freq, count=self.count))

        return dates
