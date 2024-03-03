function [mn, md, mdn] = sol_14b_vector_MeanModeMedian(x)
  mn = mean(x);
  md = mode(x);
  mdn = median(x);
end