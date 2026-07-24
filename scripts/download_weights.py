import os
import gdown
import time

def main():
    os.makedirs('weights', exist_ok=True)
    file_id = '1NZfd37POE0S-nMPI5RsGg1a7lN17HNvC'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'weights/epoch_11_qfdet_star_vtuav.pth'
    
    max_retries = 10
    for attempt in range(max_retries):
        try:
            print(f"Downloading {output} from Google Drive... (Attempt {attempt+1}/{max_retries})")
            # If the file exists, gdown won't resume by default with quiet=False unless we handle it, but wait, gdown command line has --continue. In python API, there is no continue. We'll just let it overwrite or fail.
            gdown.download(url, output, quiet=False)
            print("Download complete.")
            break
        except Exception as e:
            print(f"Download failed: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
