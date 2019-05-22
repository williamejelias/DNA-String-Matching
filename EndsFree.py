#!/usr/bin/python
import time
import sys

# ------------------------------------------------------------
# 1. Creating list of alignments
# 2. Score an alignment

"""PART 3"""


def score(x, y):
    if seq1[x] == seq2[y]:
        return 3
    else:
        return -1


best_score = 0


def dynamic_alignment(seq1, seq2):
    n = len(seq1) + 1
    m = len(seq2) + 1
    gap_score = -2
    # these variables are used frequently and its easier to save them like this

    # initialise a matrix of size ((length seq1)+1) * ((length seq2)+1), (n+1 columns and m+1 rows)
    score_matrix = [[0 for i in range(n)] for j in range(m)]
    traceback_matrix = [[" " for i in range(n)] for j in range(m)]
    traceback_matrix[0][0] = "END"

    # set base conditions
    for i in range(1, len(score_matrix)):
        traceback_matrix[i][0] = "U"  # first column of traceback matrix filled with "U"
        traceback_matrix[0][i] = "L"  # top row of traceback matrix filled with "L"

    # calculate all score_matrix[i][j]
    for row in range(1, m):
        for column in range(1, n):
            match = score_matrix[row - 1][column - 1] + score(column - 1, row - 1)
            gap_seq1 = score_matrix[row - 1][column] + gap_score
            gap_seq2 = score_matrix[row][column - 1] + gap_score
            if row == m - 1 and column == n - 1:
                score_matrix[row][column] = max(match, gap_seq1 - gap_score,
                                                gap_seq2 - gap_score)  # no gap penalty moving from bottom right cell
            elif row == m - 1:
                score_matrix[row][column] = max(match, gap_seq1,
                                                gap_seq2 - gap_score)  # no gap penalty moving from final row
            elif column == n - 1:
                score_matrix[row][column] = max(match, gap_seq1 - gap_score,
                                                gap_seq2)  # no gap penalty moving from final column
            else:
                score_matrix[row][column] = max(match, gap_seq1,
                                                gap_seq2)  # value in matrix takes the maximum value of the score for
                # each possibility up to that point
            global best_score
            best_score = score_matrix[m - 1][
                n - 1]  # update best_score with the value in the bottom right corner of the matrix

    for row in range(1, m):
        for column in range(1, n):
            if row == m - 1 and column == n - 1:
                if score_matrix[row][column] == (score_matrix[row - 1][column - 1] + score(column - 1, row - 1)):
                    traceback_matrix[row][
                        column] = "D"  # insert "D" into the traceback matrix if the max score came from the entry
                    # left-diagonally above
                elif score_matrix[row][column] == score_matrix[row - 1][column]:
                    traceback_matrix[row][
                        column] = "U"  # insert "U" into the traceback matrix if the max score came from the entry
                    # above / no gap penalty
                elif score_matrix[row][column] == score_matrix[row][column - 1]:
                    traceback_matrix[row][
                        column] = "L"  # insert "L" into the traceback matrix if the max score came from the entry
                    # left  / no gap penalty
            elif row == m - 1:
                if score_matrix[row][column] == (score_matrix[row - 1][column - 1] + score(column - 1, row - 1)):
                    traceback_matrix[row][
                        column] = "D"  # insert "D" into the traceback matrix if the max score came from the entry
                    # left-diagonally above
                elif score_matrix[row][column] == (score_matrix[row - 1][column] + gap_score):
                    traceback_matrix[row][
                        column] = "U"  # insert "U" into the traceback matrix if the max score came from the entry above
                elif score_matrix[row][column] == score_matrix[row][column - 1]:
                    traceback_matrix[row][
                        column] = "L"  # insert "L" into the traceback matrix if the max score came from the entry
                    # left  / no gap penalty
            elif column == n - 1:
                if score_matrix[row][column] == (score_matrix[row - 1][column - 1] + score(column - 1, row - 1)):
                    traceback_matrix[row][
                        column] = "D"  # insert "D" into the traceback matrix if the max score came from the entry
                    # left-diagonally above
                elif score_matrix[row][column] == score_matrix[row - 1][column]:
                    traceback_matrix[row][
                        column] = "U"  # insert "U" into the traceback matrix if the max score came from the entry
                    # above / no gap penalty
                elif score_matrix[row][column] == (score_matrix[row][column - 1] + gap_score):
                    traceback_matrix[row][
                        column] = "L"  # insert "L" into the traceback matrix if the max score came from the entry left
            else:
                if score_matrix[row][column] == (score_matrix[row - 1][column - 1] + score(column - 1, row - 1)):
                    traceback_matrix[row][
                        column] = "D"  # insert "D" into the traceback matrix if the max score came from the entry
                    # left-diagonally above
                elif score_matrix[row][column] == (score_matrix[row - 1][column] + gap_score):
                    traceback_matrix[row][
                        column] = "U"  # insert "U" into the traceback matrix if the max score came from the entry above
                elif score_matrix[row][column] == (score_matrix[row][column - 1] + gap_score):
                    traceback_matrix[row][
                        column] = "L"  # insert "L" into the traceback matrix if the max score came from the entry left
                else:
                    print("Error")

    seq1_alignment = ""
    seq2_alignment = ""  # initialise the strings of the alignment as empty

    while traceback_matrix[m - 1][n - 1] != "END":  # do for every box in the traceback matrix that doesnt contain "END"
        x = traceback_matrix[m - 1][n - 1]
        if x == "D":  # a match - insert the character from both sequences into the strings of the alignment
            seq1_alignment = seq1[-1] + seq1_alignment
            seq2_alignment = seq2[-1] + seq2_alignment
            seq1 = seq1[:-1]
            seq2 = seq2[:-1]  # chop the last character off both input sequences
            m -= 1
            n -= 1  # move the index being checked one unit left-diagonally in the traceback matrix
        elif x == "U":  # a gap - gap in seq1 matched with character from seq 2
            seq1_alignment = "-" + seq1_alignment
            seq2_alignment = seq2[-1] + seq2_alignment
            seq2 = seq2[:-1]  # chop the last character off only seq2
            m -= 1  # move index one row up in traceback matrix
        elif x == "L":  # a gap - a gap in seq2 is matched with a character from seq1
            seq1_alignment = seq1[-1] + seq1_alignment
            seq2_alignment = "-" + seq2_alignment
            seq1 = seq1[:-1]  # chop the last character off only seq1
            n -= 1  # move index one column to the right in the traceback matrix
        else:
            print("Error")
            break

    global best_alignment
    best_alignment = [seq1_alignment, seq2_alignment]


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


# ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1 = file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2 = file2.read()
file2.close()
start = time.time()

# -------------------------------------------------------------


# The sequences are contained in the variables seq1 and
# seq2 from the code above. Call the function to create the list of alignments Call the function to score each of the
# alignments. To work with the printing functions below your list of alignments should be called alignments_list. The
# best alignment should be called best_alignment and its score should be called best_score.

dynamic_alignment(seq1, seq2)

# -------------------------------------------------------------


# ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken = stop - start

# Print out the best
print('Time taken: ' + str(time_taken))
print('Best (score ' + str(best_score) + '):')
display_alignment(best_alignment)

# -------------------------------------------------------------
