#-*-coding:utf-8-*-
def city_country(city,country,population=''):
    city_name = city
    country_name = country
    if population:
        return (city_name.title() + ', '+ country_name.title() + ' - population ' + str(population))
    else:
        return (city_name.title() + ', '+ country_name.title() )

print(city_country('santiago','chile'))
