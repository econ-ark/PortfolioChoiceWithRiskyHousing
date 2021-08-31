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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Portfolio Choice with Risky Housing
# ### By Alan Lujan and the Econ-ARK team

# %% [markdown]
# [![badge](https://img.shields.io/badge/launch-binder%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/econ-ark/PortfolioChoiceWithRiskyHousing/HEAD?filepath=code%2Fpython%2Fblog_post.ipynb)    [![badge](https://img.shields.io/badge/launch-binder%20lab-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/econ-ark/PortfolioChoiceWithRiskyHousing/HEAD?urlpath=lab%2Ftree%2Fcode%2Fpython%2Fblog_post.ipynb)

# %% [markdown] pycharm={"name": "#%% md\n"} tags=[]
# Economists have long sought to use models of optimal portfolio choice to try to understand saving and investment decisions over a household's life-cycle. However, as noted in [our previous blog post](https://www.thinkforwardinitiative.com/stories/optimal-financial-investments-over-the-life-cycle) optimal choices implied by state-of-the-art models differ considerably from portfolio choices people actually make.  Here, we show that some of the results from those models may be misleading because the models neglect the implications of homeownership.
#
# Models like the one we examined before account for different types of uncertainty (labor income risk, mortality risk, and stock market risk), and allow for rational risk aversion, impatience, and many other realistic features. One interpretation of the discrepancy between the models' predictions and people's actual choices is that people are not behaving optimally.  Another possibility, though, is that the models are still missing some vitally important (and rational) factor that weighs on people's actual decisions; in this case, the models would be wrong.
#
# For most households homeownership is the biggest financial decision in their lives and, as such, it has implications for their optimal portfolio choice.   Two leading reasons homeownership _should_ matter are that homeownership exposes consumers to housing market price risk, and is associated with certain payment obligations (not just mortgages, but property taxes, maintenance costs, and so on). 
#
# These points may seem obvious, but there is a good reason they have not been incorporated in previous analyses of households' optimal choice:  Taking account of these complexities greatly increases the computational difficulty of calculating mathematically optimal behavior.  This blog post describes results obtained using the latest tools to be added to the [Econ-ARK](https://econ-ark.org/) toolkit; with these tools, it should be much easier for economists, financial planners, and others to understand the appropriate role of homeownership in modifying investors' optimal saving and financial choices.
#
# ### Portfolio Choice
#
# Our [previous blog post, Chris Carroll and the Econ-ARK team](https://www.thinkforwardinitiative.com/stories/optimal-financial-investments-over-the-life-cycle) introduced the module [`ConsPortfolioModel`](https://hark.readthedocs.io/en/latest/reference/ConsumptionSaving/ConsPortfolioModel.html). This tool evaluates the optimal choices of a household which can invest in a risky (but higher expected return) asset or a safe (but certain and lower return) asset. The toolkit is flexible enough to model various lifecycle properties such as varying labor income risk, mortality risk, and stock market inattention and misconceptions. Nevertheless, as discussed in the previous blog post, there are stark differences between this model's predictions and how people actually behave.
#
# ### The Problem: Housing
#
# Perhaps the biggest financial decision in a household's life is buying a house. Houses come in different sizes (and therefore costs), but they are generally an expensive asset that is worth at least a few times the household's yearly income. Young households usually can not buy their houses outright, as they start with little to no assets and take time to accumulate enough resources. For this reason, they rely on mortgages to purchase their houses and take on substantial amounts of debt. These young and leveraged households might thus be too sensitive to stock market risk given their risk tolerance, and cause them to reduce their stock market participation.
#
# During the repayment period, households' market resources (or liquid assets) are reduced by the fixed mortgage payment. This has 2 effects on risky asset choice: 1) It reduces market resources today, making households relatively less wealthy, and 2) It reduces market resources in following periods for any given level of current savings, making households more risk averse due to the precautionary motive. The fixed nature of mortgage payments has another important effect: since the household must be sure to have sufficient resources in the next period to pay their mortgage and the cost of house maintenance, they might want to save more of their resources in a safe account rather than in the risky stock market.
#
# Houses also generally experience price fluctuations that depend on local housing market conditions as well as broader national trends, such as recessions and expansions. The fluctuating selling value of your house, then, can bring additional uncertainty to future net worth and have significant implications regarding portfolio decisions. Because homeowners have implicit holdings in a risky asset which can not be easily adjusted---the house---they may want to reduce their exposure to additional risk and reduce their savings in another risky asset, the stock market. 
#
# Portfolio choice models, such as `ConsPortfolioModel` above, have not been able to match household behavior in the stock market. According to these models, households should all participate in the stock market and, conditional on participating, the risky share of their portfolio should be much higher. In reality, few households participate in the stock market and those who do have a lower-than-expected exposure to stocks. This gap in observed behavior is known in the economics and finance literature as the stock holding puzzle. For the reasons described above, housing might be a significant contributor to the stock-holding puzzle.
#
#
# ### The standard model
#
# Our model is an extension of the `ConsPortfolioModel` with the added features of homeownership such as mortgage payments, house maintenance costs, and housing market price risk.
#
# #### Young households
#
# The first stage of the model consists of young households making a decision to buy a house of fixed size. Importantly, young households have little to no assets and have recently joined the labor market, which means their income is also relatively small. In order to finance a home, then, young households must choose a house of a particular value and a corresponding mortgage size. The lenders, on the other hand, impose some microprudential conditions such as loan-to-income ratios to ensure that mortgages are repayable.
#
# #### Mortgage payments
#
# Once households choose a house and mortgage, they commit to fixed-rate payments for the rest of their working life, which is about 30 years. During this time, households have an implicit holding of a risky asset in their homes (because of their uncertain resell values), which may lead them to reduce their exposure to other risky assets, such as the stock market.
#
# #### Retired homeowners
#
# Once they reach retirement, households have paid of their mortgage and have accumulated savings, making them significantly wealthier than young households (house value + savings). During this period, households experience risk of house liquidation due to the possibility of being forced to move out due to poor health or old age. If they are forced to sell, they do so at their local housing market prices and this increases their liquid wealth.
#
# #### Retired renters
#
# Retired renters have none of the complexities that come with owning a home, and thus behave like standard `ConsPortfolioModel` households. Instead of choosing only consumption, however, these households choose a level of total expenditures to spend on both consumption and rental housing. After becoming renters, households remain renters for the rest of their lives.

