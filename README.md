# hello-world
My First repository
Now I am Adding new Staff

## Preflop Simulator

This repository includes a simple Monte Carlo simulator for Texas Hold'em preflop situations. Use `preflop_sim.py` to estimate win, tie, and equity percentages for a given starting hand.

### Usage

```bash
python3 preflop_sim.py "As Ks" [num_opponents] [iterations]
```

- `num_opponents` defaults to `1` if omitted.
- `iterations` defaults to `10000` if omitted.

Example:

```bash
python3 preflop_sim.py "As Ks" 1 100000
```

This will output estimated percentages for Ace-King suited against one random opponent.
