import requests

class RTC_util():

    BASE_URL = None
    def __init__(self, BASE_URL):
        self.BASE_URL = BASE_URL
    
    def create_room(self):
        '''
        Create room in RTC service

        Returns:
            str: room_code
            str: access_token
        '''
        url = f'{self.BASE_URL}/room/create'
        data = {}
        response = requests.post(url, data=data)
        response = response.json()
        room_code = response.get('code')
        access_token = response.get('access_token')
        return room_code, access_token

    def delete_room(self, room_code):
        '''
        Delete room from RTC service

        Returns:
            bool: True if successful
        '''
        url = f'{self.BASE_URL}/room/{room_code}'
        data = {}
        response = requests.delete(url, data=data)
        return response.status_code == 200

    def get_room(self, room_code):
        '''
        Get room from RTC service

        Returns:
            str: room_code
            str: access_token
        '''
        url = f'{self.BASE_URL}/room/{room_code}'
        data = {}
        response = requests.get(url, data=data)
        response = response.json()
        room_code = response.get('code')
        access_token = response.get('access_token')
        return room_code, access_token