# %%
'''
Example implementations of HARK.ConsumptionSaving.ConsPortfolioModel
'''
from HARK.ConsumptionSaving.ConsRiskyAssetModel import RiskyContribConsumerType, init_risky_contrib
from time import time
from copy import copy

from tools import plotSlices3D, plotSlices4D

# %% Base parametrization

# Make the problem infinite horizon
par_infinite_base = init_risky_contrib.copy()
par_infinite_base['cycles']   = 0

# and frictionless to start
par_infinite_base['AdjustPrb'] = 1.0
par_infinite_base['tau'] = 0.0

# Make contribution shares a continuous choice
par_infinite_base['DiscreteShareBool'] = False
par_infinite_base['vFuncBool'] = False

# %% A version with the tax
par_infinite_tax = copy(par_infinite_base)
par_infinite_tax['tau'] = 0.1

# %% A version with the Calvo friction
par_infinite_calvo = copy(par_infinite_base)
par_infinite_calvo["AdjustPrb"] = 0.25

# %% Create and solve agents with all the parametrizations

agents = {'Base': RiskyContribConsumerType(**par_infinite_base),
          'Tax': RiskyContribConsumerType(**par_infinite_tax),
          'Calvo': RiskyContribConsumerType(**par_infinite_calvo)}

for agent in agents:
    
    print('Now solving ' + agent)
    t0 = time()
    agents[agent].solve(verbose = True)
    t1 = time()
    print('Solving ' + agent +' took ' + str(t1-t0) + ' seconds.')