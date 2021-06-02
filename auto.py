import os
import shutil
import json

DATA_DIR = './data'


def make_yaml(name: str, dir: str, target: str) -> None:
    instance_json = json.load(open(os.path.join(dir, 'annotations', 'instances_default.json')))
    categories = instance_json['categories']

    template = open(os.path.join(DATA_DIR, 'template.yaml')).read()
    yaml = template.replace('/*NUM_CLASS*/', str(len(categories)))
    names = [dat['name'] for dat in categories]
    yaml = yaml.replace('/*NAMES*/', str(names))
    yaml = yaml.replace('/*TRAIN*/', os.path.join(target, 'images'))

    open(os.path.join(target, name + '.yaml'), 'w').write(yaml)


def make_cfg(name: str, dir: str, target: str) -> None:
    pass


def gen(name: str, dir: str, target: str) -> None:
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(dir, target)
    make_yaml(name, dir, target)
    make_cfg(name, dir, target)


if __name__ == '__main__':
    dir = './download/new'  # input('Input data directory')
    name = os.path.basename(dir)
    target = os.path.join(DATA_DIR, name)
    gen(name, dir, target)
