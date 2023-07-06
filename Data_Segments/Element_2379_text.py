    #  Change indicators

    #     a plus sign (+)    for an addition
    #     an asterisk (*)    for an amendment to structure
    #     a hash sign (#)    for changes to names
    #     a vertical bar (|) for changes to text for descriptions and notes
    #     a minus sign (-)   for marked for deletion (within either batch and interactive messages)
    #     a X sign (X)       for marked for deletion (within both batch and interactive messages)

    #  2379  Date or time or period format code                      [C]

    #  Desc: Code specifying the representation of a date, time or period.
    #  Repr: an..3
    #  Code Values: 


__description_name_code = (
"""
DDMMYY
Calendar date: D = Day; M = Month; Y = Year.
"""
,
"""
MMDDYY
Calendar date: M = Month; D = Day; Y = Year.
"""
,
"""
DDMMCCYY
Calendar date C=Century; Y=Year; M=Month; D=Day.
"""
,
"""
DDMMCCYYHHMM
Calendar date and time: C=Century; Y=Year; M=Month;
D=Day; H=Hour; M=Minute.
"""
,
"""
CCYYMMB
Half-month: CC=century YY=year MM=month, B=1:first half
month, B=2:second half month.
"""
,
"""
CCYYMMW
Week within a calendar month: CC=century YY=year
MM=month. W=1-5 first week to fifth week in a month.
"""
,
"""
CCYYMMDDS
Shift within a calendar day: CC=century YY=year MM=month
DD=day S=1-9 shift in a day.
"""
,
"""
CCYYMMDDPP
Time period within a calendar day: CC=century YY=year
MM=month DD=day PP=00-99 time period.
"""
,
"""
CCYYMMDDTHHMM
Calendar date including time with minutes: C=Century;
Y=Year; M=Month; D=Day; T=Time designator; H=Hour;
M=Minutes.
The character [T] shall be used as time designator to
indicate the start of the representation of the time.
For example: 20010912T1433.
"""
,
"""
YYMMDD
Calendar date: Y = Year; M = Month; D = Day.
"""
,
"""
CCYYMMDD
Calendar date: C = Century ; Y = Year ; M = Month ; D =
Day.
"""
,
"""
YYWWD
Calendar week day: Y = Year ; W = Week ; D = Day Week
number 01 is always first week of January Day number 1
is always Monday.
"""
,
"""
MMWW-MMWW
A period of time specified by giving the start week of a
month followed by the end week of a month. Data is to be
transmitted as consecutive characters without hyphen.
"""
,
"""
YYDDD
Calendar day: Y = Year ; D = Day January the first = Day
001 Always start numbering the days of the year from
January 1st through December 31st.
"""
,
"""
MMDD
Day of a month: M = Month; D = Day.
"""
,
"""
DDD
Day's number within a specific year: D = Day.
"""
,
"""
WW
Week's number within a specific year: W = Week.
"""
,
"""
MM
Month's number within a specific year: M = Month.
"""
,
"""
DD
Day's number within is a specific month: D = Day.
"""
,
"""
YYMMDDHHMM
Calendar date including time without seconds: Y = Year;
M = Month; D = Day; H = Hour; M = Minute.
"""
,
"""
YYMMDDHHMMSS
Calendar date including time with seconds: Y = Year; M =
Month; D = Day; H = Hour; m = Minutes = Seconds.
"""
,
"""
CCYYMMDDHHMM
Calendar date including time with minutes: C=Century;
Y=Year; M=Month; D=Day; H=Hour; M=Minutes.
"""
,
"""
CCYYMMDDHHMMSS
Calendar date including time with seconds:
C=Century;Y=Year;
M=Month;D=Day;H=Hour;M=Minute;S=Second.
"""
,
"""
CCYYMMDDHHMMZHHMM
Calendar date including time and time zone expressed in
hours and minutes.
ZHHMM = time zone given as offset from Coordinated
Universal Time (UTC).
"""
,
"""
YYMMDDHHMMZHHMM
Calendar date including time without seconds, with Time
Zone:
Y = Year; M = Month; D = Day; H = Hour; M = Minute,
Z = leading plus/minus sign, HHMM = difference to UTC in
Hours and Minutes.
"""
,
"""
YYMMDDHHMMSSZHHMM
Calendar date including time with seconds, with Time
Zone:
Y = Year; M = Month; D = Day; H = Hour; M = Minute, S =
Seconds
Z = leading plus/minus sign, HHMM = difference to UTC in
Hours and Minutes.
"""
,
"""
CCYYMMDDHHMMSSZHHMM
Calendar date including time with seconds, with Time
Zone:
C = Century, Y = Year; M = Month; D = Day; H = Hour; M =
Minute, S = Seconds, Z = leading plus/minus sign, HHMM =
difference to UTC in Hours and Minutes.
"""
,
"""
HHMMSSZHHMM
Time with seconds and with Time Zone:
H = Hour; M = Minute, S = Seconds, Z = leading
plus/minus sign, HHMM = difference to UTC in Hours and
Minutes.
"""
,
"""
HHMMSSZHHMM-HHMMSSZHHMM
A period of time specified by giving the start time
followed by the end time (both expressed by hours,
minutes, seconds and time zone leading plus/minus sign
and time zone difference in hours and minutes).
"""
,
"""
YYMMDDHHMMZZZ
See 201 + Z = Time zone.
"""
,
"""
YYMMDDHHMMSSZZZ
See 202 + Z = Time zone.
"""
,
"""
CCYYMMDDHHMMZZZ
See 203 plus Z=Time zone.
"""
,
"""
CCYYMMDDHHMMSSZZZ
See 204 plus Z=Time zone.
"""
,
"""
MMDDHHMM
Month, day, hours, minutes; M = Month; D = Day; H =
Hour; M = Minute.
"""
,
"""
DDHHMM
Day, hours, minutes; D = Day; H = Hour; M = Minute.
"""
,
"""
CCYYMMDDHHMMSSFFF
Calendar date including time with seconds and
milliseconds
C = century, Y = year, M = month, D = day, H = hour, M =
minute, S = second, F = millisecond.
"""
,
"""
CCYYMMDDHHMMZZZ-CCYYMMDDHHMMZZZ
A period of time which includes the century, year,
month, day, hour and minute and time zone. Format of
period to be given in actual message without hyphen.
"""
,
"""
HHMM
Time without seconds: H = Hour; m = Minute.
"""
,
"""
HHMMSS
Time with seconds: H = Hour; m = Minute; s = Seconds.
"""
,
"""
HHMMSSZZZ
See 402 plus Z=Time zone.
"""
,
"""
MMMMSS
Time without hours: m=minutes, s=seconds.
"""
,
"""
ZHHMM
Offset from Coordinated Universal Time (UTC) where Z is
plus (+) or minus (-).
"""
,
"""
HHMMHHMM
Time span without seconds: H = Hour; m = Minute;.
"""
,
"""
HHMMSS-HHMMSS
A period of time specified by giving the start time
followed by the end time (both expressed by hours
minutes and seconds). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
HHMMSSZZZ-HHMMSSZZZ
A period of time specified by giving the start time
followed by the end time (both expressed by hours
minutes, seconds and time zone). Data is to be
transmitted as consecutive characters without hyphen.
"""
,
"""
CC
Century.
"""
,
"""
YY
Calendar year: Y = Year.
"""
,
"""
CCYY
Calendar year including century: C = Century; Y = Year.
"""
,
"""
YYS
Semester in a calendar year: Y = Year; S = Semester.
"""
,
"""
CCYYS
Semester in a calendar year: C = Century; Y = Year; S =
Semester.
"""
,
"""
CCYYQ
Quarter in a calendar year: C = Century; Y = Year; Q =
Quarter.
"""
,
"""
YYMM
Month within a calendar year: Y = Year; M = Month.
"""
,
"""
CCYYMM
Month within a calendar year: CC = Century; Y = Year; M
= Month.
"""
,
"""
YYMMA
To specifiy a ten-day period within a month of a year (A
= ten day period).
"""
,
"""
CCYYMMA
To specifiy a ten-day period within a month of a year,
including century
(A = ten day period).
"""
,
"""
YYWW
Week within a calendar year: Y = Year; W = Week 1st week
of January = week 01.
"""
,
"""
CCYYWW
Week within a calendar year: CC = Century; Y = Year; W =
Week (1st week of January = week 01).
"""
,
"""
YY-YY
A period of time specified by giving the start year
followed by the end year (both without century). Data is
to be transmitted as consecutive characters without
hyphen.
"""
,
"""
CCYY-CCYY
A period of time specified by giving the start year
followed by the end year (both including century). Data
is to be transmitted as consecutive characters without
hyphen.
"""
,
"""
YYS-YYS
A period of time specified by giving the start semester
of a year followed by the end semester of a year (both
not including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
CCYYS-CCYYS
A period of time specified by giving the start semester
of a year followed by the end semester of a year (both
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
YYPYYP
Format of period to be given without hyphen (P = period
of 4 months).
"""
,
"""
CCYYP-CCYYP
Format of period to be given without hyphen (P = period
of 4 months).
"""
,
"""
YYQ-YYQ
A period of time specified by giving the start quarter
of a year followed by the end quarter of year (both not
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
CCYYQ-CCYYQ
A period of time specified by giving the start quarter
of a year followed by the end quarter of year (both
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
YYMM-YYMM
A period of time specified by giving the start month of
a year followed by the end month of a year (both not
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
CCYYMM-CCYYMM
A period of time specified by giving the start month of
a year followed by the end month of a year (both
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
YYMMDDHHMM-YYMMDDHHMM
A period of time specified by giving the start time
followed by the end time (format year, month, day, hour
and minute). Data is to be transmitted as consecutive
characters without hyphen.
"""
,
"""
YYWW-YYWW
A period of time specified by giving the start week of a
year followed by the end week of year (both not
including century). Data is to be transmitted as
consecutive characters without hyphen.
"""
,
"""
CCYYWW-CCYYWW
A period of time specified by giving the start week of a
year followed by the end week of year (both including
century). Data is to be transmitted as consecutive
characters without hyphen.
"""
,
"""
YYMMDD-YYMMDD
A period of time specified by giving the start date
followed by the end date (both not including century).
Data is to be transmitted as consecutive characters
without hyphen.
"""
,
"""
CCYYMMDD-CCYYMMDD
A period of time specified by giving the start date
followed by the end date (both including century). Data
is to be transmitted as consecutive characters without
hyphen.
"""
,
"""
CCYYMMDDHHMM-CCYYMMDDHHMM
A period of time which includes the century, year,
month, day, hour and minute. Format of period to be
given in actual message without hyphen.
"""
,
"""
DHHMM-DHHMM
Format of period to be given without hyphen (D=day of
the week, 1=Monday; 2=Tuesday; ... 7=Sunday).
"""
,
"""
Year
To indicate a quantity of years.
"""
,
"""
Month
To indicate a quantity of months.
"""
,
"""
Week
To indicate a quantity of weeks.
"""
,
"""
Day
To indicate a quantity of days.
"""
,
"""
Hour
To indicate a quantity of hours.
"""
,
"""
Minute
To indicate a quantity of minutes.
"""
,
"""
Second
To indicate a quantity of seconds.
"""
,
"""
Semester
To indicate a quantity of semesters (six months).
"""
,
"""
Four months period
To indicate a quantity of four months periods.
"""
,
"""
Trimester
To indicate a quantity of trimesters (three months).
"""
,
"""
Half month
To indicate a quantity of half months.
"""
,
"""
Ten days
To indicate a quantity of ten days periods.
"""
,
"""
Day of the week
Numeric representation of the day (Monday = 1).
"""
,
"""
Working days
Number of working days.
"""
)

