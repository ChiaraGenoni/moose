//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "AirSutherlandMuMaterial.h"
#include "Function.h"

registerMooseObject("NavierStokesApp", AirSutherlandMuMaterial);

InputParameters
AirSutherlandMuMaterial::validParams()
{
  InputParameters params = FunctorMaterial::validParams();
  params += SetupInterface::validParams();
  params.set<ExecFlagEnum>("execute_on") = {EXEC_ALWAYS};
  params.addClassDescription(
      "Something smart.");
  params.addParam<MooseFunctorName>("mu_0", 1.716e-5, "viscosity at T = T0.");
  params.addParam<MooseFunctorName>(
      "T_0", 273, "Reference temperature.");
  params.addParam<MooseFunctorName>(
      "S_mu", 111, "Sutherland constant.");
        params.addParam<MooseFunctorName>(
      "T", 300, "Temperature.");
  return params;
}

AirSutherlandMuMaterial::AirSutherlandMuMaterial(
    const InputParameters & parameters)
  : FunctorMaterial(parameters),
    _mu_0(getFunctor<Real>("mu_0")),
    _T_0(getFunctor<Real>("T_0")),
    _T(getFunctor<Real>("T")),
    _S_mu(getFunctor<Real>("S_mu"))
{
  const std::set<ExecFlagType> clearance_schedule(_execute_enum.begin(), _execute_enum.end());



  addFunctorProperty<Real>(
    "sutherland_mu",
        [this](const auto & r, const auto & t) -> Real
        {
          auto value = _mu_0(r,t)*(std::pow(_T(r,t)/_T_0(r,t), 1.5)*(_T_0(r,t) +_S_mu(r,t))/(_T(r,t)+_S_mu(r,t)));
          return Real(value);
        },
        clearance_schedule);
}