#!/usr/bin/env python                                               	         	  

#                         ~                                         	         	  
#                        (o)<  DuckieCorp Software License          	         	  
#                   .____//                                         	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor         	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	  
#                                                                   	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR     	  
# customer of DuckieCorp, to deal in the Software without restriction,        	  
# including without limitation the rights to use, copy, modify, merge,        	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to 	  
# permit persons to whom the Software is furnished to do so, subject to the   	  
# following conditions:                                             	         	  
#                                                                   	         	  
# The above copyright notice and this permission notice shall be included in  	  
# all copies or substantial portions of the Software.               	         	  
#                                                                   	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS	  
# IN THE SOFTWARE.                                                  	         	  

import time                                                         	         	  
import sys                                                          	         	  
from Report import Report                                           	         	  


rpt = Report(year=2020)                                             	         	  

if __name__ == '__main__':
    print("Reading the databases...", file=sys.stderr)
    before = time.time()
    if len(sys.argv)-1 == 0:
        print("Error: No directory was given.")
    else:
        a = sys.argv[1]
        FIPS = {}
        file = open(f'{a}/area_titles.csv')
        file.readline()
        for line in file:
            kv = line.rstrip().split(',')
            if 'C' in kv[0]:
                continue
            elif 'US' in kv[0]:
                continue
            elif '000' in kv[0][3:6]:
                continue
            else:
                if 'County' in kv[1]:
                    FIPS[kv[0]] = kv[len(kv)-2] + ',' + kv[len(kv)-1]
                else:
                    FIPS[kv[0]] = kv[len(kv)-1]
                continue

        file.close()
#-----------------------------------------------------------------------------------------------------------------------
        softInfo = {}
        allInfo = {}
        allEstabLst = []
        allWageLst = []
        allEmplLst = []
        softEstabLst = []
        softWageLst = []
        softEmplLst = []
        fobj = open(f'{a}/2020.annual.singlefile.csv')
        fobj.readline()
        for line in fobj:
            if line[0:7] in FIPS:
                k = line.rstrip().split(',')
                if k[2] == '"5112"' and k[1] == '"5"':
                    softInfo[k[0]] = line
                    rpt.soft.num_areas = len(softInfo)
                    rpt.soft.total_annual_wages += int(k[10])
                    rpt.soft.total_estab += int(k[8])
                    rpt.soft.total_empl += int(k[9])
# max annual wage

                    softWageLst.append(int(k[10]))
                    a = max(softWageLst)
                    if str(a) == k[10]:
                        max_key = max(softInfo, key=softInfo.get(str(a)))
                        rpt.soft.max_annual_wage = [FIPS[k[0]].strip('"').lstrip(), int(a)]
# max establishments

                    softEstabLst.append(int(k[8]))
                    a = max(softEstabLst)
                    if str(a) == k[8]:
                        max_key = max(softInfo, key=softInfo.get(str(a)))
                        rpt.soft.max_estab = [FIPS[k[0]].strip('"').lstrip(), int(a)]
# max employment

                    softEmplLst.append(int(k[9]))
                    a = max(softEmplLst)
                    if str(a) == k[9]:
                        max_key = max(softInfo, key=softInfo.get(str(a)))
                        rpt.soft.max_empl = [FIPS[k[0]].strip('"').lstrip(), int(a)]

                elif k[2] == '"10"' and k[1] == '"0"':
                    allInfo[k[0]] = line
                    rpt.all.num_areas = len(allInfo)
                    rpt.all.total_annual_wages += int(k[10])
                    rpt.all.total_estab += int(k[8])
                    rpt.all.total_empl += int(k[9])
#max annual wage

                    allWageLst.append(int(k[10]))
                    a = max(allWageLst)
                    if str(a) == k[10]:
                        max_key = max(allInfo, key=allInfo.get(k[10]))
                        rpt.all.max_annual_wage = [FIPS[k[0]].strip('"').lstrip(), int(a)]
#max establishments

                    allEstabLst.append(int(k[8]))
                    a = max(allEstabLst)
                    if str(a) == k[8]:
                        max_key = max(allInfo, key=allInfo.get(str(a)))
                        rpt.all.max_estab = [FIPS[k[0]].strip('"').lstrip(), int(a)]
#max employment
                    allEmplLst.append(int(k[9]))
                    a = max(allEmplLst)
                    if str(a) == k[9]:
                        max_key = max(allInfo, key=allInfo.get(str(a)))
                        rpt.all.max_empl = [FIPS[k[0]].strip('"').lstrip(), int(a)]
                else:
                    continue

        fobj.close()
    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    print(rpt)

