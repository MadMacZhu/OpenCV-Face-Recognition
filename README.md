## 项目简介

这是一个在Python语言环境下，使用了OpenCV4和face_recognition两个库联手实现的一个项目，主要功能包括：人脸定位、比较与识别标识。具体代码展示见这个[Jupyter Notebook](https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Opencv%20Face%20Recognition.ipynb)。

## 功能简介：

这个项目实现的人脸识别功能本质上是基于实列（instance-based）而不是基于模型的（model-based）。face_recognition这个Python对象的两个重要方法是face_locations和face_encodings，可以帮助定位图片中的人脸位置和获得该人脸的一个128维编码。如下：

<img display="block" margin="auto" title="马云" alt="马云" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/Jack_Ma_Original.png" />

理论上来讲一张人脸只需要这一个编码，就可以实现这个项目的主要功能，包括：

**功能1**：人脸比较（用于判别是否为同一个人）

<img display="block" margin="auto" title="马云2" alt="马云2" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/Jack_Ma.png" />

<img display="block" margin="auto" title="马斯克" alt="马斯克" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/Elon_Musk.png" />

<img display="block" margin="auto" title="马化腾" alt="马化腾" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/Ma_Huateng.png" />

**功能2**：人脸标注（一旦识别成功，在图像中标注出人脸的位置和该人的名字）

<img display="block" margin="auto" title="马云3" alt="马云3" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/Jack_Ma2.png" />

**功能3**：视频标注（在视频中标注被识别出的人的名字，以及首次出现的时间点）

## 算法简介：

这个项目本质上是对这篇[文章](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)中提出的方法的一个具体实践。

图像的处理和识别共分4步，分别用到的算法为：

1. 人脸关键点（landmarks）的定位。

<img display="block" margin="auto" title="Will Farell" alt="Will Farell" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/will_farrel.jpeg" />

2. 人脸关键点的旋转矫正。

<img display="block" margin="auto" title="landmarks" alt="landmarks" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/facial_landmarks.png" />

3. 通过一个神经网络（DNN）获得人脸的编码（encoding）。

<img display="block" margin="auto" title="Will Farell" alt="Will Farell" width="500px" src="https://github.com/MadMacZhu/OpenCV-Face-Recognition/blob/master/Figures/encoding.png" />

4. 使用SVM对人脸进行分类，判别两张人脸图片是否为同一人。

