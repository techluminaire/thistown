
#Allows suffixes on the end of days i.e. 1 => 1st, 2 => 2nd
#from http://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime
#Usage print custom_strftime('%B {S}, %Y', datetime.datime.now()) => May 5th, 2011
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(date_time_format, t):
    return t.strftime(date_time_format).replace('{S}', str(t.day) + suffix(t.day))