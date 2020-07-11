import urllib.request, json
import numpy as np
import datetime


def same_day(day1, day2):
    if day1.year == day2.year and day1.month == day2.month and day1.day == day2.day:
        return True
    else:
        return False


def is_in_lecture(current, start, end):
    num = len(start)

    for i in range(num):
        if start[i] <= current <= end[i]:
            return True

    return False


def is_between_lecture(current, start, end):
    num = len(start)

    for i in range(num - 1):
        if end[i] < current < start[i+1]:
            return True

    return False


def is_after_last_lecture(current, start, end):
    num = len(end)
    if current > end[num - 1]:
        return True
    else:
        return False


def is_before_first_lecture(current, start, end, minutes=10, seconds=10):
    if current + datetime.timedelta(minutes=minutes, seconds=seconds) > start[0] and current <= start[0]:
        return True
    else:
        return False


def readurl(current_time=datetime.datetime.fromisoformat('2020-07-13 08:50:00+02:00')):
    url = "https://sciot-calendar.azurewebsites.net/events"

    # current_time = datetime.datetime.now()
    # current_time = datetime.datetime.fromisoformat('2020-07-13 08:50:00+02:00')
    start = []
    end = []
    with urllib.request.urlopen(url) as dat:
        data = json.loads(dat.read().decode())

        for i in range(len(data)):
            temp_start = datetime.datetime.fromisoformat(data[i]['start']['dateTime'])
            if same_day(temp_start, current_time):
                start.append(temp_start)

            temp_end = datetime.datetime.fromisoformat(data[i]['end']['dateTime'])
            if same_day(temp_end, current_time):
                end.append(temp_end)

    if len(start) == 0 or len(end) == 0:
        print('no event today')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return False, False, False, False
    elif is_in_lecture(current_time, start, end):
        print('in lecture')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return True, False, False, False
    elif is_after_last_lecture(current_time, start, end):
        print('after last lecture')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return False, False, True, False
    elif is_between_lecture(current_time, start, end):
        print('lecture pause')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return False, True, False, False
    elif is_before_first_lecture(current_time, start, end, minutes=30):
        print('first lecture about to start')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return False, False, False, True
    else:
        print('too early/ some thing went wrong')
        # inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture
        return False, False, False, True


curr_time = datetime.datetime.fromisoformat('2020-07-13 08:05:00+02:00')
while True:
    readurl(curr_time)
    curr_time += datetime.timedelta(minutes=10)


