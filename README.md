# HeyGen Video Generator

HeyGen Video Generator 是一個 Python 包，提供了一個簡單的接口來使用 HeyGen API 生成視頻。

## 功能

- 上傳音頻文件
- 使用預定義的模板生成視頻
- 下載生成的視頻到指定路徑

## 安裝

你可以使用 pip 來安裝這個包：
```
bash
pip install heygen_video_generator
```

## 使用
1. 首先，導入 HeyGenVideoGenerator ：
```python
from avatar_sync_lip import HeyGenVideoGenerator
```

2. 創建 HeyGenVideoGenerator 實例，需要提供 API 密鑰：
```python
generator = HeyGenVideoGenerator(api_key='your_api_key')
```

3. 使用 generate_video 方法生成視頻：
```python
video_url = generator.generate_video(character='man1', audio_file_path='path/to/audio.mp3', save_path='path/to/save/video.mp4')
```

這個方法會上傳音頻文件，使用指定的模板生成視頻，然後將視頻下載到指定的路徑。它還會返回生成的視頻的 URL。

## 配置

該包使用預定義的模板。目前支持的模板有：

- "man1"
- "man2"
- "man3"
- "man4"
- "man5"
- "man6"
- "man7"
- "man8"
- "man9"
- "man10"
- "man11"
- "man12"
- "man13"
- "man14"
- "man15"
- "man16"
- "woman1"
- "woman2"
- "woman3"
- "woman4"
- "woman5"
- "woman6"
- "woman7"
- "woman8"
- "woman9"
- "woman10"
- "woman11"
- "woman12"
- "woman13"
- "woman14"
- "woman15"
- "woman16"

你可以在 `generate_video` 方法中指定要使用的模板。

## 依賴

- requests
- python-dotenv