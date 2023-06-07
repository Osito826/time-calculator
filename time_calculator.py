def add_time(start, duration, optional_day_of_week=False):
  
    days_in_a_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, 
    "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    days_in_a_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday", "Sunday"]

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_hours = int(start_tuple[0])
    start_min_tuple = start_tuple[2].partition(" ")
    start_minutes = int(start_min_tuple[0])
    am_or_pm = start_min_tuple[2]
    am_and_pm_reverse = {"AM": "PM", "PM": "AM"}

    amount_of_days = int(duration_hours / 24)

    minutes_end = start_minutes + duration_minutes
    if(minutes_end >= 60):
      start_hours += 1
      minutes_end = minutes_end % 60
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12)
    hours_end = (start_hours + duration_hours) % 12

    minutes_end = minutes_end if minutes_end > 9 else "0" + str(minutes_end)
    hours_end = hours_end = 12 if hours_end == 0 else hours_end
    if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1

    am_or_pm = am_and_pm_reverse[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

    returnTime = str(hours_end) + ":" + str(minutes_end) + " " + am_or_pm
    if(optional_day_of_week):
      optional_day_of_week = optional_day_of_week.lower()
      index = int((days_in_a_week_index[optional_day_of_week]) + amount_of_days) % 7
      new_day = days_in_a_week_array[index]
      returnTime += ", " + new_day

    if(amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif(amount_of_days > 1):
      return returnTime + " (" + str(amount_of_days) + " days later)"

    return returnTime
