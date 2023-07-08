# Fake and Real Logo Detection 

Input is taken in the form of images, and the model classifies the logos to be either fake or real. SVM has been used. 

## Steps taken 

1) **Importing Necessary Libraries:** Libraries like NumPy, Tensorflow, sklearn, matplotlib, etc need to be imported.
2) **Training Data:** Making 80% split for training data.
3) **Conversion:** Converting Values to NumPy arrays.
4) **Scaling:** Scaling Values in the range of 0-1.
5) **Feature Extraction:** Flatten the Images to use them as features.
6) **SVM Model:** Training the SVM Model, and evaluating the model on validation and test set.
7) **Calculating scores and Confusion Matrix:** Calculate precision, recall, and F1 score for the predicted labels, along with building confusion matrix.
8) **Conversion:** Converting Labels to Categorical
9) **Plotting:** Plot the Training and Validation Loss.
10) **Classification Report:** Convert the predicted labels from one-hot encoding to integer encoding and get the classification report for the test data.
11) **Confusion Matrix:** Convert one-hot encoded labels back to integer labels and generate the confusion matrix.
