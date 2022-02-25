# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

- This program will process and analyze a large data set and report the findings.
- The findings will be placed into the report, the report will print out the correct findings.
- This program will report correct findings despite the manipulation of the file, whether it is reversed, etc.
- A good solution will correctly report the findings, print out a usage message if no input is given, let python crash if dataset isn't an int. (eval() is evil)


- I know how to read a file line by line
- I know how manipulate strings
- I will need to watch the lecture and figure out how dictionary's work, this will aid my solution.
- FIPS codes may present an issue.

## Phase 1: System Analysis *(10%)*

**Deliver:**

- A directory will be provided by the user via the command line.
- The output will take the form of the provided report.
- The report will not include US aggregate data, per-state aggregate data, nor should it consider metropolitan areas
- This assignment will probably utilize for loops in order to loop through the file line by line.


## Phase 2: Design *(30%)*

**Deliver:**

```
def main(sys.argv):
    Takes directory from user, changes to that directory, and read the hardcoded files:`area_titles.csv` and `2020.annual.singlefile.csv`
    Utilize a dictionary in order to process FIPS
    Disclude certain FIPS if certain values are found("000", "C", US)
    Converts a string into an integer
    Uses a *probably* for loop to loop through the file line by line.
    Place values in software industry vs all industry based on "own code" and "industry code"
    print a usage error if no directory is given.
```
## Phase 3: Implementation *(15%)*

**Deliver:**

```python
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
                        rpt.soft.max_annual_wage = [FIPS[max_key].strip('"').lstrip(), int(a)]
# max establishments

                    softEstabLst.append(int(k[8]))
                    a = max(softEstabLst)
                    if str(a) == k[8]:
                        max_key = max(softInfo, key=softInfo.get(str(a)))
                        rpt.soft.max_estab = [FIPS[max_key].strip('"').lstrip(), int(a)]
# max employment

                    softEmplLst.append(int(k[9]))
                    a = max(softEmplLst)
                    if str(a) == k[9]:
                        max_key = max(softInfo, key=softInfo.get(str(a)))
                        rpt.soft.max_empl = [FIPS[max_key].strip('"').lstrip(), int(a)]

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
                        rpt.all.max_annual_wage = [FIPS[max_key].strip('"').lstrip(), int(a)]
#max establishments

                    allEstabLst.append(int(k[8]))
                    a = max(allEstabLst)
                    if str(a) == k[8]:
                        max_key = max(allInfo, key=allInfo.get(str(a)))
                        rpt.all.max_estab = [FIPS[max_key].strip('"').lstrip(), int(a)]
#max employment
                    allEmplLst.append(int(k[9]))
                    a = max(allEmplLst)
                    if str(a) == k[9]:
                        max_key = max(allInfo, key=allInfo.get(str(a)))
                        rpt.all.max_empl = [FIPS[max_key].strip('"').lstrip(), int(a)]
                else:
                    continue
```                    

- Throughout this assignment, there were a lot of things I had to learn dealing with dictionaries. When I was unable to figure out certain processes with dictionaries, I would append them to lists and do list operations.
- While testing, I ran into several issues because I was only testing a few .csv files. The csv files I tested did not cover all cases, this caused me to reassess my code for certain instances.
- I had issues with the finding the areas of the "max" portions, as well as finding the max portions. I then decided to use lists to manipulate information.
- The "total" parts of the report went very smoothly, those seemed to be the easiest part about the assignment.



## Phase 4: Testing & Debugging *(30%)*

**Deliver:**
- I did not create any personal tests, however, I did utilize 6-7 of the csv files, as well as USA_full to guaranty my code was working.
- Each case usually presented a different issue, I wasn't printing out the "x County" part, as well as issues with finding the key that corresponded with a max value.
- This was because I was just taking the last argument in the dictionary, I fixed this by searching for 'County' in the dictionary.
- Finding the max values was an easier fix, it was a simple if statement.


## Phase 5: Deployment *(5%)*

**Deliver:**

- My repository was pushed to GitLab, the final commit was present. Prior to pushing, I tested my code on several different files from the command line, the output seemed correct and should work on the grader's computer.


## Phase 6: Maintenance

**Deliver:**

###1.
- For the most part, I feel as if my code is fairly readable. I tried to seperate out the different portions of my code with comments. The comments are supposed to describe what is happening in that section of code.
- Most of my code is pretty understandable from my view, the code makes sense to me and how/why it works seems simple enough.
- Most of my debugging consisted of print statement debugging. If a problem were to arise, I feel like I could utilize this method to resolve the bug quickly.

###2.
- This code should make sense to most people, there were some portions where I could have used more descriptive variables, but overall my variables and comments were placed well in order to help people understand.
- This code will make sense to me in six months, this code is fairly well constructed. (in my opinion)

###3.
- It depends on the implementation. If it just requires searching for more data, then it should be easy enough. Especially if python has an inbuilt function.

###4.
- This program should work on new hardware, and would probably work better on new hardware.
- This program should work on new or different OS's.
- As long as the next versions don't change how dictionaries and any functions in my program work, it should run on the next version.

