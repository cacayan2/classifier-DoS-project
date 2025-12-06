# Group Members and Names
## Class: COMP 479; Dr. Manar Mohaisen Fall 2025
- **Emil Cacacayan**
    + LUC UID: ecacayan
    + LUC Student ID: 00001521140
- **Umar Siddiqui**
    + LUC UID: usiddiqui1
    + LUC Student ID: 00001519781
- **Nafisa Sabir**
    + LUC UID: nsabir
    + LUC Student ID: 00001729292
- **Fnu Syed Moosa Aleem "Moosa"**
    + LUC UID: fsyedmoosaaleem
    + LUC Student ID: 00001704732

# 1. Executive Summary and Project Goals
The goal of this project is to design, train, and evaluate machine learning classifiers that distinguish DoS (denial of service) attacks from benign traffic in the CIC-IDS2017 dataset using Wednesday traffic. DoS attacks are a robustly documented threat in cybersecurity, and there are many tools deployed on the market designed to detect and intervene such attacks. DoS attacks aim to overwhelm some network or service by sending unusually high volumes of traffic or exploiting weaknesses in the protocol, preventing users from accessing the system, hence denial of service (Kumar, Singh, & Sharma, 2020). The motivation for detecting such attacks is primarily financially and security driven: attacks can disrupt business operations and issues with client privacy, and detecting them promptly is a problem with practical and logistical implications.

This project aims to emulate as closely as possible the machine learning project paradigm introduced in COMP 479, including ETL, exploratory data analysis, preprocessing, model training, evaluation, and deployment of the best performing model as an API service. Although we may dwell on the semantics regarding the technical components, at a very high level the overall purpose is to demonstrate a test-driven, well-documented, and collaborative approach for first identifying harmful traffic problems and at large implementing, testing, and deploying machine learning models. This design is tailored (both by design by our instructor and within the group) to represent how ML models may be developed and deployed in an enterprise setting. The documentation is created in such a way that stakeholders, data engineers, and machine learning developers understand motivation, workflow, and results.

This dataset we are utilizing to both train and test the models were obtained from a well-known intrusion detection benchmark which was ultimately designed to emulate real network behavior. It contains labeled activity (benign and categories of DoS attacks) (Sharafaldin, Lashkari, & Ghorbani, 2018). Due to the rapidly evolving nature of cyberattacks, these benchmarks are mostly useful for the sake of demonstration in academic and instructional environments where labeled data is needed to experiment and develop models. 

Technically speaking, the goal of this project is to build a classification system that can distinguish between normal network traffic and different types of DoS attacks. To this end, we follow these steps:
- Loading and validating raw data
- Standardizing column names and formats
- Cleaning and transforming data into a consistent format
- Exploring relationships and distributions of features
- Training a several classification models
- Evaluating model performance, and lastly
- Preparing the best model for deployment

At each step, we document decision-making and justifications and emphasize the latter. This ADR (Architectural Decision Record) structure ensures that every design choice is explained in appropriate context and justified accordingly. This makes the project transparent and increases maintainability and potability of any code/choices we make, while allowing others to follow reasoning behind each step closely.

From an economic perspective, detecting these attacks ultimately support business goals. Especially for businesses that offer online services, being unable to provide these services can cause major losses in revenue and customer trust. In practice, abstraction of many of the ideas discussed in machine learning development (and vice-versa to machine learning engineers) are not required to be understood by business owners and other clients, but as stated earlier the interest comes from the more abstract outcomes - systems that are able to reliably flag traffic as suspicious. Such a tool can help guide manual investigations - something made more robust with structured analysis and careful handling of datasets. This reinforces the need for thoughtful data engineering choices and practices in such applications. 

From a cybersecurity perspective, detecting DoS attacks offers quite a few benefits. The ability to identify such attacks early can help limit service interruptions and reduce impact of an attack. Secondly, recognizing different types of activity allows security teams to design interventions more specifically (Rauf et al., 2021). Thirdly, collecting and analyzing traffic data helps networks establish a baseline and compare with future data to determine if a traffic flow contains the fingerprint of malicious transfers. 

Another important project goal is clear communication and collaboration. This is a group project, and so early on in the project design, expertise and interest were expressed by the members of the group. This repository's structure, project board, and communication expectations are designed to help the team maintain organization while ensuring that deliverables are submitted in a timely manner. Each notebook or script serves a purpose, and every team member is expected to record any findings, developments, or decisions in a shared and visible format. This reinforces the way collaboration is performed in the real world where teams coordinate across parts of an even larger workflow. 

