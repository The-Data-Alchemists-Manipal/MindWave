

package net.coobird.thumbnailator.filters;

import java.awt.image.BufferedImage;


public class SwapDimensions implements ImageFilter {
	private static final SwapDimensions INSTANCE = new SwapDimensions();
	private SwapDimensions() {}

	public static SwapDimensions getInstance() {
		return INSTANCE;
	}

	public BufferedImage apply(BufferedImage img) {
		return img;
	}
}
