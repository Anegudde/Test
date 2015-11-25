if rem(n,2) ~= 0
	M = odd_magic(n)
elseif rem(n,4) ~= 0
	M = single_even_magic(n)
else
	M = double_even_magic(n)
end


if A > B
	'greater'
elseif A < B
	'less'
elseif A == B
	'equal'
else
	error('Unexpected situation')
end


switch (rem(n,4)==0) + (rem(n,2)==0)
	case 0
		M = odd_magic(n)
	case 1
		M = single_even_magic(n)
	case 2
		M = double_even_magic(n)
	otherwise
		error('This is impossible')
end


for n = 3:32
	r(n) = rank(magic(n));
end
r


a = 0; fa = -Inf;
b = 3; fb = Inf;
while b-a > eps*b
	x = (a+b)/2;
	fx = x^3-2*x-5;
	if sign(fx) == sign(fa)
		a = x; fa = fx;
	else
		b = x; fb = fx;
	end
end
x


fid = fopen('magic.m','r');
count = 0;
	while ~feof(fid)
		line = fgetl(fid);
		if isempty(line) | strncmp(line,'%',1)
		continue
	end
	count = count + 1;
end
disp(sprintf('%d lines',count));

%{
Matlab Comment
%}
a = 0; fa = -Inf;
b = 3; fb = Inf;
while b-a > eps*b
	x = (a+b)/2;
	fx = x^3-2*x-5;
	if fx == 0
		break
	elseif sign(fx) == sign(fa)
		a = x; fa = fx;
	else
		b = x; fb = fx;
	end
end
x