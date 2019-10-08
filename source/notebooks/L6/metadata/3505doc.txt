                                                   06/26/2012

                  SURFACE HOURLY ABBREVIATED FORMAT

ONE HEADER RECORD FOLLOWED BY DATA RECORDS:

COLUMN  DATA DESCRIPTION

01-06   USAF = AIR FORCE CATALOG STATION NUMBER   
08-12   WBAN = NCDC WBAN NUMBER
14-25   YR--MODAHRMN = YEAR-MONTH-DAY-HOUR-MINUTE IN GREENWICH MEAN TIME (GMT)
27-29   DIR = WIND DIRECTION IN COMPASS DEGREES, 990 = VARIABLE, REPORTED AS
        '***' WHEN AIR IS CALM (SPD WILL THEN BE 000)
31-37   SPD & GUS = WIND SPEED & GUST IN MILES PER HOUR  
39-41   CLG = CLOUD CEILING--LOWEST OPAQUE LAYER
        WITH 5/8 OR GREATER COVERAGE, IN HUNDREDS OF FEET,
        722 = UNLIMITED 
43-45   SKC = SKY COVER -- CLR-CLEAR, SCT-SCATTERED-1/8 TO 4/8,
        BKN-BROKEN-5/8 TO 7/8, OVC-OVERCAST, 
        OBS-OBSCURED, POB-PARTIAL OBSCURATION   
47-47   L = LOW CLOUD TYPE, SEE BELOW
49-49   M = MIDDLE CLOUD TYPE, SEE BELOW
51-51   H = HIGH CLOUD TYPE, SEE BELOW  
53-56   VSB = VISIBILITY IN STATUTE MILES TO NEAREST TENTH 
        NOTE: FOR SOME STATIONS, VISIBILITY IS REPORTED ONLY UP TO A
        MAXIMUM OF 7 OR 10 MILES IN METAR OBSERVATIONS, BUT TO HIGHER
        VALUES IN SYNOPTIC OBSERVATIONS, WHICH CAUSES THE VALUES TO 
        FLUCTUATE FROM ONE DATA RECORD TO THE NEXT.  ALSO, VALUES
        ORIGINALLY REPORTED AS '10' MAY APPEAR AS '10.1' DUE TO DATA
        BEING ARCHIVED IN METRIC UNITS AND CONVERTED BACK TO ENGLISH.
58-68   MW MW MW MW = MANUALLY OBSERVED PRESENT WEATHER--LISTED BELOW IN PRESENT WEATHER TABLE
70-80   AW AW AW AW = AUTO-OBSERVED PRESENT WEATHER--LISTED BELOW IN PRESENT WEATHER TABLE
82-82   W = PAST WEATHER INDICATOR, SEE BELOW
84-92   TEMP & DEWP = TEMPERATURE & DEW POINT IN FAHRENHEIT 
94-99   SLP = SEA LEVEL PRESSURE IN MILLIBARS TO NEAREST TENTH 
101-105   ALT = ALTIMETER SETTING IN INCHES TO NEAREST HUNDREDTH 
107-112   STP = STATION PRESSURE IN MILLIBARS TO NEAREST TENTH
114-116  MAX = MAXIMUM TEMPERATURE IN FAHRENHEIT (TIME PERIOD VARIES)
118-120 MIN = MINIMUM TEMPERATURE IN FAHRENHEIT (TIME PERIOD VARIES)
122-126 PCP01 = 1-HOUR LIQUID PRECIP REPORT IN INCHES AND HUNDREDTHS --
        THAT IS, THE PRECIP FOR THE PRECEDING 1 HOUR PERIOD
128-132 PCP06 = 6-HOUR LIQUID PRECIP REPORT IN INCHES AND HUNDREDTHS --
        THAT IS, THE PRECIP FOR THE PRECEDING 6 HOUR PERIOD
134-138 PCP24 = 24-HOUR LIQUID PRECIP REPORT IN INCHES AND HUNDREDTHS
        THAT IS, THE PRECIP FOR THE PRECEDING 24 HOUR PERIOD
140-144 PCPXX = LIQUID PRECIP REPORT IN INCHES AND HUNDREDTHS, FOR 
        A PERIOD OTHER THAN 1, 6, OR 24 HOURS (USUALLY FOR 12 HOUR PERIOD
        FOR STATIONS OUTSIDE THE U.S., AND FOR 3 HOUR PERIOD FOR THE U.S.)
        T = TRACE FOR ANY PRECIP FIELD
