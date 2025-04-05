#!/usr/bin/env python

import pyagrum as gum

# min bug
bn = gum.fastBN("a->b<-c")
p = bn.cpt("b")
print("min=", p.min())

# https://gitlab.com/agrumery/aGrUM/issues/15
bn = gum.fastBN('a->b->d;a->c->d->e;f->b')
ie = gum.LazyPropagation(bn)
ie.makeInference()
print(ie.posterior('d'))

# https://gitlab.com/agrumery/aGrUM/issues/24
bn = gum.fastBN('a->b')
jointe = gum.Tensor().fillWith(1)
#for i in range(2):
    #jointe *= bn.cpt(i)
print(jointe)

