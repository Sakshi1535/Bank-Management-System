import json
import random
import string


class Bank:
    database = "data.json"
    data = []

    try:
        with open(database, "r") as fs:
            data = json.load(fs)
    except:
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        acc = alpha + num + spchar
        random.shuffle(acc)

        return "".join(acc)

    @classmethod
    def create_account(cls, name, age, email, pin):

        if age < 18:
            return None, "Age must be 18+"

        if len(str(pin)) != 4:
            return None, "PIN must be 4 digits"

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": cls.__accountgenerate(),
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()

        return info, "Success"

    @classmethod
    def find_user(cls, acc, pin):

        userdata = [
            user for user in cls.data
            if user["accountNo."] == acc and user["pin"] == pin
        ]

        return userdata

    @classmethod
    def deposit(cls, acc, pin, amount):

        userdata = cls.find_user(acc, pin)

        if not userdata:
            return False

        userdata[0]["balance"] += amount

        cls.__update()

        return True

    @classmethod
    def withdraw(cls, acc, pin, amount):

        userdata = cls.find_user(acc, pin)

        if not userdata:
            return "invalid"

        if userdata[0]["balance"] < amount:
            return "insufficient"

        userdata[0]["balance"] -= amount

        cls.__update()

        return "success"

    @classmethod
    def update_details(cls, acc, pin, name, email, new_pin):

        userdata = cls.find_user(acc, pin)

        if not userdata:
            return False

        user = userdata[0]

        if name:
            user["name"] = name

        if email:
            user["email"] = email

        if new_pin:
            user["pin"] = new_pin

        cls.__update()

        return True

    @classmethod
    def delete_account(cls, acc, pin):

        userdata = cls.find_user(acc, pin)

        if not userdata:
            return False

        cls.data.remove(userdata[0])

        cls.__update()

        return True