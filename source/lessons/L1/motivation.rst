Motivation for the course
=========================

The main part of the first half of this course is to learn to program in Python.
However, in addition to learning to program, we hope to help you learn a number of other skills related to open science.
These include:

1. Writing programs that are easy to understand and share
2. Keeping a log of the changes you make to your programs
3. Creating programs that ensure your science is reproducible
4. Producing simple, effective data visualizations that make your results accessible and easy to understand

To help clarify our goals, consider the example below.

Effective data visualization
----------------------------

One of the things we will learn in this course is how to use Python to plot data.
As you well know, raw data itself is often not particularly useful in helping you understand what the data shows.
Let's look at an example that might be familiar to you, global temperature data.

.. code-block:: none

    USAF  WBAN YR--MODAHRMN DIR SPD GUS CLG SKC L M H  VSB MW MW MW MW AW AW AW AW W TEMP DEWP    SLP   ALT    STP MAX MIN PCP01 PCP06 PCP24 PCPXX SD
    029740 99999 195201010000 200  23 ***  15 OVC 7 2 *  5.0 63 ** ** ** ** ** ** ** 6   36   32  989.2 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201010600 220  18 ***   8 OVC 7 2 *  2.2 63 ** ** ** ** ** ** ** 6   37   37  985.9 ***** ****** ***  34 ***** ***** ***** ***** **
    029740 99999 195201011200 220  21 ***   5 OVC 7 * *  3.8 59 ** ** ** ** ** ** ** 5   39   36  988.1 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201011800 250  16 *** 722 CLR 0 0 0 12.5 02 ** ** ** ** ** ** ** 5   36   27  991.9 ***** ******  39 *** ***** ***** ***** ***** **
    029740 99999 195201020000 220   7 *** 722 CLR 0 0 0 12.5 02 ** ** ** ** ** ** ** 0   36   28  995.8 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201020600 220  16 ***  15 OVC 5 * *  9.4 02 ** ** ** ** ** ** ** 1   36   34  997.1 ***** ****** ***  34 ***** ***** ***** ***** **
    029740 99999 195201021200 110  14 ***   8 OVC 5 * * 12.5 70 ** ** ** ** ** ** ** 2   34   28  993.1 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201021800 160  14 ***   8 OVC 7 * *  1.2 73 ** ** ** ** ** ** ** 7   34   32  985.9 ***** ******  37 *** ***** ***** ***** ***** **
    029740 99999 195201030000 180  18 ***  15 OVC 5 * *  3.8 26 ** ** ** ** ** ** ** 7   36   28  985.4 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201030600 200  14 ***  15 BKN 5 * *  5.0 02 ** ** ** ** ** ** ** 7   36   32  985.2 ***** ****** ***  32 ***** ***** ***** ***** **
    029740 99999 195201031200 250  11 ***  15 OVC 5 1 *  9.4 02 ** ** ** ** ** ** ** 7   34   30  986.8 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201031800 340   9 ***   5 BKN 5 7 *  5.6 03 ** ** ** ** ** ** ** 2   28   27  988.8 ***** ******  36 *** ***** ***** ***** ***** **
    029740 99999 195201040000 230   7 *** 722 SCT 0 0 5  9.4 02 ** ** ** ** ** ** ** 1   28   27  994.4 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201040600 270  11 ***  15 OVC 7 * *  5.0 70 ** ** ** ** ** ** ** 2   30   27  998.6 ***** ****** ***  25 ***** ***** ***** ***** **
    029740 99999 195201041200 250  15 ***  15 OVC 5 * *  5.0 71 ** ** ** ** ** ** ** 7   30   27 1002.8 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201041800 260   7 ***  40 OVC 5 * * 12.5 02 ** ** ** ** ** ** ** 7   30   27 1006.6 ***** ******  30 *** ***** ***** ***** ***** **
    029740 99999 195201050000 ***   0 *** *** BKN 5 * * 12.5 01 ** ** ** ** ** ** ** 2   28   27 1009.8 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201050600 ***   0 ***  98 OVC 7 2 *  1.9 71 ** ** ** ** ** ** ** 7   27   27 1012.2 ***** ****** ***  25 ***** ***** ***** ***** **
    029740 99999 195201051200 360   2 *** *** OVC 0 7 *  1.5 71 ** ** ** ** ** ** ** 7   27   27 1015.2 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201051800 360   7 ***  98 OVC 7 1 *  2.5 71 ** ** ** ** ** ** ** 7   25   23 1018.5 ***** ******  30 *** ***** ***** ***** ***** **
    029740 99999 195201060000 360  11 ***   8 OVC 5 7 *  9.4 02 ** ** ** ** ** ** ** 7   23   23 1021.5 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201060600 ***   0 ***   8 OVC 6 * *  7.5 02 ** ** ** ** ** ** ** 7   23   21 1023.4 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201061200 ***   0 ***  98 OVC 5 7 *  3.8 01 ** ** ** ** ** ** ** 2   23   21 1022.6 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201061800 130  18 ***  26 BKN 5 * * 12.5 02 ** ** ** ** ** ** ** 7   34   27 1017.8 ***** ******  36 *** ***** ***** ***** ***** **
    029740 99999 195201070000 200  14 ***   8 OVC 7 * *  1.9 51 ** ** ** ** ** ** ** 5   37   36 1014.1 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201070600 250   2 ***   2 OVC 7 * *  1.5 51 ** ** ** ** ** ** ** 5   39   37 1008.9 ***** ****** ***  32 ***** ***** ***** ***** **
    029740 99999 195201071200 250  18 ***   5 OVC 5 * *  6.2 02 ** ** ** ** ** ** ** 2   39   37 1003.5 ***** ****** *** *** ***** ***** ***** ***** **
    029740 99999 195201071800 270  17 ***  15 OVC 7 * *  3.8 59 ** ** ** ** ** ** ** 2   41   39 1002.4 ***** ******  43 *** ***** ***** ***** ***** **
    029740 99999 195201080000 290  16 *** 722 CLR 0 0 0 12.5 00 ** ** ** ** ** ** ** 0   34   30 1009.5 ***** ****** *** *** ***** ***** ***** ***** **
    ...

