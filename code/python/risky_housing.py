# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: PyCharm (PortfolioChoiceWithRiskyHousing-Latest)
#     language: python
#     name: pycharm-2f4f0d29
# ---

# %%
from ConsPortfolioHousingModel import (
    PortfolioRiskyHousingType,
    ConsPortfolioRiskyHousingSolver,
    init_portfolio_risky_housing,
)

import numpy as np
import matplotlib.pyplot as plt

from HARK.ConsumptionSaving.ConsPortfolioModel import PortfolioConsumerType

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
agent = PortfolioRiskyHousingType()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
solver = ConsPortfolioRiskyHousingSolver.from_agent(agent)
# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
solver.prepare_to_solve()
solver.solve()
# %% pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = solver.cFuncHse_now(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.plot(M, solver.rental_solution.cFuncRnt(M), label="rent")
plt.legend()
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
M = np.linspace(0.0, 5000, 1000)
for h in np.linspace(2.0, 10.0, 3):
    C = solver.cFuncHse_now.derivativeX(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.legend()
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
M = np.linspace(1.0, 10, 1000)
for h in np.linspace(2.0, 10.0, 3):
    C = solver.vPfuncHse_now(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.legend()
plt.xscale("log")
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = solver.ShareFuncHse_now(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.plot(M, solver.rental_solution.ShareFuncRnt(M), label="rent")
plt.legend()
plt.show()

# %%
agent.solve()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = agent.solution[0].cFuncHse(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.plot(M, agent.solution[0].cFuncRnt(M), label="rent")
plt.legend()
plt.show()

# %% pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
M = np.linspace(0.0, 5000, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = agent.solution[0].cFuncHse.derivativeX(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.legend()
plt.show()

# %%
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = agent.solution[0].ShareFuncHse(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.plot(M, agent.solution[0].ShareFuncRnt(M), label="rent")
plt.legend()
plt.show()

# %% pycharm={"name": "#%%\n"} jupyter={"outputs_hidden": false}
M = np.linspace(1.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = agent.solution[0].vFuncHse(M, h * np.ones_like(M))
    plt.plot(M, C, label=h)
plt.legend()
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
ShareFuncRnt = [soln.ShareFuncRnt for soln in agent.solution]

M = np.linspace(0.0, 100, 100)
for func in ShareFuncRnt:
    C = func(M)
    plt.plot(M, C)
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
vFuncRnt = [soln.vFuncRnt for soln in agent.solution]

M = np.linspace(1.0, 100, 100)
for func in vFuncRnt:
    C = func(M)
    plt.plot(M, C)
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
agent_portfolio = PortfolioConsumerType(**init_portfolio_risky_housing)
agent_portfolio.solve()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
ShareFuncAdj = [soln.ShareFuncAdj for soln in agent_portfolio.solution]

M = np.linspace(0.0, 100, 100)
for func in ShareFuncAdj:
    C = func(M)
    plt.plot(M, C)
plt.show()

# %% jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
