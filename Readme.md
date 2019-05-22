# DNA String Matching

Recursive, Dynamic Programming, and Ends-Free Scoring approaches to DNA String Matching (ATGC).

The purpose of this project was to understand the benefits of dynamic programming and the pitfalls of recursion.

## Usage

Sequence Data of example DNA string of varying lengths are provided in the zip file. To calculate an alignment:

```bash
python3 PROGRAM.py sequence1.txt sequence2.txt
```

where PROGRAM.py is the chosen algorithm.

The run time is given, as well as the best alignment found. Alignments are scored as follows:
* +3 for an ATGC match at an index 
* -2 for a gap (-) at an index
* -1 for an ATGC mismatch at an index.

e.g. The following alignment for GAA and TGT has a score of -2
```
-GAA
TG-T
```
