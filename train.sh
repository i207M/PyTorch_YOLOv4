python train.py --device 0 --name yolov4 \
--data data/light_coco.yaml --cfg cfg/yolov4-mine82.cfg --weights pth/yolov4.weights \
--batch-size 16 --epochs 400 --img 640 640
