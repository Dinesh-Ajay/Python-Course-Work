'''
class Insta:

    def __init__(self):
        self._post = []

    @property
    def accesspost(self):
        return self._post
    
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

dinesh = Insta()

print(dinesh.accesspost)


dinesh.accesspost = "class and object"

print(dinesh.accesspost)
'''
# Inhetritance is of %5types
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multie Level Inheritance
# 4. Heiarchi Inheritance
# 5. Hybrid Inheritance

'''
# 1. Single Inheritance
class whatappV1():
    def message(self):
        print("You can send messages to people")


class whatappV2(whatappV1):
    def calls(self):
        print("You can video/audio calls")

dinesh = whatappV1()
print("V1- Dinesh")
dinesh.message()

naresh = whatappV2()
print("V2- Naresh")
naresh.message()
naresh.calls()



# 2. Multiple Inheritance
class whatsappV1:
    def message(self):
        print("You can send messages to people")


class whatsappV2:
    def calls(self):
        print("You can video/audio calls")

class whatsappV3:
    def media(self):
        print("You can share your photos/videos")


class whatsappV4(whatsappV1,whatsappV2,whatsappV3):
    def status(self):
        print("You can share status - [24 hours]")

dinesh = whatsappV4()
print("V4- Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()


# 3. Multie Level Inheritance
class whatsappV1:
    def message(self):
        print("You can send messages to people")


class whatsappV2(whatsappV1):
    def calls(self):
        print("You can video/audio calls")

class whatsappV3(whatsappV2):
    def media(self):
        print("You can share your photos/videos")


class whatsappV4(whatsappV3):
    def status(self):
        print("You can share status - [24 hours]")

Akhil = whatsappV1()
print("V1- Akhil")
Akhil.message()

naresh = whatsappV2()
print("V2- Naresh")
naresh.message()
naresh.calls()

Ajay = whatsappV3()
print("V3- Ajay")
Ajay.message()
Ajay.calls()
Ajay.media()

dinesh = whatsappV4()
print("V4- Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()


# 4. Heiarchi Inheritance
class whatsappV1:
    def message(self):
        print("You can send messages to people")


class whatsappV2(whatsappV1):
    def emojies(self):
        print("You can send messages with emojies to people")

class whatsappV3(whatsappV1):
    def sticker(self):
        print("You can send messages with stickers to people")


Akhil = whatsappV1()
print("V1- Akhil")
Akhil.message()

naresh = whatsappV2()
print("V2- Naresh")
naresh.message()
naresh.emojies()

Ajay = whatsappV3()
print("V3- Ajay")
Ajay.message()
Ajay.sticker()


# 5. Hybrid Inheritance
class whatsappV1:
    def message(self):
        print("You can send messages to people")


class whatsappV2(whatsappV1):
    def emojies(self):
        print("You can send messages with emojies to people")

class whatsappV3(whatsappV1):
    def sticker(self):
        print("You can send messages with stickers to people")

class whatsappV4(whatsappV2,whatsappV3):
    def gif(self):
        print("You can send messages with gif to people")

Akhil = whatsappV1()
print("V1- Akhil")
Akhil.message()

naresh = whatsappV2()
print("V2- Naresh")
naresh.message()
naresh.emojies()

Ajay = whatsappV3()
print("V3- Ajay")
Ajay.message()
Ajay.sticker()

dinesh = whatsappV4()
print("V4- Dinesh")
dinesh.message()
dinesh.emojies()
dinesh.sticker()
dinesh.gif()
'''

# class whatsappV1:
#     def status(self):
#         print("You can send messages to people")


# class whatsappV2(whatsappV1):
#     def status(self):
#         super().status()
#         print("You can send messages with emojies to people")

# class whatsappV3(whatsappV2):
#     def status(self):
#         super().status()
#         print("You can send messages with stickers to people")

# Ajay = whatsappV3()
# print("V3- Ajay")
# Ajay.status()


class whatsappV1:
    def status(self):
        print("You can send messages to people")


class whatsappV2(whatsappV1):
    def status(self):
        print("You can send messages with emojies to people")

class whatsappV3(whatsappV2):
    def status(self):
        whatsappV1.status(self)
        whatsappV2.status(self)
        print("You can send messages with stickers to people")

Ajay = whatsappV3()
print("V3- Ajay")
Ajay.status()
