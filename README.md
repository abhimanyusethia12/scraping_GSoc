# scraping_GSoc.py
The programme extracts the data (Name, Organisation, Project) from a webpage (whose URL is given by the user) and writes it into a csv file 

## To run the programme
Enter the following command in terminal

`python scraping_GSoc <url>`

substitute `<url>` with the url of the webpage which is to be scraped

## Features
1. The programme has been made to scrape a page that has this layout: https://summerofcode.withgoogle.com/archive/2019/projects/
2. The data will be written in a csv file named 'GSoc.csv' in the same directory where the programme is located and run
3. The data will be written into the csv file in the following format
>  Name1 Organisation1 Project1

>  Name2 Organisation2 Project2

# student_names.py
1. This is a program that takes a CSV file and a JSON file as input. 
2. The CSV file need to have the same format, as the one created above. 
3. This program first finds names that do not look like official names and print them. A name is non-official, if it qualifies at least one of the following properties:
        1) The name contains any of the special symbols or numbers.
        2) The name consists of only one word.
        3) The name contains only lowercase letters.
4. The remaining names (that are official names) should be matched against the JSON file that is provided by the user
5. The programme prints (to stdout) the details of all the names that are present both in the JSON file and in the CSV file, in the following format:
> Name(common to both JSON and CSV), Roll No(from JSON), Branch(from JSON), Organisation(from CSV), Project(from CSV)

## To Run the Programme
Enter the following command in your terminal

`python student_names.py <CSV File Name> <JSON File Name>`

In place of `<CSV File Name>` write the name of the csv file (Eg. GSoc.csv)
In place of `<JSON File Name>` write the name of the JSON file (Eg. students.json)

An example JSON file (students.json) can be found in this repo

_This project was done as a part of the Round 1 of selection process for Secretary, PClub, IIT Kanpur_ 
