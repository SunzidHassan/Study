function [ysum, ydiff] = square_cube_sum2(x1, x2)
  ysum = x1*x1 + x2*x2*x2;
  ydiff = x2*x2*x2 - x1*x1;
end