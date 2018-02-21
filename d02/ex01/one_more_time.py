#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import calendar
import re


def main():
    lc_days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    up_days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "vendredi", "Samedi", "Dimanche"]
    lc_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
               "décembre"]
    up_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
               "Décembre"]
    lc_na_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre",
               "decembre"]
    up_na_mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre",
               "Decembre"]
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            array = sys.argv[i].split(' ')
        if len(array) != 5:
            print "Wrong Format (len)"
            exit()
        else:
            day = array[0]
            if day in lc_days or day in up_days:
                day
            else:
                print ("Wrong Format (day)")
                exit()
            date = array[1]
            if len(date) == 1 or len(date) == 2:
                try:
                    date = int(array[1])
                except (TypeError, ValueError, AttributeError):
                    print ('it\'s not an int date')
                    exit()
            else:
                print "Wrong Format (date)"
                exit()
            month = array[2]
            if month in lc_mois or month in up_mois or month in lc_na_mois or month in up_na_mois:
                month
            else:
                print ("Wrong Format (month)")
                exit()
            year = array[3]
            if len(year) == 4:
                try:
                    year = int(array[3])
                except (TypeError, ValueError, AttributeError):
                    print ("Wrong Format (year)")
                    exit()
            else:
                print "Wrong Format (year)"
                exit()
            timestamp = array[4]
            if len(timestamp) == 8:
                if re.match(r'([0-9][0-9]:[0-9]{2}:[0-9]{2})', timestamp):
                    d = timestamp
                else:
                    print "Wrong Format (timestamp)"
                    exit()
            else:
                print "Wrong Format (timestamp)"
                exit()




if __name__ == "__main__":
    main()