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

class DarcyFrictionFactorMaterialFunctor : public FunctorMaterial
{
public:
  static InputParameters validParams();

  DarcyFrictionFactorMaterialFunctor(const InputParameters & parameters);

protected:
  const Moose::Functor<ADReal> & _mu;          
  const Moose::Functor<ADReal> & _rho;          
  const Moose::Functor<ADReal> & _porosity;
  //const Moose::Functor<ADReal> & _c;
  const Moose::Functor<ADReal> & _Dp_1;
  const Moose::Functor<ADReal> & _Dp_2;


};
