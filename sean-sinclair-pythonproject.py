# Author: Sean Sinclair

# Title of project
print("----- Job Tracker -----")
print(" ===================== ")

# User enters how many jobs they wish to input 
number_of_jobs = int(input("How many jobs would you like to enter: "))
print("\n")

# creates a list to store the number of jobs entered
jobs_number = []
# loops through the range of numbers that was entered and adds them to the list
# the number of jobs has 1 added to it, as using range() will cut it one number short
for jobs in range(1, number_of_jobs + 1):
    jobs_number.append(jobs)


# lists for full-time and part-time jobs
full_time = []
part_time = []

# variable for invalid input
invalid_input = ("Input invalid, please try again\n")


# list designation for the complete table
jobs = []
companys = []
exp = []
pay = []
time = []
earn = []


for number in jobs_number:

    # Loops through the number list and outputs the job details for however many jobs were inputed
    print(f"Enter Job {number} details")
    print("-" * 26)

    # User enters job details
    job_title = input("Enter the job title: ")
    
    # checks if the user input is just letters and if it has space or not
    # makes the user input the right data until it is in the correct form
    while not job_title.isalpha() or job_title.isspace():
        print(invalid_input)
        job_title = input("Enter the job title: ")
    else:
        jobs.append(job_title)
        pass
  
        # pretty much same thing as the job details 
    company_name = input("Enter the company name: ")    
    while not company_name.isalpha() or company_name.isspace():  
        print(invalid_input) 
        company_name = input("Enter the company name: ")
    else:
        companys.append(company_name)
        pass

    
    # full time lists
    fulltime_job_titles = []
    fulltime_company_names = []
    fulltime_experience = []
    fulltime_hours = []
    fulltime_pay = []
    fulltime_earning = []


    # part time lists
    parttime_job_titles = []
    parttime_company_names = []
    parttime_experience = []
    parttime_hours = []
    parttime_pay = []
    parttime_earning = []
    

    # checks if the job is part-time or full-time
    type_of_employment = input("""Please enter the type of employment
    1. Full-time
    2. Part-time
    ==> """)

    
    while type_of_employment != "1" and type_of_employment != "2":
        print(invalid_input)
        type_of_employment = input("==> ")
    else:
        pass
    
        if type_of_employment == "1":
            # full-time hours is set to 40 hours by default
            hours_per_week = 40
            time.append(hours_per_week)
             
        else: 
            hours_per_week = int(input("What are the weekly hours: "))
            while hours_per_week < 1 or type(hours_per_week) != int:
                print(invalid_input)
                hours_per_week = int(input("What are the weekly hours: "))
            else:
                time.append(hours_per_week)
                pass
    
    
    experience_required = input("Does the job require experience (y/n): ")
    while experience_required != "y" and experience_required != "n":
        print(invalid_input)
        experience_required = input("Does the job require experience (y/n): ")
    else:
        exp.append(experience_required)
        pass

        # converts the single letter input into a word
        if experience_required == "y":
            experience_required = "yes"
        elif experience_required == "n":
            experience_required = "no"
    

    pay_rate = float(input("What is the rate of pay per hour : "))
    while pay_rate < 1 or type(pay_rate) != float:  
        print(invalid_input)
        pay_rate = float(input("What is the rate of pay per hour: "))
    else:
        pay.append(pay_rate)
        pass


        # to get the total earnings the hours is multiplied by the pay rate
    earnings = float((format(hours_per_week * pay_rate, ".2f")))
    earn.append(earnings)
    pass

    # skips a line to make the code neater
    print("\n")

        # headings for the table       
    heading1 = "ID"
    heading2 = "JOB TITLE"
    heading3 = "LOCATION"
    heading4 = "EXP"
    heading5 = "RATE(€)"
    heading6 = "HOURS"
    heading7 = "EARNINGS"

    # checks if the job is full-time
    # if it full-time then it adds all the data to the lists to store them
    if type_of_employment == "1":

        fulltime_job_titles.append(job_title)
        fulltime_company_names.append(company_name)
        fulltime_hours.append(hours_per_week)
        fulltime_experience.append(experience_required)
        fulltime_pay.append(pay_rate)
        fulltime_earning.append(earnings)

        # opens a text file and writes to it with all the data for the full-time jobs
        with open("fulltime.txt", "a") as file_object:
                for x, a, b, c, d, e, f in zip(jobs_number, fulltime_job_titles, fulltime_company_names, fulltime_experience, fulltime_pay, fulltime_hours, fulltime_earning):
                    file_object.write(f"{x:<8}{a:<15}{b:<15}{c:<10}{d:<10}{e:<10}{f:<10}\n")

    else:
        parttime_job_titles.append(job_title)
        parttime_company_names.append(company_name)
        parttime_hours.append(hours_per_week)
        parttime_experience.append(experience_required)
        parttime_pay.append(pay_rate)
        parttime_earning.append(earnings)

        # opens a text file and writes to it with all the data for the part-time jobs
        with open("parttime.txt", "a") as file_object:
            for x, a, b, c, d, e, f in zip(jobs_number, parttime_job_titles, parttime_company_names, parttime_experience, parttime_pay, parttime_hours, parttime_earning):
                file_object.write(f"{x:<8}{a:<15}{b:<15}{c:<10}{d:<10}{e:<10}{f:<10}\n")


# creates a table for all the jobs whether or not it is full-time or part-time
print(f"{heading1:<8}{heading2:<15}{heading3:<15}{heading4:<10}{heading5:<10}{heading6:<10}{heading7:<10}")
print("=" * 100)

# loops through the lists and prints out the job and its respective details 
for x, a, b, c, d, e, f in zip(jobs_number, jobs, companys, exp, pay, time, earn):
    print(f"{x:<8}{a:<15}{b:<15}{c:<10}{d:<10}{e:<10}{f:<10}")
print("\n")
print("Summary")
print("=" * 12)

# the "pay" list is sorted to that the minimum wage goes to the the start of the list and the maximum wage goes to the end.
pay.sort()
print(f"Hourly pay ranges from €{pay[0]} to €{pay[-1]}")

# if only 1 job is entered the the average if automatically that one job
if len(jobs_number) <= 1:
    print(f"Average pay is €{pay[0]}")
elif len(jobs_number) >= 1:
    # otherwise if more jobs are entered then the pay of the jobs is added together and divided by the number of jobs.
    average = (format(sum(pay) / number_of_jobs, ".2f"))
    print(f"Average pay is €{average}")

#to get the highest paying job the indexe is gotten of the maximum earnings 
maximum = (earn.index(max(earn)))
# the position of the maximum earning is the applied to the jobs and companys list to get the name and loctaion.
highest_job_title = (jobs[maximum])
highest_job_place = (companys[maximum])
print(f"The highest paying job is: {highest_job_title} at {highest_job_place}")
