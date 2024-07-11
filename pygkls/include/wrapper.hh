#include <vector>

namespace GKLS {
  using namespace std;
  
  void set_default();

  int generate(unsigned int nf);

  void set_dim(unsigned int dim);

  void set_num_minima(unsigned int num_minima);

  void set_domain(double domain_lo, double domain_hi);

  void set_global_dist(double global_dist);

  void set_global_radius(double global_radius);

  void set_global_value(double global_value);

  double get_d_func(vector<double> &x);

  double get_d2_func(vector<double> &x);

  double get_nd_func(vector<double> &x);

  vector<double> get_d_gradient(vector<double> &x);

  vector<double> get_d2_gradient(vector<double> &x);

  vector<vector<double>> get_d2_hessian(vector<double> &x);

  double get_global_minimum();

  void free_gkls();
}