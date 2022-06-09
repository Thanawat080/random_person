def generate():

    from faker import Faker
    from datetime import date
    from datetime import datetime
    from random import randint
    import random

    current_year = date.today().year

    fake = Faker(['th_TH'])

    profile = fake.profile()

    name = profile['name']
    birth = fake.date_of_birth(maximum_age=80, minimum_age = 14)
    address = profile['address']
    gender = profile['sex']
    age = current_year - birth.year
    job = profile['job']
    blood = profile['blood_group']
    mail = profile['mail']
    ssn_number = profile['ssn']
    username = profile['username']
    bank = fake.bban()
    # ibank = fake.iban()
    weight = ("{:.2f}".format(random.uniform(38.1, 85)))
    statusmarry = ['สมรส', 'โสด', 'หย่า', 'หม้าย', 'แยกกันอยู่']
    mylist = ["พุทธ", "คริสต์", "อิสลาม"]
    religion = random.choice(mylist)
    hobby_adult = ['ฟังเพลง', 'ดูหนัง', 'นอนหลับ', 'วิดีโอเกม', 'ขับรถ', 'เดินทาง', 'อ่านหนังสือ', 'ทำอาหาร', 'ปั่นจักรยาน', 'เดินเล่น']
    hobby_baby = ['ฟังเพลง', 'ดูหนัง', 'นอนหลับ', 'วิดีโอเกม', 'อ่านหนังสือ', 'ปั่นจักรยาน', 'เดินเล่น']
    marry = 'โสด'
    son = 0

    if gender == 'M' and age < 15:
        hobby = random.choice(hobby_baby)
        name = 'ด.ช. ' + name
    if gender == 'M' and age >= 15:
        hobby = random.choice(hobby_adult)
        marry = random.choice(statusmarry)
        son = randint(0,5)
        name = 'นาย ' + name
    if gender == 'F' and age < 15:
        hobby = random.choice(hobby_baby)
        name = 'ด.ญ. ' + name
    if gender == 'F' and age >= 15:
        hobby = random.choice(hobby_adult)
        marry = random.choice(statusmarry)
        if age < 18:
            son = randint(0,2)
        else:
            son = randint(0,5)        
        if marry == 'โสด':
            name = 'น.ส. ' + name
        else:
            name = 'นาง ' + name
    if 'ด.ช.' or 'ด.ญ.' in name:
        heigth = (randint(150,165))
    if 'นาย' in name:
        heigth = (randint(158,180))

    if 'น.ส.' in name:
        heigth = (randint(153,175))

    thisdict = {
        "ชื่อ" : name,
        "วัน/เดือน/ปี เกิด" : birth,
        "ที่อยู่": address,
        "เลขบัตรประชาชน":ssn_number,
        "งาน":job,
        "กรุ้ปเลือด":blood,
        "ธนาคาร":bank,
        "อายุ":age,
        "น้ำหนัก":weight,
        "ส่วนสูง": heigth,
        "ศาสนา": religion,
        "สถานะ":marry,
        "มีลูก":son,
        "งานอดิเรก":hobby,
        "username":username
    }

    print(profile)
    return thisdict
