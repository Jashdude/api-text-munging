import re
import pprint

# Question 1: open the file for reading
with open("MonsterJobsData_variations.txt", 'r' ) as f:
    lines = f.readlines()
    final_list, list2, list3, list4, list5 = [], [], [], [], []
    val, spl, und, htm, dotb = 0,0,0,0,0
    # Question 2: for each line in the file, use a RE to scan the line and capture any email address of the type show below.
    # You may assume there can be at most one email address (of any type) per line.
    for line in lines:
        # Search 1 - a valid email address format
        #valid = re.search(r'[\w\.-]+@[\w\.-]+', line)
        valid = re.search(r"[\w\.!#$%&'*+-/=?^_`{|}~]+@[\w\.-]+", line)
        if valid is not None:
            val += 1
            final_list.append(valid.group().replace('com.','com'))
        # Search 4 - Find patterns like email ids masked with spaces jeff dot Roberts at duq dot edu
        dot_before = re.search(r"\w+\s+d+o+t+\s+\w+\s+a+t+\s+\w+\s+d+o+t+\s+\w+", line)
        if dot_before is not None:
            dotb += 1
            list5.append(dot_before.group())
        # Search 2 - Find patterns like - robertsj1503 at duq dot edu
        special = re.search(r"\w+\s+a+t+\s+\w+\s+d+o+t+\s+\w+", line)
        if special is not None:
            spl += 1
            list2.append(special.group())
        # Search 3 - Find patterns like email ids masked with underscore - robertsj1503_at_duq_dot_edu
        underscore = re.search(r"\w+_+a+t+_+\w+_+d+o+t+_+\w+", line)
        if underscore is not None:
            und += 1
            list3.append(underscore.group())
        # Search 5 - Find patterns like email ids masked with html tags <!-- -->robertsj1503<!-- -->@<!-- -->duq<!-- -->edu<!-- -->
        htmlstyle = re.search(r"<!-- -->\w+<!-- -->@<!-- -->\w+<!-- -->\w+<!-- -->", line)
        if htmlstyle is not None:
            htm += 1
            list4.append(htmlstyle.group())

    final_non_rfc_emails = final_list+list2+list3+list4+list5
    with open("found_emails.txt",mode='w', newline='') as f:
        for i in final_non_rfc_emails:
            f.write(i+'\n')
    print(f"File found_emails.txt is successfully written to current directory")

    print(f"Number of valid emails found are: {len(final_list)}")
    # Sanitize the data to replace word at with @, dot with . ,and com. with com
    print(f"Number of emails found matching pattern [robertsj1503 at duq dot edu] are : {len(list2)}")
    for item in list2:
        final_list.append(f"{item} | {item.replace('....','').replace(' at ', '@').replace(' dot ', '.').replace('com.','com')}")
    # Sanitize the data to replace word _at_ with @, _dot_ with . and com. with com
    print(f"Number of emails found matching pattern [robertsj1503_at_duq_dot_edu] are: {len(list3)}")
    for item in list3:
        final_list.append(f"{item} | {item.replace('....','').replace('_at_', '@').replace('_dot_', '.').replace('com.','com')}")
    # Sanitize the data to replace the html tags to spaces and . where necessary.
    print(f"Number of emails found matching pattern [<!-- -->robertsj1503<!-- -->@<!-- -->duq<!-- -->edu<!-- -->] are : {len(list4)}")
    for item in list4:
        sanitized_1 = re.sub(r'<!--\s+-->', ' ',item)
        sanitized_2 = re.sub(r'\s@\s', '@', sanitized_1)
        sanitized_final = sanitized_2.lstrip().rstrip().replace(' ','.').replace('....','')
        final_list.append(f"{item} | {sanitized_final}")
    print(f"Number of emails found matching pattern [jeff dot Roberts at duq dot edu] are : {len(list5)}")
    for item in list5:
        final_list.append(f"{item} | {item.replace(' at ', '@').replace(' dot ', '.').replace('com.','com').replace('....','')}")


    print(f"Total number of emails found with matching patterns listed in assignment is: {len(final_list)}")
    pprint.pprint(final_list)
    #final_set = set(final_list)
    #print(f"Total number of unique emails found after sanitizing the emails to valid format are: {len(final_set)}, below is the list:")
    #pprint.pprint(final_set)
    # Challenge Accepted
    with open("Challenge_Solution.txt",mode='w', newline='') as f:
        for i in final_list:
            f.write(i+'\n')
    print(f"File Challenge_Solution.txt is successfully written to current directory")
