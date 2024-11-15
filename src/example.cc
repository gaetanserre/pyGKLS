#include <cstdio>
#include <vector>
#include "wrapper.hh"

int main(int argc, char **argv)
{
  GKLS::set_default();
  GKLS::generate(1);
  std::vector<double> x = {0.5, 0.5};
  printf("D_f x = %f\n", GKLS::get_d_func(x));
  return 0;
}