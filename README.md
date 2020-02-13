# api-text-munging
Text Sequence Manipulation in Python

Question 1 - Spammer
You work for SPAM Marketing Co. Your supervisor has just received a text file (MonsterJobsData_variations.txt – a UTF-8 encoded file) containing, what she believes, will be pure SPAM marketing gold - previously un-spammed email addresses.
You have been asked to author a Python script and the necessary regular expressions to extract all of the email addresses from that file.
Since HTTP is case insensitive, your RE patterns should be case insensitive.
Script Name Requirement: spammer.py
Input Files Used: MonsterJobsData_variations.txt – a UTF-8 encoded file
Requirements Overview
1. open the file for reading
2. for each line in the file, use a RE to scan the line and capture any email address of the type show below. You may assume there can be at most one email address (of any type) per line.
3. Output all captured email addresses.
Additional Information
Obscured Email Addresses
Regarding emails, alas, some folks are wise to your “spammer” tactics and obscure their email addresses in cleaver ways. Specifically, you are to recognize and retain emails of the following form:
a. a valid email address format (see below)
b. robertsj1503 at duq dot edu
c. robertsj1503_at_duq_dot_edu
d. jeff dot Roberts at duq dot edu
e. <!-- -->robertsj1503<!-- -->@<!-- -->duq<!-- -->edu<!-- -->
(This is my personal favorite - plenty of HTML comment tags!)
Valid Email Addresses
The local-part of a valid email address (the part before the @) may use any of these ASCII characters:
 uppercase and lowercase latin letters A to Z and a to z
 digits 0 to 9
 printable characters !#$%&'*+-/=?^_`{|}~.
The domain-part of a valid email address (the part after the @) may be composed of several subdomains separated by a dot (.). Each subdomain’s element may contain only:
Page – 2
 uppercase and lowercase ASCII letters A to Z and a to z
 digits 0 to 9
 hyphen -
Output
Write the list of email addresses (one email per line) to a text file named found_emails.txt. For this assignment, do not change or otherwise re-interpret the non-standard emails into RFC 5322 compliant email addresses. Just output the emails as you found them. (Ex: robertsj1503 at duq dot edu).
Challenge
Want a challenge? Author the conversion code to convert all of your found emails to RFC 5322 compliant email addresses. However, this is not a requirement. If you implement the challenge please, output both the original email text followed by the converted email text on the same line using a pipe separator (|). Ex: robertsj1503 at duq dot edu|robertsj1503@duq.edu
Question 2 – Poor-Man’s Sentiment Analysis (Part 1)
Use Yelp’s GraphQL search API to return 50 Dentists in the in the Downtown, Pittsburgh, PA location. Once found, sort the list of dentists according to their ratings.
Script Name Requirement: yelp_sent_analysis_p1.py
Requirements Overview
1. Your initial search should search for and return 50 Dentists in the “Downtown, Pittsburgh, PA” location
2. Your search query must request the results by sorted by the best_match criterion
3. Your GraphQL search query need only request a business object’s name, rating, and id attributes
4. Sort the returned list of dentists in descending order according to their Yelp ratings. Any ratings ties can be ignored.
5. Output the captured business information.
Output
Write your ordered lists of dentists to yelp_dentists.csv using a CSV file format (one dentist per line).
Question 3 – Poor-Man’s Sentiment Analysis (Part 2)
In this question you will use the yelp_dentists.csv file created in the previous question to conduct a bag-of-words sentiment analysis.
Script Name Requirement: yelp_sent_analysis_p2.py
Input Files Used:
 yelp_dentists.csv – UTF-8 encoded csv file
 positive_words.txt – ANSI encoded text file
 negative_words.txt – ANSI encoded text file
Requirements Overview
1. Ingest the positive words into a single list
Page – 3
2. Ingest the negative words into a single list
3. open the csv file for reading
4. parse the opened file using the csv module
5. for each business, use Yelp’s GraphQL reviews query API to return the business’ review text
6. For each business, record the (a) count of positive words and (b) count of negative words occurring across all reviews for that business
7. Output your results
Output
Print your results as follows (replace the bracketed items using your results):
‘The reviews for Business Id: <id>, Business Name: <name> contained the most positive words with <xxx> positive words.’
‘The reviews for Business Id: <id>, Business Name: <name> contained the most negative words with <xxx> negative words.’
Question 4 – The Latin Pig Cipher
It turns out Julius Caesar was more paranoid than first thought. He had another cipher which was a combination of Pig Latin and step cipher. You are tasked with implementing the so-called Latin Pig Cipher (LPC). You may use any combination of RE or string operations you wish in constructing your solution.
The latin_pig_cipher function receives a (word/string) and a step value as parameters. The objective of the function is to convert an incoming string to its LPC equivalent and return the result.
Script Name Requirement: latin_pig_cipher.py.
Requirements Overview
1. A word is a consecutive sequence of letters (a-z, A-Z) and numeric digits (0-9). You may assume that the string input to the function will only be a single "word". Examples: Zebra29, apple85, etc.
2. A cipher shifted letter is substitution cipher in which the letter in the plaintext is replaced by a letter some fixed number of step positions down the alphabet. For example, with a step of 2, D would be replaced by F, E would become G. Numeric digits are not cipher shifted.
3. If word ends with a digit, or a series of consecutive digits, the minimum digit in the series becomes the cipher step value. Thus, overriding (replacing) the step input parameter. Note: a series composed of a single digit has a minimum value equal to that digit.
4. If a word starts with a vowel, the LPC version is the original word with the string ŵāŷ (latin small letter W with circumflex (Unicode code point \x0175) + latin small letter A with macron (Unicode code point \x0101) + latin small letter Y with circumflex (Unicode code point \x0177)) to the end.
5. If the first letter of a word is the letter 'y', the 'y' should be treated as a consonant, unless it is followed by a numeric digit. If the first letter of a word is a 'y' followed by a digit, it is to treated as a vowel as are any other occurrences of 'y'.
Page – 4
6. If a word starts with a consonant, or a series of consecutive consonants, the LPC version transfers ALL cipher shifted consonants up to the first vowel to the end of the word, and adds the string "āŷ" (latin small letter A with macron (Unicode code point \x0101) + latin small letter Y with circumflex (Unicode code point \x0177) to the end.
7. If the original word was capitalized, the new LPC version of the word should also be capitalized in the first letter. If the original capital letter was a consonant, and thus moved, it should no longer be capitalized in its new location.
Output
Print the results of your algorithm against the test data.
Test Data
Test Word
Latin Pig Cipher
football415
ootball415gāŷ
Pittsburgh
Ittsburghpāŷ
Y2ellow
Y2ellowŵāŷ
yellow
ellowyāŷ
yttrium
iumyttrāŷ
Assignment Deliverables
Once you have completed the tasks above, create a single ZIP file containing the contents of the folder that holding all of your solution scripts and output files (ie, your project workspace). You may upload your ZIP file solutions as many times as necessary. FAVOR: your workspace folder (and thus your ZIP file) should not contain sub-folders.
