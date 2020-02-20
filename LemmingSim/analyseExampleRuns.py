#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analysis of Lemmings program, commit version 57289af3.
Ran simulation with 1, 2, 3 Lemmings, each 11 times.
There were 7x7 boxes (25 red, 24 blue).
Simulations were automatically stopped once > 80% of blue boxes
were pushed toward a wall of the arena, independent of how many
red boxes were remaining in the center of the arena.
"""

import pandas as pd
from pylab import array, plot, tile, ylim, title, xticks, ylabel, xlabel,\
                  tight_layout, figure

# At the end of simulation, the lapsed steps and
# percent of remaining red boxes in the arena was recorded.
steps_1 = array([49942, 56212, 58021, 61538, 69538,
                 40871, 45208, 76312, 58319, 59731, 46786])
prc_red_1 = array([40, 64, 32, 68, 60,
                   48, 48, 68, 28, 76, 44])

steps_2 = array([26994, 43051, 17633, 22916, 20251,
                 24148, 26260, 27559, 38211, 32192, 40226])
prc_red_2 = array([52, 60, 44, 48, 44,
                   76, 40, 48, 64, 60, 64])

steps_3 = array([14647, 18825, 25744, 32373, 33770,
                 26422, 12223, 19438, 26086, 28273, 27184])
prc_red_3 = array([44, 52, 44, 56, 64,
                   72, 36, 52, 56, 48, 52])

data1 = pd.DataFrame({'robots': 1, 'steps': steps_1, 'prc_red': prc_red_1})
data2 = pd.DataFrame({'robots': 2, 'steps': steps_2, 'prc_red': prc_red_2})
data3 = pd.DataFrame({'robots': 3, 'steps': steps_3, 'prc_red': prc_red_3})
data = pd.concat([data1, data2, data3])

means = data.groupby(by='robots').mean()
stds = data.groupby(by='robots').std()

# plot duration decline
figure(figsize=(5, 4))
for robots, df in data.groupby(by='robots'):
    xaxs = tile(robots, df['robots'].size)
    plot(xaxs, df['steps'], 'ko', alpha=0.33)

plot(means['steps'], 'k-', lw=2, alpha=0.8)
ylim((0, 80000))
xticks((1, 2, 3))
ylabel('no. of sim steps', fontsize=12)
xlabel('no. of Lemmings', fontsize=12)
title('Duration to sort 80% blue boxes to edge of arena')
tight_layout()

# plot percentage of remaining red boxes
figure(figsize=(5, 4))
for robots, df in data.groupby(by='robots'):
    xaxs = tile(robots, df['robots'].size)
    plot(xaxs, df['prc_red'], 'ro', alpha=0.33)

plot(means['prc_red'], 'r-', lw=2, alpha=0.5)
ylim((0, 100))
xticks((1, 2, 3))
ylabel('percent of red boxes', fontsize=12)
xlabel('no. of Lemmings', fontsize=12)
title('Percentage of remaining red boxes in arena')
tight_layout()

