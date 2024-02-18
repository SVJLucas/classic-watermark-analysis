import numpy as np
import pywt
import scipy.linalg as la

class DiscreteWaveletTransformSVD:
    def __init__(self, wavelet='haar', alpha=0.1):
        """
        Initializes the DWT+SVD watermarking object with the specified wavelet and alpha.

        Args:
            wavelet (str): The name of the wavelet to be used in DWT and IDWT.
            alpha (float): Scaling factor used for modifying the singular values during watermark embedding.
        """
        self.wavelet = wavelet
        self.alpha = alpha
        self.Uw,self.Vw = (None, None)
        self.watermark_size_is_same_size_image = False
        self.name = 'Discrete Wavelet Transform (DWT) + SVD'

    def encode(self, image: np.ndarray, watermark: np.ndarray, key: int = 42) -> np.ndarray:
        """
        Embeds a watermark into an image using DWT followed by SVD.

        Args:
            image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the image.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            watermarked_image (np.ndarray): A numpy array of the same shape as image with the watermark embedded.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.
        """
        # Perform DWT on the image
        coeffs = pywt.dwt2(image, self.wavelet)
        LL, (LH, HL, HH) = coeffs

        # Perform SVD on the LL sub-band
        U, s, V = la.svd(LL, full_matrices=False)

        # Perform SVD on the watermark
        self.Uw, sw, self.Vw = la.svd(watermark, full_matrices=False)
        # Modify the singular values of LL with those of the watermark
        s_marked = s + self.alpha * sw[:len(s)]

        # Reconstruct the LL sub-band with modified singular values
        LL_marked = np.dot(U, np.dot(np.diag(s_marked), V))

        # Perform inverse DWT to get the watermarked image
        watermarked_image = pywt.idwt2((LL_marked, (LH, HL, HH)), self.wavelet)
        watermarked_image = np.clip(watermarked_image, 0, 255).astype(np.uint8)

        return watermarked_image, watermark

    def decode(self, original_image: np.ndarray, watermarked_image: np.ndarray, key: int = 42) -> np.ndarray:
        """
        Extracts the watermark from a watermarked image using Discrete Wavelet Transform + SVD method.

        Args:
            original_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the original image.
            watermarked_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the watermarked image.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            extracted_watermark (np.ndarray): A numpy array indicating the estimated watermark, represented by changes in specific pixels.
        """
        # Decompose both images using DWT
        coeffs_original = pywt.dwt2(original_image, self.wavelet)
        LL_original, _ = coeffs_original
        coeffs_watermarked = pywt.dwt2(watermarked_image, self.wavelet)
        LL_watermarked, _ = coeffs_watermarked

        # Perform SVD on both LL sub-bands
        U_original, s_original, V_original = la.svd(LL_original, full_matrices=False)
        U_watermarked, s_watermarked, V_watermarked = la.svd(LL_watermarked, full_matrices=False)

        # Estimate the singular values of the watermark
        sw_estimated = (s_watermarked - s_original) / self.alpha

        extracted_watermark = np.dot(self.Uw, np.dot(np.diag(sw_estimated), self.Vw))

        # Normalize the differences to a 0-1 range
        estimated_differences_normalized = (extracted_watermark - np.min(extracted_watermark)) / (np.max(extracted_watermark) - np.min(extracted_watermark))

        threshold = 0.5
        extracted_watermark = np.where(estimated_differences_normalized > threshold, 255, 0)

        return extracted_watermark
