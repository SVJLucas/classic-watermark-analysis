# Putting Pixels to the Test: Evaluating the Power and Pitfalls of Traditional Frequency Domain Watermarking

# Summary

- [Conclusion](#Conclusion)
- [Introduction and Motivation](#IntroductionandMotivation)

# Introduction and Motivation

In the digital age, watermarking has emerged as a crucial technique for copyright protection, authentication, and ensuring the integrity of digital media. "Putting Pixels to the Test: Evaluating the Power and Pitfalls of Traditional Frequency Domain Watermarking" delves into the resilience and vulnerabilities of conventional frequency domain watermarking methods. Through a meticulous comparison of Discrete Cosine Transform (DCT) [1,2,3], Discrete Wavelet Transform (DWT) [4,5,6], and the combination of Discrete Wavelet Transform with Singular Value Decomposition (DWT+SVD) [7,8], this analysis sheds light on how these techniques fare when faced with various image manipulation attacks. From subtle noise additions to aggressive geometric transformations, we explore the effectiveness of each watermarking strategy in preserving the hidden watermark's integrity. This exploration not only highlights the technological prowess of these methods in safeguarding digital assets but also exposes their limitations, offering invaluable insights into the complex landscape of digital watermarking.

# Watermarking using the Galaxy10 DECals Dataset

In this study, we delve into the realm of digital watermarking. Our focus lies on an image derived from the green-band of a galaxy, selected from the esteemed Galaxy10 DECals dataset [9]. The Galaxy10 DECals dataset is an extensive collection of galaxy images, gathered through the Dark Energy Camera Legacy Survey (DECals). This dataset stands out for its comprehensive representation of various galaxy morphologies, captured with high resolution and precision.

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/cb3874aa-2976-473d-a082-9316078dc927" alt="Green-Band from one galaxy of the Galaxy10 DECals Dataset" width="250px"/>
</p>
<p align="center"><b>Figure 1</b>: Image to be Watermarked</p>

To evaluate the robustness and invisibility of our watermarking approach, we introduce simple binary watermark image. This process not only underscores the technical prowess required to manipulate images within the frequency domain but also highlights the potential for watermarking in safeguarding and authenticating digital media within scientific datasets.


<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/35ce3879-7e2d-4330-bdca-5c021dc85a5d" alt="Watermark" width="250px"/>
</p>
<p align="center"><b>Figure 2</b>: Watermark</p>

#  Considered Attacks

Assessing the resilience of watermarking algorithms involves simulating a variety of conditions to test their robustness. These tests include manipulating image orientation, introducing visual noise, and varying image visibility through cropping, scaling, and blurring. Additionally, the algorithms are challenged with changes in brightness and contrast to evaluate their performance under different lighting and exposure conditions. 

- **Rotation Attack Test**:The Rotation Attack Test evaluates an algorithm's tolerance to orientation changes by rotating images by a random angle within a specified range (e.g., -5 to 5 degrees). This simulates real-world variations in camera angle or object orientation, challenging the algorithm's ability to recognize rotated objects without loss of accuracy.

- **Noise Test**: The Noise Test assesses an algorithm's robustness against visual noise by adding Gaussian noise with a random standard deviation to images. This mimics sensor noise or low-light conditions, testing the algorithm's capability to maintain performance despite the presence of random pixel value fluctuations.

- **Crop Ratio Test**: The Crop Ratio Test determines the impact of partial visibility on algorithm performance by cropping a random percentage of the image's border and resizing it back to the original dimensions. This simulates scenarios where objects are partially occluded or outside the camera's field of view.

- **Resize Scale Test**: The Resize Scale Test investigates the algorithm's resilience to scale variations by resizing images by a random scale factor and then resizing back to original dimensions. It mimics real-world conditions of objects appearing larger or smaller due to changes in distance to the camera.

- **Gaussian Blur Test**: The Gaussian Blur Test examines an algorithm's ability to handle images with reduced sharpness by applying Gaussian blur with a random intensity. This simulates motion blur or out-of-focus conditions, challenging the algorithm's capacity to recognize blurred objects.

- **Brightness Test**: The Brightness Test evaluates how changes in image brightness affect an algorithm's performance by adjusting the brightness with a random value within a specified range. This test simulates variations in lighting conditions, from underexposure to overexposure.

- **Contrast Test**: The Contrast Test assesses the effect of contrast adjustments on an algorithm's accuracy by modifying the contrast of images with a random factor. This simulates conditions with varying levels of contrast, testing the algorithm's ability to discern objects against backgrounds with minimal to significant contrast differences.

Each attack provides insight into specific aspects of algorithm robustness, highlighting vulnerabilities and areas for improvement in handling real-world image variations.

# Transformations and Post-Attack Extraction Visualizations

## Discrete Cossine Transform (DCT)

The process leverages the DCT to convert image data from the spatial domain to the frequency domain. This transformation facilitates the manipulation of specific frequency components to embed a watermark—a set of alterations imperceptible to the human eye but detectable algorithmically.

### Embedding Watermarks

1. **DCT Application**: The image is divided into blocks, and the DCT is applied to each block, transforming the image from the spatial domain to the frequency domain. The equation for the 2D DCT is given by:
   
   $F(u,v) = \frac{1}{4} C(u) C(v) \sum_{x} \sum_{y} f(x,y) \cos\left[\frac{(2x+1)u\pi}{2M}\right] \cos\left[\frac{(2y+1)v\pi}{2N}\right]$

   where:
   - $F(u,v)$ is the DCT coefficient at frequencies $u$ and $v$,
   - $f(x,y)$ is the pixel intensity in the spatial domain,
   - $M$ and $N$ are the dimensions of the image block,
   - $C(u)$ and $C(v)$ are normalization factors.

2. **Watermark Embedding**: The watermark is embedded by modifying specific DCT coefficients according to the watermark data. This alteration is scaled by a factor $\alpha$ to control the visibility and robustness of the watermark.

3. **Inverse DCT**: The inverse DCT is applied to the modified coefficients to transform the data back to the spatial domain, resulting in a watermarked image.

### Extracting Watermarks

1. **DCT on Original and Watermarked Images**: The DCT is applied to both the original and the watermarked images to obtain their frequency domain representations.

2. **Watermark Extraction**: The watermark is estimated by calculating the difference between the DCT coefficients of the watermarked and the original images, divided by the scaling factor $\alpha$. This difference highlights the alterations made during the watermark embedding process.

3. **Binarization**: The estimated watermark is then binarized to produce the final watermark data, distinguishing between watermarked and non-watermarked components based on a threshold.

### Post-Attack Extraction of Image Watermarks

Here, we present a comparison of the various watermarks extracted after subjecting the watermarked images to different types of attacks:

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/d831595b-1185-4282-8f6d-a5102eeaeab8" alt="Results for DCT" height="1800px" />
</p>
<p align="center"><b>Figure 3</b>: Post-Attack Extraction of Image Watermarks for DCT</p>

## Discrete Wavelet Transform (DWT)

DWT decomposes an image into a set of wavelet coefficients, representing different frequency bands within the image. These coefficients are divided into approximate (low-frequency) and detail (high-frequency) components. For watermarking, modifications are typically made to the approximate component to maintain image quality while embedding the watermark.

### Embedding Watermarks

1. **DWT Application**: The image is decomposed using DWT into four sub-bands: LL (low-low), LH (low-high), HL (high-low), and HH (high-high). The LL sub-band represents the approximate image, while the other three capture details in various orientations.

2. **Watermark Embedding**: The watermark is embedded into the LL sub-band by adding a scaled version of the watermark to it. This scaling is controlled by a factor $\alpha$, which adjusts the strength of the watermarking to balance visibility and robustness.

3. **Inverse DWT**: The inverse DWT (IDWT) is applied to the modified and unmodified sub-bands to reconstruct the watermarked image.

### Extracting Watermarks

1. **DWT on Original and Watermarked Images**: Both the original and the watermarked images are decomposed using DWT to obtain their respective wavelet coefficients.

2. **Watermark Extraction**: The difference between the LL sub-bands of the watermarked and original images, divided by $\alpha$, estimates the watermark. This difference highlights the changes made to the approximate component during embedding.

3. **Normalization and Thresholding**: The estimated differences are normalized to a 0-1 range, and a threshold is applied to binarize the estimated watermark, distinguishing watermarked areas from the rest of the image.
   
### Post-Attack Extraction of Image Watermarks

Here, we present a comparison of the various watermarks extracted after subjecting the watermarked images to different types of attacks:

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/ed2417a0-673c-4f86-bfa9-5f708482eec5" alt="Results for DWT" height="1800px" />
</p>

<p align="center"><b>Figure 4</b>: Post-Attack Extraction of Image Watermarks for DWT</p>

## Discrete Wavelet Transform (DWT) + SVD

The process combines the spatial-frequency decomposition capabilities of DWT with the mathematical robustness of SVD. DWT decomposes the image into frequency sub-bands, and SVD is applied to the approximate sub-band to embed the watermark. The singular values of this sub-band are modified according to the watermark's singular values, providing a subtle yet effective embedding method.

### Embedding Watermarks

1. **DWT Application**: The image is decomposed using DWT into sub-bands: LL, LH, HL, HH. The LL sub-band represents the low-frequency components, which are less sensitive to changes and ideal for watermarking.

2. **SVD on LL Sub-band**: SVD decomposes the LL sub-band into matrices U, S, and V, where S contains the singular values. SVD is known for its stability and the fact that small changes in singular values do not significantly affect image quality.

3. **Watermark Embedding**: The singular values of the LL sub-band are altered by adding a scaled version of the watermark's singular values. This scaling factor, denoted by $\alpha$, controls the embedding strength.

4. **Inverse Operations**: The modified LL sub-band is reconstructed using inverse SVD, followed by applying inverse DWT to obtain the watermarked image. The watermarked image maintains high visual similarity to the original while containing the embedded watermark.

### Extracting Watermarks

1. **DWT and SVD on Watermarked and Original Images**: The original and watermarked images are decomposed using DWT, followed by SVD on their respective LL sub-bands.

2. **Watermark Extraction**: The difference in singular values between the watermarked and original LL sub-bands, divided by $\alpha$, estimates the watermark's singular values. This process inversely mirrors the embedding method.

3. **Reconstruction of Watermark**: Utilizing the estimated singular values along with the U and V matrices from the watermark's SVD (stored during embedding), the watermark is reconstructed. The result is then thresholded to obtain a binary watermark image.

### Post-Attack Extraction of Image Watermarks

Here, we present a comparison of the various watermarks extracted after subjecting the watermarked images to different types of attacks:

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/e9c57d78-ae17-4d0b-93d8-4f47afb474f7" alt="Results for DWT+SVD" height="1800px" />
</p>

<p align="center"><b>Figure 5</b>: Post-Attack Extraction of Image Watermarks for DWT+SVD</p>

# Metrics, Results and Discussion

The results from the tables bellow [Table 1, Table 2, Table 3] reveal interesting insights into the performance of Discrete Cosine Transform (DCT), Discrete Wavelet Transform (DWT), and Discrete Wavelet Transform combined with Singular Value Decomposition (DWT+SVD) under various image manipulation scenarios. Notably, even without any attacks, the DWT+SVD method does not achieve perfect normalized correlation (NC) or a zero bit error rate (BER), unlike DCT and DWT. This deviation could be attributed to the inherent properties of SVD, which, when applied after DWT, introduces a layer of complexity in accurately capturing and reconstructing the watermark's singular values. SVD focuses on capturing the essence of the watermark in a few singular values, which might not perfectly align with the original watermark, especially when the watermark is binary.

### NC (Normalized Correlation) Results [Table 1]

| Test                   | DCT          | DWT          | DWT+SVD      |
|------------------------|--------------|--------------|--------------|
| No Attack              | **1.0000**   | **1.0000**   | 0.9006       |
| Rotation Attack Test   | 0.3991       | **0.4475**   | 0.0000       |
| Noise Test             | 0.4997       | **0.9659**   | 0.9049       |
| Crop Ratio Test        | 0.3979       | 0.5105       | **0.8522**   |
| Resize Scale Test      | 0.4069       | 0.5717       | **0.8616**   |
| Gaussian Blur Test     | 0.5266       | **0.7787**   |   0.0000     |
| Brightness Test        | 0.7039       | **0.8418**   |   0.7016     |
| Contrast Test          | 0.5482       | 0.5166       | **0.7907**   |

Across the different tests, DWT consistently outperforms DCT and DWT+SVD in terms of resilience to noise, with a significantly higher NC and lower BER in the noise test. This illustrates DWT's capability to maintain watermark integrity even in the presence of significant noise, likely due to its multi-resolution analysis that effectively separates image components into different frequency bands. DWT+SVD shows strengths in handling crop and resize attacks better than DCT, as indicated by higher NC values in these scenarios. This suggests that the combination of wavelet transform and SVD provides a robust framework against geometric transformations, likely due to the more stable watermark embedding in singular values that are less sensitive to such changes. However, the DWT+SVD method's vulnerability to rotation and Gaussian blur attacks, as evidenced by the NC dropping to 0, highlights a potential weakness in maintaining watermark integrity under these specific conditions.

### BER (Bit Error Rate) Results [Table 2]

| Test                   | DCT          | DWT          | DWT+SVD      |
|------------------------|--------------|--------------|--------------|
| No Attack              | **0.0000**   | **0.0000**   | 0.0749       |
| Rotation Attack Test   | 0.4972       | 0.4884       | **0.3671**   |
| Noise Test             | 0.4495       | **0.0225**   |   0.0711     |
| Crop Ratio Test        | 0.4986       | 0.3957       |   0.1212     |
| Resize Scale Test      | 0.4961       | 0.6663       | **0.1112**   |
| Gaussian Blur Test     | 0.4332       | **0.2933**   |   0.3671     |
| Brightness Test        | 0.3232       | 0.2458       | **0.1546**   |
| Contrast Test          | 0.4230       | 0.4623       | **0.1221**   |

The DCT method shows moderate resilience across all tests but generally performs worse than DWT and DWT+SVD in handling geometric transformations and noise. This can be attributed to DCT's nature of concentrating signal energy, which makes it less effective in distinguishing between the original and altered components after such attacks. On the other hand, the DWT method's superior performance in the Gaussian blur test underscores its effectiveness in dealing with blurring, a common issue in image processing. The mixed performance of DWT+SVD across different tests, with particular strengths in resize scale and contrast adjustments, underlines the importance of choosing the right watermarking technique based on the expected types of attacks or manipulations an image might undergo. Overall, each method has its strengths and weaknesses, with DWT excelling in noise resilience, DWT+SVD showing promise against geometric transformations, and DCT offering a balanced performance across a range of tests.


### FPR (False Positive Rate) Results [Table 3]

| Test                   | DCT          | DWT          | DWT+SVD      |
|------------------------|--------------|--------------|--------------|
| No Attack              | **0.0000**   | **0.0000**   | 0.1104       |
| Rotation Attack Test   | 0.4962       | 0.5430       | 0.0672       |
| Noise Test             | 0.4996       | **0.0218**   | 0.1048       |
| Crop Ratio Test        | 0.4977       | 0.3958       | **0.1786**   |
| Resize Scale Test      | 0.5008       | 0.9804       | **0.1630**   |
| Gaussian Blur Test     | 0.4975       | 0.4318       | **0.0672**   |
| Brightness Test        | 0.4676       | 0.3603       | **0.1077**   |
| Contrast Test          | 0.4996       | 0.4926       | **0.1247**   |

# Conclusion

Our exploration into the application of traditional frequency domain watermarking techniques has illuminated both the potential and the limitations of current methodologies. The study's findings underscore the necessity for tailored approaches that consider the unique characteristics of the content being protected. Through testing against various attacks, we have identified key strengths and vulnerabilities inherent to Discrete Cosine Transform (DCT), Discrete Wavelet Transform (DWT), and the hybrid DWT+SVD methods, paving the way for future advancements in digital watermarking technology. This endeavor not only contributes to the field of digital image processing but also enhances the security and integrity of data.


# References

[1]  M. Rafigh, M.E. Moghaddam, A robust evolutionary based digital image watermarking technique in DCT domain, in: 2010 Seventh International Conference on Computer Graphics, Imaging and Visualization, IEEE, 2010, pp. 105–109.

[2] R. Mehta, N. Rajpal, V.P. Vishwakarma, Adaptive image watermarking scheme using fuzzy entropy and GA-ELM hybridization in DCT domain for copyright protection, J. Signal Process. Syst. 84 (2) (2016) 265–281.

[3] Adrian G Bors and Ioannis Pitas, “Image watermarking using dct domain constraints,” in ICIP, 1996

[4] Xiang-Gen Xia, Charles G Boncelet, and Gonzalo R Arce, “Wavelet transform based watermark for digital images,” Optics Express, 1998.

[5] C. Agarwal, A. Mishra, A. Sharma, Gray-scale image watermarking using GA-BPN hybrid network, J. Vis. Commun. Image Represent. 24 (7) (2013) 1135–1146.

[6] M. Ali, C.W. Ahn, An optimal image watermarking approach through cuckoo search algorithm in wavelet domain, Int. J. Syst. Assur. Eng. Manag. 9 (3) (2018) 602–611.

[7] N.R. Zhou, A.W. Luo, W.P. Zou, Secure and robust watermark scheme based on multiple transforms and particle swarm optimization algorithm, Multimedia Tools Appl. 78 (2) (2019) 2507–2523

[8] V. Verma, V.K. Srivastava, F. Thakkar, DWT-SVD based digital image watermarking using swarm intelligence, in: 2016 International Conference on Electrical, Electronics, and Optimization Techniques (ICEEOT), IEEE, 2016, pp. 3198–3203

[9] Henry W. Leung and Jo Bovy. Deep learning of multi-element abundances from high-resolution spectroscopic data. MNRAS, 483(3):3255–3277, March 2019. doi: 10.1093/mnras/sty3217.
