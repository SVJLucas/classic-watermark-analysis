from scipy.fftpack import dct, idct
import numpy as np

class DiscreteCosineTransform:
    """
    A class for embedding and extracting watermarks in images using the Discrete Cosine Transform (DCT) method.
    This technique involves transforming image blocks into the frequency domain using DCT,
    modifying specific coefficients to embed the watermark, and then performing an inverse DCT to reconstruct the watermarked image.
    """

    def __init__(self, alpha: float = 0.01):
        """
        Initializes the DiscreteCosineTransform object, setting up its key parameters.

        Args:
            alpha (float, optional): A scaling factor used to control the strength of the watermark embedding.
                                      Values closer to 0 result in less visible watermarks,
                                      while values closer to 1 lead to more robust but potentially more noticeable watermarks.
                                      Defaults to 0.1 for a balance between visibility and robustness.
        """
        self.alpha = alpha
        self.watermark_size_is_same_size_image = True
        self.name = 'Discrete Cosine Transform (DCT)'

    def _dct2(self, a):
        """
        Performs a 2-dimensional Discrete Cosine Transform (DCT-II) on an input array.

        Args:
            a: The input array to be transformed.

        Returns:
            The 2D DCT-II transformed array.

        Utilizes the `dct` function from SciPy for efficient DCT computation.
        Applies DCT twice, first along rows and then along columns, for a 2D transformation.
        Specifies `norm='ortho'` to ensure orthogonality of the DCT basis vectors.
        """
        return dct(dct(a.T, norm='ortho').T, norm='ortho')

    def _idct2(self, a):
        """
        Performs a 2-dimensional Inverse Discrete Cosine Transform (IDCT-II) on an input array.

        Args:
            a: The input array to be inverse transformed.

        Returns:
            The 2D IDCT-II transformed array.

        Utilizes the `idct` function from SciPy for efficient IDCT computation.
        Applies IDCT twice, first along rows and then along columns, for a 2D inverse transformation.
        Specifies `norm='ortho'` to ensure orthogonality of the IDCT basis vectors.
        """
        return idct(idct(a.T, norm='ortho').T, norm='ortho')


    def encode(self, image: np.ndarray, watermark: np.ndarray, key: int = 42) -> np.ndarray:

        """
        Embeds a watermark into a grayscale image using Discrete Cosine Transform.

        Args:
            image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the image.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            watermarked_image (np.ndarray): A numpy array of the same shape as image with the watermark embedded.
            watermark (np.ndarray): A numpy array of the same shape as image with integers (each 0 or 1) representing the watermark to be embedded.

        Raises:
            ValueError: If the shape of the image and watermark do not match, or if the watermark contains values other than 0s and 1s.
        """

        if image.shape != watermark.shape:
            raise ValueError("Image and watermark must have the same shape.")

        # Apply DCT to the image block
        dct_block = self._dct2(image)

        # Insert the watermark by modifying DCT coefficients
        dct_block_watermarked = dct_block + self.alpha * watermark

        # Apply inverse DCT to get the watermarked image back in spatial domain
        watermarked_image = self._idct2(dct_block_watermarked)

        return watermarked_image, watermark

    def decode(self, original_image: np.ndarray, watermarked_image: np.ndarray, key: int = 42) -> np.ndarray:

        """
        Extracts the watermark from a watermarked image by Discrete Cosine Transform.

        Args:
            original_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the original image.
            watermarked_image (np.ndarray): A numpy array of integers (0-255) representing the pixel values of the watermarked image.
            key (int): The seed used during encoding, allowing for the reconstruction of the modified pixel positions.

        Returns:
            extracted_watermark (np.ndarray): A numpy array indicating the estimated watermark, represented by changes in specific pixels.
        """
        # Apply DCT to both original and watermarked images
        dct_original = self._dct2(original_image)
        dct_watermarked = self._dct2(watermarked_image)

        # Estimate the watermark by calculating the difference in the DCT domain
        estimated_dct_watermark = (dct_watermarked - dct_original) / self.alpha

        # Binarize the estimated watermark
        extracted_watermark = np.clip(np.round(estimated_dct_watermark),0,1)

        return extracted_watermark