# %% [markdown]
# #### (Dots below represent computer code that produces all our results; click to expose)

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
import matplotlib.pyplot as plt
import numpy as np

from ConsPortfolioHousingModel import (
    PortfolioRiskyHousingType,
    portfolio_housing_params,
)

# %% jupyter={"source_hidden": true} tags=[]
portfolio_risky_housing = portfolio_housing_params(
    CRRA=10,
    DiscFac=0.96,
    T_cycle=8,
    T_retire=1,
    PermShkStd=0.1029563,
    PermShkCount=3,
    Rfree=1.02,
    RiskyAvg=1.08,
    RiskyStd=0.157,
    RiskyCount=3,
    HouseAvg=1.0,
    HouseStd=0.2,
    HouseShkCount=7,
    HseGroFac=1.01,
    HseDiscFac=0.01,
    HseInitPrice=1.0,
)

agent = PortfolioRiskyHousingType(**portfolio_risky_housing)

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
agent.solve()

# %% jupyter={"source_hidden": true} tags=[]
solution = agent.solution

# %% [markdown] pycharm={"name": "#%% md\n"}
# ### Results
#
# #### Homeownership increases intensive margin of stock market participation
#
# The proportion of liquid assets invested in the stock market is known as the risky portfolio share, or risky share for short. According to the model, retired households who own their homes and expect to sell them by next period have a higher  **risky share** than retired households who rent, and their risky share increases with house size, holding liquid wealth constant.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    A = M - C - 0.02 * h
    plt.plot(M, C, label="House size = {}".format(h))
plt.plot(M, solution[-2].ShareFuncRnt(M), label="Rental")
plt.legend()
plt.grid()
plt.ylabel("Risky Portfolio Share")
plt.xlabel("Beginning of Period Wealth")
plt.title("Risky Portfolio Share conditional on House Size")
plt.show()