Finally, we want to develop our tools and deployment in a way that fosters reproducibility, maintainability, and code potability. In this project, we also outline a schema file describing the final structure of the cleaned dataset so that both end-users and developers forking off the project can apply the same manipulations to their own datasets consistently. This is essential for maintaining reliable data pipelines in production-level environments (Breck et al., 2019). Even though our project does not involve full production deployment, preparing an API skeleton and defining data requirements is a fundamental part of this development process and helps reinforce all previously mentioned points.

The project goals can be divided into 5 parts:
1. Build an end-to-end and well-documented pipeline for detecting adverse network traffic.
2. Demonstrate collaborative best practices and defining clear roles, structured documentation, and clear lines of communication.
3. Produce interpretable results that help understand the data/ML engineering relevance and the data-driven patterns underlying denial of service attacks.
4. Prepare a foundation for a deployable system.
5. Prioritize clarity over speed and complexity so that the final product is easily evaluated by both the team and outside audience.

# 2. Data Sources
## 2.1 Context and Technology Choice
The primary data source for this project is a publicly available intrusion detection dataset developed by the Canadian Institute for Cybersecurity (CIC). The dataset is available on the following website: https://www.unb.ca/cic/datasets/ddos-2019.html and contains labeled network traffic representing normal activity as well as several different types of cyberattacks (the main focus being DoS attacks). This dataset was generated using realistic traffic patterns and controlled attack scenarios in order to capture the behavior of true network systems (Sharafaldin et al., 2018).

The reason for selecting this dataset is twofold - the first is that it is widely recognized within the realms of cybersecurity and intrusion detection as a high-quality benchmark (Ring et al., 2019). In addition, attack classes outlined by the assignment include GoldenEye, Hulk, slowhttptest, slowloris, and Heartbleed allow for a more heterogeneous exploration of binary classification. For this assignment, the data was provided in a few different formats (`.csv`, `.json`, `.parquet`) so that we had the opportunity to demonstrate different loading techniques and practice with ETL while utilizing different file types.

## 2.2 Justifications
This dataset is appropriate for the goals of the project for a few reasons:

1. **The dataset is highly relevant for modern DoS behavior**

This dataset includes many different types of DoS attacks along with different strategies, which actually line up pretty well with the descriptions about how DoS attacks have evolved over time (Kumar et al., 2020).

2. **Acceptance of the dataset as a benchmark within cybersecurity and machine learning research**

A few surveys identify this dataset and the rest of its family (CIC-IDS) as one of the more commonly used and meticulously designed options for experimentation (Ring et al., 2019). This allows for our work to be easily comparable with other similar research projects.

3. **Availability of labels**

This dataset includes well-defined labels for every type of traffic - this lends itself to supervised learning and allows for easier evaluation of our models.

4. **Practical for ETL**

Because the dataset is fairly large and the files provided to us are quite diverse, it provides an environment for demonstrating real data engineering tasks. 

5. **Alignment with assignment requirements**

Although this is self-explanatory, it's important to note - this is the dataset outlined specifically by the project requirements. 

## 2.3 Status
**Status**: Accepted
**Date**: November 26, 2025
**Team Members**: Emil Cacayan, Umar Siddiqui, Nafisa Sabir, Fnu Syed Moosa Aleem "Moosa"

# 3. Data Integration (Extract)
## 3.1 Context and Technology Choice
The goal of the integration/extract phase of this project is to bring together the raw files provided (a collection of `.csv`, `.parquet`, and `.json` files) from the aforementioned CICIDS dataset and load the files into memory so they can be further digested by univariate and multivariate exploratory data analysis and subsequent model training and testing. To this end we utilized Python libraries with data loading tools (mainly `pands.read_csv()`, `json.load()`, and `pyarrow.parquet.read_table()`). 

This extraction was coded into the script `etl/load_files.py` and documented in `notebooks/00_etl_exploration.ipynb`. The preprocessed data was saved into `data/interm/combined_raw.csv`. This represents the data that will be used for remaining downstream analyses/applications.

This process follows ETL processes generally use for most ML applications and the model introduced in class involving the processing of raw data from multiple sources and unifying into a single dataframe or data representation that is preserved prior to subsequent cleaning or data transformation. 

