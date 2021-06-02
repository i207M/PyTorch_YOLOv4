source /home/dlenv/anaconda3/bin/activate
conda activate yolo-fix
cd /home/dlenv/deploy/PyTorch_YOLOv4
python train.py --device=1 --name new_2021-06-02_18-20-22 --data ./data/new/new.yaml --cfg ./data/new/new.cfg --weights pth/yolov4.weights --batch-size 16 --epochs 300 --img 640 640
