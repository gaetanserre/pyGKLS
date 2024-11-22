#include <random>
#include "rnd_gen.hh"

std::default_random_engine engine;
std::uniform_real_distribution<double> dist(0.0, 1.0);

void ranf_start(long seed)
{
  engine.seed(seed);
}

void ranf_array(double aa[], int n)
{
  for (int i = 0; i < n; i++)
  {
    aa[i] = dist(engine);
  }
}