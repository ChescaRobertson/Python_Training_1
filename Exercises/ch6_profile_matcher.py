def build_profile():
    profile = {
        "age": 0,
        "hobbies": []
    }
    p_age = int(input("Please enter your age: "))
    profile["age"] = p_age

    while True:
        hobby = input("Please enter a hobby: ")
        profile["hobbies"].append(hobby)

        more = input("Would you like to input more hobbies? y/n: ")
        if more.lower() == 'n':
            break
    return profile

def match(profile1, profile2):
    match_quality = 0
    if abs(profile1["age"] - profile2["age"]) <= 5:
    #if (profile2["age"] - 5) < profile1["age"]  < (profile2["age"] + 5):
        match_quality += 1
    
    for hobby in profile1["hobbies"]:
        if hobby in profile2["hobbies"]:
            match_quality += 1

    return match_quality