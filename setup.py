from setuptools import setup, find_packages

long_desc = """
STS - Smart Trading System
===============

Installation
--------------
    pip install sts
    
Upgrade
---------------
    pip install sts --upgrade
    
"""

setup(
    name = 'sts',
    version = '0.0.1',
    keywords = ('sts', 'trading system', 'quant', 'strategy development'),
    description = 'STS - Smart Trading System',
    license = 'MIT License',
    install_requires = [],

    author = 'Yuke Gao',
    author_email = 'yuke.gao@patternfinance.com',
    url='https://www.patternfinance.com',
    
    packages = find_packages(),
    platforms = 'any',
)