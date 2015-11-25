classdef WeekDays
   enumeration
      Monday, Tuesday, Wednesday, Thursday, Friday
   end
end


today = WeekDays.Tuesday;

methods(today)


today = WeekDays.Friday;
['Today is ',char(today)]



function c = Reminder(day)
   % Add error checking here
   switch(day)
      case WeekDays.Monday
         c = 'Department meeting at 10:00';
      case WeekDays.Tuesday
         c = 'Meeting Free Day!';
      case {WeekDays.Wednesday WeekDays.Friday}
         c = 'Team meeting at 2:00';
      case WeekDays.Thursday
         c = 'Volley ball night';
   end
end

classdef Bearing < uint32
   enumeration
      North (0)
      East  (90)
      South (180)
      West  (270)
   end
end
a = Bearing.East;


classdef WeekDays
   enumeration
      Monday, Tuesday, Wednesday, Thursday, Friday
   end
   methods
      function tf = isMeetingDay(obj)
         tf = ~(WeekDays.Tuesday == obj);
      end
   end
end