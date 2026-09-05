"""Quant swing engine v1 — anti garbage-in-garbage-out.

Pipeline: data.load -> scrub.gate -> strategy.run -> backtest.run_backtest
          -> validate.walk_forward -> signal.generate
"""
__version__ = "0.1.0"
