# Recommender System with Attention (LAB 4)

## Overview
This repository contains the code and resources for a university assignment focused on building a recommender system using deep learning techniques, specifically exploring attention mechanisms within the NeuMF (Neural Matrix Factorization) model. 

## Authors
- Alessandro Viviani 843234
- Francesca Arredondo 820354
- Fabio Turchetta 898572

## Project Structure
- `Assignment_Viviani_Arredondo_Turchetta.ipynb`: Main Jupyter notebook containing code, explanations, and results. It includes:
  - Data loading and preprocessing
  - Implementation of NeuMF with attention
  - Experiments, evaluation, and discussion
  - Comparative notes on alternative architectures designed by team members
- `References/`: Contains key research papers on recommender systems, collaborative filtering, and attention mechanisms.

## Main Features
- Implementation of a NeuMF-based recommender system with attention layers
- Comparative analysis of different architectural variants
- Data handling for the MovieLens dataset (100k and 1M supported)
- Evaluation metrics and visualization of results

## Requirements
- Python 3.x
- Jupyter Notebook
- PyTorch
- NumPy
- Pandas
- Matplotlib

Install requirements using pip (if needed):
```bash
pip install torch numpy pandas matplotlib
```

## Usage
1. Download or clone this repository:
   ```bash
   git clone <repo-url>
   ```
2. Open `Assignment_Viviani_Arredondo_Turchetta.ipynb` in Jupyter Notebook or Google Colab.
3. Follow the notebook to:
   - Mount Google Drive (if using Colab)
   - Download and preprocess the MovieLens dataset
   - Train and evaluate the NeuMF model with attention
   - Review results and analysis

## References
Key papers included in the `References/` folder:
- Deep Collaborative Recommendation Algorithm Based on.pdf
- Neural Collaborative Filtering.pdf
- Recommender systems Deep Recommendations.pdf
- Yudan Liu.pdf

## Notes
- The notebook is designed for educational purposes and demonstrates the application of attention in recommender systems.
- Only one full implementation (Viviani's) is shown; the other team members' designs are discussed in comments.

## License
This project is for academic use only. Please cite the original authors and referenced papers if using this work.
