import pandas as pd
from typing import Callable


def run_backtest(df: pd.DataFrame, strategy: Callable[[pd.DataFrame], float]) -> float:
    """Run a backtest on the given data using a strategy function."""
    return strategy(df)
