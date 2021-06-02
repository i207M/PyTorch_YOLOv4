import os
import shutil
import time
import json

DATA_DIR = './data'


def make_yaml(name: str, dir: str, target: str):
    instance_json = json.load(open(os.path.join(dir, 'annotations', 'instances_default.json')))
    categories = instance_json['categories']

    template = open(os.path.join(DATA_DIR, 'template.yaml')).read()
    yaml = template.replace('/*NUM_CLASS*/', str(len(categories)))
    names = [dat['name'] for dat in categories]
    yaml = yaml.replace('/*NAMES*/', str(names))
    yaml = yaml.replace('/*TRAIN*/', os.path.join(target, 'images'))

    open(os.path.join(target, name + '.yaml'), 'w').write(yaml)

    return instance_json


def make_cfg(name: str, target: str, n_class: int) -> None:
    max_bathes = n_class * 2000
    template = open(os.path.join(DATA_DIR, 'template.cfg')).read()

    cfg = template.replace('/*MAX_BATCHES*/', str(max_bathes))
    cfg = cfg.replace('/*STEPS*/', f'{int(0.8*max_bathes)},{int(0.9*max_bathes)}')
    cfg = cfg.replace('/*CLASSES*/', str(n_class))
    cfg = cfg.replace('/*FILTERS*/', str((n_class + 5) * 3))

    open(os.path.join(target, name + '.cfg'), 'w').write(cfg)


def make_sh(name: str, target: str) -> None:
    sh_path = os.path.join(target, name + '_train.sh')
    with open(sh_path, 'w') as f:
        f.write('source /home/dlenv/anaconda3/bin/activate\n')
        f.write('conda activate yolo-fix\n')
        f.write('cd /home/dlenv/deploy/PyTorch_YOLOv4\n')
        f.write(
            f'python train.py --device=1 --name {name}_{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())} '
            f'--data {os.path.join(target,name+".yaml")} --cfg {os.path.join(target,name+".cfg")} --weights pth/yolov4.weights '
            f'--batch-size 16 --epochs 300 --img 640 640\n'
        )
    os.chmod(sh_path, 0o777)


def make_label(target: str, instance_json) -> None:
    label_dir = os.path.join(target, 'labels')
    os.mkdir(label_dir)
    imgid_to_data = {}
    label_dict = {}
    for dat in instance_json['images']:
        id = dat['id']
        label_dict[id] = []
        imgid_to_data[id] = {'name': dat['file_name'], 'w': dat['width'], 'h': dat['height']}
    for dat in instance_json['annotations']:
        # WARNING: MINUS 1
        imgid = dat['image_id']
        hw = imgid_to_data[imgid]
        category_id = dat['category_id'] - 1
        bbox = dat['bbox']
        nom_center_x = (bbox[0] + bbox[2] / 2) / hw['h']
        nom_center_y = (bbox[1] + bbox[3] / 2) / hw['w']
        nom_w = bbox[2] / hw['w']
        nom_h = bbox[3] / hw['h']
        label_dict[imgid].append(f'{category_id} {nom_center_x} {nom_center_y} {nom_w} {nom_h}\n')

    for id, labels in label_dict.items():
        with open(os.path.join(label_dir, imgid_to_data[id]['name'][:-4] + '.txt'), 'w') as f:
            f.write(''.join(labels))


def gen(name: str, dir: str, target: str) -> None:
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(dir, target)
    instance_json = make_yaml(name, dir, target)
    make_label(target, instance_json)
    make_cfg(name, target, len(instance_json['categories']))
    make_sh(name, target)


if __name__ == '__main__':
    dir = './download/new'  # input('Input data directory')
    name = os.path.basename(dir)
    target = os.path.join(DATA_DIR, name)
    gen(name, dir, target)
