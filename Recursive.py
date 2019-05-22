#!/usr/bin/python
import time
import sys

# 1. Creating list of alignments
# 2. Score an alignment

"""PART1"""

alignments_list = []


def all_alignments(n, m, seq1, seq2):
    if len(seq1) == 0 or len(seq2) == 0:  # if seq1 or seq2 are empty then fill up the remaining
        if len(seq1) == 0:  # bits of the strings in the alignment with the same
            m = seq2 + m  # amount of hyphens as the length of the remaining unaligned
            n = "-" * len(seq2) + n  # string in either seq1 or seq2 (whichever isnt empty)
        elif len(seq2) == 0:
            n = seq1 + n
            m = "-" * len(seq1) + m
        alignments_list.append([n, m])
    else:
        n_new = seq1[-1] + n
        m_new = seq2[-1] + m
        n = "-" + n
        m = "-" + m
        all_alignments(n_new, m_new, seq1[:-1], seq2[:-1])  # case where (n, m) added into alignment
        all_alignments(n, m_new, seq1, seq2[:-1])  # case of (blank, m) added into alignment
        all_alignments(n_new, m, seq1[:-1], seq2)  # case of (n, blank) added into alignment        


def score(str1, str2):
    current_score = 0
    for j in range(min(len(str1), len(str2))):
        if str1[j] == str2[j]:
            current_score += 3  # match
        elif str1[j] == "-" or str2[j] == "-":
            current_score -= 2  # gap
        elif str1[j] != str2[j]:
            current_score -= 1  # mis-match
    return current_score


def best_alignment():
    global best_score
    best_score = score(alignments_list[0][0], alignments_list[0][1])
    global best_alignment_
    best_alignment_ = (alignments_list[0][0], alignments_list[0][1])
    for i in alignments_list:  # for each pair of strings making an alignment
        string1 = i[0]
        string2 = i[1]
        alignment_score = score(string1, string2)
        if alignment_score >= best_score:  # update best score and best alignment
            best_score = alignment_score
            best_alignment_ = i

# ------------------------------------------------------------


# ------------------------------------------------------------
# Given an alignment, which is two strings, display it

def display_alignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            string3 = string3 + "|"
        else:
            string3 = string3 + " "
    print('Alignment ')
    print('String1: ' + string1)
    print('         ' + string3)
    print('String2: ' + string2 + '\n\n')


# ------------------------------------------------------------


# ------------------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1 = file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2 = file2.read()
file2.close()
start = time.time()

# -------------------------------------------------------------


# -------------------------------------------------------------
# The sequences are contained in the variables seq1 and
# seq2 from the code above. Call the function to create the list of alignments Call the function to score each of the
# alignments. To work with the printing functions below your list of alignments should be called alignments_list. The
# best alignment should be called best_alignment and its score should be called best_score.

all_alignments("", "", seq1, seq2)
print(alignments_list)
best_alignment()

# -------------------------------------------------------------


# ------------------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken = stop - start

# Print out the best
print('Alignments generated: ' + str(len(alignments_list)))
print('Time taken: ' + str(time_taken))
print('Best (score ' + str(best_score) + '):')
print("Best alignment: ", best_alignment_)
display_alignment(best_alignment_)

# -------------------------------------------------------------
