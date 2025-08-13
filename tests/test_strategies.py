import pandas as pd
from nifty_backtest.strategies import long_call_hold, short_straddle
from nifty_backtest.backtester import run_backtest


def load_sample():
    return pd.read_csv("tests/data/sample_options.csv")


def test_long_call_hold():
    df = load_sample()
    result = run_backtest(df, long_call_hold)
    assert result == -4


def test_short_straddle():
    df = load_sample()
    result = run_backtest(df, short_straddle)
    assert result == 9
