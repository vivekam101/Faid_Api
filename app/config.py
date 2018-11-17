import json

#***
#   REGISTRATION
#****

REGISTRATION_CONFIG = {
    "excel_filepath" : "data/recipe_final.csv",
}

def _map_registration_data(data):
    _mapping ={
        "_id" : "id",
        "_location" : "location",
        "_cuisine" : "cuisine",
        "_long" : "long_term_illness",
        "_allergy" : "allergy",
        "_food_type" : "food_type",
        "_food_pref" : "food_preference",
        "_avoid_food" : "avoid_food",
        "_avoid_flavor" : "avoid_flavor",
        "_height" : "height",
        "_weight" : "weight",
        "_age" : "age"
    }

    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    # _out["_cuisine"] = data.get("LeadCategory__r",{}).get("Name")

    return _out

REGISTRATION_API_CONFIG = {
    "data_map":_map_registration_data
}


#***
#RECOMMENDATION
#***

RECOMMENDATION_CONFIG = {
    "excel_filepath" : "data/recipe_final.csv",
}

def _map_recommendation_data(data):
    _mapping ={
        "_id" : "id",
        "_current_location" : "location",
        "_time" : "time"
    }

    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    # _out["_cuisine"] = data.get("LeadCategory__r",{}).get("Name")

    return _out

RECOMMENDATION_API_CONFIG = {
    "data_map":_map_recommendation_data
}
