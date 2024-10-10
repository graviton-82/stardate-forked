#!/usr/bin/python3
# Date: Mon 24 Jun 2019 17:36:52 CEST
# Author: Nicolas Flandrois
# Description: Running Stardate

# Edited to simply return stardate to terminal - Basil Williams

import datetime
import os
import platform
from sdcompute import Compute

def only_stardate():
    return Compute.sdconvert(datetime.datetime.now().timetuple())
def today_stardate():
    print("Current Earthdate : ", datetime.datetime.now())
    print("Current Stardate  : ", Compute.sdconvert(
          datetime.datetime.now().timetuple()))

#only_stardate
#print(today_stardate())

today_stardate()
