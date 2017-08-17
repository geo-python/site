# Geo-Python 

This repo contains the source files of course material available at [https://geo-python.github.io/2017/](https://geo-python.github.io/2017/)

The course you to the basic concepts of computer programming in the Python programming language. 


## Course topics

## Lecture notes

## Building the GitHub-pages

This course website has been constructed in a similar way as the full [automating GIS-processes pages](https://github.com/Automating-GIS-processes/2016).
The pages are built using [Sphinx](http://www.sphinx-doc.org/en/1.4.9/) with modified version of the [Read The Docs theme](http://docs.readthedocs.io/en/latest/theme.html).
The following packages are needed in order to modify the pages (We recommend using [conda](http://conda.pydata.org/docs/using/pkgs.html#install-a-package) from [Anaconda Python distribution package](https://www.continuum.io/downloads)):

 - Sphinx

    ```
    conda install -c anaconda sphinx=1.5.1
    ```

 - Read The Docs Theme

    ```
    conda install -c anaconda sphinx_rtd_theme=0.1.9
    ```

## .rst files

Sphinx uses .rst -files ([reStucturedText](https://en.wikipedia.org/wiki/ReStructuredText)), and thus the source for the pages need to be written into .rst-files.
Markdown-dokuments `.md` can be converted to `.rst` -format using [Pandoc_convert_md_to_rst.py](/Pandoc_convert_md_to_rst.py) (converts all `.md`-files from the source directory to `.rst`-files).

`.rst` -files for these course pages are found under the [source](/source) -folder, and `.html` pages in the [docs](/docs) -folder (these are automatically generated using the make.bat command, see below).

## Building the pages

Shinx pages need to be built into html-format before publishing online.

- If you are starting from scratch, make sure you have a branch `gh-pages`.

`git branch -a`

If you can't see gh-pages in the list (in addition to master-branch), create it using

`git branch gh-pages` -command in the Terminal-window (you only need to do this once!)

## Generate html-files

- html-pages are built using the make.bat -batchfile:

`make html` (html-files will be under the docs-folder in the master-branch - useful if you don't want to publish changes straight away!)

`make gh-pages` (html-files are generated under the docs-folder in the gh-pages-branch - by default changes will be published online)

- Note! When building site with `make gh-pages` it is necessary to have a folder called `data` with at least a single template file in the root of the repo. Typically you end up having there many files but it is important to have at least a single file there when starting to build your site.

## Publish gh-pages online

- in GitHub, go to [settings](https://github.com/Automating-GIS-processes/FEC/settings)-page of the repo and set the Source for GitHub Pages to gh-pages branch.


