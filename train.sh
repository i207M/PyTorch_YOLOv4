python train.py --device 0 --name data/light_coco/coco.names \
--data data/light_coco.yaml --cfg cfg/yolov4-mine82.cfg --weights pth/yolo.weights \
--batch-size 16 --epochs 300 --img 640 640
