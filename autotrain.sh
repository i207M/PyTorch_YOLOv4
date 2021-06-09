python3 auto.py
# << ./download/new
# >> ./data/new
cd ./data/new
bash train_new.sh
bash tensorboard.sh (port:6007)

export MODEL_NAME=exp0_new_2021-06-03_21-08-55

# cd ../../runs/${MODEL_NAME}/weights

# deploy:
export MODEL_PATH=./runs/
