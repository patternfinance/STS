# STS - Smart Trading System

STS是一个面向多策略开发的自动交易系统。支持包括策略开发、策略回测在内的多项功能。



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
tsObj = DataSource.cut(tsObj, '2014-01-01', DataSource.today())
```




## STS功能介绍



## STS交易系统开发理念



## 帮助和支持