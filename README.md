# 5_Data_Preparation_for_Machine_Learning

The data need to be prepared before going into the machine learning algorithms. 

# Table of content

1. [One-Hot Encoding](#1)
2. [Label Encoder](#2)


<a name="1"></a>
# One-Hot Encoding
One of these data preparation techniques is **One-Hot Encoding**. It is defined as a process by which categorical variables are converted into a form that could be provided to machine elarning algorithms to do a better job in prediction [1]. One-hot encoding works pretty well when variables take less than 15 different values [2]. One-hot encoding generates new binary columns for each category. Only one column in each row can take a value of 1 and the remaining columns in each row take a value of zero (Fig. 1). Therefore, it is named One-Hot Encoding.

![2](https://user-images.githubusercontent.com/54812742/138953327-2c20d4b8-90a4-4b08-a70a-fd47dfc83047.PNG)

Fig. 1: The way One-hot encoding works [2] 

To demonstrate the necessity to apply One-Hot Encoding, the data from the 4th week of Machine Learning class, offered by Prof. Andrew Ng from Stanford University, was used. In this dataset, which is a subset of MNIST handwritten digit dataset (http://yann.lecun.com/exdb/mnist/), the data are in the form of a native Octave matrix format. These data are the images of the handwritten digits (20 by 20 by 1) along with their labels, indicating the corresponding digits. The images are unrolled and so presented in the form of a vector with 400 elements. The labels, stored in y variable, are in the form of the following when imported through loadmat from scipy into Python:

![1](https://user-images.githubusercontent.com/54812742/138951805-0478932d-ee4d-41bb-9864-ee6035bda8fc.PNG)

Fig. 2: Labels indicating the digit shown in every image 

The labels are from 1 to 10. 10 is assigned to number 0 (to prevent confusion in Octave indexing), while the rest i.e., 1 to 9 are consistently labeled through 1 to 9. These data first needs to be One-Hot-Encoded. To do so, the to_categorical from tensorflow.keras.utils can be used to generate the following data, which is ready to go into the machine learning algorithm:

![4](https://user-images.githubusercontent.com/54812742/138960789-889119b7-0e24-4c9c-b99a-f588fc94ddef.PNG)

Fig. 3: One-Hot Encoded labels

<a name="2"></a>
# Label Encoder



References:

[1] https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f

[2] https://www.kaggle.com/dansbecker/using-categorical-data-with-one-hot-encoding