def get_description(position):
    position = int(position)
    position -= 1
    #global description_name_code
    try:
        return __description_name_code[position]
    except:
        return ''

import datetime
# 2 - 7
dtmf = ('%d%m%y', '%m%d%y', '%d%m%Y', '%d%m%Y%H%M', '%Y%m%%', '%Y%m%W')
# 8 - 10
dtmf2 = ('%Y%m%d', '%Y%m%d', '%Y%m%d%H%M')
# 101 - 110
dtmf3 = ('%y%m%d', '%Y%m%d', '%y%W%w', '%m%W-%m%W', '%y%d%w', '%m%d', '107', '%W', '%m', '%d')
# 201 - 210
dtmf4 = ('%y%m%d%H%M', '%y%m%d%H%M%S', '%Y%m%d%H%M', '%Y%m%d%H%M%S', '%Y%m%d%H%M%z', '%y%m%d%H%M%z', '%y%m%d%H%M%S%z', '%Y%m%d%H%M%S%z', '%H%M%S%z', '%H%M%S%z-%H%M%S%z')
# 301 - 308
dtmf5 = ('%y%m%d%H%M%Z', '%y%m%d%H%M%S%Z', '%Y%m%d%H%M%Z', '%Y%m%d%H%M%S%Z', '%m%d%H%M', '%d%H%M', '%Y%m%d%H%M%S%f', '%Y%m%d%H%M%Z-%Y%m%d%H%M%Z')
# 401 - 402
dtmf6 = ('%H%M', '%H%M%S')
# 404 - 409
dtmf6_2 =  ('%H%M%S%Z', '405', '406') 
# 405 : MMMMSS  Time without hours: m=minutes, s=seconds.
# 406 : ZHHMM   Offset from Coordinated Universal Time (UTC) where Z is plus (+) or minus (-).
# 501- 503
dtmf7 = ('%H%M%H%M', '%H%M%S-%H%M%S', '%H%M%S%Z-%H%M%S%Z')
# 600 - 616
dtmf8 = ('%C', '%y', '%Y', '%yS', '%YS', '%YQ', '%y%m', '%Y%m', '%y%mA', '%Y%mA', '%y%W', '%Y%W')
# 701 - 720
dtmf9 = ('%y-%y', '%Y-%Y', '%yS-%yS', '%YS-%YS', '%yP%yP', '%YP-%YP', '%y-%y', '%Y-%Y', '%y%m-%y%m', '%Y%m-%Y%m', '%y%m%d%H%M-%y%m%d%H%M', '%y%W-%y%W', '%Y%W-%Y%W', '%y%m%d-%y%m%d', '%Y%m%d-%Y%m%d', '%Y%m%d%H%M-%Y%m%d%H%M', '%u%H%M-%u%H%M')
# 801 - 814
dtmf10 = ('Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second', 'Semester', 'Four months period', 'Trimester', 'Half month', 'Ten days', 'Day of the week', 'Working days')

