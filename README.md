# bib_cleaner
The Chicago reference style in BibTeX does not support URLs by default. This script hence takes a common `.bib` file, looks for `@misc` entries, takes the `url` and `urldate` parameters and saves these to a new `note` parameter, which is supported by the Chicago reference style. 

The result looks like this: 
Betterment (2018). Plans for every investor. https://www.betterment.com/pricing/ Accessed on: July 28, 2018.

# How to
1. Create a regular BibTeX file (named `bib.bib`by default). Internet sources should be saved as web pages, such that they appear as `@misc` entries in the bib file.
2. Export as `bib.bib`.
3. Run `bib_cleaner.py`. 
4. A new `bib_clean.bib` file is created. Attention: by default, the script appends entries to the bib file. Hence, it might be useful to create an emtpy file first.
5. Set `bib_clean.bib` as bibliography in TeX document. 

# Exceptions
In case no access date is specified in the original `.bib` file, the default behaviour is to  print `NO DAY`, `NO MONTH`, or `NO YEAR`, such that these cases can be easily spotted in the printed bibliography.
