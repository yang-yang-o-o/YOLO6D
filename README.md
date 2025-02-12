<div style="display: flex; justify-content: center; align-items: center; height: 10vh;">
  <h1>YOLO6D</h1>
</div>

YOLO6D is an open-source project aimed at 6D object pose estimation through object detection. Based on the YOLO architecture, YOLO6D combines deep learning and computer vision techniques to accurately predict the class, location, and pose of objects in images.


<!-- <div style="display: flex; justify-content: space-between; gap: 20px;">
  <div style="flex: 1; max-width: 45%;">
    <img src="Demo_1.gif" alt="Demo 1" style="width: 100%; height: auto;">
    <img src="Demo_2.gif" alt="Demo 2" style="width: 100%; height: auto;">
  </div>
  <div style="flex: 1; max-width: 45%;">
    <img src="Demo_3.gif" alt="Demo 3" style="width: 100%; height: auto;">
  </div>
</div> -->

| ![Demo 1](assets/Demo_1.gif) | ![Demo 3](assets/Demo_3.gif)     |
|-|-|

## Project Overview

YOLO6D is an extension of the traditional YOLO model, specifically designed to solve the 6D pose estimation problem. This project leverages deep learning models for object detection and accurately predicts the spatial location and orientation of objects. YOLO6D is particularly useful in fields such as industrial automation, augmented reality, and robot navigation.

## Environment Setup

Follow these steps to set up the environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/yang-yang-o-o/YOLO6D.git
   cd YOLO6D
   ```

2. Create a Python 3.6 and cuda-10.1 environment:

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Training

1. Data Preparation: Place your dataset in the data/ folder. The dataset should include images with annotations (e.g., class labels, pose information). [download](https://pan.baidu.com/s/1uOqs62xg42YV9lfe5Sly7w?pwd=ask4)

2. Configuration: Edit the config.yaml file to specify model hyperparameters, dataset paths, and other settings.

3. Start Training:

    ```bash
    python train.py --datacfg cfg/beer.data
    ```

4. During training, logs and model weights will be saved to the output/ directory.

## Testing

1. Load the trained model:

    ```bash
    python test.py --datacfg cfg/beer.data --modelcfg cfg/yolo-pose.cfg --weightfile backup/obj_name/model.weights
    ```

2. The testing process will output predictions and visualize the detected objects and their poses.

## Acknowledgements

This project is based on the following open-source code and research:

- [SINGLESHOTPOSE](https://github.com/microsoft/singleshotpose?tab=readme-ov-file) -  "Real-Time Seamless Single Shot 6D Object Pose Prediction", CVPR 2018.
- [YOLOv2-pytorch](https://github.com/longcw/yolo2-pytorch)

Thanks to all contributors and the open-source community for their support.

## License

MIT License. See LICENSE for more details.