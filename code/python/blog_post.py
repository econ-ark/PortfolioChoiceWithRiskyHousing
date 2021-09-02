# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Portfolio Choice with Risky Housing
# ### By Alan Lujan and the Econ-ARK team

# %% [markdown]
# [![badge](https://img.shields.io/badge/launch-binder%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/econ-ark/PortfolioChoiceWithRiskyHousing/HEAD?filepath=code%2Fpython%2Fblog_post.ipynb)    [![badge](https://img.shields.io/badge/launch-binder%20lab-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/econ-ark/PortfolioChoiceWithRiskyHousing/HEAD?urlpath=lab%2Ftree%2Fcode%2Fpython%2Fblog_post.ipynb)

# %% [markdown] pycharm={"name": "#%% md\n"} tags=[]
# Economists have long sought to use models of mathematically optimal behavior to try to understand saving and investment decisions over a household's life-cycle.  
#
# If you had no uncertainty (about, say, investment returns), calculating optimal choices would not be very hard.  For example, you would want to invest your whole financial portfolio in whatever asset you knew (in advance) would yield the highest rate of return.
#
# But in the real world, assets that -- on average -- yield higher returns (like stocks), also are much riskier than low-return safe assets (like bank deposits).  Aversion to risk is a perfectly rational motivation, so how much to invest in risky versus safe assets is far from obvious.  Furthermore, there are many other risks (to your job, your health, to house prices, and more) that should further temper any rational person's appetite for risky investment.
#
# As we noted in [our previous blog post](https://www.thinkforwardinitiative.com/stories/optimal-financial-investments-over-the-life-cycle), calculating truly optimal behavior in a realistically uncertain world is such a difficult challenge that only recently has it become feasible to do with a reasonably high degree of realism.  Rational choice models like the one we examined there must account for many important features of reality, including different types of uncertainty (labor income risk, mortality risk, and stock market risk), and should allow for reasonable choices of risk aversion, impatience, and other preferences.  They need properly to account for for the path of income over the life cycle and into retirement, effects of aging and mortality, interest rates and economic growth, and myriad other factors.
#
# All of this is so difficult that professional financial advisors do not attempt it, relying instead on rules of thumb and intuition to guide their clients. 
# Indeed, despite the current excitement about the wonders of artificial intelligence, even  online "robo-advisors" do not incorporate the degree of realism described above.  Serious mathematical optimization efforts have been restricted to the pages of top academic economics journals -- and the associated computer code used to solve the models in those papers has been so impenetrable as to be unusable.
#
# Our first blog post described the first phase of our work sponsored by TFI in building a public, easy-to-use, open-source software toolkit of the computer code that can solve these kinds of problems.  We showed that our free tools are able easily and quickly to reproduce the results that have been published in the academic literature.  
#
# However, as noted in [our previous blog post](https://www.thinkforwardinitiative.com/stories/optimal-financial-investments-over-the-life-cycle) those models of optimal decisionmaking imply that, given the robust rate of return that risky assets ('stocks') have earned in the past, most consumers should invest ALL of their financial wealth in stocks over most of their lifetimes.
#
# A tempting interpretation of the discrepancy between the models' predictions and people's actual choices is that most people are just making a mistake in not investing more in stocks.
#
# Another possibility, though, is that the models are still missing some vitally important (and rational) factor that weighs on people's actual decisions; in this case, people might be making rational decisions and the models might be wrong.
#
# There's an obvious candidate for the missing factor.  For most households homeownership is the biggest financial decision in their lives.  Homeownership _should_ matter for consumers' choices about how willing they should rationally be to expose themselves to risky financial assets, for at least two reasons.  First, homeownership exposes consumers to housing market price risk, which should have the effect of reducing their appetite for being exposed to other kinds of risk.  Second, homeownership is associated with certain payment obligations (not just mortgages, but property taxes, maintenance costs, and so on), which reduces the flexibility they may have in adjusting their spending in response to income fluctuations.
#
# These points may seem obvious, but there is a good reason they have not been incorporated in previous analyses of households' optimal choice:  Taking account of these complexities greatly increases the computational difficulty of calculating  optimal decisions.  This blog post describes results obtained using the latest tools to be added to the [Econ-ARK](https://econ-ark.org/) toolkit; with these tools, it should be much easier for economists, financial planners, and others to understand the appropriate role of homeownership in modifying investors' optimal saving and financial choices.
#
# ### The Problem: Housing
#
# Perhaps the biggest financial decision in a household's life is buying a house. Houses come in different sizes (and therefore costs), but they are generally an expensive asset whose value is at least a few times the household's yearly income. Young households usually cannot buy their houses outright, as they start with little to no assets and take time to accumulate enough resources. They therefore usually rely on mortgages to purchase their houses. These young and leveraged households might thus be sensitive to stock market risk, causing them to reduce their stock market participation.
#
# During the repayment period, households' market resources (or liquid assets) are reduced by the fixed mortgage payment. This has two effects on risky asset choice: 1) It reduces 'market resources' (current income, plus current non-housing wealth) today, making households relatively less wealthy, and 2) It reduces market resources in following periods for any given level of current savings, making households more risk averse due to the precautionary motive. The fixed nature of mortgage payments has another important effect: since the household must be sure to have sufficient resources in the next period to pay their mortgage and the cost of house maintenance, they might want to save more of their resources in a safe account rather than in the risky stock market.
#
# Houses are also subject to price fluctuations that depend on local housing market conditions as well as broader national trends, such as recessions and expansions. The uncertain sale price of your house, then, constitutes additional uncertainty in future net worth and could thus have significant implications for portfolio decisions. One way to think about this is to realize that the owner of a house has an implicit holding of a risky asset, which should motivate them to want to reduce their exposure to additional risk in another risky asset, the stock market. 
#
# ### The standard model
#
# The new model in our toolkit, called [](), is an extension of the model we described in the earlier blog post, [`ConsPortfolioModel`](), with the added features of homeownership such as mortgage payments, house maintenance costs, and housing market price risk.
#
# #### Young households
#
# The first stage of the model consists of young households making a decision to buy a house of fixed size. Importantly, young households have little to no assets and have recently joined the labor market, which means their income is also relatively small. In order to finance a home, then, young households must choose a house of a particular value and a corresponding mortgage size. Lenders are assumed impose some microprudential conditions such as loan-to-income ratios to ensure that mortgages are repayable.
#
# #### Mortgage payments
#
# Once households choose a house and mortgage, they commit to fixed-rate payments for the rest of their working life, which is about 30 years. During this time, households have an implicit holding of a risky asset in their homes (because of their uncertain resale values), which may lead them to reduce their exposure to other risky assets, such as the stock market.
#
# #### Retired homeowners
#
# Once they reach retirement, households in our model have paid of their mortgage and have accumulated savings, making them significantly wealthier (where 'wealth = house value + liquid assets') than young households. During this period, households experience a risk of house liquidation due to the possibility of being forced to move out due to poor health or old age. If they are forced to sell, they do so at their local housing market prices; the value of the house gets transformed into liquid wealth.
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
# We examine here the behavior of retired households on the cusp of the liquidation of the value of their house.  As usual, we are assuming that the household anticipates some form of guaranteed pension income ('Social Security'), but expects to finance any other consumption out of the returns on their assets.
#
# The proportion of liquid assets invested in the stock market is known as the risky portfolio share, or **risky share** for short. 
#
# Our previous blog post reviewed the logic of the model without housing. For a person with no housing wealth and little liquid wealth, the first dollar of investment in the stock market poses very little risk, so the model implies that the proportion of any additional wealth that will be invested in the stock market is 100 percent.  But as wealth gets very large, the consumer becomes reluctant to put all of it in the stock market, because that would be putting more and more of their consumption at risk.  (See that blog post for further discussion of this point).
#
# The figure below shows how the picture is modified for consumers who, in addition to their liquid assets, own homes of various sizes.
#
# According to the model, retired households who own their homes and expect to sell them by next period have a higher risky share than retired households who rent, and their risky share increases with house size, holding liquid wealth constant.

