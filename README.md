# capstone-RDD
conda env create -f environment.yml
source ~/anaconda3/etc/profile.d/conda.sh
conda activate RDD_env
mim install mmcv-full==1.6.0 
mim install mmcls
pip install ipykernel
python -m ipykernel install --user --name RDD_env --display-name RDD
pip install -r yolov5/requirements.txt
pip install -r yolov7/requirements.txt
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .
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
cd datasets/RDD2022
python gene_train_val.py
cd ../..
python datasets/RDD2022/xml2yolo.py --class_file datasets/RDD2022/damage_classes.txt --input_file datasets/RDD2022/train.txt
python datasets/RDD2022/gene_file_list.py
mkdir datasets/RDD2022/test1_images
cp datasets/RDD2022/China_MotorBike/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Czech/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/India/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Norway/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/Japan/test/images/* datasets/RDD2022/test1_images/
cp datasets/RDD2022/United_States/test/images/* datasets/RDD2022/test1_images/
mv val.txt datasets/RDD2022/Czech/train
