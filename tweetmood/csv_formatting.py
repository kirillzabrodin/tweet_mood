# import csv
#
# with open("tweetmood/trainingsample.csv","rt") as source:
#     rdr= csv.reader( source )
#     with open("tweetmood/formatted_train.csv","wt") as result:
#         wtr= csv.writer( result )
#         in_iter= ( (r[5], r[0]) for r in rdr )
#         wtr.writerows( in_iter )