# %% pycharm={"name": "#%%\n"} tags=[]
M = np.linspace(0.0, 100, 100)
for h in np.linspace(2.0, 10.0, 3):
    C = solution[-2].ShareFuncHse(M, h * np.ones_like(M))
    A = M - C - 0.02 * h
    plt.plot(M, C, label="House size = {}".format(h))
plt.plot(M, solution[-2].ShareFuncRnt(M), label="Rental")
plt.legend()
plt.grid()
plt.ylabel("Risky Portfolio Share")
plt.xlabel("Beginning of Period Wealth (excl house)")
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
# ### Increasing house price risk decreases risky share
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
# ### Larger houses increase households' absolute risk taking
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
# ### House size crowds out investment
#
# However, when comparing households on a total wealth basis, i.e. their liquid assets plus expected house liquidation, we can see that house size crowds out investment for households with low liquid wealth. In the graph below, we can consider a household whose house size is equal to 5 (5 times their yearly net income) and liquid assets are \\$0, so their total expected wealth is \\$5. As this household becomes wealthier, they invest all of their liquid assets in the stock market (such that their risky share is 100 percent), up to the point where they start rebalancing their portfolio between the risky and the safe asset. In this region, they are constrained from investing in the stock market by their low liquid wealth, as they surely would like to invest more in the market. This point becomes clearer by comparing the household to an equally wealthy peer with a smaller house.  At the point where the household with house size of 5 has liquid wealth of \\$1 (1 times their yearly net income), they are investing less into the stock market in absolute terms than an equally wealthy household whose house size is equal to 2 and liquid assets are equal to \\$4. The total expected wealth of both these households is \\$6, but the household with the larger house is investing fewer assets in the stock market than the household with the smaller house. As their total wealth increases, however, both households are unconstrained by their house size and end up investing about the same amount into the stock market in absolute terms.

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

