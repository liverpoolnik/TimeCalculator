def add_time(start, duration, weekday=''):
    a = duration.split(':')
    m1 = int(a[1])
    a = int(a[0])
    b = a % 24
    d = b
    r = 0
    t = start.split(' ')
    t1 = (str(t[0])).split(':')
    h = int(t1[0])
    m = int(t1[1])

    am = str(t[1]).upper()
    st_day = weekday.lower()
    day = a // 24

    week_day = ''
    if m + m1 > 59:
        h += 1
        m = (m + m1) - 60
    else:
        m = m + m1
    if (12 - h) < d <= 12 + (12 - h):
        r = d - (12 - h)
    elif d > 12 + (12 - h):
        r = d - (12 - h) - 12

    else:
        r = d + h
    if 12 - h <= d < 12 + (12 - h):
        if am == "AM":
            am = 'PM'
        else:
            am = 'AM'
            day += 1
    st_day1 = day % 7
    monday = {1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    tuesday = {1: 'Wednesday', 2: 'Thursday', 3: 'Friday', 4: 'Saturday', 5: 'Sunday', 6: 'Monday'}
    wednesday = {1: 'Thursday', 2: 'Friday', 3: 'Saturday', 4: 'Sunday', 5: 'Monday', 6: 'Tuesday'}
    thursday = {1: 'Friday', 2: 'Saturday', 3: 'Sunday', 4: 'Monday', 5: 'Tuesday', 6: 'Wednesday'}
    friday = {1: 'Saturday', 2: 'Sunday', 3: 'Monday', 4: 'Tuesday', 5: 'Wednesday', 6: 'Thursday'}
    saturday = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
    sunday = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    week = {'monday': monday, 'tuesday': tuesday, 'wednesday': wednesday,
            'thursday': thursday, 'friday': friday,
            'saturday': saturday, 'sunday': sunday}
    if m < 10:
        m = str(m).rjust(2, '0')
    else:
        m = str(m)
    if day == 1:
        day_r = "(next day)"
    else:
        day_r = '(' + str(day) + ' days later)'

    if len(st_day) == 0:
        new_time = str(r) + ':' + m + ' ' + am + ' ' + day_r
        if day == 0:
            new_time = str(r) + ':' + m + ' ' + am

        return new_time
    else:
        if day > 7 and st_day1 > 0:
            week_day = week[st_day][st_day1]
        elif day >= 7 and st_day1 == 0:
            week_day = st_day.capitalize()
        elif day == 0:
            week_day = st_day.capitalize()
        else:
            week_day = week[st_day][day]
        new_time = str(r) + ':' + m + ' ' + am + ', ' + week_day + ' ' + day_r
        if day == 0:
            new_time = str(r) + ':' + m + ' ' + am + ', ' + week_day
        return new_time


print(add_time("11:06 PM", "2:02"))
print(add_time("3:30 PM", "2:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
