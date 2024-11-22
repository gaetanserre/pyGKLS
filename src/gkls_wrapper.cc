#include "gkls.hh"

double *gen_point(vector<double> &x)
{
  double *point = (double *)malloc(x.size() * sizeof(double));
  for (int i = 0; i < x.size(); i++)
  {
    point[i] = x[i];
  }
  return point;
}

vector<double> list_to_vec(double *l, unsigned int size)
{
  vector<double> result(size);
  for (int i = 0; i < size; i++)
  {
    result[i] = l[i];
  }
  return result;
}

double GKLS::get_d_func(vector<double> x)
{
  double *point = gen_point(x);
  double result = GKLS_D_func(point);
  free(point);
  return result;
}

double GKLS::get_d2_func(vector<double> x)
{
  double *point = gen_point(x);
  double result = GKLS_D2_func(point);
  free(point);
  return result;
}

double GKLS::get_nd_func(vector<double> x)
{
  double *point = gen_point(x);
  double result = GKLS_ND_func(point);
  free(point);
  return result;
}

vector<double> GKLS::get_d_gradient(vector<double> x)
{
  double *point = gen_point(x);
  double *gradient = (double *)malloc(x.size() * sizeof(double));
  GKLS_D_gradient(point, gradient);
  vector<double> result = list_to_vec(gradient, x.size());
  free(point);
  free(gradient);
  return result;
}

vector<double> GKLS::get_d2_gradient(vector<double> x)
{
  double *point = gen_point(x);
  double *gradient = (double *)malloc(x.size() * sizeof(double));
  GKLS_D2_gradient(point, gradient);
  vector<double> result = list_to_vec(gradient, x.size());
  free(point);
  free(gradient);
  return result;
}

vector<vector<double>> GKLS::get_d2_hessian(vector<double> x)
{
  double *point = gen_point(x);
  double **hessian = (double **)malloc(x.size() * sizeof(double *));
  for (int i = 0; i < x.size(); i++)
  {
    hessian[i] = (double *)malloc(x.size() * sizeof(double));
  }
  GKLS_D2_hessian(point, hessian);
  vector<vector<double>> result(x.size());
  for (int i = 0; i < x.size(); i++)
  {
    result[i] = list_to_vec(hessian[i], x.size());
    free(hessian[i]);
  }
  free(point);
  free(hessian);
  return result;
}

double GKLS::get_global_minimum()
{
  return GKLS_global_value;
}