#!/usr/bin/env python3
import argparse
import pandas as pd


def recommend_prices(df, floor=1.0, ceiling=100.0, target_margin=0.2):
    # Calculate recommended prices using rule-based and ML-like scoring.
    base_price = df['cost'] * (1 + target_margin)
    adjustment = 0.5 * (df['competitor_price'] - df['cost']) + 2 * df['demand_score']
    price = base_price + adjustment
    price = price.clip(lower=floor, upper=ceiling)
    return price


def main():
    parser = argparse.ArgumentParser(description="Dynamic Pricing & Cost Optimization CLI")
    parser.add_argument('input_csv', help='Path to input CSV with columns cost, competitor_price, demand_score')
    parser.add_argument('output_csv', help='Path to save CSV with recommended prices')
    parser.add_argument('--floor', type=float, default=1.0, help='Minimum allowed price')
    parser.add_argument('--ceiling', type=float, default=100.0, help='Maximum allowed price')
    parser.add_argument('--target_margin', type=float, default=0.2, help='Target margin over cost')
    args = parser.parse_args()
    df = pd.read_csv(args.input_csv)
    df['recommended_price'] = recommend_prices(df, floor=args.floor, ceiling=args.ceiling, target_margin=args.target_margin)
    df.to_csv(args.output_csv, index=False)
    print(f"Saved recommendations to {args.output_csv}")


if __name__ == '__main__':
    main()
