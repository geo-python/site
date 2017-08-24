# -*- coding: utf-8 -*-
"""
Simple script to convert markdown files into RsT files using Pandoc. 

Usage: Put all md-files into a same directory ('indir') and specify output directory with 'outdir' variable. You may need to run this with
administrator rights (from cmd-prompt). The names of the rst files are using the same filename as their markdown counterparts. 

Created on Mon Feb 20 23:50:55 2017

@author: hentenka
"""

import subprocess
import glob
import os

# Input directory for md-files
indir = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Python-for-geo-people\Lesson-1-Course-Environment\MDs"

# Output directory for rst-files
outdir = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Python-for-geo-people\Lesson-1-Course-Environment\RST"

# Read all md files
files = glob.glob(os.path.join(indir, "*.md"))

# Iterate over MD-files and convert them to RST
for f in files:
    # Basename
    basename = os.path.basename(f)
    # Output path
    opath = os.path.join(outdir, basename.replace('.md', '.rst'))
    # Command
    cmd = "pandoc --from=markdown --to=rst --output=%s %s" % (opath, f)
    print(cmd)
    # Execute
    subprocess.call(cmd)
    
    