def transform_time(timeString, code_id):
    position = int(code_id)
    if position<8: # 2 - 7
        position -= 2
        time_format = dtmf[position]
    elif position == 8: # '%Y%m%dS' # 8
        position -= 8
        dayshift = timeString[-1:] #ignoring
        timeString = timeString[:-1]
        time_format = dtmf2[position]
    elif position == 9: # '%Y%m%dPP' # 9
        position -= 8
        timeperiod = timeString[-2:] # ignoring
        timeString = timeString[:-2]
        time_format = dtmf2[position]
        # timeperiod = PP=00-99 time period.
    elif position==10: # '%Y%m%dT%H%M' # 10
        position -= 8
        tmpTimeString = timeString[:-5] #removing seperator 'T'
        tmpTimeString += timeString[9:]
        timeString = tmpTimeString
        time_format = dtmf2[position]

    elif (position>100) & (position<111): # 101 - 110
        position -= 101
        if position == 6: # 107
            return timeString # 'DDD'
        else:
            time_format = dtmf3[position]
    elif (position>200) & (position<211): # 201 - 210
        position -= 201
        time_format = dtmf4[position]
    elif (position>300) & (position<309): # 301 - 308
        position -= 301
        time_format = dtmf5[position]
    elif (position>400) & (position<403): # 401 - 402
        position -= 401
        time_format = dtmf6[position]
    elif (position>400) & (position<309): # 404 - 409
        position -= 404
        if position == 0: # 404
            time_format = dtmf6_2[position]
        elif position == 1:
            minutes = timeString[:4]
            seconds = timeString[4:]
            hours = minutes/60
            minutes = minutes%60
            return (hours, minutes, seconds)
        else:
            return timeString
    elif (position>500) & (position<504): # 501 - 503
        position -= 501
        time_format = dtmf7[position]
    elif (position>599) & (position<617): # 600 - 616
        position -= 600
        time_format = dtmf8[position]
    elif (position>700) & (position<721): # 701 - 720
        position -= 701
        time_format = dtmf8[position]
    else:
        return timeString
    try:
        utcDT = datetime.datetime.strptime(timeString,time_format)
        # print('Done DT_Transform: ',timeString, time_format)
        return utcDT
    except:
        return timeString

# print(transform_time('2','110'))