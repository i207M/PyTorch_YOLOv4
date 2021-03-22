python test.py --device 1 --names data/light_coco/coco.names \
--data data/light_coco.yaml --cfg cfg/yolov4-mine82.cfg --weights pth/29_best.pt \
--batch 8 --conf-thres 0.4 --iou-thres 0.4 --img 640
