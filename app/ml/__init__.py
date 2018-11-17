import pickle
import numpy as np
import pandas as pd
import json

def filter_dishes(x, item_list, column):
    for item in item_list:
        if item.lower() in x[column].lower(): # matching item in x
#           print(item,x)
            return True
        else:
            pass
    return False


# function add food items or remove based on health or allergic conditions
def add_to_bucket(item_string, item):
    if item_string:
        item_string = item_string+ ";"+item.lower()
    else:
        item_string = item_string+ item.lower()
    return item_string


def remove_flavors(x,avoid_flavor_list):
    for item in avoid_flavor_list:
        if x:
            # print(x)
            json_acceptable_string = x.replace("'", "\"")
            d = json.loads(json_acceptable_string)
            if d[item] > 0.17:
                return False
    return True


def mapping(_df):
    # Course based on time
    if _df['time'] < 11:
        _df['course'] = "Salads;Breads;Breakfast and Brunch;combine lamb;\
                        Condiments and Sauces"  # till noon; breakfast and brunch
    else:
        _df['course'] = "Salads;Breads;Main Dishes;Desserts;\
                        Soups;Condiments and Sauces;Side Dishes;Appetizers "  # lunch or dinner

    # food type (veg, non-veg, egg)
    if _df['food_type'] == "veg":
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "turkey;salmon;chicken;\
                            pork;lamb;egg;duck;ham;beef;shrimp;fish;crab;squid;prawns;steak")
        _df['avoid_flavor'] = add_to_bucket(_df['avoid_flavor'], "meaty")
    elif _df['food_type'] == "egg":
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "turkey;salmon;chicken;pork;\
                            lamb;duck;ham;beef;shrimp;fish;crab;squid;prawns;steak")
        _df['avoid_flavor'] = add_to_bucket(_df['avoid_flavor'], "meaty")

    # avoid based on allergic condition
    for item in ['egg', 'milk', 'peanut', 'walnut', 'almond', 'hazelnut', 'cashew', 'pistachio', 'brazil', 'wheat',
                 'soybean',
                 'tuna', 'salmon', 'halibut', 'shellfish', 'crab', 'lobster', 'shrimp', 'mussels', 'seasame',
                 'mushroom']:
        if item in _df['allergy'].lower():
            _df['avoid_food'] = add_to_bucket(_df['avoid_food'], item)

    # health condition diarrhoea
    if "diarrhoea" in _df['health'].lower():
        #     print("diarrhoea")
        _df['add_food'] = add_to_bucket(_df['add_food'], "rice;porridge;honey;cumin;coriander; butter milk;\
                                                        goat’s milk;pomegranate;banana")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "maida;peas;black gram;chickpea;sugarcane juice;\
                                                            Jack fruit;beans;longcucumber;cucumber;Bathua;\
                                                            pumpkin;alcohol;curd")

    if "dysentery" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "ginger;pomegranate;banana;cumin;coriander;curd")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "wheat;barley;mango;sugarcane;betel nut")

    if "constipation" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "wheat;Green vegetables; papaya;carrot;cucumber;cabbage")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "banana;potato")

    if "acidity" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "barley;green vegetables;bitter gourd")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "potato;brinjal;rice;flour")

    if "ulcer" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "banana;coconut;cow milk;barley")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "ginger;pulces;mustard oil;rai;fish;alcohol")

    if "vomiting" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "Green gram;chickpea;Green vegetables;lemon;pomegranate;\
                                                        Cow’s milk;cardamom; fennel;cumin;clove")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "Beans;koshataki;blackmustard;kunduru;banana")

    if "diabetes" in _df['health'].lower():
        _df['add_food'] = add_to_bucket(_df['add_food'], "barley;wheat;Green gram;kulattha;pigeonpea;\
                                                        alasi;chickpea;Patola;bitter gourd;pepper;Honey;\
                                                        betel nut;rock salt")
        _df['avoid_food'] = add_to_bucket(_df['avoid_food'], "rice;Milk;curd;butter milk;clarifiedbutter;\
                                                            oil;jaggery;alcohol;sugarcane")
        _df['avoid_flavor'] = add_to_bucket(_df['avoid_flavor'], "sweet")

    return _df


