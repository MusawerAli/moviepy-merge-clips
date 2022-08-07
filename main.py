from merge_vide import MERGE_VIDEO
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file = f"{BASE_DIR}/data/1.mp4"
merge_data = MERGE_VIDEO(file,vcodec='libvpx-vp9',base_dir=BASE_DIR,dynamic_name='dynamic_video.mp4')
print(merge_data.merge_video())