# This is a short program which will convert the raw data from the large library
# available from http://help.sentiment140.com/for-students/ into a format which
# is readily compatible with the HolmesClassifier class - the source and
# destination file paths can be amended accordingly
#
# import csv
#
# with open("path/to/unformatted/csv", "rt") as source:
#     rdr = csv.reader(source)
#     with open("path/to/formatted/csv", "wt") as result:
#         wtr = csv.writer(result)
#         in_iter = ((str(r[5]), r[0]) for r in rdr)
#         wtr.writerows(in_iter)
