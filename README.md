# Putting Pixels to the Test: Evaluating the Power and Pitfalls of Traditional Frequency Domain Watermarking
Test &amp; compare classic watermarking techniques: LSB, Patchwork, DCT, DWT and DWT-SVD. Analyze strengths, weaknesses, robustness against attacks. Python code included

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/cb3874aa-2976-473d-a082-9316078dc927" alt="Green-Band from one galaxy of the Galaxy10 DECals Dataset" width="250px"/>
</p>

Green-Band from one galaxy of the Galaxy10 DECals Dataset[1]
# Transformations

## Discrete Cossine Transform
<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/4eba359f-f286-4303-96f2-b8e8ac6e91aa" alt="Results for DCT" height="1800px" />
</p>

## Discrete Wavelet Transform

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/5069de7e-b44a-4eff-811f-8b62da6b89e9" alt="Results for DWT" height="1800px" />
</p>

## Discrete Wavelet Transform + SVD

<p align="center">
  <img src="https://github.com/SVJLucas/classic-watermark-analysis/assets/60625769/5e7efff6-e0a6-4479-91e7-3741ece3df3d" alt="Results for DWT+SVD" height="1800px" />
</p>

# Results

The results from the tables bellow [Table 1, Table 2, Table 3] reveal interesting insights into the performance of Discrete Cosine Transform (DCT), Discrete Wavelet Transform (DWT), and Discrete Wavelet Transform combined with Singular Value Decomposition (DWT+SVD) under various image manipulation scenarios. Notably, even without any attacks, the DWT+SVD method does not achieve perfect normalized correlation (NC) or a zero bit error rate (BER), unlike DCT and DWT. This deviation could be attributed to the inherent properties of SVD, which, when applied after DWT, introduces a layer of complexity in accurately capturing and reconstructing the watermark's singular values. SVD focuses on capturing the essence of the watermark in a few singular values, which might not perfectly align with the original watermark, especially when the watermark is binary.

Across the different tests, DWT consistently outperforms DCT and DWT+SVD in terms of resilience to noise, with a significantly higher NC and lower BER in the noise test. This illustrates DWT's capability to maintain watermark integrity even in the presence of significant noise, likely due to its multi-resolution analysis that effectively separates image components into different frequency bands. DWT+SVD shows strengths in handling crop and resize attacks better than DCT, as indicated by higher NC values in these scenarios. This suggests that the combination of wavelet transform and SVD provides a robust framework against geometric transformations, likely due to the more stable watermark embedding in singular values that are less sensitive to such changes. However, the DWT+SVD method's vulnerability to rotation and Gaussian blur attacks, as evidenced by the NC dropping to 0, highlights a potential weakness in maintaining watermark integrity under these specific conditions.

The DCT method shows moderate resilience across all tests but generally performs worse than DWT and DWT+SVD in handling geometric transformations and noise. This can be attributed to DCT's nature of concentrating signal energy, which makes it less effective in distinguishing between the original and altered components after such attacks. On the other hand, the DWT method's superior performance in the Gaussian blur test underscores its effectiveness in dealing with blurring, a common issue in image processing. The mixed performance of DWT+SVD across different tests, with particular strengths in resize scale and contrast adjustments, underlines the importance of choosing the right watermarking technique based on the expected types of attacks or manipulations an image might undergo. Overall, each method has its strengths and weaknesses, with DWT excelling in noise resilience, DWT+SVD showing promise against geometric transformations, and DCT offering a balanced performance across a range of tests.

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


# References

1 - Henry W. Leung and Jo Bovy. Deep learning of multi-element abundances from high-resolution spectroscopic data. MNRAS, 483(3):3255–3277, March 2019. doi: 10.1093/mnras/sty3217.
