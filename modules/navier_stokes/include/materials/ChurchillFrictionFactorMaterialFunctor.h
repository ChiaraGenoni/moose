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

class ChurchillFrictionFactorMaterialFunctor : public FunctorMaterial
{
public:
  static InputParameters validParams();

  ChurchillFrictionFactorMaterialFunctor(const InputParameters & parameters);

protected:
  const Moose::Functor<ADReal> & _Re;                
  const Moose::Functor<ADReal> & _epsilon;
  const Moose::Functor<ADReal> & _D_h;
  const Moose::Functor<ADReal> & _porosity;
  const Moose::Functor<ADReal> & _rho;
};
