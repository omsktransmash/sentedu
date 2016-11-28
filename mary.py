# -*- coding: utf-8 -*-
import codecs
print "mary:D"

file = codecs.open('raw_data\industry_academy_age_gender_income.csv')
line= file.readline()
print line
file.close()
