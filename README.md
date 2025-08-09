# Dynamic Pricing and Cost Optimization

This project implements a simple dynamic pricing recommender for retail and resources sectors, balancing rule-based logic with a machine-learning style scoring function. **Guardrails** ensure prices stay within ethical and commercial bounds.

## Methodology

1. **Rule-Based Pricing**: Base price equals cost plus a target margin.  2. **ML Scoring**: Adjustments based on competitor pricing and demand signals.  3. **Guardrails**: Apply floor and ceiling limits and ensure compliance with pricing policies.

## Scenarios

- **GCC Retail**: Optimize product prices while maintaining margins and avoiding undercutting competitors.  - **AU Resources**: Manage price volatility for resources by incorporating cost fluctuations and demand forecasts.

## Compliance & Ethics

Pricing recommendations respect regulatory requirements and avoid discriminatory practices. Parameters like floor, ceiling, and margin are configurable to align with company policy.

## How to Run

```bash
python cli.py sample_input.csv output.csv --floor 5 --ceiling 100 --target_margin 0.2
```

The script reads an input CSV containing `cost`, `competitor_price`, and `demand_score` columns and outputs a new CSV with a `recommended_price` column.

## Industry Relevance

- **Retail/FMCG (GCC)**: Supports strategic pricing campaigns.  - **Energy/Resources (Australia)**: Helps navigate commodity price volatility while safeguarding margins.

Licensed under the MIT License.
