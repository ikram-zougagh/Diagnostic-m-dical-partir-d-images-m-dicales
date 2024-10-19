<div align="center">
    <h1 style="color: #2C3E50;">🔬 Medical Diagnosis from Medical Images</h1>
    <img src="https://example.com/your-logo.png" alt="Logo" width="200">
</div>

<p style="font-size: 16px; color: #34495E;">
    This project aims to apply <strong>deep learning</strong> techniques for the analysis and classification of MRI (Magnetic Resonance Imaging) images of the brain, specifically to detect and classify brain tumors. The project leverages <strong>Convolutional Neural Networks (CNN)</strong> as well as pre-trained models like <strong style="color: #E74C3C;">VGG16</strong> and <strong style="color: #E74C3C;">VGG19</strong> to improve diagnostic accuracy.
</p>

<h2 style="color: #2980B9;">🎯 Objectives</h2>

<p style="color: #34495E;">
    The main objective is to develop a model capable of:
</p>
<ul>
    <li style="color: #27AE60;"><strong>Detecting anomalies</strong> in brain MRI images.</li>
    <li style="color: #27AE60;"><strong>Classifying brain tumors</strong> according to their type (gliomas, meningiomas, etc.).</li>
    <li style="color: #27AE60;">Providing a <strong>user interface</strong> via a web application to allow submission of MRI images and receive automatic diagnostics.</li>
</ul>

<h2 style="color: #2980B9;">🔍 Approach</h2>

<p style="color: #34495E;">
    The project uses three main models to achieve its objectives:
</p>
<ol>
    <li style="color: #2980B9;"><strong>Convolutional Neural Networks (CNN)</strong> to train a model from scratch.</li>
    <li style="color: #2980B9;"><strong>VGG16</strong> and <strong>VGG19</strong>, two pre-trained models, to take advantage of optimized deep neural network architectures.</li>
</ol>

<h3 style="color: #8E44AD;">1. CNN (Convolutional Neural Networks)</h3>
<p style="color: #34495E;">
    The CNN model was specifically designed for this project from the ground up. Here are the key steps:
</p>
<ul>
    <li><strong>Convolution</strong>: Extracting important features from MRI images.</li>
    <li><strong>MaxPooling</strong>: Reducing dimensionality while preserving relevant information.</li>
    <li><strong>Fully Connected Layers</strong>: Classifying tumors based on the extracted features.</li>
</ul>

<h3 style="color: #8E44AD;">2. Pre-trained Models: VGG16 and VGG19</h3>
<p style="color: #34495E;">
    To enhance performance and leverage models already optimized on millions of images, we utilized the <strong>VGG16</strong> and <strong>VGG19</strong> models:
</p>
<ul>
    <li><strong>VGG16</strong>: A deep neural network model consisting of 16 layers. It is used to extract complex features from MRI images. This model was fine-tuned with the training data from this project.</li>
    <li><strong>VGG19</strong>: Similar to VGG16, but with 19 layers, providing a deeper architecture capable of extracting even finer details from MRI images.</li>
</ul>

<h4 style="color: #E67E22;">Fine-tuning the VGG Models</h4>
<p style="color: #34495E;">
    We applied <strong>transfer learning</strong> by reusing the pre-trained convolutional layers of the VGG16 and VGG19 models, adjusting only the final layers to fit our tumor classification task. This technique speeds up training while improving results.
</p>

<h2 style="color: #2980B9;">📊 Dataset</h2>
<p style="color: #34495E;">
    The project uses a public dataset consisting of brain MRI images, classified into several categories based on tumor type. The images are divided into three sets:
</

