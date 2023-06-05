---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-05-19" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Spinal Cord Segmentation Generalizable Across Datasets"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: []

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2023/bouchard_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
# website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [mri, segmentation, spinal cord, python]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "My idea is to train a deep learning model on multiple (4) spinal cord segmentation datasets to improve generalizability to new contrasts, vendors, pathologies, etc...

My project aims to train the nnU-Net model architecture, a state-of-the-art deep learning architecture for biomedical segmentation, on four aggregated datasets and compare its generalizability capabilities with the four specific models trained on each individual dataset. I will conclude by comparing the two approaches on a fifth and sixth dataset outside of the training domain."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "images/cover_image.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

![Background overview](images/background.png)

Spinal cord segmentation is the process of identifying the spinal cord area in MRI images. This is clinically relevant notably to compute cross-sectional area for the diagnosis and monitoring of neurodegenerative diseases such as multiple sclerosis.

Performing automatic spinal cord segmentation is complicated even with deep learning methods due to the wide range of MRIs that can be produced from various contrasts, machine vendors and pathologies of the patient. This results in very different output images that no individual model can handle yet.

Typically, we use one model per data sub-set to reduce the complexity of the task, like a specific contrast (e.g. T2w), and end up with *N* models where we test each of them to select the optimal model for new images. This is not reliable and scalable.

My goal is to build a more general model to automatically perform spinal cord segmentation across contrasts, vendors and pathologies.

Below is a visual example of the segmentation result on one subject using a contrast outside of the training scheme comparing the ground truth or manual segmentation (left) with the aggregated model (center) and one of the specific models (right).

![Visual result example](images/result_basel_visual.gif)

### Tools

Main tools: Python/Pytorch/Git/ssh/Jupyter Notebooks

Most important: [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) -> a state-of-the-art “self-configuring method for deep learning-based biomedical image segmentation”.


### Methodology
Train and compare 2 frameworks (individual models vs. general model) for performing automatic spinal cord segmentation.

![Frameworks overview](images/frameworks.png)

### Data

Various (6) Spinal Cord MRI datasets available at Neuropoly with manual segmentation.

Our training datasets:
* Spine Generic Public Database* (multi-subject), n=244, 3 vendors, 6 contrasts (T2w, T1w, T2*w, 3D axial GRE (MTon), GRE-T1w (MToff), DWI), pathology: Mild Compression, Healthy Controls.
* INSPIRED, n=79, 1 contrast (acq-cspineAxial_T2w), pathology: Degenerative Cervical Myelopathy (38), Spinal Cord Injury, Healthy Controls.
* SCI-Colorado, n=80, 1 contrast (T2w), pathology: Spinal Cord Injury.
* Canproco, n=445, 1 contrast (T2w), pathology: MS.

