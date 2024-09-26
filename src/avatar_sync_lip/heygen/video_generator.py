from .config import TEMPLATES
from .api_client import HeyGenAPIClient
import time
import requests
import os


class HeyGenVideoGenerator:
    def __init__(self, api_key):
        self.api_client = HeyGenAPIClient(api_key)

    def generate_video(self, character, audio_file_path, save_path):
        # 步驟1：獲取模板ID
        template_id = TEMPLATES[character]["template_id"]

        # 步驟2：上傳音頻文件
        audio_url = self.api_client.upload_audio(audio_file_path)

        # 步驟3：獲取並更新模板JSON
        template_json = self.api_client.get_template(template_id)
        template_json['data']['variables']['my_audio']['properties']['url'] = audio_url
        data = template_json['data']

        # 步驟4：開始生成視頻
        video_id = self.api_client.generate_video(template_id, data)

        # 步驟5：等待並獲取視頻URL
        video_url = None
        while not video_url:
            time.sleep(10)  # 每10秒檢查一次
            try:
                video_url = self.api_client.get_video_status(video_id)
            except:
                pass  # 如果視頻還未準備好，繼續等待

        # 步驟6：下載視頻
        if video_url:
            self._download_video(video_url, save_path)

        return video_url

    def _download_video(self, video_url, save_path):
        response = requests.get(video_url)
        response.raise_for_status()

        # 確保保存路徑存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"影片已儲存到: {save_path}")
