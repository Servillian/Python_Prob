def is_capital(state, city):
    dict = {"New South Wales": "Sydney", "Queensland": "Brisbane", "South Australia": "Adelaide", "Tasmania": "Hobart", "Victoria": "Melbourne", "Western Australia": "Perth"}
    if dict.get(state) == city:
        return "True"
    else:
        return "False"

print(is_capital("Queensland", "Brisbane"))