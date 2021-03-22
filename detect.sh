python detect.py --device 2 --names data/light_coco/coco.names \
--source data/light_coco/images/IMG_0044.MOV --cfg cfg/yolov4-mine82.cfg --weights pth/30_best.pt \
--conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/
