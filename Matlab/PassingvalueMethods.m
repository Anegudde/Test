classdef SimpleClass
   properties
      Color
   end
   methods
      function obj = SimpleClass(c)
         if nargin > 0
            obj.Color = c;
         end
      end
   end
end

obj = SimpleClass('red');

function y = g(x)
   x.Color = 'blue';
   y = x;
end
y = g(obj);
obj.Color