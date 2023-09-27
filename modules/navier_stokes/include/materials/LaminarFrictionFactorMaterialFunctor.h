//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#pragma once

#include "FunctorMaterial.h"

class LaminarFrictionFactorMaterialFunctor : public FunctorMaterial
{
public:
  static InputParameters validParams();

  LaminarFrictionFactorMaterialFunctor(const InputParameters & parameters);

protected:
  const Moose::Functor<ADReal> & _mu;                
  const Moose::Functor<ADReal> & _porosity;
  const Moose::Functor<ADReal> & _D_h;

};
