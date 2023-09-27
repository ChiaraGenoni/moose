//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "LaminarFrictionFactorMaterialFunctor.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", LaminarFrictionFactorMaterialFunctor);

InputParameters
LaminarFrictionFactorMaterialFunctor::validParams()
{
  InputParameters params = FunctorMaterial::validParams();
  params += SetupInterface::validParams();
  params.set<ExecFlagEnum>("execute_on") = {EXEC_ALWAYS};
  params.addClassDescription(
      "Something smart.");
  params.addParam<MooseFunctorName>("mu", "The functor corresponding to the viscosity.");
  params.addParam<MooseFunctorName>(
      "porosity", 0, "The functor corresponding to the porosity.");
  params.addParam<MooseFunctorName>(
      "D_h", "The functor corresponding to the hydraulic diameter.");
  return params;
}

LaminarFrictionFactorMaterialFunctor::LaminarFrictionFactorMaterialFunctor(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _mu(getFunctor<ADReal>("mu")),
    _porosity(getFunctor<ADReal>("porosity")),
    _D_h(getFunctor<ADReal>("D_h"))
{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());

  addFunctorProperty<ADReal>(
        "laminar_friction_factor",
        [this](const auto & r, const auto & t) -> ADReal
        {
          auto value = 32*_mu(r,t)/std::pow(_D_h(r,t),2)/_porosity(r,t);
          return ADReal(value);
        },
        clearance_schedule);
}
