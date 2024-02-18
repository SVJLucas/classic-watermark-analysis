import numpy as np
import pywt

class DiscreteWaveletTransform:
    def __init__(self, alpha: float = 0.1, wavelet='haar'):
        """
        Initializes the DiscreteWaveletTransform object with the specified wavelet.

        Args:
            alpha (float, optional): A scaling factor used to control the strength of the watermark embedding.
                                      Values closer to 0 result in less visible watermarks,
                                      while values closer to 1 lead to more robust but potentially more noticeable watermarks.
                                      Defaults to 0.1 for a balance between visibility and robustness.
            wavelet (str): The name of the wavelet to be used in DWT and IDWT.
        """
        self.wavelet = wavelet
        self.alpha = alpha
        self.watermark_size_is_same_size_image = False
        self.name = 'Discrete Wavelet Transform (DWT)'

    def encode(self, image: np.ndarray, watermark: np.ndarray, key: int = 42) -> np.ndarray:
        """
        Embeds a watermark into a grayscale image using Discrete Wavelet Transform.

        Args:
            image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the image.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            watermarked_image (np.ndarray): A numpy array of the same shape as image with the watermark embedded.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.
        """
        # Check dimensions
        if image.shape[0] //2 != watermark.shape[0] and image.shape[1] //2 != watermark.shape[1]:
            raise ValueError("Watermark dimensions: half image width x half image height")

        # Decompose the image using DWT
        coeffs = pywt.dwt2(image, self.wavelet)
        LL, (LH, HL, HH) = coeffs

        # Embed the watermark into the LL sub-band
        LL_marked = LL + self.alpha * watermark

        # Reconstruct the image with the embedded watermark
        watermarked_image = pywt.idwt2((LL_marked, (LH, HL, HH)), self.wavelet)

        return watermarked_image, watermark

    def decode(self, original_image: np.ndarray, watermarked_image: np.ndarray, key: int = 42) -> np.ndarray:
        """
        Extracts the watermark from a watermarked image using Discrete Wavelet Transform.

        Args:
            original_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the original image.
            watermarked_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the watermarked image.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            extracted_watermark (np.ndarray): A numpy array indicating the estimated watermark, represented by changes in specific pixels.
        """
        # Decompose both original and watermarked images
        coeffs_original = pywt.dwt2(original_image, self.wavelet)
        coeffs_watermarked = pywt.dwt2(watermarked_image, self.wavelet)

        # Extract the LL sub-bands
        LL_original, _ = coeffs_original
        LL_watermarked, _ = coeffs_watermarked

        # Estimate the watermark from the difference between the LL sub-bands
        estimated_differences = (LL_watermarked - LL_original) / self.alpha

        # Normalize the differences to a 0-1 range
        estimated_differences_normalized = (estimated_differences - np.min(estimated_differences)) / (np.max(estimated_differences) - np.min(estimated_differences))

        # Apply a threshold to convert to binary (0 and 1) values
        threshold = 0.5  # This threshold may need adjustment based on your specific use case
        estimated_watermark = np.where(estimated_differences_normalized > threshold, 1, 0)

        return estimated_watermark
