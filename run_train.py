run_str = 'python train.py --device 0 --name yolov4 \
--data ./data/light_coco.yaml --cfg ./cfg/yolov4-mine.cfg --weights ./pth/yolov4.weights \
--batch-size 16 --epochs 300 --img 640 640'

test_str = 'python test.py --device 0 \
--data ./data/light_coco.yaml --cfg ./cfg/yolov4-mine.cfg --weights weights/best_yolov4.pt \
--batch 8 --conf 0.001 --img 640'

print(run_str)
print(test_str)
