//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "FrictionFactorFromMuMaterial.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", FrictionFactorFromMuMaterial);

InputParameters
FrictionFactorFromMuMaterial::validParams()
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
      "c_x", "The functor corresponding to the friction factor constant.");
  params.addParam<MooseFunctorName>(
      "c_y", "The functor corresponding to the friction factor constant.");
  params.addParam<MooseFunctorName>(
      "c_z", "The functor corresponding to the friction factor constant.");

  return params;
}

FrictionFactorFromMuMaterial::FrictionFactorFromMuMaterial(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _mu(getFunctor<ADReal>("mu")),
    _porosity(getFunctor<ADReal>("porosity")),
    _c_x(getFunctor<Real>("c_x")),
    _c_y(getFunctor<Real>("c_y")),
    _c_z(getFunctor<Real>("c_z"))
{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());

  addFunctorProperty<ADRealVectorValue>(
        "darcy_friction_factor",
        [this](const auto & r, const auto & t) -> ADRealVectorValue
        {
          auto value = _mu(r,t)*(1-std::pow(_porosity(r,t),2))/std::pow(_porosity(r,t),3);
          return ADRealVectorValue(value/_c_x(r,t), value/_c_y(r,t), value/_c_z(r,t));
        },
        clearance_schedule);
}
