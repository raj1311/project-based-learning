import pandas as pd


def long_call_hold(df: pd.DataFrame) -> float:
    """Buy a call option on the first day and hold to expiry.

    Profit = max(underlying_final - strike, 0) - call_premium
    """
    start = df.iloc[0]
    end_underlying = df.iloc[-1]["underlying"]
    payoff = max(end_underlying - start["strike"], 0)
    return payoff - start["call_price"]


def short_straddle(df: pd.DataFrame) -> float:
    """Sell call and put on the first day and hold to expiry."""
    start = df.iloc[0]
    end_underlying = df.iloc[-1]["underlying"]
    payoff = (
        start["call_price"] + start["put_price"]
        - max(end_underlying - start["strike"], 0)
        - max(start["strike"] - end_underlying, 0)
    )
    return payoff
