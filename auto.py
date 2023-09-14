import os
from random import randint
from tqdm import tqdm
import argparse

name = ["차도흔", "이승훈", "이동엽", "장현진", "최부광", "이지훈", "이은찬", "고은송", "이희원", "고은우"]
sep = ', '

parser = argparse.ArgumentParser()
parser.add_argument("person_name", type=str, help=f"{sep.join(name)} 중 이름 입력")
args = parser.parse_args()

mine, tot = name.index(args.person_name), len(name)


base_folder = "D:/SKTAI/KoDALLE/data/coco"
input_folder, style_folder, output_folder = [base_folder + i for i in ("/val2014", "/style", "/style_val2014")]


content_imgs = os.listdir(input_folder)[2146:]
style_imgs = os.listdir(style_folder)

part = len(content_imgs)//tot
content_imgs = content_imgs[mine*part:(mine+1)*part] if mine<5 else content_imgs[mine*part:]

os.system("conda activate style")
for cimg in tqdm(content_imgs):
    simg = style_imgs[randint(1, len(style_imgs))-1]
    message = f"style_transfer {input_folder}\\{cimg} {style_folder}\\{simg} -o {output_folder}\\{cimg} -cw 0.2"
    tqdm.write(message)
    os.system(message)