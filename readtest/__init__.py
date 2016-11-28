def readtest():
    import csv

    csvfile = open('raw_data\industry_academy_age_gender_income.csv', 'rb')
    reader = csv.reader(csvfile, delimiter=',')
    row1 = next(reader)

    print row1
    csvfile.close()