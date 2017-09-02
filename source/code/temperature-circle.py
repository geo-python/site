#
# Hi all,
# this is the Python code I used to make the visualization "Temperature circle"
# (https://twitter.com/anttilip/status/892318734244884480).
# Please be aware that originally I wrote this for my tests only so the
# code was not ment to be published and is a mess and has no comments.
# Feel free to improve, modify, do whatever you want with it. If you decide
# to use the code, make an improved version of it, or it is useful for you
# in some another way I would be happy to know about it. You can contact me
# for example in Twitter (@anttilip). Unchecked demo data (no quarantees)
# for year 2017 Jan-Jul is included here and this code draws only a single image.
# The animation code is basically just a loop through the years. To keep
# it simple, I only included one year here.
#
# Thanks and have fun!
# Antti
#
# ---------
#
# Copyright 2017 Antti Lipponen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

backgroundcolor = '#faf2eb'
fontname = 'Lato'
yearname = '2017'

data2017 = {
    'AMERICA': [
        ['Antigua and Barbuda', 0.68],
        ['Argentina', 0.89],
        ['Bahamas', 0.65],
        ['Barbados', 0.68],
        ['Belize', 1.22],
        ['Bolivia', 1.22],
        ['Brazil', 1.23],
        ['Canada', 1.72],
        ['Chile', 0.93],
        ['Colombia', 0.88],
        ['Costa Rica', 0.76],
        ['Cuba', 0.78],
        ['Dominica', 0.64],
        ['Dominican Republic', 0.82],
        ['Ecuador', 1.16],
        ['El Salvador', 0.66],
        ['Grenada', 0.75],
        ['Guatemala', 1.25],
        ['Guyana', 0.65],
        ['Haiti', 0.56],
        ['Honduras', 1.1],
        ['Jamaica', 0.51],
        ['Mexico', 1.75],
        ['Nicaragua', 0.96],
        ['Panama', 0.65],
        ['Paraguay', 1.02],
        ['Peru', 1.25],
        ['Saint Kitts and Nevis', 0.68],
        ['Saint Lucia', 0.73],
        ['Saint Vincent and the Grenadines', 0.75],
        ['Suriname', 0.62],
        ['Trinidad and Tobago', 0.73],
        ['United States', 1.92],
        ['Uruguay', 1.02],
        ['Venezuela', 0.86],
    ],
    'OCEANIA': [
        ['Australia', 0.77],
        ['Fiji', 0.64],
        ['Kiribati', 0.21],
        ['Marshall Islands', 0.66],
        ['Micronesia', 0.9],
        ['Nauru', 0.82],
        ['New Zealand', 0.47],
        ['Palau', 0.94],
        ['Papua New Guinea', 0.92],
        ['Samoa', 0.77],
        ['Solomon Island', 1.0],
        ['Tonga', 0.86],
        ['Vanuatu', 1.17],
    ],
    'EUROPE': [
        ['Albania', 1.07],
        ['Andorra', 1.88],
        ['Armenia', 0.38],
        ['Austria', 1.66],
        ['Azerbaijan', 0.51],
        ['Belarus', 1.58],
        ['Belgium', 1.79],
        ['Bosnia and Herzegovina', 1.4],
        ['Bulgaria', 0.89],
        ['Croatia', 1.5],
        ['Cyprus', 0.38],
        ['Czech Republic', 1.68],
        ['Denmark', 1.73],
        ['Estonia', 1.67],
        ['Finland', 1.48],
        ['France', 1.62],
        ['Georgia', 0.44],
        ['Germany', 1.76],
        ['Greece', 0.77],
        ['Hungary', 1.49],
        ['Iceland', 1.66],
        ['Ireland', 1.57],
        ['Italy', 1.57],
        ['Latvia', 1.70],
        ['Liechtenstein', 1.74],
        ['Lithuania', 1.70],
        ['Luxembourg', 1.79],
        ['Macedonia', 0.99],
        ['Malta', 1.03],
        ['Moldova', 1.12],
        ['Montenegro', 1.25],
        ['Netherlands', 1.77],
        ['Norway', 1.63],
        ['Poland', 1.67],
        ['Portugal', 1.71],
        ['Romania', 1.14],
        ['San Marino', 1.59],
        ['Serbia', 1.23],
        ['Slovakia', 1.56],
        ['Slovenia', 1.59],
        ['Spain', 1.89],
        ['Sweden', 1.69],
        ['Switzerland', 1.76],
        ['Ukraine', 1.23],
        ['United Kingdom', 1.68],
    ],
    'AFRICA': [
        ['Algeria', 1.79],
        ['Angola', 0.70],
        ['Benin', 1.13],
        ['Botswana', 0.65],
        ['Burkina Faso', 1.20],
        ['Burundi', 1.20],
        ['Cameroon', 1.05],
        ['Cape Verde', 0.72],
        ['Central African Republic', 1.06],
        ['Chad', 1.04],
        ['Comoros', 0.90],
        ['Congo', 0.88],
        ['Democratic Republic of Congo', 0.97],
        ['Djibouti', 1.2],
        ['Egypt', 0.7],
        ['Equatorial Guinea', 0.92],
        ['Eritrea', 1.22],
        ['Ethiopia', 1.35],
        ['Gabon', 0.86],
        ['Gambia', 1.43],
        ['Ghana', 1.08],
        ['Guinea', 1.34],
        ['Guinea-Bissau', 1.39],
        ['Ivory Coast', 1.22],
        ['Kenya', 1.14],
        ['Lesotho', 0.84],
        ['Liberia', 1.21],
        ['Libya', 0.94],
        ['Madagascar', 1.16],
        ['Malawi', 0.89],
        ['Mali', 1.32],
        ['Mauritania', 1.56],
        ['Mauritius', 1.16],
        ['Morocco', 1.86],
        ['Mozambique', 0.90],
        ['Namibia', 0.94],
        ['Niger', 0.90],
        ['Nigeria', 1.10],
        ['Rwanda', 1.23],
        ['Sao Tome and Principe', 0.86],
        ['Senegal', 1.41],
        ['Seychelles', 0.99],
        ['Sierra Leone', 1.29],
        ['Somalia', 1.19],
        ['South Africa', 0.91],
        ['South Sudan', 1.27],
        ['Sudan', 1.17],
        ['Swaziland', 0.69],
        ['Tanzania', 1.01],
        ['Togo', 1.20],
        ['Tunisia', 1.81],
        ['Uganda', 1.26],
        ['Zambia', 0.59],
        ['Zimbabwe', 0.58],
    ],
    'ASIA': [
        ['Afghanistan', 1.78],
        ['Bahrain', 1.48],
        ['Bangladesh', 0.52],
        ['Bhutan', 0.61],
        ['Brunei', 0.77],
        ['Burma (Myanmar)', 0.65],
        ['Cambodia', 0.84],
        ['China', 1.80],
        ['East Timor', 0.34],
        ['India', 0.96],
        ['Indonesia', 0.67],
        ['Iran', 1.48],
        ['Iraq', 0.68],
        ['Israel', 0.52],
        ['Japan', 1.03],
        ['Jordan', 0.56],
        ['Kazakhstan', 1.91],
        ['Kuwait', 1.24],
        ['Kyrgyzstan', 1.57],
        ['Laos', 0.87],
        ['Lebanon', 0.42],
        ['Malaysia', 0.79],
        ['Maldives', 0.70],
        ['Mongolia', 3.05],
        ['Nepal', 0.71],
        ['North Korea', 2.01],
        ['Oman', 1.53],
        ['Pakistan', 1.76],
        ['Philippines', 0.81],
        ['Qatar', 1.86],
        ['Russian Federation', 3.01],
        ['Saudi Arabia', 1.46],
        ['Singapore', 0.51],
        ['South Korea', 1.65],
        ['Sri Lanka', 0.90],
        ['Syria', 0.40],
        ['Tajikistan', 1.39],
        ['Thailand', 0.85],
        ['Turkey', 0.39],
        ['Turkmenistan', 1.50],
        ['United Arab Emirates', 2.08],
        ['Uzbekistan', 1.54],
        ['Vietnam', 0.72],
        ['Yemen', 1.37],
    ]
}


