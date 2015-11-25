classdef (Sealed) MyClass < handle
   properties (Access = private)
      Prop1 = datenum(date);
   end
   properties
      Prop2
   end
   methods
      function obj = MyClass(x)
         obj.Prop2 = x;
      end
   end
   methods (Access = {?MyOtherClass})
      function d = myMethod(obj)
         d = obj.Prop1 + x;
      end
   end
   events (ListenAccess = protected)
      StateChanged
   end
end