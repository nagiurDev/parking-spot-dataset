# **Parking Spot Detection Dataset**

## **Project Overview**

This project aims to create a high-quality dataset for parking spot detection using outdoor parking lot videos. The dataset includes annotated images for training machine learning models, specifically YOLO, to detect parked cars and empty parking spots. This project also includes preprocessing scripts, data augmentation, and model evaluation tools to assist in training object detection models.

## **Dataset Structure**

The dataset is organized into training, validation, and test sets in YOLO format, along with the relevant metadata.

<!--
```
parking-spot-dataset/
│
├── data/
│   ├── raw_videos/              # Original parking lot videos
│   ├── extracted_frames/         # Frames extracted from raw videos
│   ├── annotations/              # YOLO format annotations (bounding boxes)
│   ├── data_augmentation/        # Augmented data
│   └── labeled_data/             # Final dataset (train, test, valid)
│
├── notebooks/                    # Jupyter notebooks for data exploration and metrics
│   ├── eda.ipynb                 # Exploratory Data Analysis (EDA)
│   ├── metrics_extraction.ipynb  # Extract performance metrics
│   └── visualization.ipynb       # Dataset visualization notebook
│
├── src/                          # Python scripts for data processing
│   ├── extract_frames.py         # Script to extract frames from videos
│   ├── evaluate_yolo.py          # Script to evaluate YOLO model
│   ├── vehicle_detection.py      # Object detection script for cars
│   ├── zone_configuration.py     # Configures parking zones
│   ├── generate_visuals.py       # Generates visual reports
│   └── create_report.py          # Creates final report summarizing dataset
│
├── models/                       # YOLO model files
│   └── yolo/
│       ├── yolov5/               # YOLOv5 related files
│       └── parking_spot_yolo.yaml # YOLO model configuration file
│
├── output-dataset/               # Final dataset ready for release
│   └── parking-spot-dataset-v1.0/
│       ├── train/
│       ├── test/
│       ├── valid/
│       └── data.yaml             # YOLO dataset config file
│
└── documentation/                # Documentation files
    ├── dev_process.md            # Step-by-step development process
    ├── git_commits_draft.md      # Draft of git commit messages
    ├── project_structure.md      # Explanation of project structure
    └── reference.md              # References used for the project
```
-->

## **Installation**

### 1. Clone the Repository:

```bash
git clone https://github.com/your-username/parking-spot-dataset.git
cd parking-spot-dataset
```

### 2. Install Dependencies:

Set up a Python environment and install the required packages listed in `requirements.txt` (if provided):

```bash
pip install -r requirements.txt
```

### 3. Extract Frames from Videos:

Run the script to extract frames from raw videos:

```bash
python src/extract_frames.py --input data/raw_videos/ --output data/extracted_frames/
```

### 4. Data Augmentation (Optional):

You can apply data augmentation to increase the variability of the dataset:

```bash
python src/data_augmentation.py --input data/extracted_frames/ --output data/data_augmentation/
```

### 5. Train YOLO Model (Optional):

Use the YOLOv5 configuration to train the model on the dataset:

```bash
python src/train_yolo.py --data output-dataset/parking-spot-dataset-v1.0/data.yaml --weights yolov5s.pt
```

## **Usage**

1. **Dataset**: The final dataset (version 1.0) is organized into train, validation, and test sets, ready for model training.
2. **Scripts**: Use the provided scripts for frame extraction, annotation verification, and model evaluation.
3. **Notebooks**: Explore the dataset, analyze metrics, and visualize results using the Jupyter notebooks in the `notebooks/` directory.

## **Contributing**

We welcome contributions! If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with detailed information.

## **License**

This project is licensed under the MIT License – see the `LICENSE` file for details.

## **References**
