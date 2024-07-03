#    https://www.codewars.com/kata/56f5594a575d7d3c0e000ea0/train/python


def conference_picker(citiesVisited, citiesOffered):
    for city in citiesOffered:
        if city not in citiesVisited:
            return city
    return 'No worthwhile conferences this year!'

citiesVisited = ['Mexico City', 'Johannesburg', 'Stockholm', 'Osaka', 'Saint Petersburg', 'London']
citiesOffered = ['Stockholm', 'Paris', 'Melbourne']
print(conference_picker(citiesVisited, citiesOffered))

citiesVisited = ['Mexico City', 'Johannesburg', 'Stockholm', 'Osaka', 'Saint Petersburg', 'London']
citiesOffered = ['Stockholm', 'London']
print(conference_picker(citiesVisited, citiesOffered))