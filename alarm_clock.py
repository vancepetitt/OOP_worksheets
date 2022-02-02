class AlarmClock:

    def __init__(self, current_time_passed, alarm_is_on, alarm_set_time_passed):
        self.current_time = current_time_passed
        self.alarm_is_on = alarm_is_on
        self.alarm_set_time = alarm_set_time_passed

    def set_current_time(self):
        self.current_time = input('Enter current time: ')
        print(f'Current time is {self.current_time}')
    
    def alarm_toggle(self):
        if self.alarm_is_on == True:
            self.alarm_is_on = False
            print('Alarm OFF')
        elif self.alarm_is_on == False:
            self.alarm_is_on = True
            print('Alarm ON')
         
    def set_alarm_time(self):
        self.alarm_set_time = input('Enter alarm set time: ')
        print(f'Alarm set to {self.alarm_set_time}')