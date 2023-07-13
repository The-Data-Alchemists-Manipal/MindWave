
package net.coobird.thumbnailator.resizers.configurations;

import net.coobird.thumbnailator.resizers.ProgressiveBilinearResizer;


public enum ScalingMode {
	/**
	 * A hint to use bilinear interpolation when resizing images.
	 */
	BILINEAR,
	
	/**
	 * A hint to use bicubic interpolation when resizing images.
	 */
	BICUBIC,
	
	/**
	 * A hint to use progressing bilinear interpolation when resizing images.
	 * <p>
	 * For details on this technique, refer to the documentation of the
	 * {@link ProgressiveBilinearResizer} class.
	 */
	PROGRESSIVE_BILINEAR,
	;
}
