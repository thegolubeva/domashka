user_name = input("Как тебя зовут?:")
birth_year = input("В каком году ты родился(ась)?:")
year_x = input("К какому году нужно посчитать возраст?:")

birth_year=int(birth_year)
year_x=int(year_x)

if year_x < birth_year:
    print(user_name, ", ты еще не родился(ась) ))")
elif (year_x - birth_year) > 100:
    print(user_name, ", столько не живут))")
else:
    print(user_name,", тебе будет", (year_x - birth_year))


