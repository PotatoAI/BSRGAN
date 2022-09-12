import sys
import os
import glob
from tqdm import tqdm

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    print(f"Converting {input_path} -> {output_path}")

    in_pic_path = f"tmp/{input_path}"
    os.makedirs(in_pic_path, exist_ok=True)
    out_pic_path = f"tmp/{output_path}"
    os.makedirs(out_pic_path, exist_ok=True)

    command = f"ffmpeg -i {input_path} {in_pic_path}/%04d.png -hide_banner"
    print(command)
    os.system(command)

    files = glob.glob(f"{in_pic_path}/*.png")
    os.system('clear')
    for fname in tqdm(files):
        basefname = os.path.basename(fname)
        in_path = f"{in_pic_path}/{basefname}"
        out_path = f"{out_pic_path}/{basefname}"
        command = f"poetry run python main.py {in_path} {out_path}"
        print(command)
        os.system(command)
        os.system('clear')

    command = f"ffmpeg -framerate 15 -pattern_type glob -i '{out_pic_path}/*.png' -c:v libx264 -pix_fmt yuv420p {output_path}"
    print(command)
    os.system(command)