146-147 SD = SNOW DEPTH IN INCHES  


NOTES:  

- *'s IN FIELD INDICATES ELEMENT NOT REPORTED.

- SOME VALUES WERE CONVERTED FROM METRIC TO ENGLISH UNITS.  THIS WILL
OCCASIONALLY RESULT IN MINOR DIFFERENCES VS ORIGINAL DATA DUE TO ROUNDING.

- COLUMN POSITION REFERS TO ASCII TEXT DATA.  

- THIS FORMAT CAN BE EASILY IMPORTED INTO A SPREADSHEET OR A DATABASE
MANAGEMENT SYSTEM SINCE FIELDS ARE SPACE-DELIMITED.

- THIS FORMAT DOES NOT INCLUDE QUALITY CONTROL FLAGS, WHICH ARE AVAILABLE
IN THE ADVANCED FORMAT THROUGH THE CLIMATE DATA ONLINE SYSTEM.


                    PRESENT WEATHER CODE TABLE 

The code that denotes a specific type of weather observed.
-----------------------------------------------------------------
00-49  No precipitation at the station at the time of observation
-----------------------------------------------------------------
00-19  No precipitation, fog, ice fog (except for 11 and 12),
duststorm, sandstorm, drifting or blowing snow at the station at the
time of observation or, except for 09 and 17, during the preceding
hour
-----------------------------------------------------------------
00: Cloud development not observed or not observable
01: Clouds generally dissolving or becoming less developed
02: State of sky on the whole unchanged
03: Clouds generally forming or developing
04: Visibility reduced by smoke, e.g. veldt or forest fires,
industrial smoke or volcanic ashes
05: Haze
06: Widespread dust in suspension in the air, not raised by wind at
or near the station at the time of observation
07: Dust or sand raised by wind at or near the station at the time of
observation, but no well-developed dust whirl(s) or sand whirl(s),
and no duststorm or sandstorm seen or, in the case 
of ships, blowing spray at the station
08: Well developed dust whirl(s) or sand whirl(s) seen at or near the
station during the preceding hour or at the time of observation, but
no duststorm or sandstorm
09: Duststorm or sandstorm within sight at the time of observation,
or at the station during the preceding hour
10: Mist
11: Patches of shallow fog or ice fog at the station, whether on land
or sea, not deeper than about 2 meters on land or 10 meters at sea
12: More or less continuous shallow fog or ice fog at the station,
whether on land or sea, not deeper than about 2 meters on land or 10
meters at sea 
13: Lightning visible, no thunder heard
14: Precipitation within sight, not reaching the ground or the
surface of the sea
15: Precipitation within sight, reaching the ground or the surface of
the sea, but distant, i.e., estimated to be more than 5 km from the
station
16: Precipitation within sight, reaching the ground or the surface of
the sea, near to, but not at the station
17: Thunderstorm, but no precipitation at the time of observation
18: Squalls at or within sight of the station during the preceding
hour or at the time of observation
19: Funnel cloud(s) (Tornado cloud or waterspout) at or within sight
of the station during the preceding hour or at the time of
observation 
-----------------------------------------------------------------
20-29  Precipitation, fog, ice fog or thunderstorm at the station
during the preceding hour, but not at the time of observation
-----------------------------------------------------------------
20: Drizzle (not freezing) or snow grains not falling as shower(s)
21: Rain (not freezing) not falling as shower(s)
22: Snow not falling as shower(s)
23: Rain and snow or ice pellets not falling as shower(s)
24: Freezing drizzle or freezing rain not falling as shower(s)
25: Shower(s) of rain
26: Shower(s) of snow or of rain and snow
27: Shower(s) of hail (Hail, small hail, snow pellets), or rain and
hail
28: Fog or ice fog
29: Thunderstorm (with or without precipitation)
-----------------------------------------------------------------
30-39  Duststorm, sandstorm, or blowing snow
-----------------------------------------------------------------
30: Slight or moderate duststorm or sandstorm has decreased during
the preceding hour
31: Slight or moderate duststorm or sandstorm no appreciable change
during the preceding hour
32: Slight or moderate duststorm or sandstorm has begun or has
increased during the preceding hour
33: Severe duststorm or sandstorm has decreased during the preceding
hour
34: Severe duststorm or sandstorm no appreciable change during the
preceding hour
35: Severe duststorm or sandstorm has begun or has increased during
the preceding hour
36: Slight or moderate drifting snow generally low (below eye level)
37: Heavy drifting snow generally low (below eye level)
38: Slight or moderate blowing snow generally high (above eye level)
39: Heavy blowing snow generally high (above eye level)
-----------------------------------------------------------------
40-49  Fog or ice fog at the time of observation
-----------------------------------------------------------------
40: Fog or ice fog at a distance at the time of observation, but not
at the station during the preceding hour, the fog or ice fog
extending to a level above that of the observer
41: Fog or ice fog in patches
42: Fog or ice fog, sky visible, has become thinner during the
preceding hour
43: Fog or ice fog, sky invisible, has become thinner during the
preceding hour
44: Fog or ice fog, sky visible, no appreciable change during the
preceding hour
45: Fog or ice fog, sky invisible, no appreciable change during the
preceding hour
46: Fog or ice fog, sky invisible, has begun or has become thicker
during the preceding hour
47: Fog or ice fog, sky invisible, has begun or has become thicker
during the preceding hour
48: Fog, depositing rime, sky visible
49: Fog, depositing rime, sky invisible
-----------------------------------------------------------------
50-99  Precipitation at the station at the time of observation
-----------------------------------------------------------------
50-59  Drizzle
-----------------------------------------------------------------
50: Drizzle, not freezing, intermittent, slight at time of
observation
51: Drizzle, not freezing, continuous, slight at time of observation
52: Drizzle, not freezing, intermittent, moderate at time of
observation
53: Drizzle, not freezing, continuous, moderate at time of
observation
54: Drizzle, not freezing, intermittent, heavy (dense) at time of
observation
55: Drizzle, not freezing, continuous, heavy (dense) at time of
observation
56: Drizzle, freezing, slight
57: Drizzle, freezing, moderate or heavy (dense)
58: Drizzle and rain, slight
59: Drizzle and rain, moderate or heavy
-----------------------------------------------------------------
60-69  Rain
-----------------------------------------------------------------
60: Rain, not freezing, intermittent, slight at time of observation
61: Rain, not freezing, continuous, slight at time of observation
62: Rain, not freezing, intermittent, moderate at time of observation
63: Rain, not freezing, continuous, moderate at time of observation
64: Rain, not freezing, intermittent, heavy at time of observation
65: Rain, not freezing, continuous, heavy at time of observation
66: Rain, freezing, slight
67: Rain, freezing, moderate or heavy
68: Rain or drizzle and snow, slight
69: Rain or drizzle and snow, moderate or heavy
-----------------------------------------------------------------
70-79  Solid precipitation not in showers
-----------------------------------------------------------------
70: Intermittent fall of snowflakes, slight at time of observation
71: Continuous fall of snowflakes, slight at time of observation
72: Intermittent fall of snowflakes, moderate at time of observation
73: Continuous fall of snowflakes, moderate at time of observation
74: Intermittent fall of snowflakes, heavy at time of observation
75: Continuous fall of snowflakes, heavy at time of observation
76: Diamond dust (with or without fog)
77: Snow grains (with or without fog)
78: Isolated star-like snow crystals (with or without fog)
79: Ice pellets
-----------------------------------------------------------------
80-99  Showery precipitation, or precipitation with current or recent
thunderstorm
-----------------------------------------------------------------
80: Rain shower(s), slight
81: Rain shower(s), moderate or heavy
82: Rain shower(s), violent
83: Shower(s) of rain and snow mixed, slight
84: Shower(s) of rain and snow mixed, moderate or heavy
85: Show shower(s), slight
86: Snow shower(s), moderate or heavy
87: Shower(s) of snow pellets or small hail, with or without rain or
rain and snow mixed, slight
88: Shower(s) of snow pellets or small hail, with or without rain or
rain and snow mixed, moderate or heavy
89: Shower(s) of hail (hail, small hail, snow pellets) , with or
without rain or rain and snow mixed, not associated with thunder,
slight
90: Shower(s) of hail (hail, small hail, snow pellets), with or
without rain or rain and snow mixed, not associated with thunder,
moderate or heavy
91: Slight rain at time of observation, thunderstorm during the
preceding hour but not at time of observation
92: Moderate or heavy rain at time of observation, thunderstorm
during the preceding hour but not at time of observation
93: Slight snow, or rain and snow mixed or hail (Hail, small hail,
snow pellets), at time of observation, thunderstorm during the
preceding hour but not at time of observation
94: Moderate or heavy snow, or rain and snow mixed or hail(Hail,
small hail, snow pellets) at time of observation, thunderstorm during
the preceding hour but not at time of observation
95: Thunderstorm, slight or moderate, without hail (Hail, small hail,
snow pellets), but with rain and/or snow at time of observation,
thunderstorm at time of  observation
96: Thunderstorm, slight or moderate, with hail (hail, small hail,
snow pellets) at time of observation, thunderstorm at time of
observation
97: Thunderstorm, heavy, without hail (Hail, small hail, snow
pellets), but with rain  and/or snow at time of observation,
thunderstorm at time of observation
98: Thunderstorm combined with duststorm or sandstorm at time of
observation, thunderstorm at time of observation
99: Thunderstorm, heavy, with hail (Hail, small hail, snow pellets)
at time of observation, thunderstorm at time of observation


                           PAST WEATHER CODE TABLE

