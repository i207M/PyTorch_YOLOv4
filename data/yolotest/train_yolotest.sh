source /home/dlenv/anaconda3/bin/activate
conda activate yolo-fix
cd /home/dlenv/deploy/PyTorch_YOLOv4
python train.py --device=1 --name yolotest_2021-06-09_16-59-52 --data ./data/yolotest/yolotest.yaml --cfg ./data/yolotest/yolotest.cfg --weights pth/yolov4.weights --batch-size 8 --epochs 300 --img-size 640 640
