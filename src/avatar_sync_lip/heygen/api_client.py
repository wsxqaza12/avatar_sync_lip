import requests


class HeyGenAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.heygen.com"

    def upload_audio(self, file_path):
        url = "https://upload.heygen.com/v1/asset"
        headers = {
            "Content-Type": "audio/mpeg",
            "X-Api-Key": self.api_key,
        }
        with open(file_path, "rb") as file:
            response = requests.post(url, headers=headers, data=file)
        response.raise_for_status()
        return response.json()['data']['url']

    def get_template(self, template_id):
        url = f'{self.base_url}/v2/template/{template_id}'
        headers = {
            'accept': 'application/json',
            'x-api-key': self.api_key,
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def generate_video(self, template_id, data):
        url = f'{self.base_url}/v2/template/{template_id}/generate'
        headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['data']['video_id']

    def get_video_status(self, video_id):
        url = f'{self.base_url}/v1/video_status.get'
        params = {'video_id': video_id}
        headers = {
            'Accept': 'application/json',
            'X-Api-Key': self.api_key
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()['data']['video_url']
