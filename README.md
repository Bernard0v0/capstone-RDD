# capstone-RDD
## reproduce the enviornment
conda env create -f environment.yml
## activate the enviornment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate RDD_env
## download mmcv & other required packages
mim install mmcv-full==1.6.0 
sudo yum install -y openssl11
pip install mmengine
pip install -r yolov5/requirements.txt
pip install -r yolov7/requirements.txt
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .
## enable ipynb detect the enviornment
pip install ipykernel
python -m ipykernel install --user --name RDD_env --display-name RDD
## download datasets
cd ../
cd datasets
cd RDD2022
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Japan.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_India.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Czech.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Norway.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_United_States.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_China_MotorBike.zip
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_China_Drone.zip
unzip RDD2022_Japan.zip
unzip RDD2022_India.zip
unzip RDD2022_Czech.zip
jar xvf RDD2022_Norway.zip
unzip RDD2022_United_States.zip
unzip RDD2022_China_Drone.zip
unzip RDD2022_China_MotorBike.zip
## data pre-processing for yolo
python gene_train_val.py
## data pre-processing for mmdetection
cd ../..
python datasets/RDD2022/xml2yolo.py --class_file datasets/RDD2022/damage_classes.txt --input_file datasets/RDD2022/train.txt
python datasets/RDD2022/gene_file_list.py
## test images preparation
mkdir datasets/RDD2022/test1_images
cp datasets/RDD2022/China_MotorBike/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Czech/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/India/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Norway/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Japan/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/United_States/test/images/* datasets/RDD2022/test1_images/
mv val.txt datasets/RDD2022/Czech/train
## debugging
- ERROR:torch.distributed.elastic.multiprocessing.api:failed (exitcode: 2) local_rank: 0 (pid: 31797) of binary: /home/ec2-user/anaconda3/envs/RDD_test/bin/python || https://stackoverflow.com/questions/69468128/fail-attributeerror-module-collections-has-no-attribute-container



# Acknowledgement
- https://github.com/ultralytics/yolov5
- https://github.com/WongKinYiu/yolov7
- https://github.com/open-mmlab/mmdetection
- https://github.com/berry-ding/ShiYu_SeaView_GRDDC2022