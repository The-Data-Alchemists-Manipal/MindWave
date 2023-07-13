
package net.coobird.thumbnailator.filters;

import java.awt.image.BufferedImage;

public interface ImageFilter {
	/**
	 * Applies a image filtering operation on an image.
	 * 
	 * @param img		The image to apply the filtering on.
	 * @return			The resulting image after applying this filter.
	 */
	public BufferedImage apply(BufferedImage img);
}