## 3.2 Justifications
Python and its libraries allow for a paradigm that lends itself to big data processing and machine learning applications. The tools outlined in the context and techonology section allowed us to stitch together different data sources into a single dataset that matches the intended structure of the dataset. In particular, the `pandas` module contains different modules that have been well-documented and tested for its ability to handle, merge, and concatenate large structured datasets. Integrating the data into a single file allows for consistent data representation in downstream applications and serves as a checkpoint so that any transformations of the dataset can be traced/rolled back to this intermediate state. 

## 3.3 Status
**Status**: Accepted
**Date**: November 29, 2025
**Team Members**: Nafisa Sabir (designated ETL lead), agreed upon with Emil Cacayan, Umar Siddiqui, and Fnu Syed Moosa Aleem "Moosa"

# 4. Data Transformation (Transform)
## 4.1 Context and Technology Choice
In the transformation step, the data was cleaned and standardized to increase fidelity and reproducibility of downstream transformations and training. This process includes dropping unnecessary (such as index) columns or duplicates, implementing consistent column naming patterns, and filtering out particular labels (in this case, `Heartbleed` was filtered out due to not being a DoS attack, which models downstream will be trained to discriminate). 

All of these operations are performed in the script `etl/clean_dataset.py` and documented in `notebooks/00_etl_exploration.ipynb`. This cleaned dataset is saved in `data/cleaned/wednesday_clean.csv`, the naming is due to the fact that this dataset (theoretically) contains label from Wednesday traffic, since the Wednesday traffic flows contain the labels required for training our model. Lastly, to ensure this classification task remains binary and not categorical, the different DoS attacks were encoded to binary 0/1 (representing benign or attack respectively). 

In other words,

$\text{Label}(\text{Wednesday}) \in \{\text{DoS GoldenEye}, \text{DoS Hulk}, \text{DoS slowloris}, \text{DoS Heartbleed}, \text{Benign}\}$


## 4.2 Justifications
This step is necessary because the raw dataset contains inconsistent column naming conventions across the different file types - testing of this dataset resulted in the failure of downstream processes (creation of duplicate columns, etc.). This could also result in ambiguous columns/features. In addition, numeric fields load as objects/strings - to ensure that transformations can be applied to these numeric features, some must be directly typecastd to float/integer data types. In addition, this assignment is a binary classification task for detecting denial of service attacks - because `Heartbleed` is not a DoS attack, it must be removed, and the remaining features must be encoded to fit the binary classification task. Abstracting this task in code is required for reproducibility internally within the team and with end clients, users, or developers.

## 4.3 Status
**Status**: Accepted
**Date**: November 29, 2025
**Team Members**: Nafisa Sabir (designated ETL lead), agreed upon with Emil Cacayan, Umar Siddiqui, and Fnu Syed Moosa Aleem "Moosa"

# 5. Data Storage (Load)
## 5.1 Context and Technology Choice
## 5.2 Justifications
## 5.3 Status

# 6. Reading Data
## 6.1 Context and Technology Choice
## 6.2 Justifications
## 6.3 Status

# 7. Exploratory Data Analysis
## 7.1 Context and Technology Choice
The purpose of univariate exploratory data analysis (EDA) is to understand distributional properties of features in a dataset prior to exploring relationships between two variables (bivariate analysis) or across multiple features (multivariate analysis). This step identifies inconsistencies, anomalies, outliers, and sources of bias - ensuring that downstream transformations and training rely on robust, meaningful, and interpretable features. Network intrusion often exhibit skewed numerical distributions, heavy-tailed traffic features, or artifact that is inherently present from the somewhat inconsistent sampling of traffic data (i.e. we must address missingness), it is essential that features be examined early and independently prior to building classification models (Ring et al., 2019). 

Our team utilized Python, Jupyter notebooks, the Python module `pandas`, `numpy`, and `matplotlib`/`seaborn` for variety of univariate EDA related tasks. These tools were chosen because of their efficiency in processing big data, intuitive visualization capability, and historically being well-documented and tested. All analysis for this stage is stored in the notebook `notebooks/01_univariate_eda.ipynb` and the cleaned dataset used in this analysis can be found in `data/cleaned/wednesday_clean.csv`. 

