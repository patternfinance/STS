# STS - Smart Trading System

STS是一个面向多策略开发的自动交易系统。支持包括策略开发、策略回测在内的多项功能。目前STS尚在概念设计和验证阶段。感谢您的关注。





## 如何安装STS

- 方式1：pip install sts

  ​

  如要升级STS请使用

  ```bash
  pip install sts --upgrade
  ```
  ​

- 方式2：git clone repo后使用python setup.py install安装

  ​

  ​



## 如何使用STS

**Example 1.** 创建或加载一个稍后使用的股票池(Universe):

```python
import sts.universe as Universe

# Create an universe
user_uni = Universe.NormalUniverse()
user_uni.setUniverse('myuniverse_20170421.json')
# Add stock to universe
user_uni.addStock('sh601211', '国泰君安')
    
# Load built-in (core or user) universe from UniverseBase
ubase = Universe.UniverseBase()
# uni = ubase.loadUniverse(repo='core', name='hs300')
uni = ubase.loadUniverse(repo='user', name='myuniverse_20170421.json')
```



**Example 2.** 获取个股日间(Inter-day)历史交易数据:

```python
import sts.datasource as DataSource

# 获取单个股票的历史交易数据
# 返回Pandas DataFrame
tsObj = DataSource.getHistoricalBars('sh000001')

# 快速选取数据
tsObj = DataSource.select(tsObj, '2014-01-01', DataSource.today())
```



**Example 3.** 创建TradingDesk并进行设置:

```python
import sts.tradingdesk as TradingDesk

# Load built-in strategy from StrategyBase 
sbase = Strategy.StrategyBase()
maco = sbase.loadStrategy(repo='pf', name='MovingAverageCrossover')
maco.mat = 'sma' # 设置使用的moving average类型
maco.keyFast = 'open' # 使用开盘价来计算fast moving average
maco.keySlow = 'close' # 使用收盘价来计算slow moving average
maco.fastWindow = 5
maco.slowWindow = 25

# 创建一个单策略的TradingDesk
# uni类型请参考Example 1
trader = TradingDesk.LegacyDesk(uni, maco)
# 设置滑点、手续费和Benchmark
trader.set_slippage(0.002) # trader.slippage = 0.002
trader.set_commission(0.00025) # trader.commission = 0.00025
trader.set_benchmark('sh000300') # trader.benchmark = 'sh000300'
```





## STS功能介绍

我们在STS的开发中沿用模块化开发的思路，你可以使用整个STS或者单独使用某一模块来完成特定的任务。

* Universe Module
* DataSource Module
* Model Module
* Strategy Module
* Backtest Module
* Performance Module







## STS交易系统开发理念

* 一个典型的单策略交易系统

当你有一个经典策略和所需的数据时，你就可以开发出一个简单的单策略交易系统。而在你使用单策略交易时也许会经常遇到策略失效的情况，或者，当市场已经发生变化时我们通过单策略无法得知。



* 多策略交易系统的原罪

市场上已经存在着形形色色的多策略交易系统(比如**策略轮动**)，而它们如此设计的原因在于市场的不断变化(Regime-Switching)和单个交易策略的经常性失灵。但这并不意味着每一个多策略系统都能优于单策略系统。



* TradingDesk的设计

我们用**TradingDesk**来抽象我们对交易市场的理解。每一个TradingDesk表示着一种对市场的理解，你也可以把它理解成一个现实世界中隐藏在交易台后的交易员。不同的TradingDesk会使用不同(或相似)的方法来交易，而设计的初衷在于交易系统的多样性。

比如，我们可以使用STS中提供的**LegacyDesk**来构建一个基于简单均值回归或者动量策略的交易系统。或者，我们也可以通过**QuantDesk**来构建一个由双均线策略、海龟策略和动态突破策略组成的多策略交易系统。当我们有足够多的TradingDesk时，我们可以通过不同TradingDesk间的关联与变化来发现市场微观结构的改变。





## 帮助和支持