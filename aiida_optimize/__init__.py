# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>
"""
A plugin for AiiDA which defines a generic optimization workchain, and
engines and wrappers for .
"""

__version__ = '0.3.2'

from ._optimization_workchain import OptimizationWorkChain
from . import engines
from . import wrappers

__all__ = ['OptimizationWorkChain', 'engines', 'wrappers']