The code that denotes a specific type of past weather observed.
0: Cloud covering 1/2 or less of the sky throughout the appropriate
period
1: Cloud covering more than 1/2 of the sky during part of the
appropriate period and covering 1/2 or less during part of the period
2: Cloud covering more than 1/2 of the sky throughout the appropriate
period
3: Sandstorm, duststorm or blowing snow
4: Fog or ice fog or thick haze
5: Drizzle
6: Rain
7: Snow, or rain and snow mixed
8: Shower(s)
9: Thunderstorm(s) with or without precipitation


                              LOW CLOUD TYPE

0: No low clouds
1: Cumulus humulis or Cumulus fractus other than of bad weather or
both 
2: Cumulus mediocris or congestus, with or without Cumulus of
species  fractus or humulis or Stratocumulus all having bases at the
same level
3: Cumulonimbus calvus, with or without Cumulus, Stratocumulus or
Stratus
4: Stratocumulus cumulogenitus
5: Stratocumulus other than Stratocumulus cumulogenitus
6: Stratus nebulosus or Stratus fractus other than of bad weather,
or both
7: Stratus fractus or Cumulus fractus of bad weather, or both
(pannus) usually below Altostratus or Nimbostratus
8: Cumulus and Stratocumulus other than Stratocumulus cumulogenitus,
with bases at different levels
9: Cumulonimbus capillatus (often with an anvil), with or without
Cumulonimbus calvus, Cumulus, Stratocumulus, Stratus or pannus
  

                            MIDDLE CLOUD TYPE