Test datasets (outside training distribution):
* Basel-mp2rage, n=283, 1 contrast (MP2RAGE "UNI"), pathology: Multiple Sclerosis (180), Healthy Controls (103).
* Extra: [Rohan](https://github.com/brainhack-school2023/banerjee_project)’s fMRI test set, n=8, 1 contrast (EPI-GRE).


**Cohen-Adad, J., Alonso-Ortiz, E., Abramovic, M., Arneitz, C., Atcheson, N., Barlow, L., Barry, R.L., Barth, M., Battiston, M., Büchel, C., et al.: Open-access quantitative mri data of the spinal cord and reproducibility across participants, sites and manufacturers. Scientific data 8(1), 219 (2021)

### Objectives

* Create a script for converting N BIDS datasets into one large “nnU-Net-ready” dataset train/test split. Read more [here](https://github.com/brainhack-school2023/bouchard_project/tree/main/docs).
* Compare a general model to specific models for spinal cord segmentation on the datasets’ test sets. Results shown [here](https://github.com/brainhack-school2023/bouchard_project/blob/main/results/results_analysis.ipynb).
* Test the resulting 2 frameworks on a fifth and sixth dataset to demonstrate the generalizability capabilities of the larger model. Results shown [here](https://github.com/brainhack-school2023/bouchard_project/blob/main/results/results_analysis.ipynb).

### Deliverables

* A Github repository with codes and scripts to reproduce training and testing `github.com/brainhack-school2023/bouchard_project`.
* A [jupyter notebook](https://github.com/brainhack-school2023/bouchard_project/blob/main/results/results_analysis.ipynb) of the analysis codes and visualizations for comparing the results.
* Documentation. This README file and the README in `docs/`.
* Model checkpoints for the nnUnet models trained on all 4 datasets (right now available on /duke for Neuropoly members).

## Results

### Progress overview

The project was initiated by Louis-François Bouchard, based on the existing BrainHack template. I started from existing scripts for the nnU-Net method and adapted them for my needs. There are now all necessary updated scripts in the `scripts` folder and documentation in `docs` through a clear README file to reproduce the project. A notebook is available with all results as well as the final project presentation powerpoint for more information. Ultimately, the project was a success and the hypothesis (aggregating datasets == better general model) was confirmed.

### Tools I learned during this project

 * **Git, GitHub, Git-Annex -** I learned to better use git, github and git-annex for training models and creating a project repository with appropriate documentation and hierarchy.
 * **nnU-Net -** I learned to successfully prepare data, train a model, and analyze the results for spinal cord segmentation using the nnU-Net model framework (library).
 * **Python/Pytorch/Notebooks/BIDS/ssh/GPU training/bash -** I got more familiar with pytorch for training and testing models remotely on a server with multiple GPUs. I also used and wrote many bash scripts for pre-processing images (from BIDS to nnU-Net, but also re-orienting, resampling..) and automate tasks more efficiently. Overall, this project helped me develop important skills as well as understanding the necessary steps in working on this kind of project from scratch.

### Results

#### Deliverable 1: A GitHub repository with code and scripts to reproduce the project

This README along with the README in the `docs` folder allows anyone to reproduce these experiments and use the `scripts/` and notebooks adapting the commands with their own paths and data.

#### Deliverable 2: A notebook with results analysis

The deliverable 2 is available in the [results/](https://github.com/brainhack-school2023/bouchard_project/tree/main/results) folder where I show both quantitative (mean dice results) and qualitative (visual results) results of the different (3) experiments. 
The experiments were (i) to compare the general model to specific models on their respective tasks (e.g. compare the general model to the spine generic-trained model on the spine generic test set to see if the general model kept a similar "understanding" of this sub-set of the data), (ii) compare the general model to the specific models to two unseen sets of data (with unseen image contrasts), including the Basel dataset with MP2RAGE contrast and [Rohan](https://github.com/brainhack-school2023/banerjee_project)'s fMRI test set with EPI-GRE contrast.

Bellow is the most important outcome, showing how the aggregated (or general) model outperforms specific models on unseen data, here reporting the mean dice over the Basel-MP2RAGE dataset, which uses a contrast (MP2RAGE) that was not seen in any training scheme prior testing.

![Dice comparison on Basel-MP2RAGE with all approaches](images/BASEL_TESTS.png)

See more interesting results in [the notebook](https://github.com/brainhack-school2023/bouchard_project/blob/main/results/results_analysis.ipynb)!


#### Deliverable 3: Documentation

I believe this documentation along with `docs/README` and the comments in the different scripts allows for anyone to re-use and replicate this project easily.

#### Deliverable 4: Model checkpoints

Right now the models are available on `duke/` for Neuropoly students. An improved version of the general model will be shared and pushed to [SCT](https://github.com/sct-pipeline) once the results are satisfying enough.

## Conclusion and acknowledgement

To conclude, I believe this project was a success, showing how aggregating datasets can build a more general model while keeping the "specialized capabilities" similar. Adding more diverse data is a promising next step to further improve the model as well as performing proper visual analysis and cross-validation to ensure the validity of the results and better understand the results' quality and problems to solve.

I wanted to highlight some limitations of this project like the fact that the datasets are of various sizes, which may hurt the comparison. Likewise, most datasets use the T2w contrast only, which is not ideal for building a more general model, but was the only way to correctly split our dataset and keep contrast "not seen in training" outside any training frameworks and only in our testing datasets. Finally, the time constraints didn't allow me to perform proper cross-validation of the different models as well as in-depth analysis of the results visually, as mentioned above for an interesting next step.

Still, the goal of this project was to learn how to use nnU-Net, improve my git, github and git-annex skills and improve my understanding of MRIs, contrasts and spinal cord segmentation. In those terms, the project was a success and is a promising start for my PhD work.

## TMP section - TO DO:
(TO DO JUNE 2)
- [x] Prepare Spine Generic dataset for nnU-Net.
- [x] Prepare Basel-mp2rage dataset for nnU-Net.
- [x] Prepare INSPIRED dataset for nnU-Net.
- [x] Prepare SCI-Colorado dataset for nnU-Net.
- [x] Prepare canproco dataset for nnU-Net.
- [x] Merge + prepare Spine Generic, INSPIRED, canproco, SCI-Colorado datasets into one nnunet dataset.
- [x] Clean script to merge datasets + add doc.
- [x] Run nnunet preprocessing on Spine Generic.
- [x] Run nnunet preprocessing on SCI-Colorado.
- [x] Run nnunet preprocessing on INSPIRED.
- [x] Reorient to RPI and resample data and labels for canproco.
- [x] Run nnunet preprocessing on canproco.
- [x] Reorient to RPI data and labels Basel-mp2rage
- [x] Run nnunet preprocessing on merged dataset.
- [x] Train single model on SCI-Colorado.
- [x] Train single model on INSPIRED.
- [x] Train single model on Spine Generic.
- [x] Train single model on canproco.
- [x] Train large nnunet on merged dataset - 1600 -> 2000+ epochs instead of 1k -> could not converge.
- [x] Test all models on INSPIRED.
- [x] Test all models on SCI-Colorado
- [x] Test all models on Spine Generic
- [x] Test all models on canproco
- [x] Test all models on Basel-mp2rage
- [ ] Build qualitative and quantitative analysis notebook.
- [ ] Work on presentation.

(TO DO JUNE 9)
- [x] Clean code.
- [x] Improve documentation to reproduce everything.
- [x] Write project report.
- [x] Finish README for using the script
- [x] Finish README for the whole project recap.
- [x] Implement below additions to the README
- [x] Use of open-science best practices: Expectation: the project uses 3 open-science tools learnt during week 1, or provides a convincing reason to not use them. The 3 tools may be selected in the following list, but other relevant tools will be accepted too. -Git-GitHub-Containers -Python-BIDS-Jupyter notebooks-Binder
- [x] Skills and technologies learnt Expectation: the project uses 1 skill, method or technology learnt by the student during the school, through formal presentations or informal interactions. The skill, method or technology may be selected in the following list, but other relevant ones will be accepted too. -Machine learning -Multivariate statistics and matrix factorizations -Estimation of connectivity -High-performance computing -DataLad
- [x] Project relevance: Expectation: the project is relevant to brain/CNS imaging data analysis.
- [x] Clarity Expectation: the README/presentation is easy to follow, and supported by convincing material (e.g., images, diagrams, text, graphs).
- [x] Highly reproducible project (0-1)
- [ ] Technological achievement (0-1)
- [x] Exciting presentation (0-1)
- [ ] Nice brain picture (0-1)