# Avatar Sync Lip

Avatar Sync Lip 是一個 Python 包，提供了一個簡單的接口來使用 HeyGen API 生成影片以及全身動畫 avatar。

## 功能
### HeyGen API
- 上傳音檔文件
- 使用預定義的模板生成影片
- 下載生成的影片到指定路徑

### 全身動畫 avatar
- 生成全身動畫 avatar 視頻
- 支持自定義音檔輸入
- 多種預設角色可選

## 安裝
你可以使用 pip 來安裝這個包：
```bash
pip install avatar_sync_lip-*.whl
```


# HeyGen API 文件
## 使用
1. 首先，導入 HeyGenVideoGenerator ：
```python
from avatar_sync_lip import HeyGenVideoGenerator
```

2. 創建 HeyGenVideoGenerator 實例，需要提供 API 密鑰：
```python
generator = HeyGenVideoGenerator(api_key='HeyGen_key')
```

3. 使用 generate_video 方法生成影片：
```python
video_url = generator.generate_video(
    character='man1',
    audio_file_path='path/to/audio.mp3',
    save_path='path/to/save/video.mp4'
)
```
這個方法會上傳音檔文件，使用指定的模板生成影片，然後將影片下載到指定的路徑。它還會返回生成的影片的 URL。

## 參數說明
- `character`：要使用的角色名稱
- `audio_file_path`：音頻文件的路徑
- `save_path`：生成的視頻保存路徑

## 支持的角色

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


# 全身動畫 avatar 文件
## 使用
1. 首先，導入 FullBodyAvatarGenerator：
```python
from avatar_sync_lip import FullBodyAvatarGenerator
```

2. 創建 FullBodyAvatarGenerator 實例，需要提供 API URL：
```python
generator = FullBodyAvatarGenerator(api_url="http://0.0.0.0:1234")
```

3. 使用 generate_full_body_avatar 方法生成全身動畫 avatar 影片：
```python
video_url = generator.generate_full_body_avatar(
    character='woman1',
    audio_file_path='test.mp3',
    save_path='input/video.mp4'
)
```

這個方法會上傳音檔文件，使用指定的角色生成全身動畫 avatar 影片，然後將影片下載到指定的路徑。它還會返回生成的影片的 URL，方便後須續處理。

## 參數說明

- `character`：要使用的角色名稱
- `audio_file_path`：音檔文件的路徑
- `save_path`：生成的影片保存路徑

## 支持的角色

目前支持為 "man1", "man2", "woman1", "woman2"。
