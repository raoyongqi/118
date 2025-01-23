import subprocess
import os

import subprocess

def download_audio_with_ffmpeg(m3u8_url, output_path):
    print(f"正在使用 FFmpeg 下载音频: {output_path}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    result = subprocess.run([
        "ffmpeg", "-i", m3u8_url, "-vn", "-acodec", "libmp3lame", "-ar", "44100", "-ab", "192k", "-headers", str(headers), output_path
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"音频下载完成: {output_path}")
    else:
        print(f"FFmpeg 下载失败: {result.stderr.decode()}")

def download_multiple_audios(m3u8_urls, output_directory="downloads"):
    # 创建下载目录（如果不存在）
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for index, url in enumerate(m3u8_urls, start=0):
        # 使用序号作为文件名
        file_name = f"{index}.mp3"
        output_path = os.path.join(output_directory, file_name)

        print(f"正在下载第 {index} 个音频...")
        try:
            download_audio_with_ffmpeg(url, output_path)
        except Exception as e:
            print(f"下载第 {index} 个音频时出错: {e}. 跳过此音频并继续下载下一个.")


if __name__ == "__main__":
    # M3U8 URL 列表
    m3u8_urls = [
        "https://hls.vdtuzv.com/videos4/56739faf9dede2dcc28a5f3772a6f62e/56739faf9dede2dcc28a5f3772a6f62e.m3u8?auth_key=1737511176-679051089c59f-0-062a0dc73b58304a7fbd5265eaae2431&v=3&time=0",   ]
    # 下载音频
    download_multiple_audios(m3u8_urls)
