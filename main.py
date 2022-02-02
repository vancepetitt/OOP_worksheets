from alarm_clock import AlarmClock

alarm_clock = AlarmClock(1130, True, 600)

print(alarm_clock.current_time)

alarm_clock.set_current_time()
print(alarm_clock.current_time)

alarm_clock.set_alarm_time()
print(alarm_clock.alarm_set_time)

alarm_clock.alarm_toggle()
alarm_clock.alarm_toggle()
