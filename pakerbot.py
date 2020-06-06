import time

from fbchat import log, Client
from fbchat.models import *


class PakerBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type,  **kwargs):

        if message_object.text == "!reputacja" and thread_type == ThreadType.GROUP and thread_id == "2458017120955707":
            self.send(Message(text="Nasi bohaterowie:\nKrzysztof 9999pkt rep\nRobert 666 pkt rep\nKrzysztof 40 pkt rep\nBronisław 15 pkt rep"), thread_id="2458017120955707", thread_type=ThreadType.GROUP)

    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        
        if (
            removed_id != self.uid
            and author_id != self.uid
        ):
            log.info("{} ktoś nam spierdolił. Zaraz go dodam!".format(removed_id))
            self.addUsersToGroup(removed_id, thread_id=thread_id)       
            self.send(Message(text="Nie tym razem byczq"), thread_id="2458017120955707", thread_type=ThreadType.GROUP)

#Imiona

    def onMessage(self, author_id, message_object, thread_id, thread_type,  **kwargs):

        if message_object.text == "rovert" or message_object.text == "rupert" or message_object.text == "roland" or message_object.text == "rower" and thread_type == ThreadType.GROUP and thread_id == "2458017120955707":
            self.send(Message(text="Dla Ciebie Książe Krwi Królewskiej Robert*"), thread_id="2458017120955707", thread_type=ThreadType.GROUP)

    def onMessage(self, author_id, message_object, thread_id, thread_type,  **kwargs):

        if message_object.text == "krzychu" or message_object.text == "krzych" or message_object.text == "krzysiek" and thread_type == ThreadType.GROUP and thread_id == "2458017120955707":
            self.send(Message(text="Dla Ciebie Jaśnie Wielmożny Hrabia Krzysztof*"), thread_id="2458017120955707", thread_type=ThreadType.GROUP)

    def onMessage(self, author_id, message_object, thread_id, thread_type,  **kwargs):

        if message_object.text == "Gronek" or message_object.text == "Bronek" or message_object.text == "Broniu" or message_object.text == "broniu" or message_object.text == "bronek" or message_object.text == "gronek" or message_object.text == "Groniu" and thread_type == ThreadType.GROUP and thread_id == "2458017120955707":
            self.sendLocalImage(
                "gronek2.jpg",
                thread_id="2458017120955707", thread_type=ThreadType.GROUP)

client = PakerBot(variable)
client.listen()

     #      and message_object.text == "!ucieczka"