from datetime import datetime,time
def is_restaurant_open():
    now=datetime.now()
    current_day=now.weekday()
    current_time=now.time()
    opening_hours={
        0:(time(9,0),time(22,0)),
        1:(time(9,0),time(22,0)),
        2:(time(9,0),time(22,0)),
        3:(time(9,0),time(22,0)),
        4:(time(9,0),time(22,0)),
        5:(time(10,0),time(23,0)),
        6:(time(10,0),time(23,0)),
    }
    open_time,close_time=opening_hours.get(current_day)
    if open_time<=current_time<=close_time:
        return True
    return False