## 7.2 Justifications
As mentioned previously, univariate EDA is essential for later preprocessing and modeling decisions for the following reasons:

1. **Identification of Outliers**

Many network traffic features demonstrated having very long-tailed distributions - particularly the features having to do with flow duration, packet counts, and byte rates. Univariate EDA assists in identifying outliers that could distort scaling, central tendency statistics, or cause unstable model behavior. Our professor recommended use of the interquartile range method (IQR) for outlier detection and filtering, which we utilized.

2. **Detection of Low-Variance or Zero-Variance Features**

As many academics in statistics courses and papers have stated in the past, variance is information. Features with minimal variance provide little information of utility to a classifier and should be removed or at the very least deprioritized for modeling. Methods such as k-nearest neighbors or SVM's are not robust to features with low or zero-variance particularly when scaling is applied. 

3. **Verification of Data Types and Statistical Properties**

Summary statistics (central tendency such as mean and median and dispersion such as standard deviation and range) were computed to ensure fidelity was not lost for features originally in object type following conversion to numeric. This step is important as occasionally datasets network contain malformed numerical fields with artifact stemming from improper structering, formatting, or invalid characters (Sharafaldin et al., 2018). 

4. **Detection of Skewed Distributions**

Highly imbalanced features should be scaled or transformed and may require adjustments in evaluation approaches. Skew is common in these types of datasets because benign behavior dominates most distributions (Kumar et al., 2020).

5. **Preparation for Downstream EDA and Modeling**
These preliminary evaluations help inform which features may later require special handling during normalization, standardization, transformation, feature selecction, or modeling. This is generally accepted to be machine learning best practice, which emphasize detection of anomalies and artifact to reduce error propogation (Huyen, 2022). 

## 7.3 Status
**Status**: Accepted
**Date**: December 1, 2025
**Team Members**: Fnu Syed Moosa Aleem "Moosa" (histogram and boxplot generation, outlier detection), Umar Siddiqui (summary statistics, low-variance feature identification, skew investigation), Nafisa Sabir (assisted Moosa with figure saving and summarizing outliers)

# 8. Data Preprocessing
## 8.1 Context and Technology Choice
## 8.2 Justifications
## 8.3 Status

# 9. Feature Engineering
## 9.1 Context and Technology Choice
## 9.2 Justifications
## 9.3 Status

# 10. Processed Data Loading
## 10.1 Context and Technology Choice
## 10.2 Justifications
## 10.3 Status

# 11. Model Selection and Training
## 11.1 Context and Technology Choice
## 11.2 Justifications
## 11.3 Status

# 12. Model Evaluation
## 12.1 Context and Technology Choice
## 12.2 Justifications
## 12.3 Status

# 13. Model Deployment
## 13.1 Context and Technology Choice
## 13.2 Justifications
## 13.3 Status

# 14. Concluding Remarks and Project Summary
## 14.1 Context and Technology Choice
## 14.2 Justifications
## 14.3 Status

# 15. References
Breck, E., Polyzotis, N., Roy, S., Whang, S. E., & Zinkevich, M. (2019). Data validation for machine learning. In Proceedings of Machine Learning and Systems 1 (pp. 1–16). MLSys. proceedings.mlsys.org

Huyen, C. (2022). Designing machine learning systems: An iterative process for production-ready applications. O'Reilly Media. 

Kumar, P., Singh, A., & Sharma, R. (2020). Denial-of-Service attacks and their mitigation techniques: A survey. International Journal of Network Security, 22(4), 634–648.

Rauf, I., Petre, M., Tun, T., Lopez, T., Lunn, P., Van der Linden, D., Towse, J., Sharp, H., Levine, M., Rashid, A., & Nuseibeh, B. (2021). The case for adaptive security interventions. ACM Transactions on Software Engineering and Methodology, 31(1), Article 9. https://doi.org/10.1145/3471930

Ring, M., Wunderlich, S., Scheuring, D., Grüdl, D., Landes, D., & Hotho, A. (2019). A survey of network-based intrusion detection data sets. Computers & Security, 86, 147–167. 

Sharafaldin, I., Lashkari, A. H., & Ghorbani, A. A. (2018). Toward generating a new intrusion detection dataset and intrusion traffic characterization. ICISSP 2018—Proceedings of the 4th International Conference on Information Systems Security and Privacy, 108–116. https://doi.org/10.5220/0006639801080116 
