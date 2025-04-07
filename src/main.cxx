#include <iostream>
#include <agrum/BN/BayesNet.h>
#include <agrum/base/multidim/tensor.h>

int main()
{
  auto bn = gum::BayesNet< double >::fastPrototype("A->B<-C");
  auto p = gum::Tensor(bn.cpt("B"));
  std::cout << "min="<<p.min() << std::endl;
  return 0;
}
