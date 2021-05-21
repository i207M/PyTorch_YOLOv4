Python >= 3.7

TL;DR

```
python detect_server.py
python udp_send_yolo.py
```

## 启动服务器

`python detect_server.py`

服务器从UDP9876端口接受 以UTF-8编码的**图像的相对/绝对路径**。

最后生成的结果保存在`output/`

## 测试

`python udp_send_yolo.py`

向UDP9876端口发送测试图片的路径。
