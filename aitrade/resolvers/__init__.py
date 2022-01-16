# flake8: noqa: F401
# isort: off
from aitrade.resolvers.iresolver import IResolver
from aitrade.resolvers.exchange_resolver import ExchangeResolver
# isort: on
# Don't import HyperoptResolver to avoid loading the whole Optimize tree
# from freqtrade.resolvers.hyperopt_resolver import HyperOptResolver
from aitrade.resolvers.pairlist_resolver import PairListResolver
from aitrade.resolvers.protection_resolver import ProtectionResolver
from aitrade.resolvers.strategy_resolver import StrategyResolver