def rotText(areaText, defaultspacing, rotangleoffset, rText, fontname):
    angle = areaText[0][1]
    for ii, l in enumerate(areaText):
        if ii > 0:
            angle += defaultspacing + l[1]
        plt.text(
            (rText) * np.sin(np.deg2rad(angle)),
            (rText) * np.cos(np.deg2rad(angle)),
            '{}'.format(l[0]),
            {'ha': 'center', 'va': 'center'},
            rotation=-angle + rotangleoffset,
            fontsize=15,
            fontname=fontname,
        )


plt.rcParams['axes.facecolor'] = backgroundcolor
mpl.rcParams.update({'font.size': 22})

cmap = plt.get_cmap('RdYlBu_r')
norm = mpl.colors.Normalize(vmin=-2.0, vmax=2.0)

Ncountries = 0
Ncontinents = 0
for countrylist in data2017.items():
    Ncountries += len(countrylist[1])
    Ncontinents += 1

spaceBetweenContinents = 3.0  # degrees
Nspaces = Ncontinents - 1
anglePerCountry = (345.0 - Nspaces * spaceBetweenContinents) / (Ncountries - 1)


fig, ax = plt.subplots(figsize=(12, 12))
renderer = fig.canvas.get_renderer()
transf = ax.transData.inverted()

