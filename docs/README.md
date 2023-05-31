# Reproducing results from this repository

This is a clear `README` file to reproduce the results using the rest of the documentation present in this directory for more detailed instructions.

## Code organization

The codes are written in `python` and using external libraries listed in the `requirements` file.

We will assume the project is run on a Linux operating system with available GPUs to train the models.

## Reproduce training

### Installation
Required: Conda.
1. Create a conda environment in your terminal using the following commands.
`conda create -n nnunet_env python=3.9.16`
`conda activate nnunet_env`

2. Install the requirements running the command below in the home directory of this github repository.
`pip install -r requirements.txt`

    - Note: You may want to install the nnUnet by [cloning the repository instead](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/installation_instructions.md) to have more control on the training parameters!

3. nnU-Net needs to know where you intend to save raw data, preprocessed data and trained models. For this you need to set a few environment variables. Please follow the instructions [here](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/set_environment_variables.md).

4. (OPTIONAL) Install [hiddenlayer](https://github.com/waleedka/hiddenlayer). hiddenlayer enables nnU-net to generate
   plots of the network topologies it generates (see [Model training](how_to_use_nnunet.md#model-training)). 
To install hiddenlayer,
   run the following command:
    ```bash
    pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git
    ```

### Data and model preparation
The source data are from:
1. The [spine-generic multi-subject](https://github.com/spine-generic/data-multi-subject/) dataset.
2. The INSPIRED dataset, `git@data:datasets/inspired`.
3. The [SCI-Colorado](https://github.com/ivadomed/model_seg_sci) dataset, `git@data:datasets/sci-colorado`.
4. The [Canproco](https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-021-02447-7) dataset, `git@data:datasets/canproco`
5. The [Basel-mp2rage](https://github.com/ivadomed/model_seg_ms_mp2rage) dataset, `git@data:datasets/basel-mp2rage`.

#### Preparing nnU-Net data (from BIDS)
1. Install the BIDS dataset on your machine either through git-annex or downloading it.
2. Create the required nnunet folders with this architecture, starting with `nnUNet_data` and the 3 folders below inside it:
    Example tree structure:
    ```
    nnUNet_raw/
    ├── nnUNet_preprocessed
    ├── nnUNet_raw
    ├── nnUNet_results
3. For some datasets using Ivadomed you may require a joblib file. If so, copy it into the script folder of this repository where the ` convert_bids_to_nnUnetv2.py` file is located.
4. Convert your BIDS data into nnunet-ready format!
    * Go into the script folder.
    * run the following command adapting the arguments to your machine and dataset.

    ```bash
    python convert_spine-generic_to_nnUNetv2.py --path-data <path-to-the-copied-dataset> --split 0.8 0.2 --label-suffix seg-manual --contrasts T1w T2w --path-out ${nnUNet_raw} -dname spineGNoCropSoftAvgBin -dnum <dnum> --seed <nSeed>
    ```

    NOTES:
    - `dname` - is the dataset name that nnUNet refers
    - `dnum` or `dataset-number` - is the number associated with the dataset name. The name and number can be anything. 
    - `contrasts` are the contrast to be taken for conversion.
    - `seed` is the seed for the split if you want to keep the same splits for comparing models.
    - `split` is the training/testing split.
    - `label-suffix` is the label sufix used in the BIDS dataset, for example it could be something like `seg-manual`. It is the last part of your image name after the contrast.
    - To work with more than one dataset, simply run this command for all datasets using the same `dname` and `dnum`, and then edit the produced `dataset.json` within the output folder with the correct number of training and testing examples adding all dataset examples.
    - Ensure all datasets use the same orientation (e.g. RPI)!
        - Here's a bash command to re-orient data in the BIDS format using SCT that may be useful.
        ```
        for file in sub*/anat/*.nii.gz;do sct_image -i ${file} -setorient RPI -o ${file}; done
        ``` 

5. Verify that he dataset was converted correctly using this command:
```bash
nnUNetv2_plan_and_preprocess -d <dnum> --verify_dataset_integrity
```

### Training
1. To train the model, run the following command:

```bash
CUDA_VISIBLE_DEVICES=X nnUNetv2_train <dnum> 3d_fullres 0
```

This runs the full-resolution 3D model on fold 0 of the dataset.

### Testing
1. Once training is done, run the following command to test the model:

```bash
CUDA_VISIBLE_DEVICES=X nnUNetv2_predict -i ${nnUNet_raw}/Dataset713_spineGNoCropSoftAvgBin/imagesTs -o <path-to-nnunet-folder>/nnUNet_results/<dnum_and_dataset_name>/test -d <dnum> -f 0 -c 3d_fullres
```

This commands runs the inference on the test set specified by the `imagesTs/` folder and saves the results in the `test/` folder in the results corresponding to the dataset. An example of `<dnum_and_dataset_name>` is `Dataset713_spineGNoCropSoftAvgBin`.

2. Calculate metrics using the `compute_test_metrics_anima.py` script and following the steps in the heading of the script and adapt it to your dataset and model and paths.

```bash

```