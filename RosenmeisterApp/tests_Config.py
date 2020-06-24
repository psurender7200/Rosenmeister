DATE_FROM = "1910-01-01"
DATE_TO = "2000-01-01"
#This is for existing data in database, if you try to insert the data, then it should give validation
#error as this data is already present, Before checking this, you need to make sure, the same data is already
#present in database --> first create the same data in database, then you can test this functionality
EXISTING_JSON_DATA =[
    {
        "first_name": "Surender",
        "last_name": "Potta",
        "email": "surender@germany.de",
        "birthday": "01.03.1989"

    },
    {
        "first_name": "User2",
        "last_name": "test",
        "email": "user2@germany.de",
        "birthday": "30.03.1989"

    },
    ]

NEW_JSON_DATA =[
    {
        "first_name": "Surender",
        "last_name": "Potta",
        "email": "Surender45@Germany.de",
        "birthday": "01.03.1989"

    },
    {
        "first_name": "User2",
        "last_name": "test",
        "email": "user26@germany.de",
        "birthday": "30.03.1989"

    },
    ]

LETTERS_DIGITS_DATA = {"value":"a2b"}