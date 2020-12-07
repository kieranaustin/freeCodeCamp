def get_weekday_string(weekday, days):
    weekday_to_num = {
       "Monday"   :1,
       "Tuesday"  :2,
       "Wednesday":3,
       "Thursday" :4,
       "Friday"   :5,
       "Saturday" :6,
       "Sunday"   :7 }
    num_to_weekday = {
       1:"Monday"    ,
       2:"Tuesday"   ,
       3:"Wednesday" ,
       4:"Thursday"  ,
       5:"Friday"    ,
       6:"Saturday"  ,
       0:"Sunday"     }

    weekday = weekday.lower().capitalize()
    weekday_num = weekday_to_num[weekday]
    weekday_num += days
    weekday_num %= 7

    return num_to_weekday[weekday_num]


def add_time(start, duration, weekday=""):
    # make sure no whitespace
    time_start = start.strip()

    # extract hour and minute from start
    sep_pos = time_start.find(":")
    hour_start = int(time_start[:sep_pos])
    minute_start = int(time_start[sep_pos+1:sep_pos+3])

    # convert to 24 hour clock and check special points
    noon = time_start[len(time_start)-2:]
    if noon == "AM":
        if hour_start==12:
            hour_start = 0
    elif noon == "PM":
        hour_start += 12

    # extract hours and minutes from duration
    sep_pos = duration.strip().find(":")
    hours_add = int(duration.strip()[:sep_pos])
    minutes_add = int(duration.strip()[sep_pos+1:sep_pos+3])

    # calculate end time and number of days
    hours_total = hour_start + hours_add
    minutes_total = minute_start + minutes_add
    if minutes_total >= 60:
        minutes_total -= 60
        hours_total += 1
    days_total = hours_total // 24
    hours_total = hours_total % 24

    # convert back to am/pm
    if hours_total >= 12:
        noon = "PM"
        if hours_total > 12:
            hours_total -= 12
    else:
        noon = "AM"
        if hours_total == 0:
            hours_total = 12

    # prepare output string
    hours_total = str(hours_total)
    minutes_total = str(minutes_total)
    if len(minutes_total) < 2:
        minutes_total = "0" + minutes_total
    new_time = hours_total + ":" + minutes_total + " " + noon 
    if weekday != "":
        new_time += ", " + get_weekday_string(weekday, days_total) 
    if days_total == 1:
        new_time += " (next day)"
    if days_total > 1:
        new_time += " (" + str(days_total) + " days later)"

    

    return new_time
