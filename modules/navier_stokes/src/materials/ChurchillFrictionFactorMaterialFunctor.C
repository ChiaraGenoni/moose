//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "ChurchillFrictionFactorMaterialFunctor.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", ChurchillFrictionFactorMaterialFunctor);

InputParameters
ChurchillFrictionFactorMaterialFunctor::validParams()
{
  InputParameters params = FunctorMaterial::validParams();
  params += SetupInterface::validParams();
  params.set<ExecFlagEnum>("execute_on") = {EXEC_ALWAYS};
  params.addClassDescription(
      "Something smart.");
  params.addParam<MooseFunctorName>("Re", "The functor corresponding to the reynolds number.");
  params.addParam<MooseFunctorName>(
      "epsilon", 0, "The functor corresponding to the roughness.");
  params.addParam<MooseFunctorName>(
      "D_h", "The functor corresponding to the hydraulic diameter.");
  params.addParam<MooseFunctorName>(
      "porosity", 1, "The functor corresponding to the porosity.");
  params.addParam<MooseFunctorName>(
      "rho", "The functor corresponding to the density.");
  return params;
}

ChurchillFrictionFactorMaterialFunctor::ChurchillFrictionFactorMaterialFunctor(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _Re(getFunctor<ADReal>("Re")),
    _epsilon(getFunctor<ADReal>("epsilon")),
    _D_h(getFunctor<ADReal>("D_h")),
    _porosity(getFunctor<ADReal>("porosity")),
    _rho(getFunctor<ADReal>("rho"))
    

{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());

  addFunctorProperty<ADReal>(
        "churchill_friction_factor",
        [this](const auto & r, const auto & t) -> ADReal
        { 
          auto  a = std::pow(2.457 * std::log(1.0 / (std::pow(7.0 / _Re(r,t), 0.9) + 0.27 * _epsilon(r,t) / _D_h(r,t))), 16);
          auto  b = std::pow(3.753e4 / _Re(r,t), 16);
          auto value = 2.0 * std::pow(std::pow(8.0 / _Re(r,t), 12) + 1.0 / std::pow(a + b, 1.5), 1.0 / 12.0)*_rho(r,t)/(2*_D_h(r,t)*std::pow(_porosity(r,t),2));
          return value;
        },
        clearance_schedule);
}
