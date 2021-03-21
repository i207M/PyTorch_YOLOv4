command_str = 'python train.py --device 0 --name yolov4 \
--data data/light/coco.yaml --cfg cfg/yolov4-mine.cfg --weights pth/yolov4.weights \
--batch-size 16 --epochs 300 --img 640 640'

print(command_str)
