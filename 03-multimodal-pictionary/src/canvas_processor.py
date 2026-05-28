import numpy as np
from PIL import Image

def normalize_canvas_image_layers(raw_canvas_image: np.ndarray) -> Image.Image:
    """Extracts raw stroke streams and strips alpha-channel transparency noise for visual optimization."""
    # Split layer matrices
    rgba_array = np.array(raw_canvas_image)
    
    # Isolate alpha values transparency data mask
    alpha_channel = rgba_array[:, :, 3]
    
    # Create target RGB structure canvas background map
    optimized_background = np.ones_like(rgba_array[:, :, :3]) * 255
    
    # Overlay strokes securely onto clean, solid white matrix coordinates
    mask = alpha_channel > 0
    optimized_background[mask] = rgba_array[:, :, :3][mask]
    
    # Compile safe operational image stream wrapper container
    return Image.fromarray(optimized_background.astype('uint8'), 'RGB')
