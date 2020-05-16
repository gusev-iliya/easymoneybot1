import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

mytoken='392aa5dcd93b90a721a202d4a7a606133908b6e93c401dfd8ccf836047a41832219979fb7c9f1daf6c008'

def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if('привет' in request.strip()):
                answer='Ну привет, если не шутишь!'
            else:
                answer='Я только на "Привет" реагирую'
            write_msg(event.user_id, answer)
