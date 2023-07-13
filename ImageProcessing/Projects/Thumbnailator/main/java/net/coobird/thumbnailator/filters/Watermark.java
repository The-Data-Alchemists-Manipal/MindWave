

package net.coobird.thumbnailator.filters;

import java.awt.AlphaComposite;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.image.BufferedImage;

import net.coobird.thumbnailator.builders.BufferedImageBuilder;
import net.coobird.thumbnailator.geometry.Position;


public class Watermark implements ImageFilter {
	
	private final Position position;
	
	
	private final BufferedImage watermarkImg;
	
	/**
	 * The opacity of the watermark.
	 */
	private final float opacity;

	/**
	 * The insets for the watermark.
	 */
	private final int insets;

	/**
	 * Instantiates a filter which applies a watermark to an image.
	 * 
	 * @param position			The position of the watermark.
	 * @param watermarkImg		The watermark image.
	 * @param opacity			The opacity of the watermark.
	 * 							<p>
	 * 							The value should be between {@code 0.0f} and
	 * 							{@code 1.0f}, where {@code 0.0f} is completely
	 * 							transparent, and {@code 1.0f} is completely
	 * 							opaque.
	 * @param insets			Inset size around the watermark.
	 * 							Cannot be negative.
	 */
	public Watermark(Position position, BufferedImage watermarkImg, float opacity, int insets) {
		if (position == null) {
			throw new NullPointerException("Position is null.");
		}
		if (watermarkImg == null) {
			throw new NullPointerException("Watermark image is null.");
		}
		if (opacity > 1.0f || opacity < 0.0f) {
			throw new IllegalArgumentException("Opacity is out of range of " +
					"between 0.0f and 1.0f.");
		}
		if (insets < 0) {
			throw new IllegalArgumentException("Insets cannot be negative.");
		}
		
		this.position = position;
		this.watermarkImg = watermarkImg;
		this.opacity = opacity;
		this.insets = insets;
	}

	/**
	 * Instantiates a filter which applies a watermark to an image.
	 *
	 * @param position			The position of the watermark.
	 * @param watermarkImg		The watermark image.
	 * @param opacity			The opacity of the watermark.
	 * 							<p>
	 * 							The value should be between {@code 0.0f} and
	 * 							{@code 1.0f}, where {@code 0.0f} is completely
	 * 							transparent, and {@code 1.0f} is completely
	 * 							opaque.
	 */
	public Watermark(Position position, BufferedImage watermarkImg, float opacity) {
		this(position, watermarkImg, opacity, 0);
	}

	public BufferedImage apply(BufferedImage img) {
		int width = img.getWidth();
		int height = img.getHeight();
		int type = img.getType();

		BufferedImage imgWithWatermark =
			new BufferedImageBuilder(width, height, type).build();
		
		int watermarkWidth = watermarkImg.getWidth();
		int watermarkHeight = watermarkImg.getHeight();

		Point p = position.calculate(
				width, height, watermarkWidth, watermarkHeight,
				insets, insets, insets, insets
		);

		Graphics2D g = imgWithWatermark.createGraphics();
		
		// Draw the actual image.
		g.drawImage(img, 0, 0, null);
		
		// Draw the watermark on top.
		g.setComposite(
				AlphaComposite.getInstance(AlphaComposite.SRC_OVER, opacity)
		);
		
		g.drawImage(watermarkImg, p.x, p.y, null);
		
		g.dispose();

		return imgWithWatermark;
	}
}
