apartments = {
    "A101": {
        "rent": 750,
        "reviews": [4, 5, 3]
    },
    "B203": {
        "rent": 640,
        "reviews": [2, 3]
    },
    "C305": {
        "rent": 900,
        "reviews": [5, 5, 4, 4]
    },
    "D404": {
        "rent": 550,
        "reviews": []
    }
}


def apartment_summary(apartments, max_rent):
    filtered_apartments = {
        apartment: sum(apartments[apartment]["reviews"])/len(apartments[apartment]["reviews"]) 
        if apartments[apartment]["reviews"] else "No review"
        for apartment in apartments if apartments[apartment]["rent"] <= max_rent
        }
    return filtered_apartments

print(apartment_summary(apartments,1000))