def change_type(_df):
    df_dict = {}
    df_dict['time'] = _df._time.astype('int').values[0]
    # age = _df._age.astype('int').values
    df_dict['height'] = _df._height.astype('float').values[0]
    df_dict['weight'] = _df._weight.astype('float').values[0]
    df_dict['food_type'] = _df._food_type.astype('str').values[0]
    df_dict['add_food'] = _df._food_pref.astype('str').values[0]
    df_dict['avoid_food'] = _df._avoid_food.astype('str').values[0]
    df_dict['avoid_flavor'] = _df._avoid_flavor.astype('str').values[0]
    df_dict['allergy'] = _df._allergy.astype('str').values[0]
    df_dict['health'] = _df._long.astype('str').values[0]
    df_dict['cuisine'] =  _df._cuisine.astype('str').values[0]
    return df_dict


def convert_to_array(_df):
    # convert string to list based on delimiter
    _df['course_list'] = _df['course'].split(';')

    _df['cuisine_list'] = _df['cuisine'].split(';')

    _df['add_list'] = []
    if _df['add_food']:
        _df['add_list'] = set(_df['add_food'].split(';'))

    _df['avoid_list'] = []
    if _df['avoid_food']:
        _df['avoid_list'] = set(_df['avoid_food'].split(';'))

    _df['avoid_flavor_list'] = []
    if _df['avoid_flavor']:
        _df['avoid_flavor_list'] = set(_df['avoid_flavor'].split(';'))

    return _df


def CB_recommend_df(_df, _repo_df):
    course_df = _repo_df[
        _repo_df.apply(lambda x: filter_dishes(x, _df['course_list'], "course"), axis=1)]  # filter based on time

    # print(course_df)
    if len(course_df) > 0:
        cuisine_df = course_df[
            course_df.apply(lambda x: filter_dishes(x, _df['cuisine_list'], "cuisine"), axis=1)]  # filter based on cuisine

    if _df['add_list'] is not None or len(cuisine_df) > 0:
        add_df = cuisine_df[np.logical_or(
            cuisine_df.apply(lambda x: filter_dishes(x, _df['add_list'], "ingredient_amount"), axis=1),
            cuisine_df.apply(lambda x: filter_dishes(x, _df['add_list'], "name"), axis=1)
            )]
    else:
        add_df = cuisine_df

    if _df['avoid_list'] is not None or len(add_df) > 0:
        avoid_df = add_df[~np.logical_or(
            add_df.apply(lambda x: filter_dishes(x, _df['avoid_list'], "ingredient_amount"), axis=1),
            add_df.apply(lambda x: filter_dishes(x, _df['avoid_list'], "name"), axis=1)
            )]
    else:
        avoid_df = add_df
    print(avoid_df)

    if _df['avoid_flavor_list'] is not None or len(avoid_df) > 0:  # remove dish with given flavors
        avoid_flavor_df = avoid_df[avoid_df.flavor.map(lambda x: remove_flavors(x, _df['avoid_flavor_list']))]
    else:
        avoid_flavor_df = avoid_df

    if len(avoid_flavor_df) > 0:
        return avoid_flavor_df.groupby("course").apply(lambda x: x.sort_values("rating", ascending=False).head(5))
    else:
        return None


def recommendation(_df):
    # Content Based filtering
    # _df has user profile details, dishes are recommended based on incredients matching the profile and purchase
    _repo_df = pd.read_csv("data/faid.csv")  # reading from recipe-incredients repo
    # print(_repo_df.head(3))
    _repo_df.flavor = _repo_df.flavor.fillna('')
    _df = change_type(_df)
    print("after changing types",_df)
    _df = mapping(_df)
    print("after mapping", _df)
    _df = convert_to_array(_df)
    print("changing to array done.")
    print(_df)
    _cb_df = CB_recommend_df(_df, _repo_df)
    print(_cb_df)


    # Collaborative Filtering
    # _df has user profile.
    # Based on similarity of faid user with other users in the system, new dishes rated high are recommended

    faid_rating = pd.read_csv('faid_rating.csv')
    pivot_faid_rating = faid_rating.pivot_table(cols=['user'], rows=['dish'], values='rating')
    faid_user = _df['user']
    faid_user_rating = pivot_faid_rating[faid_user]
    faid_user_sim = pivot_faid_rating.corrwith(faid_user_rating)
    filter_df = faid_rating[pivot_faid_rating[faid_rating.title].isnull().values & \
                            (faid_rating.user != faid_user)]
    filter_df['similarity'] = filter_df['user'].map(faid_user_rating.get)
    filter_df['sim_rating'] = filter_df.similarity * filter_df.rating

    CF_recommend_df = filter_df.groupby('dish').apply(lambda s: s.sim_rating.sum() / s.similarity.sum())
    _cf_df = CF_recommend_df.order(ascending=False)
    print(_cf_df)

    _df = _cf_df.append(_cb_df)

    return _df