Not that exciting, right?
There is an interesting story here, but we need some way to illustrate the power of this data.

One option is to use an *x*-*y* plot of temperature anomalies versus time.

.. figure:: https://www.ncdc.noaa.gov/sotc/service/global/global-land-ocean-mntp-anom/201101-201112.png
    :width: 800px
    :align: center
    :alt: Global mean temperature anomalies

    Global mean temperature anomalies from 1880-2011. Source: https://www.ncdc.noaa.gov/sotc/global/201113

This is obviously much better, showing clearly how temperatures have changed with time and how global temperatures have increased significantly since 1970.
Now we see a clear step toward making the data easier to understand.
However, this is global data and we are missing something important about the data, its connection to geographical locations.

Let's consider another option, plotting temperature anomalies on a map.

.. figure:: https://www.ncdc.noaa.gov/sotc/service/global/map-blended-mntp/202001.png
    :width: 800px
    :align: center
    :alt: Global mean temperature anomaly map

    Global temperature anomalies for January 2020. Source: https://www.ncdc.noaa.gov/sotc/global/201603

And yet again, this helps us understand the data further.
Not only do we see the changed in temperature, but now we see how temperatures vary across the globe.
The drawback here is that we only see a single time snapshot, rather than a time series.
To see both will require a truly remarkable visualization.

So, let's look now at some excellent examples of data visualization with Python.
We have essentially the same data plotted above, but now we can see how temperatures vary in space and time.

.. raw:: html

    <video width="800" controls>
      <source src="../../_static/Temp-anomalies-2018.mp4" type="video/mp4">
    </video>
    <p style="text-align:center"><i>Global temperature anomalies by country from 1900-2017. Visualization by Antti Lipponen (<a href="https://twitter.com/anttilip">@anttilip</a>). Source: <a href="https://t.co/ZdGPVTM5yO">https://t.co/ZdGPVTM5yO</a></i></p>

This animated "pill packet" plot of temperature anomalies conveys a huge amount of information in a simple form.
People can immediately understand what is plotted, and the combination of the plot format, colors and animation are very effective.
What even better is the fact that this animation was made using Python!

Another example shows similar data in a different format, including a peek into the future.

.. raw:: html

    <video width="800" controls>
      <source src="../../_static/Temp-anomalies-2019.mp4" type="video/mp4">
    </video>
    <p style="text-align:center"><i>Global temperature anomalies past and future, 1900-2100. Visualization by Antti Lipponen (<a href="https://twitter.com/anttilip">@anttilip</a>). Source: <a href="https://t.co/NP22dZ0sCu">https://t.co/NP22dZ0sCu</a></i></p>

This plot nicely conveys the warming of different regions on Earth, again in an intuitive format.

For the rest of the first part of this course, plots like that above can be our inspiration.
In fact, we will be working with similar data throughout this part of the course and may even end up producing similar plots in by the end of this teaching period.