# %% [markdown]
# # Conclusions
#
# Most people who need advice about how to invest in financial markets are also homeowners.  
#
# But until now, even the most sophisticated and realistic analyses of how people should optimally invest in financial markets have not accounted for the (undeniably important) ramifications of homeownership for their financial choices.
#
# That's because constructing a model that correctly tracks all the potential interactions between homeownership, financial risk, and other kinds of risk is remarkably difficult.
#
# This blog post describes a free, publicly available open-source software tool that does these complex calculations.  Sponsorship by the Think Forward Initiative has allowed us to add this tool to the free, open-source, [Econ-ARK](https://econ-ark.org) toolkit, thus making it available to financial institutions, financial planners, robo-advisors, academics, and anyone else who might be interested in a rigorous analysis of these questions.
#
# Despite their combinatorial complexity, the answers that come from the model make intuitive sense.  
#
# A first conclusion is that greater uncertainty about future house prices should make you less willing to invest in the stock market.  In other words, a homeowner who lives in a place with wild house-price swings will find it best to have less exposure to other kinds of risk (like stock market risk) than someone with circumstances that are otherwise similar, but who lives in a place where house prices are more stable.
#
# Another conclusion might seem to push in the other direction, but really does not: Among homeowners whose mortgage is paid off, for a given level of _nonhousing_ net worth (say, \$200K of financial assets net of mortgage debt), a person whose house is more valuable should invest more in risky financial asset.  The reason is simple:  For a given amount of liquid assets, the person with a bigger house is richer, and a richer person will want to have more money (in absolute terms) invested in the stock market).
#
# The final point is that the existence of homeownership does not reverse one of the more surprising implications of the baseline model without homeownership:  The richer you are, the lower is the optimal share of your portfolio in risky assets.  This implication of the model does not match the available data well.  The conclusion is easy to reverse by introducing a bequest motive in which bequests are a luxury good; but how exactly such a motive should be constructed is by no means a settled question, either among financial planners or among academic researchers.  It is a topic we hope to address in future releases of our toolkit.
#
#
