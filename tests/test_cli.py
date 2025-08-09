import pandas as pd
from cli import recommend_prices


def test_recommendation_within_bounds():
    df = pd.DataFrame({
        'cost': [10, 20],
        'competitor_price': [12, 18],
        'demand_score': [1, 0.5]
    })
    prices = recommend_prices(df, floor=5.0, ceiling=30.0, target_margin=0.3)
    assert all(prices >= 5.0) and all(prices <= 30.0)


def test_positive_relationship():
    df = pd.DataFrame({
        'cost': [10, 10],
        'competitor_price': [10, 20],
        'demand_score': [1, 1]
    })
    prices = recommend_prices(df)
    assert prices.iloc[1] > prices.iloc[0]
