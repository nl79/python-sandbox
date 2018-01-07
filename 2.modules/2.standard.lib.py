import shelve
import webbrowser
import time
import random
import datetime
import pytz


#print(dir())
#print(dir(__builtins__))

# for m in dir(__builtins__):
#     print(m)

#print(dir(shelve))

# for obj in dir(shelve):
#     if obj[0] != '_':
#         print(obj)

#help(shelve)

# webbrowser.open("https://www.python.org")
# help(webbrowser)

# safari = webbrowser.get(using='safari')
# safari.open('https://www.python.org')

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())
#
# time_here = time.localtime()
# print(time_here)
# print('Year:', time_here[0], time_here.tm_year)
# print('Month: ', time_here[1], time_here.tm_mon)
# print('Day: ', time_here[2], time_here.tm_mday)

# input('Press enter to start')
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# #start_time = time.time()
# #start_time = time.perf_counter()
# # start_time = time.monotonic()
# start_time = time.process_time()
#
# input('Press enter to stop')
#
# #end_time = time.time()
# #end_time = time.perf_counter()
# # end_time = time.monotonic()
# end_time = time.process_time()
#
# print("Started at: " + time.strftime('%X', time.localtime(start_time)))
# print('Ended at: ' + time.strftime('%X', time.localtime(end_time)))
#
# print('Your reaction time has {} seconds'.format(end_time - start_time))
#
# print('time: ', time.get_clock_info('time'))
# print('perf_counter: ', time.get_clock_info('perf_counter'))
# print('monotonic: ', time.get_clock_info('monotonic'))
# print('process_time: ', time.get_clock_info('process_time'))

# print('The epoch on this system starts at ' + time.strftime('%c', time.gmtime()))
# print('The current timezone is {0} with an offset of {1}'.format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print('\tDaylight Saving Time is in effect for this location')
#     print('\tThe DST timezone is ' + time.tzname[1])
#
# print('Locale time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#
#
# print(datetime.datetime.today())
# print(datetime.datetime.utcnow())
# print(datetime.datetime.now())

# country = 'Europe/Moscow'
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print('The time in {} is {}'.format(country, local_time))
# print('UTC is {}'.format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ': ' + pytz.country_names[x])
#
# for x in sorted(pytz.country_names):
#     print('{}: {}: {}'.format(x, pytz.country_names.get(x), pytz.country_timezones.get(x)))

# for x in sorted(pytz.country_names):
#     print('{}: {}'.format(x, pytz.country_names.get(x)))
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print('\t\t{}: {}'.format(zone, local_time))
#     else:
#         print('\t\tNo Timezone defined')

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print('Naive local time {}', format(local_time))
print('Naive UTC {}'.format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print('Aware local time {}, time zone {}'.format(aware_local_time, aware_local_time.tzinfo))
print('Ware UTC {}, time zone {}'.format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 144573300
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print('{} seconds since the epoch is {}'.format(s, dt1))
print('{} seconds since the epoch is {}'.format(t, dt2))

