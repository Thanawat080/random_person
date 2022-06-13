import sys
sys.path.append("..\person")
from function.random_function import  random_function
from random import randint
import random

def random_person():
    profile = random_function.random_profile()
    print(profile)
    name = profile['name']
    job = profile['job']
    address = profile['address']
    gender = profile['sex']
    ssn_number = profile['ssn']
    username = profile['username']
    bank = random_function.random_bank()
    weight = random_function.random_weight()
    status = 'โสด'
    religion = random_function.random_religion()
    son = 0
    prefix = ''
    birth = random_function.random_birth_day()
    print(birth)
    blood = random_function.random_blood_type()
    age = random_function.get_current_year() - birth.year


    # person
    if gender == 'M' and age < 15:
        simple_name = random_function.random_simple_name_m()
        prefix = 'ด.ช.'
        hobby = random_function.random_hobby_baby()
    if gender == 'M' and age >= 15:
        simple_name = random_function.random_simple_name_m()
        hobby = random_function.random_hobby_adult()
        status = random_function.random_marry()
        son = random_function.random_son(0,5)
        prefix = 'นาย'
    if gender == 'F' and age < 15:
        simple_name = random_function.random_simple_name_f()
        hobby = random_function.random_hobby_baby()
        prefix = 'ด.ญ.'
    if gender == 'F' and age >= 15:
        simple_name = random_function.random_simple_name_f()
        hobby = random_function.random_hobby_adult()
        status = random_function.random_marry()
        if age < 18:
            son = random_function.random_son(0,2)
        else:
            son = random_function.random_son(0,5)       
        if status == 'โสด':
            prefix = 'น.ส.'
        else:
            prefix = 'นาง'
    if prefix == 'ด.ช.' or 'ด.ญ.':
        heigth = random_function.random_heigth(150,165)
    if prefix == 'นาย':
        heigth = random_function.random_heigth(158,180)

    if prefix == 'น.ส.':
        heigth = random_function.random_heigth(153,175)

    # child
    last_name = name.split(" ")
    dict_son=[]
    for _ in range(son):
        simplename_son = ''
        prefix_son = ''
        range_age = age - (randint(14,16))
        profile_son = random_function.random_profile()
        age_son = ("{:.1f}".format(random.uniform(0.1,range_age)))
        age_son1 = age_son.split('.')
        name_son =  profile_son['name']
        if profile_son['sex'] == 'M' and int(age_son1[0]) < 15:
            simplename_son = random_function.random_simple_name_m()
            prefix_son = 'ด.ช.'
        elif profile_son['sex'] == 'F' and int(age_son1[0]) < 15:
            simplename_son = random_function.random_simple_name_f()
            prefix_son = 'ด.ญ.'
        elif profile_son['sex'] == 'M' and int(age_son1[0]) > 15:
            simplename_son = random_function.random_simple_name_m()
            prefix_son = 'นาย'
        elif profile_son['sex'] == 'F' and int(age_son1[0]) > 15:
            simplename_son = random_function.random_simple_name_f()
            prefix_son = random.choice(['น.ส.', 'นาง'])
        lname_son = name_son.split(" ")
        name_son = name_son.replace(lname_son[1], last_name[1])
        dict_son.append({"prefix":prefix_son,"name":name_son,'blood_type':random_function.random_blood_type(), 'age':'{} ปี {} เดือน'.format(age_son1[0],age_son1[1]), 'nick_name':simplename_son})



    person_dict = {
        "prefix":prefix,
        "name" : name,
        "birth_day" : birth,
        "address": address,
        "ssn_number":ssn_number,
        "job":job,
        "blood_type":blood,
        "bank_id":bank,
        "age":age,
        "weight":weight,
        "heigth": heigth,
        "religion": religion,
        "status":status,
        "kids_count":son,
        "hobby":hobby,
        "username":username,
        "kids":dict_son,
        'nick_name':simple_name
    }
    return person_dict