limitangles = np.linspace(np.deg2rad(5.0), np.deg2rad(355.0), 500)
scaleRs = [
    [1.5, '-2.0', True, 0.25],
    [0.5 * (1.5 + 2.25), '-1.0', True, 0.25],
    [2.25, '0.0', True, 1.0],
    [0.5 * (3.0 + 2.25), '+1.0', True, 0.25],
    [3.0, '+2.0', True, 0.25],
    [3.3, '$^\\circ$C', False, 0.0]
]
for r in scaleRs:
    if r[2]:
        ax.plot(r[0] * np.sin(limitangles), r[0] * np.cos(limitangles), linewidth=r[3], color='#888888', linestyle='-')
    plt.text(
        0.0,
        r[0],
        '{}'.format(r[1]),
        {'ha': 'center', 'va': 'center'},
        fontsize=12,
        fontname=fontname,
    )

angle = 7.5
rText = 3.96
for continent in ['AFRICA', 'ASIA', 'EUROPE', 'AMERICA', 'OCEANIA']:
    for country in data2017[continent]:

        if angle < 185.0:
            rotangle = -angle + 90.0
        else:
            rotangle = -angle - 90.0

        plt.text(
            (rText) * np.sin(np.deg2rad(angle)),
            (rText) * np.cos(np.deg2rad(angle)),
            '{}'.format(country[0]),
            {'ha': 'center', 'va': 'center'},
            rotation=rotangle,
            fontsize=8,
            fontname=fontname,
            bbox={
                'facecolor': backgroundcolor,
                'linestyle': 'solid',
                'linewidth': 0.0,
                'boxstyle': 'square,pad=0.0'
            }
        )

        ax.plot(
            [1.3 * np.sin(np.deg2rad(angle)), 3.8 * np.sin(np.deg2rad(angle))],
            [1.3 * np.cos(np.deg2rad(angle)), 3.8 * np.cos(np.deg2rad(angle))],
            linewidth=0.6,
            linestyle='--',
            color='#DEDEDE'
        )

        lowerRoffset = 0.015
        temperatureAnomaly = country[1]

        rValue = 1.5 + (temperatureAnomaly + 2.0) / 4.0 * 1.5  # a lot more clever way for computing the radius should be used here...
        ax.plot(
            [(1.3 + lowerRoffset) * np.sin(np.deg2rad(angle)), rValue * np.sin(np.deg2rad(angle))],
            [(1.3 + lowerRoffset) * np.cos(np.deg2rad(angle)), rValue * np.cos(np.deg2rad(angle))],
            linewidth=4.3,
            linestyle='-',
            color='#202020'
        )
        ax.plot(
            [(1.3 + lowerRoffset) * np.sin(np.deg2rad(angle)), rValue * np.sin(np.deg2rad(angle))],
            [(1.3 + lowerRoffset) * np.cos(np.deg2rad(angle)), rValue * np.cos(np.deg2rad(angle))],
            linewidth=4.0,
            linestyle='-',
            color=cmap(norm(temperatureAnomaly))
        )

        angle += anglePerCountry
    angle += spaceBetweenContinents

