# Basic Keras code for Alexnet and VGG-16
## Here you can use these nets as feature extractors for images.
The codes hosted here were used for my masters degree project. Here, these neural networks were used for feature extraction from images. Each net was trained on images sourced from VEDAI dataset for aerial imagery. The end result is a neural net to identify vehicles from aerial imagery.
Current work serves as a precursor to a proprietary automated vehicle detection system for aerial imagery.
## Neural nets for feature extraction
Convolutional neural nets are higly powerful image classifiers, that distinguish images based on common characteristics of images  belonging to same class. They do this by extracting feature maps of these images and tuning their weights accordingly. 

Andrej Karpathy's tutorial is a good read to get in depth understanding of CNNs. It can be found here: http://cs231n.github.io/

These feature maps can be used to train external classifiers like Support Vector Machines and Random Forest. Relevance of such an approach is when there is insufficient data to train neural nets. Scarcity of data could lead the net to over-fit. Such a situation could be avoided by above mentioned approach.

Here VGG-16 net and Alexnet can be used to extract features.
## Details of included files.
