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

summary: "My idea is to train a deep learning model on multiple (3) spinal cord segmentation datasets to improve generalizability to new contrasts, vendors, pathologies, ...

My project aims to train the nnU-Net model architecture, a state-of-the-art deep learning architecture for biomedical segmentation, on three aggregated datasets and compare its generalizability capabilities with specific models trained on each dataset. I will conclude by comparing the two approaches on a fourth dataset outside of the training domain."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "cover_image.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Spinal cord segmentation is the process of annotating the spinal cord area in MRI images. This is clinically relevant notably to compute cross-sectional area for the diagnosis and monitoring of neurodegenerative diseases such as multiple sclerosis.

Performing automatic spinal cord segmentation is complicated even with deep learning methods due to the wide range of MRIs that can be produced from various contrasts, machine vendors and pathologies of the patient. This results in very different output images that no model can handle yet.

Typically, we use one model per data sub-set, like a specific contrast, and end up with N models where we select the optimal model for new images. This is not reliable and scalable.

My goal is to build a more general model to automatically perform spinal cord segmentation across contrasts, vendors and pathologies.

### Tools

Main tools: Python/Pytorch/Git/ssh/Jupyter Notebooks

Most important: nnU-Net -> a state-of-the-art “self-configuring method for deep learning-based biomedical image segmentation”.

### Methodology
Train and compare 2 frameworks (individual models vs. general model) for performing automatic spinal cord segmentation.

### Data

Various (4) Spinal Cord MRI datasets at Neuropoly with available manual segmentation.

Including:

* Spine Generic Public Database* (multi-subject), n=244, 3 vendors, 6 contrasts, pathology: Mild Compression, Healthy Controls.
* Basel-mp2rage, n=283, 1 contrast, pathology: Multiple Sclerosis (180), Healthy Controls (103).
* INSPIRED, n=79, 5 contrasts, pathology: Degenerative Cervical Myelopathy (38), Spinal Cord Injury, Healthy Controls.
* SCI-Colorado, n=80, 2 contrasts, pathology: Spinal Cord Injury.
Multiple contrasts, conditions, vendors… 👍

**Cohen-Adad, J., Alonso-Ortiz, E., Abramovic, M., Arneitz, C., Atcheson, N., Barlow, L., Barry, R.L., Barth, M., Battiston, M., Büchel, C., et al.: Open-access quantitative mri data of the spinal cord and reproducibility across participants, sites and manufacturers. Scientific data 8(1), 219 (2021)*

### Objectives

* Create a script for converting N BIDS datasets into one large “nnU-Net-ready” dataset train/test split.
* Compare a general model to specific models for spinal cord segmentation on the datasets’ test sets.
* Test the resulting 2 frameworks on a fourth dataset to demonstrate the generalizability capabilities of the larger model.

### Deliverables

* A Github repository with codes and scripts to reproduce training and testing.
* A jupyter notebook of the analysis codes and visualisations for comparing the results.
* Documentation.
* Model checkpoints for the nnUnet models trained on all 3 datasets.

## Results

### Progress overview

The project was initiated by Louis-François Bouchard, based on the existing BrainHack template. I will start from existing scripts for the nnU-Net method and adapt them for my needs.

### Tools I learned during this project

 * **TODO** TODO
 * **TODO-** TODO
 * **TODO** TODO

### Results

#### Deliverable 1: TODO

TODO

#### Deliverable 2: TODO

TODO

## Conclusion and acknowledgement

TODO

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
- [ ] Train large nnunet on merged dataset - 1600 -> 2000+ epochs instead of 1k -> could not converge.
- [x] Test all models on INSPIRED.
- [x] Test all models on SCI-Colorado
- [x] Test all models on Spine Generic
- [x] Test all models on canproco
- [x] Test all models on Basel-mp2rage
- [ ] Build qualitative and quantitative analysis notebook.
- [ ] Work on presentation.

(TO DO JUNE 9)
- [ ] Clean code.
- [ ] Improve documentation to reproduce everything.
- [ ] Write project report.
- [ ] Finish README for using the script
- [ ] Finish README for the whole project recap.
- [ ] Implement below additions to the README
- [ ] Use of open-science best practices: Expectation: the project uses 3 open-science tools learnt during week 1, or provides a convincing reason to not use them. The 3 tools may be selected in the following list, but other relevant tools will be accepted too. -Git-GitHub-Containers -Python-BIDS-Jupyter notebooks-Binder
- [ ] Skills and technologies learnt Expectation: the project uses 1 skill, method or technology learnt by the student during the school, through formal presentations or informal interactions. The skill, method or technology may be selected in the following list, but other relevant ones will be accepted too. -Machine learning -Multivariate statistics and matrix factorizations -Estimation of connectivity -High-performance computing -DataLad
- [ ] Project relevance: Expectation: the project is relevant to brain/CNS imaging data analysis.
- [ ] Clarity Expectation: the README/presentation is easy to follow, and supported by convincing material (e.g., images, diagrams, text, graphs).
- [ ] Highly reproducible project (0-1)
- [ ] Technological achievement (0-1)
- [ ] Exciting presentation (0-1)
- [ ] Nice brain picture (0-1)