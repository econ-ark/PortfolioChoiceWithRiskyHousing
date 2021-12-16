import numpy as np

# %% Preferences

# Relative risk aversion
CRRA = 10
# Discount factor
DiscFac = 0.96

# Survival probabilities
n = 14
survprob = np.ones(n)
# Now we have 14 probabilities of death,
# for ages 30 to 95, every 5 years

# Labor income

# They assume its a polinomial of age. Here are the coefficients
a = -2.170042 + 2.700381
b1 = 0.16818
b2 = -0.0323371 / 10
b3 = 0.0019704 / 100

time_params = {"Age_born": 1, "Age_retire": 7, "Age_death": 15}
# born = 30, retire = 60, death = 100
t_start = time_params["Age_born"]
t_ret = time_params[
    "Age_retire"
]  # We are currently interpreting this as the last period of work
t_end = time_params["Age_death"]

# They assume retirement income is a fraction of labor income in the
# last working period
repl_fac = 0.68212

# Compute average income at each point in (working) life
f = np.arange(t_start, t_ret + 1) * 5 + 25
f = a + b1 * f + b2 * (f ** 2) + b3 * (f ** 3)
det_work_inc = np.exp(f)

# Retirement income
det_ret_inc = repl_fac * det_work_inc[-1] * np.ones(t_end - t_ret)

# Get a full vector of the deterministic part of income
det_income = np.concatenate((det_work_inc, det_ret_inc))

# ln Gamma_t+1 = ln f_t+1 - ln f_t
gr_fac = np.exp(np.diff(np.log(det_income)))

# Now we have growth factors for T_end-1 periods.

# Finally define the normalization factor used by CGM, for plots.
# ### IMPORTANT ###
# We adjust this normalization factor for what we believe is a typo in the
# original article. See the REMARK jupyter notebook for details.
norm_factor = det_income * np.exp(0)

# %% Shocks

# Transitory and permanent shock variance from the paper
std_tran_shock = np.sqrt(5 * 0.0738)
std_perm_shock = 0

# Vectorize. (HARK turns off these shocks after T_retirement)
std_tran_vec = np.array([std_tran_shock] * (t_end - t_start))
std_perm_vec = np.array([std_perm_shock] * (t_end - t_start))

# %% Financial instruments

# Risk-free factor over 5 years
Rfree = 1.02 ** 5

# Creation of risky asset return distributions

# 1 year equity premium is 0.06, so 1 year risky return is Mu + Rfree = 1.08
# To calculate 5 year equity premium, 1.08 ** 5 - Rfree ** 5
Mu = 1.08 ** 5 - Rfree  # Equity premium over 5 years
Std = np.sqrt(5 * 0.157 ** 2)  # standard deviation of rate-of-return shocks

T_cycle = t_end - t_start

RiskyAvg = [Mu + Rfree] * T_cycle
RiskyStd = list(np.linspace(Std, Std + 0.2, T_cycle))

RiskyAvgTrue = Mu + Rfree
RiskyStdTrue = Std

ExRiskyShareBool = True
ExRiskyShare = [1.0] * 7 + [0.5] * 7
FixRiskyAvg = True
FixRiskyStd = False
WlthNrmAvg = np.linspace(1.0, 20.0, 14)

# Make a dictionary to specify the rest of params
dict_portfolio = {
    # Usual params
    "CRRA": CRRA,
    "Rfree": Rfree,
    "DiscFac": DiscFac,
    # Life cycle
    "T_age": t_end - t_start + 1,  # Time of death
    "T_cycle": t_end - t_start,  # Number of non-terminal periods
    "T_retire": t_ret - t_start + 1,
    "LivPrb": survprob.tolist(),
    "PermGroFac": gr_fac.tolist(),
    "cycles": 1,
    # Income shocks
    "PermShkStd": std_perm_vec,
    "PermShkCount": 1,
    "TranShkStd": std_tran_vec,
    "TranShkCount": 9,
    "UnempPrb": 0,
    "UnempPrbRet": 0,
    "IncUnemp": 0,
    "IncUnempRet": 0,
    "BoroCnstArt": 0,
    "tax_rate": 0.0,
    # Portfolio related params
    "RiskyAvg": RiskyAvg,
    "RiskyStd": RiskyStd,
    "RiskyAvgTrue": RiskyAvgTrue,
    "RiskyStdTrue": RiskyStdTrue,
    "RiskyCount": 3,
    "RiskyShareCount": 30,
    # Grid
    "aXtraMin": 0.001,
    "aXtraMax": 400,
    "aXtraCount": 400,
    "aXtraExtra": [None],
    "aXtraNestFac": 3,
    # General
    "vFuncBool": False,
    "CubicBool": False,
    # Simulation params
    "AgentCount": 10,
    # Mean of log initial permanent income (only matters for simulation)
    "pLvlInitMean": np.log(det_income[0]),
    "pLvlInitStd": std_perm_shock,  # Standard deviation of log initial permanent income (only matters for simulation)
    "T_sim": (t_end - t_start + 1) * 50,
    # Unused params required for simulation
    "PermGroFacAgg": 1,
    "aNrmInitMean": -50.0,  # Agents start with 0 assets (this is log-mean)
    "aNrmInitStd": 0.0,
    # Beliefs
    "ExRiskyShareBool": True,
    "ExRiskyShare": np.linspace(1.0, 0.5, 14),
    "FixRiskyAvg": False,
    "FixRiskyStd": True,
    "WlthNrmAvg": np.linspace(1.0, 20.0, 14),
}

age_plot_params = [6, 7, 8, 10, 12, 14]
