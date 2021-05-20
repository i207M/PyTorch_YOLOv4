python detect.py --device 2 --names data/light_coco/coco.names --cfg cfg/yolov4-mine82.cfg \
--source data/light_coco/images/one.txt --save-txt --weights pth/29_best.pt \
--conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/

python detect_server.py --device 3 --names data/light_coco/coco.names  --cfg cfg/yolov4-mine82.cfg\
--save-txt --weights pth/29_best.pt \
--conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/
