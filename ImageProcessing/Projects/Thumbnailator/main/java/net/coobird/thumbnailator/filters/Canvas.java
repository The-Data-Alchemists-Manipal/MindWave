

package net.coobird.thumbnailator.filters;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.image.BufferedImage;

import net.coobird.thumbnailator.builders.BufferedImageBuilder;
import net.coobird.thumbnailator.geometry.Position;


public class Canvas implements ImageFilter {
	
	private final int width;
	
	
	private final int height;
	
	
	private final Position position;
	
	private final Color fillColor;
	
	private final boolean crop;
	
	/**
	 * Instantiates a {@code Canvas} filter.
	 * <p>
	 * No fill color will be applied to the filtered image. If the image to
	 * filter does not have a transparency channel, the image will be filled
	 * black.
	 * <p>
	 * Crops the enclosed image if the enclosing image is smaller.
	 * 
	 * @param width			The width of the filtered image.
	 * @param height		The height of the filtered image.
	 * @param position		The position to place the enclosed image.
	 */
	public Canvas(int width, int height, Position position) {
		this(width, height, position, true, null);
	}
	
	/**
	 * Instantiates a {@code Canvas} filter.
	 * <p>
	 * No fill color will be applied to the filtered image. If the image to
	 * filter does not have a transparency channel, the image will be filled
	 * black.
	 * 
	 * @param width			The width of the filtered image.
	 * @param height		The height of the filtered image.
	 * @param position		The position to place the enclosed image.
	 * @param crop			Whether or not to crop the enclosed image if the
	 * 						enclosed image has dimensions which are larger than
	 * 						the specified {@code width} and {@code height}.
	 */
	public Canvas(int width, int height, Position position, boolean crop) {
		this(width, height, position, crop, null);
	}
	
	/**
	 * Instantiates a {@code Canvas} filter.
	 * <p>
	 * Crops the enclosed image if the enclosing image is smaller.
	 * 
	 * @param width			The width of the filtered image.
	 * @param height		The height of the filtered image.
	 * @param position		The position to place the enclosed image.
	 * @param fillColor		The color to fill portions of the image which is
	 * 						not covered by the enclosed image. Portions of the
	 * 						image which is transparent will be filled with
	 * 						the specified color as well.
	 */
	public Canvas(int width, int height, Position position, Color fillColor) {
		this(width, height, position, true, fillColor);
	}
	
	/**
	 * Instantiates a {@code Canvas} filter.
	 * 
	 * @param width			The width of the filtered image.
	 * @param height		The height of the filtered image.
	 * @param position		The position to place the enclosed image.
	 * @param crop			Whether or not to crop the enclosed image if the
	 * 						enclosed image has dimensions which are larger than
	 * 						the specified {@code width} and {@code height}.
	 * @param fillColor		The color to fill portions of the image which is
	 * 						not covered by the enclosed image. Portions of the
	 * 						image which is transparent will be filled with
	 * 						the specified color as well.
	 */
	public Canvas(int width, int height, Position position, boolean crop, Color fillColor) {
		super();
		this.width = width;
		this.height = height;
		this.position = position;
		this.crop = crop;
		this.fillColor = fillColor;
	}

	public BufferedImage apply(BufferedImage img) {
		int widthToUse = width;
		int heightToUse = height;
		
		/*
		 * To prevent cropping when cropping is disabled, if the dimension of
		 * the enclosed image exceeds the dimension of the enclosing image,
		 * then the enclosing image will have its dimension enlarged.
		 * 
		 */
		if (!crop && img.getWidth() > width) {
			widthToUse = img.getWidth();
		}
		if (!crop && img.getHeight() > height) {
			heightToUse = img.getHeight();
		}
		
		Point p = position.calculate(
				widthToUse, heightToUse, img.getWidth(), img.getHeight(),
				0, 0, 0, 0
		);
		
		BufferedImage finalImage = new BufferedImageBuilder(
				widthToUse,
				heightToUse,
				img.getType()
		).build();
		
		Graphics g = finalImage.getGraphics();
		
		if (fillColor == null && !img.getColorModel().hasAlpha()) {
			/*
			 * Fulfills the specification to use a black fill color for images
			 */
			g.setColor(Color.black);
			g.fillRect(0, 0, width, height);

		} else if (fillColor != null) {
			g.setColor(fillColor);
			g.fillRect(0, 0, widthToUse, heightToUse);
		}
		
		g.drawImage(img, p.x, p.y, null);
		g.dispose();
		
		return finalImage;
	}
}
