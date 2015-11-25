classdef Cube < Shape
   properties
      SideLength = 0;
      Color = [0 0 0];
   end
   methods
      function cubeObj = Cube(length,color,upvector,viewangle)
         if nargin == 0
            super_args{1} = [0 0 1];
            super_args{2} = 10;
         elseif nargin == 4
            super_args{1} = upvector;
            super_args{2} = viewangle;
         else
            error('Wrong number of input arguments')
         end
         cubeObj@Shape(super_args{:});
         if nargin > 0 % Use value if provided
            cubeObj.SideLength = length;
            cubeObj.Color = color;
         end
         ...
      end
   ...
   end
end


classdef myClass < baseClass1
   properties
      ComputedValue
   end
   methods
      function obj = myClass(a,b,c)

%%% Pre Initialization %%%
% Any code not using output argument (obj)
         if nargin == 0
         % Provide values for superclass constructor
         % and initialize other inputs 
            a = someDefaultValue;
            args{1} = someDefaultValue;
            args{2} = someDefaultValue;
         else
           % When nargin ~= 0, assign to cell array, 
           % which is passed to supclass constructor
            args{1} = b;
            args{2} = c;
         end
         compvalue = myClass.staticMethod(a);

%%% Object Initialization %%%
% Call superclass constructor before accessing object
% You cannot conditionalize this statement
         obj = obj@baseClass1(args{:});

%%% Post Initialization %%%
% Any code, including access to object
         obj.classMethod(...);
         obj.ComputedValue = compvalue;
         ...
      end
      ...
   end
   ...
end