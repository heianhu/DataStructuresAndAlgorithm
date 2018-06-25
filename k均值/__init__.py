#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

from k均值 import kMeans
from numpy import *

if __name__ == '__main__':
    fileName = 'places.txt'
    imgName = 'Portland.png'
    kMeans.clusterClubs(fileName=fileName, imgName=imgName, numClust=5)
