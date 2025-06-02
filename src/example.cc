#include <cstdio>
#include <vector>
#include "gkls.hh"

int main(int argc, char **argv)
{
  GKLS gkls(2, 2, -1, 1, -1, "g");
  std::vector<double> x = {0.5, 0.5};
  double y = gkls.get_d_func(x);
  printf("D_f x = %g\n", y);

  GKLS gkls2(2, 2, -1, 1, -1, "g");
  double y2 = gkls2.get_d_func(x);
  printf("y1 = %g, y2 = %g\n", gkls.get_d_func(x), y2);
  return 0;
}