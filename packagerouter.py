#! /usr/bin/env python3
import csv
from hashtable import HashTable
from anneal import Anneal
class PackageRouter():
    def __init__(self):
        self.packages = HashTable(41)
        self.locations = HashTable(41)

    def loadPackages(self, packageFile):
        packageReader = csv.reader(open(packageFile), delimiter=',')
        next(packageReader)
        for row in packageReader:
            package = HashTable()
            package['id'] = row[0]
            package['address'] = row[1]
            package['city'] = row[2]
            package['state'] = row[3]
            package['zip'] = row[4]
            package['readyTime'] = row[5]
            package['deadline'] = row[6]
            package['mass'] = row[7]
            package['group'] = row[8]
            package['truck'] = row[9]
            if package['truck']:
                package['truckRequired'] = True
            else:
                package['truckRequired'] = False
            self.packages[package['id']] = package

    def loadAddresses(self, addressFile):
        row_count = 0 
        addressCounter = csv.reader(open(addressFile), delimiter=',')
        row_count = sum(1 for row in addressCounter)
        addressReader = csv.reader(open(addressFile), delimiter=',')
        for row in addressReader:
            location = HashTable()
            location['id'] = row[0]
            location['description'] = row[1]
            location['address'] = row[2]
            location['zipcode'] = row[3]
            location['distances'] = [None] * row_count
            for i, distance in enumerate(row[4:]):
                if distance:
                    location['distances'][i] = distance
                    if i < int(location['id']):
                        print ("[{}][{}]".format(str(i),location['id']))
                        self.locations[str(i)]['distances'][int(location['id'])] = distance
                else:
                    break
            self.locations[location['id']] = location
        
    def correlate(self):
            
