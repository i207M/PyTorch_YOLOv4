export DATA_NAME=yolotest
#python3 auto.py ./download/${DATA_NAME}

#bash ./data/${DATA_NAME}/train_${DATA_NAME}.sh

export MODEL_NAME=exp4_yolotest_2021-06-09_16-59-52
source /home/dlenv/anaconda3/bin/activate
conda activate yolo-fix
cp ./runs/${MODEL_NAME}/weights/best.pt ./pth/${DATA_NAME}.pt
python3 detect_server.py --device 2 --names data/${DATA_NAME}/names --cfg data/${DATA_NAME}/${DATA_NAME}.cfg --save-txt --weights pth/${DATA_NAME}.pt --conf-thres 0.4 --iou-thres 0.5 --img 640 --output /home/dlenv/deploy/http-wrapper-lab/yolo_out/

#cd ../http-wrapper-lab/
#bash server_http.sh

#python3 yolo_client.py
