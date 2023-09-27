//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "ContractionFrictionFactorMaterialFunctor.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", ContractionFrictionFactorMaterialFunctor);

InputParameters
ContractionFrictionFactorMaterialFunctor::validParams()
{
  InputParameters params = FunctorMaterial::validParams();
  params += SetupInterface::validParams();
  params.set<ExecFlagEnum>("execute_on") = {EXEC_ALWAYS};
  params.addClassDescription(
      "Something smart.");
  params.addParam<MooseFunctorName>("A_1", "The functor corresponding to the bigger cross section.");
  params.addParam<MooseFunctorName>(
      "A_2", "The functor corresponding to the smaller cross section.");
  params.addParam<MooseFunctorName>(
      "L", "The functor corresponding to the length where the contraction is localized.");
  params.addParam<MooseFunctorName>(
      "porosity", 1, "The functor corresponding to the porosity.");
  params.addParam<MooseFunctorName>(
      "rho", "The functor corresponding to the density.");
  return params;
}

ContractionFrictionFactorMaterialFunctor::ContractionFrictionFactorMaterialFunctor(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _A_1(getFunctor<ADReal>("A_1")),
    _A_2(getFunctor<ADReal>("A_2")),
    _L(getFunctor<ADReal>("L")),
    _porosity(getFunctor<ADReal>("porosity")),
    _rho(getFunctor<ADReal>("rho"))
    

{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());

  addFunctorProperty<ADReal>(
        "contraction_friction_factor",
        [this](const auto & r, const auto & t) -> ADReal
        { 
          auto  K = std::pow(((_A_1(r,t)/_A_2(r,t))-1),2);
          auto value = K*_rho(r,t)/(2*_L(r,t)*std::pow(_porosity(r,t),2));
          return value;
        },
        clearance_schedule);
}
