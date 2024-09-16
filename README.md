# Machine Learning Meets Omics: Explainable AI Strategies for Omics Data Analysis

Due to the increasing amount of publicly available omics datasets we nowadays have the unique opportunity to integrate omics datasets from multiple sources into large-scale omics datasets. The complexity and size of those datasets typically requires an analysis with machine learning (ML) algorithms. The increasing interest in using ML for omics data analysis comes along with the need for education on how to train and interpret the results of such ML models. Especially, since complex supervised ML models are often considered to be “Black Boxes”, offering limited insight into how their outputs are derived.

In this tutorial, we will use the Google Collaboratory environment and Python programming language to showcase how to train, optimize and evaluate a ML classifier on large-scale omics datasets and how to subsequently apply state-of-the-art XAI methods to dissect the model’s output. We will illustrate ML best practices and coding principles in a hands-on session on a transcriptomics dataset using sklearn and other relevant Python package. We will further dive into important aspects of model training like hyperparameter optimization or validation strategies for multi-source datasets. Additionally, we will discuss common pitfalls when applying XAI methods, ensuring that the participants not only gain technical proficiency but also a critical perspective on the interpretability of ML models in scientific research. We will conclude the tutorial with a practical session where the participants will get the opportunity to apply their learnings to the transcriptomics dataset or their own dataset.

For the practical sessions we will use a publicly available datasets that comes along with a reference publication: Warnat-Herresthal, S. et al. (2020). https://doi.org/10.1016/j.isci.2019.100780

## Schedule

|  Time | Session  | Duration  |
|---|---|---|
| 13:00 – 13:30 | ML Best-Practices for Omics Data | 30 min|
| 13:30 – 13:40 | Introduction to eXplainable AI (XAI) | 10 min|
| 13:40 – 14:30 | Interpretation with Model-Agnostic XAI Methods | 50 min|
| 14:30 – 15:00 | Coffee Break | 30 min|
| 15:00 – 15:30 | Interpretation with Model-Specific XAI Methods | 30 min| 
| 15:30 – 16:15 | XAI Best-Practices for Omics Data | 45 min|

## Venue

Location: Radisson Blu Marina Palace Hotel, 
Address: Linnankatu 32, 20100 Turku.

**Note for attendees:** Please bring your own laptop for the tutorial. Basic knowledge of Python and access to google collab is required to actively participate in the hands-on sessions. For participants without access to google collab, we will provide a requirements file at the beginning of the tutorial for installation of required packages.


## Speaker

- Lisa Barros de Andrade e Sousa ([lisa.barros@helmholtz-munich.de](mailto:lisa.barros@helmholtz-munich.de))
- Elisabeth Georgii ([elisabeth.georgii@helmholtz-munich.de](mailto:elisabeth.georgii@helmholtz-munich.de))
- Till Richter 
- Fatemeh Hashemi 


## Requirements and Setup

It is possible to either create an environment and install all the necessary packages locally (using the requirements.txt file) or to execute the notebooks on the browser, by clicking the 'Open in Colab' button. This second option doesn't require any further installation, but the user must have access to a Google account.

If you prefer to run the notebooks on your device, create a virtual environment using the requirements.txt file:
```
conda create -n xai python=3.11
conda activate xai
pip install -r requirements.txt
```

Once your environment is created, clone `ECCB-2024` brach branch of the repo using the following command:

```
git clone --branch ECCB-2024 https://github.com/HelmholtzAI-Consultants-Munich/XAI-Tutorials.git
```

## Contributions

Comments and input are very welcome! If you have a suggestion or think something should be changed, please open an issue or submit a pull request. 