# %% [markdown] pycharm={"name": "#%% md\n"}
# Clearly, the bigger the house size, the wealthier the agents are in terms of net worth. In the standard portfolio choice model, wealthier households actually reduce their risky share to reduce risk in next period's consumption. In the presence of housing, however, households still reduce their risk exposure as liquid wealth increases, but at a lower rate.
#
# A better comparison is to add the expected value of the house to liquid wealth. In this way, we compare an agent with $w$ net worth with all liquid wealth and no home, with an agent with $w$ net worth, some of which is liquid wealth $m$, and the rest is the expected house valuation $E[Q]h$,  such that $w = m + E[Q]h$, where $Q$ dentotes house prices and $h$ represents the size of the agent's house.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    plt.plot(M + h, C, label="House size = {}".format(h))
plt.plot(M, solution[-2].ShareFuncRnt(M), label="Rental")
plt.legend()
plt.grid()
plt.gca().set_xlim(right=100)
plt.ylabel("Risky Portfolio Share")
plt.xlabel("Beginning of Period Net Wealth")
plt.show()

# %% [markdown] pycharm={"name": "#%% md\n"}
# Additionally, an interesting observation is that according to the model retired households who are about to sell their homes are willing to risk at least the full expected value of their homes ($E[Q]h$) for certain when they have low liquidity. In other words, their risky share is equal to 1 at least up to the point where their liquid wealth is equal to their expected house valuation. If we shift their liquid wealth leftward by the amount of their expected house valuation, we see that their risky share starts dropping at about the same point as it would if they rented a house instead. We can conclude that having a house shifts the risky share curve rightward by an amount equal to the expected value of the house, but this is not the only effect. A larger house also reduces the rate at which the risky share decreases.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.geomspace(1, 111, 1000) - 1
for h in np.linspace(2.0, 10.0, 3):
    C = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    plt.plot(M - h, C, label="House size = {}".format(h))
plt.plot(M, solution[-2].ShareFuncRnt(M), label="Rental")
plt.legend()
plt.xlim([-5, 100])
plt.ylabel("Risky Portfolio Share")
plt.xlabel("Beginning of Period Wealth")
plt.grid()
plt.show()

# %% [markdown]
# ### Increasing House price risk decreases risky share
#
# The volatility of the housing market can have strong implications for the portfolio decisions of households who own their houses. A higher standard deviation in house prices implies a larger implicit holding of a risky asset (the house), regardless of house size. For this reason, households would optimally choose to avoid risk in other risky assets. As we see in the figure below for 2 households who have a house of equal size, the risky share of a household in a more volatile market is lower than that of a household in a less volatile market, except at low levels of market resources. Households that experience high price volatility in the housing market reduce their exposure to risk elsewhere, leading to lower risky portfolio shares.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
portfolio_risky_housing["HouseStd"] = 0.5
agent2 = PortfolioRiskyHousingType(**portfolio_risky_housing)
agent2.solve()
solution2 = agent2.solution

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0, 50, 100)
h = 5.0
C = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
C2 = solution2[-2].ShareFuncHse(M, h * np.ones_like(M))
plt.plot(M, C, label="House risk = {}".format(0.2))
plt.plot(M, C2, label="House risk = {}".format(0.5))
plt.legend()
plt.grid()
plt.ylabel("Risky share")
plt.xlabel("Market Resources")
plt.savefig("fig1.pdf")
plt.savefig("fig1.png")
plt.show()

# %% [markdown] pycharm={"name": "#%% md\n"}
# ### Larger houses increase households absolute risk taking
#
# As mentioned before, a house represents an implicit holding in a risky market that is otherwise uncorrelated with the stock market. A larger house, however, provides a higher expected value of house liquidation which also means a higher expected future liquid wealth. Households with more valuable homes, then, have a higher absolute risk tolerance and thus invest more resources in the risky asset market than they would if they had smaller homes.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0.0, 20, 100)
for h in [2.0, 5.0]:
    S = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    C = solution[-2].cFuncHse(M, h * np.ones_like(M))
    A = M - C - 0.02 * h
    plt.plot(A, S * A, label="House size = {}".format(h))
