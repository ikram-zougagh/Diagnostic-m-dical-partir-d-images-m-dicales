<div align="center">
    <h1 style="color: #2C3E50;">🔬 Medical Diagnosis from Medical Images</h1>
    <img src="https://example.com/your-logo.png" alt="Logo" width="200">
</div>

<p style="font-size: 16px; color: #34495E;">
    This project aims to apply <strong>deep learning</strong> techniques for the analysis and classification of MRI (Magnetic Resonance Imaging) brain images, particularly to detect and classify brain tumors. The project utilizes <strong>convolutional neural networks (CNN)</strong> as well as pretrained models like <strong style="color: #E74C3C;">VGG16</strong> and <strong style="color: #E74C3C;">VGG19</strong> to enhance diagnostic accuracy.
</p>

<h2 style="color: #2980B9;">🎯 Objectives</h2>

<p style="color: #34495E;">
    The main objective is to develop a model capable of:
</p>
<ul>
    <li style="color: #27AE60;"><strong>Detecting anomalies</strong> in brain MRI images.</li>
    <li style="color: #27AE60;"><strong>Classifying brain tumors</strong> according to their type (gliomas, meningiomas, etc.).</li>
    <li style="color: #27AE60;">Providing a <strong>user interface</strong> via a web application to submit MRI images and receive an automatic diagnosis.</li>
</ul>

<h2 style="color: #2980B9;">🔍 Approach</h2>

<p style="color: #34495E;">
    The project employs three main models to achieve its objectives:
</p>
<ol>
    <li style="color: #2980B9;"><strong>Convolutional Neural Networks (CNN)</strong> to train a model from scratch.</li>
    <li style="color: #2980B9;"><strong>VGG16</strong> and <strong>VGG19</strong>, two pretrained models, to leverage deep and optimized neural network architectures.</li>
</ol>

<h3 style="color: #8E44AD;">1. CNN (Convolutional Neural Networks)</h3>
<p style="color: #34495E;">
    The CNN model was specifically designed for this project from the ground up. Here are the key steps:
</p>
<ul>
    <li><strong>Convolution</strong>: Extracting important features from MRI images.</li>
    <li><strong>MaxPooling</strong>: Reducing dimensions while preserving relevant information.</li>
    <li><strong>Fully Connected Layers</strong>: Classifying tumors based on the extracted features.</li>
</ul>

<h3 style="color: #8E44AD;">2. Pretrained Models: VGG16 and VGG19</h3>
<p style="color: #34495E;">
    To improve performance and benefit from models already optimized on millions of images, we utilized the <strong>VGG16</strong> and <strong>VGG19</strong> models:
</p>
<ul>
    <li><strong>VGG16</strong>: A deep neural network model with 16 layers. It is used to extract complex features from MRI images. This model was fine-tuned with the training data of this project.</li>
    <li><strong>VGG19</strong>: Similar to VGG16 but with 19 layers, offering a deeper architecture capable of capturing even finer details from MRI images.</li>
</ul>

<h4 style="color: #E67E22;">Fine-tuning VGG Models</h4>
<p style="color: #34495E;">
    We applied <strong>transfer learning</strong> by reusing the pretrained convolutional layers of the VGG16 and VGG19 models and adjusting only the last layers to fit our tumor classification task. This technique speeds up training while improving results.
</p>

<h2 style="color: #2980B9;">📊 Dataset</h2>
<p style="color: #34495E;">
    The project utilizes a public dataset consisting of brain MRI images, categorized into several categories based on tumor type. The images are divided into three sets:
</p>
<ul>
    <li><strong>Training</strong>: To adjust the model parameters.</li>
    <li><strong>Validation</strong>: To fine-tune hyperparameters and avoid overfitting.</li>
    <li><strong>Test</strong>: To evaluate the final performance of the model.</li>
</ul>

<h2 style="color: #2980B9;">📈 Results</h2>
<p style="color: #34495E;">
    The three models were compared based on several metrics such as accuracy, recall, and F1-score:
</p>
<ul>
    <li><strong>CNN</strong>: Achieved a baseline accuracy of around <strong>99.07%</strong> after several training iterations.</li>
    <li><strong>VGG16</strong>: Showed a significant improvement with an accuracy of <strong>98.13%</strong> due to the use of transfer learning.</li>
    <li><strong>VGG19</strong>: Slightly surpassed VGG16 with an accuracy of <strong>96.26%</strong>, thanks to its increased depth that allows it to capture more details in the images.</li>
</ul>

<h2 style="color: #2980B9;">🌐 Application</h2>
<p style="color: #34495E;">
    The project includes a <strong>web application</strong> developed in <strong>Flask</strong>, allowing users to submit MRI images and receive instant predictions. Users can upload an image, and the model returns a prediction regarding the type of detected tumor, providing a simple interface for doctors and researchers.
</p>

<h2 style="color: #2980B9;">📝 Conclusion</h2>
<p style="color: #34495E;">
    This project demonstrates the power of deep learning models, particularly through the use of <strong>CNN</strong>, <strong>VGG16</strong>, and <strong>VGG19</strong>, in medical diagnosis based on images. Utilizing pretrained models improved accuracy and reduced training time. This solution could be a useful tool for healthcare professionals to quickly detect brain tumors and enhance diagnostic precision.
</p>

