import requests
import time
import os
from .config import ALLOWED_CHARACTERS


class FullBodyAvatarGenerator:
    def __init__(self, api_url):
        self.api_url = api_url

    def generate_full_body_avatar(self, audio_file_path, character, save_path):
        if character not in ALLOWED_CHARACTERS:
            raise ValueError(
                f"無效的角色名稱。允許的角色名稱為: {', '.join(ALLOWED_CHARACTERS)}")

        # 步驟1：上傳音頻並獲取video_id
        video_id = self._upload_audio_and_get_video_id(
            audio_file_path, character)

        # 步驟2：等待並獲取視頻URL
        video_url = self._wait_for_video_completion(video_id)

        # 步驟3：下載視頻
        if video_url:
            self._download_video(video_url, save_path)

        return video_url

    def _upload_audio_and_get_video_id(self, audio_file_path, character):
        url = f"{self.api_url}/process_video"
        files = {'audio': open(audio_file_path, 'rb')}
        data = {'character_name': character}
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        return response.json()['video_id']

    def _wait_for_video_completion(self, video_id):
        url = f"{self.api_url}/get_video/{video_id}"
        while True:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data['video_url'] is not None:
                return data['video_url']
            elif data['video_url'] == 'Error':
                raise Exception("視頻生成失敗")
            time.sleep(10)  # 每10秒檢查一次

    def _download_video(self, video_url, save_path):
        response = requests.get(f"{self.api_url}{video_url}")
        response.raise_for_status()

        # 確保保存路徑存在
        save_dir = os.path.dirname(save_path)
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"影片已儲存到: {save_path}")
