# Search-Vocabulary-By-Kanji

How to use:

```bash
./main.py k:<kanjiListFile> w:<wordListFile> o:<outputFile> t:<type>
```
File names without spaces.

Any argument can be ommited.
Default values for arguments are:
- k: known-kanji.csv
- w: wordlist.csv
- o: output.csv
- t: all

Avalible types are:
- all - all words form word list
- alk - only words with all kanji known
- ku - only words with unknown kanji
- ko - only kana only words

When unknown type entered type will be set to all  
List of known kanji should have 1 column, list of words 2 columns.
