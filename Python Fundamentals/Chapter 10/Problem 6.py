# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(ranjit, fro, to):
        print(f"Ticket is booked in train no:  {ranjit.trainNo} from {fro} to {to}")

    def getStatus(raj):
        print(f"Train no: {raj.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")


t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")