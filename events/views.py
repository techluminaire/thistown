from django.http import HttpResponse
from django.template import RequestContext, loader
import calendar

# Create your views here.
def event_index(request, year, month, day): 
    #Default page not found view
    template = loader.get_template('events/event_index.html')
    context = RequestContext(request,{
                                      'calendar': create_calendar(),                     
                                      }) 
    response = template.render(context)
    return HttpResponse(response)  



def create_calendar():
    cal = EventCalendar()
    return cal.formatmonth(2007, 7)

class EventCalendar(calendar.HTMLCalendar):
    def formatday(self, day, weekday):
        """
          Return a day as a table cell.
        """
        
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            
            return '<td><input type="submit" id="{0}" class="event_day" value="{1}"></td>'.format(day, day)
            #return '<td class="%s"><a href="%s">%d</a></td>' % (self.cssclasses[weekday], weekday, day)