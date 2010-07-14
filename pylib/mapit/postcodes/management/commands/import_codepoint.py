# This script is used to import Great Britain postcode information from
# Code-Point Open, released by the Ordnance Survey. Compared to the
# scripts we had in 2003, and that the data is free, I'm in heaven.
# 
# The fields of Code-Point Open CSV file are:
#   Postcode, Quality, 8 blanked out fields, Easting Northing, Country,
#   NHS region, NHS health authority, County, District, Ward, blanked field

import csv
from django.contrib.gis.geos import Point
from django.core.management.base import LabelCommand
from mapit.postcodes.models import Postcode

class Command(LabelCommand):
    help = 'Import OS Code-Point Open postcodes'
    args = '<Code-Point CSV files>'
    count = 0
    def handle_label(self, file, **options):
        for row in csv.reader(open(file)):
            if row[1] == '90': continue # Bad postcode
            postcode = row[0].strip().replace(' ', '')
            location = Point(map(float, row[10:12]), srid=27700)
            Postcode.objects.update_or_create({ 'postcode': postcode }, { 'location': location })
            self.count += 1
            if self.count % 10000 == 0:
                print "Imported %d" % self.count
