women_clothes = {"XXS": {"Rusnya": 42, "Germany": 36, "USA": 8, "France": 38, "United Kingdom": 24},
                 "XS": {"Rusnya": 44, "Germany": 38, "USA": 10, "France": 40, "United Kingdom": 26},
                 "S": {"Rusnya": 46, "Germany": 40, "USA": 12, "France": 42, "United Kingdom": 28},
                 "M": {"Rusnya": 48, "Germany": 42, "USA": 14, "France": 44, "United Kingdom": 30},
                 "L": {"Rusnya": 50, "Germany": 44, "USA": 16, "France": 46, "United Kingdom": 32},
                 "XL": {"Rusnya": 52, "Germany": 46, "USA": 18, "France": 48, "United Kingdom": 34},
                 "XXL": {"Rusnya": 54, "Germany": 48, "USA": 20, "France": 50, "United Kingdom": 36},
                 "XXXL": {"Rusnya": 56, "Germany": 50, "USA": 22, "France": 52, "United Kingdom": 38}}

while True:
    user_international_size = input(
        "Enter any value from the example without quotes ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'): ")
    test_string = "No such element!!!"

    international_size = women_clothes.get(user_international_size, test_string)
    if not international_size == test_string:
        user_country_size = input(
            "Enter any value from the example without quotes ('Rusnya', 'Germany', 'USA', 'France', 'United Kingdom'): ")
        country_size = women_clothes[user_international_size].get(user_country_size, test_string)
        if not country_size == test_string:
            print(f"Your size is: {women_clothes[user_international_size][user_country_size]}")
            break
        else:
            print(country_size)
    else:
        print(international_size)

    print("\nImagine that the console has cleared and re-enter the suggested example\n")