0: No middle clouds
1: Altostratus translucidus
2: Altostratus opacus or Nimbostratus
3: Altocumulus translucidus at a single level
4: Patches (often lenticular) of Altocumulus translucidus,
continually changing and occurring at one or more levels
5: Altocumulus translucidus in bands, or one or more layers of
Altocumulus translucidus or opacus, progressively invading the sky;
these Altocumulus clouds generally thicken as a whole
6: Altocumulus cumulogentis (or cumulonimbogentus)
7: Altocumulus translucidus or opacus in two or more layers, or
Altocumulus opacus in a single layer, not progressively invading the
sky, or Altocumulus with Altostratus or Nimbostratus
8: Altocumulus castellanus or floccus
9: Altocumulus of a chaotic sky; generally at several levels


                             HIGH CLOUD TYPE 

0: No High Clouds
1: Cirrus fibratus, sometimes uncinus, not progressively invading
the sky
2: Cirrus spissatus, in patches or entangled sheaves, which usually
do not increase and sometimes seem to be the remains of the upper
part  of a Cumulonimbus; or Cirrus castellanus or floccus
3: Cirrus spissatus cumulonimbogenitus
4: Cirrus unicinus or fibratus, or both, progressively invading the
sky; they generally thicken as a whole
5: Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone,
progressively invading the sky; they generally thicken as a whole,
but the continuous veil does not reach 45 degrees above the horizon
6: Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone,
progressively invading the sky; they generally thicken as a whole;
the continuous veil extends more than 45 degrees above the horizon,
without the sky being totally covered
7: Cirrostratus covering the whole sky
8: Cirrostratus not progressively invading the sky and not entirely
covering it
9: Cirrocumulus alone, or Cirrocumulus predominant among the High
clouds
