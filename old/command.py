run_str = 'python train.py --device 0 --name data/light_coco/coco.names \
--data data/light_coco.yaml --cfg cfg/yolov4-mine82.cfg --weights pth/yolo.weights \
--batch-size 16 --epochs 300 --img 640 640'

test_str = 'python test.py --device 1 --name data/light_coco/coco.names \
--data data/light_coco.yaml --cfg cfg/yolov4-mine82.cfg --weights pth/24_best.pt \
--batch 8 --conf-thres 0.4 --iou-thres 0.35 --img 640'

det_str = 'python detect.py --device 2 --name data/light_coco/coco.names \
--source data/light_coco/images/test.txt --cfg cfg/yolov4-mine82.cfg --weights pth/29_best.pt \
--conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/'

print(run_str)
print(test_str)
print(det_str)
