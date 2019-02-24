# Start the program
print("Welcome to age checker. This program checks how old you were in the year or the grade specified.");


# Initialize Variables
month_born = None;
year_born = None;
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November","December"];

# Get the month born from the user
while (month_born == None):

    # Get the month born as input string from the user
    month_born = input("\nWhat month were you born in? (Enter a number from 1-12 or a month): ");

    # If the input string was an integer
    try:
        month_born = int(month_born);

        # If the number is not in the range of 1-12
        if month_born < 1 or month_born > 12:
            print("You need to enter a number from 1-12 or a month.");
            month_born = None;

        # If the number is in the range of 1-12
        else:

            # Loop through months to find the month string for the number entered
            for index, value in enumerate(months, 1):
                if month_born == index:
                    print("You were born in "+value+".");

                    # Set the month born from the number to the string of the month
                    month_born = value;
                    break;

    # If the input was a string
    except ValueError:

        # Capitalize the input string
        month_born = str.capitalize(month_born);

        # Make sure a real month was entered
        if month_born not in months:
            print("You need to enter a number from 1-12 or a month.");
            month_born = None;
        else:
            print("You were born in the month of "+month_born);

# Get the year born from the user
while (year_born == None):

    year_born = input("\nWhat year were you born in? (number only from 1919-2019)");

    try:
        year_born = int(year_born)

        # If the number is not in the range of 1919-2019
        if year_born < 1919 or year_born > 2019:
            print("You need to enter a number from 1919 to 2019.");
            year_born = None;

        # If the number is in the range of 1919-2019
        else:
            print("You were born in the year "+str(year_born)+".")

    except ValueError:
        print("You need to enter a number from 1919 to 2019.")
        year_born = None;

# Find out if the user wants to know how old they were in a certain year
# or if they want to know what year they were in a certain grade
choice = None;
while choice == None:

    # Get a choice from the user as in input string
    print("\nYou were born in "+month_born+", "+str(year_born)+". Would you like to:");
    print("1. Find out how old you were in a certain year?");
    print("2. Find out how old you were in a certain grade at school?");
    choice = input("Make a choice (number 1 or 2): ");

    # Try to convert the input string to an integer
    try:
        choice = int(choice);

        # Make sure the integer isn't out of range for the choices
        if choice < 1 or choice > 2:
            print("You need to enter a choice, 1 or 2.")
            choice = None;

    # If the string was not a number
    except ValueError:
        print("You must enter a selection (number 1 or 2).");
        choice = None;

    # Find out how old you were in a certain year
    if choice == 1:

        age_year = None;
        while age_year == None:

            # Get the requested year from the user
            age_year = input("What year would you like to know your age in?: ")

            # Try to convert the age_year string into an integer
            try:
                age_year = int(age_year);

                # If the number is not in the range of birth year to 2019
                if age_year < year_born+1 or age_year > 2019:
                    print("You need to enter a year from "+str(year_born+1)+" to 2019.");
                    age_year = None;

                # If the number is in the range of 1919-2019
                else:
                    agePossibility1 = str((age_year - year_born)-1);
                    agePossibility2 = str(age_year - year_born);
                    print("In the year "+str(age_year)+", you would have been "+agePossibility1+" or "+agePossibility2+" depending on the month.")
                    choice = None;

            # If the age_year string wasn't a number
            except ValueError:
                age_year = None;
                choice = None;
                print("You need to enter a year from "+str(year_born+1)+"-2019.");

    # Find out how old you were in a certain grade
    elif choice == 2:

        grade_choice = None;
        while grade_choice == None:

            # Get the requested year from the user
            grade_choice = input("What school grade would you like to know your age in?: ")

            # Try to convert the age_year string into an integer
            try:
                grade_choice = int(grade_choice);

                # If the number is not in the range of 0 to 12
                if grade_choice < 0 or grade_choice > 12:
                    print("You need to enter a grade from 0 (for Kindergarten) to 12.");
                    grade_choice = None;

                # If the number is in the range of 1919-2019
                else:
                    yearPossibility1 = year_born + 5 + grade_choice;
                    yearPossibility2 = year_born + 5 + grade_choice + 1;
                    print("\nYou were in Grade "+str(grade_choice)+" for the "+str(yearPossibility1)+"-"+str(yearPossibility2)+" school year.");
                    agePossibility = str(5 + grade_choice);
                    print("You would have been "+str(agePossibility)+" by "+str(yearPossibility2)+", turning "+str(int(agePossibility)+1)+" that year.");
                    choice = None;

            # If the age_year string wasn't a number
            except ValueError:
                grade_choice = None;
                choice = None;
                print("You need to enter a Grade from 0 (for Kindergarten) to 12.");