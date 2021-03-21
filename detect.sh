python detect.py --device 2 --name data/light_coco/coco.names \
--source data/light_coco/images/test.txt --cfg cfg/yolov4-mine82.cfg --weights pth/29_best.pt \
--conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/
