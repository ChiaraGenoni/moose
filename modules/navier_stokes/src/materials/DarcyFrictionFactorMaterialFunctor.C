//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "DarcyFrictionFactorMaterialFunctor.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", DarcyFrictionFactorMaterialFunctor);

InputParameters
DarcyFrictionFactorMaterialFunctor::validParams()
{
  InputParameters params = FunctorMaterial::validParams();
  params += SetupInterface::validParams();
  params.set<ExecFlagEnum>("execute_on") = {EXEC_ALWAYS};
  params.addClassDescription(
      "Something smart.");
  params.addParam<MooseFunctorName>("mu", "The functor corresponding to the viscosity.");
  params.addParam<MooseFunctorName>("rho", "The functor corresponding to the density.");
  params.addParam<MooseFunctorName>(
      "porosity", 0, "The functor corresponding to the porosity.");
  // params.addParam<MooseFunctorName>(
  //     "c", "The functor corresponding to the friction factor constant.");
  params.addParam<MooseFunctorName>(
      "Dp_1", "The functor corresponding to the particle diameter in Darcy coefficient.");
        params.addParam<MooseFunctorName>(
      "Dp_2", "The functor corresponding to the particle diameter in Forechheimer coefficient.");

  return params;
}

DarcyFrictionFactorMaterialFunctor::DarcyFrictionFactorMaterialFunctor(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _mu(getFunctor<ADReal>("mu")),
    _rho(getFunctor<ADReal>("rho")),
    _porosity(getFunctor<ADReal>("porosity")),
    // _c(getFunctor<ADReal>("c"))
    _Dp_1(getFunctor<ADReal>("Dp_1")),
    _Dp_2(getFunctor<ADReal>("Dp_2"))

{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());

  addFunctorProperty<ADReal>(
        "darcy_friction_factor",
        [this](const auto & r, const auto & t) -> ADReal
        {
          auto value = _mu(r,t)*std::pow((1-_porosity(r,t)),2)/std::pow(_porosity(r,t),3);
          //return ADReal(value/_c(r,t));
          return ADReal(150./std::pow(_Dp_1(r,t),2) * value);
        },
        clearance_schedule);

  addFunctorProperty<ADReal>(
        "forchheimer_friction_factor",
        [this](const auto & r, const auto & t) -> ADReal
        {
          auto value = _rho(r,t)*(1-_porosity(r,t))/std::pow(_porosity(r,t),3);
          //return ADReal(value/_c(r,t));
          return ADReal(1.75 / _Dp_2(r,t) * value);
        },
        clearance_schedule);
}