plt.legend()
plt.grid()
plt.ylabel("Liquid Assets Invested in Stock Market")
plt.xlabel("Household's Amount of Liquid Assets")
plt.title("Effect of House Size on Liquid Asset Investment in Stocks")
plt.gca().set_xlim(right=8)
plt.savefig("fig2.pdf")
plt.savefig("fig2.png")
plt.show()

# %% [markdown] pycharm={"name": "#%% md\n"}
# ### House Size crowds out investment
#
# However, when comparing households on a total wealth basis, i.e. their liquid assets plus expected house liquidation, we can see that house size crowds out investment for households with low liquid wealth. In the graph below, we can consider a household whose house size is equal to 5 (5 times their yearly net income) and liquid assets are \\$0, so their total expected wealth is \\$5. As this household becomes wealthier, they invest all of their liquid assets in the stock market (such that their risky share is 100\\%), up to the point where they start rebalancing their portfolio between the risky and the safe asset. In this region, they are constrained from investing in the stock market by their low liquid wealth, as they surely would like to invest more in the market. This point becomes clearer by comparing the household to an equally wealthy peer with a smaller house.  At the point where the household with house size of 5 has liquid wealth of \\$1 (1 times their yearly net income), they are investing less into the stock market in absolute terms than an equally wealthy household whose house size is equal to 2 and liquid assets are equal to \\$4. The total expected wealth of both these households is \\$6, but the household with the larger house is investing fewer assets in the stock market than the household with the smaller house. As their total wealth increases, however, both households are unconstrained by their house size and end up investing about the same amount into the stock market in absolute terms.

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"}
h_sizes = [2.0, 5.0]
M = np.linspace(0.0, 70, 100)
maxX = 100
for i in range(len(h_sizes)):
    h = h_sizes[i]
    S = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    C = solution[-2].cFuncHse(M, h * np.ones_like(M))
    A = M - C - 0.02 * h
    g1 = S * A
    g2 = (1 - S) * A
    g3 = h / (A + h)

    X = A + h
    maxX = np.minimum(maxX, np.nanmax(X))
    plt.plot(X, g1, label="House size = {}".format(h))
plt.legend()
plt.gca().set_xlim(right=maxX)
plt.grid()
plt.ylabel("Liquid Assets invested in Stock Market")
plt.xlabel("Household's Expected Total Wealth")
plt.savefig("fig3.pdf")
plt.show()

# %% [markdown] pycharm={"name": "#%% md\n"}
# ### Optimal Portfolio Choice over the Lifecycle
#
# A result that is consistent with `ConsPortfolioModel` is that younger households have a higher risky share of assets than older households, when comparing households of equal house size and no mortgage debt. Similarly, older households consume more than younger households, as their consumption horizon gets shorter and the likelihood that they receive a windfall of wealth from their house liquidation increases.
#

# %% jupyter={"source_hidden": true} pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0, 30, 100)
h = 1.0
ages = [2, 4, 6]
for age in ages:
    C = solution[age].ShareFuncHse(M, h * np.ones_like(M))
    c2 = solution[age].ShareFuncRnt(M)
    A = M - C - 0.02 * h
    plt.plot(M, C, label="Age = {}".format(age * 5 + 60))
plt.legend()
plt.grid()
plt.ylabel("Risky Portfolio Share")
plt.xlabel("Beginning of Period Liquid Wealth")
plt.show()

# %% jupyter={"source_hidden": true} tags=[]
M = np.linspace(0.0, 10, 100)
h = 5.0
ages = [2, 4, 6]
for age in ages:
    C = solution[age].cFuncHse(M, h * np.ones_like(M))
    A = M - C - 0.02 * h
    plt.plot(M, C, label="Age = {}".format(age * 5 + 60))
plt.legend()
plt.grid()
plt.ylabel("Consumption")
plt.xlabel("Beginning of Period Liquid Wealth")
plt.show()
