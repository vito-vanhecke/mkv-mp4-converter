import os
import subprocess

if not os.path.exists('assets'):
    raise Exception(
        'Please run this script from the root directory of the project.')

mkv_list = os.listdir('assets')

if not os.path.exists('results'):
    os.mkdir('results')

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != '.mkv':
        raise Exception('Please only use mkv files.')

    ouput_name = name + '.mp4'
    try:
        subprocess.run(
            ['./ffmpeg', '-i', f"assets/{mkv}", '-codec', 'copy', f"results/{ouput_name}"], check=True
        )
    except:
        raise Exception('Something went wrong.')
print(f"{len(mkv_list)} files converted.")
