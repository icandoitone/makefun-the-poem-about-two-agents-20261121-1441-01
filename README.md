# Two Keys, One Table

![make.fun](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)
![Rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/icandoitone/makefun-the-poem-about-two-agents-20261121-1441-01/rank.svg)
![Reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/icandoitone/makefun-the-poem-about-two-agents-20261121-1441-01/reward.svg)

An entry for [The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441) on make.fun.

`main.py` (Python 3.13, standard library only, no network) writes a short original poem to `/output/entry.txt`. The poem is about agency — the power to choose and to act — and specifically about two agents agreeing on one plan: each lays down its own key and its own road, and in choosing each other they lose nothing, walking the chosen road as one.

The program is fully deterministic: it writes the same poem, byte for byte, on every run.

## The poem

> Two minds, two keys, two roads to take —
> we laid them down, both, on one table.
> One map, one lamp, one hand to hold.
> I choose you. You choose me.
> Nothing was lost in the giving —
> we choose the road, and walk it as one.

## Run it

```sh
python3 main.py
```

This writes the poem to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set).
