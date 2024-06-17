# Stability of circumbinary planets
A model that predicts the orbital stability of circumbinary planets using Machine Learning fits to N-body simulations.

The N-body simulations explore systems with a variety of binary and planetary mass ratios, binary and planetary eccentricities from 0 to 0.9 and orbital mutual inclinations ranging from 0 to 180 degrees. Planetary masses range between the size of Mercury and 13 Jupiter masses.

The trained machine learning models are based on XGBRegressor.

Included as pickle files are 4 trained models, corresponding to the inner and outer stability radius for low and high eccentricity planets. 

inference.py is a simple inference script. It loads the saved models, take input, and make prediction. 

For more information please check our paper:

https://arxiv.org/abs/2404.13746