c = Circle((0.0, 0.0), radius=1.0, fill=True, color='#fff9f5')
ax.add_patch(c)
plt.text(
    0.0,
    -0.52,
    yearname,
    {'ha': 'center', 'va': 'bottom'},
    fontsize=40,
    fontname=fontname,
)
plt.text(
    0.0,
    0.27,
    'Year',
    {'ha': 'center', 'va': 'center'},
    fontsize=26,
    fontname=fontname,
)

angles = np.linspace(np.deg2rad(0.0), np.deg2rad(360.0), 1000)
rs = [1.0, 1.3]
for r in rs:
    ax.plot(r * np.sin(angles), r * np.cos(angles), linewidth=1.0, color='#666666', linestyle='-')

plt.text(
    5.87,
    -4.67,
    'Antti Lipponen (@anttilip)',
    {'ha': 'right', 'va': 'center'},
    fontsize=10,
    fontname=fontname,
)

plt.text(
    -6.3 + 0.015,
    4.385 - 0.015,
    'Temperature anomalies',
    {'ha': 'left', 'va': 'center'},
    fontsize=27,
    fontname=fontname,
    color='#909090'
)

plt.text(
    -6.3,
    4.385,
    'Temperature anomalies',
    {'ha': 'left', 'va': 'center'},
    fontsize=27,
    fontname=fontname,
    color='#0D0D0D'
)

plt.text(
    -6.35,
    -4.35,
    'Data source:\nNASA GISS Surface Temperature Analysis (GISTEMP)\nLand-Ocean Temperature Index, ERSSTv4, 1200km smoothing\nhttps://data.giss.nasa.gov/gistemp/\nAverage of monthly temperature anomalies. GISTEMP base period 1951-1980.',
    {'ha': 'left', 'va': 'center'},
    fontsize=10,
    fontname=fontname,
)

areaText = [
    ['A', 46.0],
    ['f', 0.3],
    ['r', -0.05],
    ['i', -0.15],
    ['c', -0.15],
    ['a', 0.2],
]
rText, defaultspacing, rotangleoffset = 1.13, 4.4, 0.0
rotText(areaText, defaultspacing, rotangleoffset, rText, fontname)

areaText = [
    ['E', 236.0],
    ['u', 0.0],
    ['r', 0.3],
    ['o', 0.7],
    ['p', 0.0],
    ['e', 0.0],
]
rText, defaultspacing, rotangleoffset = 1.155, -5.5, 180.0
rotText(areaText, defaultspacing, rotangleoffset, rText, fontname)

areaText = [
    ['A', 147.0],
    ['s', -0.8],
    ['i', 0.0],
    ['a', 0.0],
]
rText, defaultspacing, rotangleoffset = 1.155, -4.7, 180.0
rotText(areaText, defaultspacing, rotangleoffset, rText, fontname)

areaText = [
    ['A', 276.0],
    ['m', 2.5],
    ['e', 0.6],
    ['r', -0.15],
    ['i', -2.0],
    ['c', -2.0],
    ['a', -0.15],
]
rText, defaultspacing, rotangleoffset = 1.13, 5.85, 0.0
rotText(areaText, defaultspacing, rotangleoffset, rText, fontname)

areaText = [
    ['O', 328.5],
    ['c', 1.0],
    ['e', 0.0],
    ['a', 0.2],
    ['n', 0.2],
    ['i', -0.3],
    ['a', -0.3],
]
rText, defaultspacing, rotangleoffset = 1.125, 4.8, 0.0
rotText(areaText, defaultspacing, rotangleoffset, rText, fontname)

ax.set_xlim([-5.0, 5.0])
ax.set_ylim([-5.0, 5.0])
plt.axis('off')
plt.savefig('temperatureCircle.png', facecolor=backgroundcolor, edgecolor='none', dpi=160)
plt.close()

# and finally I used imageMagick to crop the image for animation