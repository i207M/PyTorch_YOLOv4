Python: `conda activate yolo-fix`

TL;DR

```
python detect_server.py --device 3 --names data/light_coco/coco.names --cfg cfg/yolov4-mine82.cfg --source data/light_coco/images/one.txt --save-txt --weights pth/29_best.pt --conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/

python udp_send_yolo.py
```

## 启动服务器

```
python detect_server.py --device 3 --names data/light_coco/coco.names --cfg cfg/yolov4-mine82.cfg --source data/light_coco/images/one.txt --save-txt --weights pth/29_best.pt --conf-thres 0.4 --iou-thres 0.5 --img 640 --output output/
```

服务器从UDP9876端口接受 以UTF-8编码的**图像的相对/绝对路径**。

最后生成的结果保存在`output/`

## 测试

`python udp_send_yolo.py`

向UDP9876端口发送测试图片的路径。
