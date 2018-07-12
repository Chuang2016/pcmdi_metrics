from __future__ import print_function

import cdms2
import cdtime
import cdutil
import os
import sys
 
pathin = '/work/cmip5-test/new/historical/atmos/day/pr/'
 
lst = os.listdir(pathin)

list_regions = ['ASM']  # Will be added later

debug = True


regions_specs = {}
exec(compile(open(sys.prefix + "/share/pmp/default_regions.py").read(),
             sys.prefix + "/share/pmp/default_regions.py", 'exec'))


for l in lst[0:1]:  # model loop
 
    print(pathin + l)
    fc = cdms2.open(pathin + l)
    d = fc['pr']  # NOTE: square brackets does not bring data into memory, only coordinates!
    t = d.getTime()
    c = t.asComponentTime()
   
    startYear = c[0].year
    startMonth = c[0].month
    endYear = c[-1].year
    endMonth = c[-1].month

    # Consider entire calendar years only
    if startMonth > 1:
        startYear += 1
    if endMonth < 12:
        endYear -= 1

    if debug:
        print('debug: startYear: ', type(startYear), startYear)
        print('debug: startMonth: ', type(startMonth), startMonth)
        print('debug: endYear: ', type(endYear), endYear)
        print('debug: endMonth: ', type(endMonth), endMonth)

    if debug:
        endYear = startYear
   
    for year in range(startYear, endYear+1):  # year loop, endYear+1 to include last year
        d = fc('pr',time=(cdtime.comptime(year),cdtime.comptime(year+1)))
        print('debug: year: ', year)
        print('debug: d.shape: ', d.shape)
      
        for region in list_regions:
            d_sub = d(regions_specs[region]['domain'])  # extract for monsoon region
            d_sub_aave = cdutil.averager(d_sub, axis='xy', weights='weighted')  # area average
            if debug: 
                print('debug: region: ', region)
                print('debug: d_sub.shape: ', d_sub.shape)
                print('debug: d_sub_aave.shape: ', d_sub_aave.shape)
  
   
