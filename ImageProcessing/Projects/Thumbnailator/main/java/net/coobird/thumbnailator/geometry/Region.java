

package net.coobird.thumbnailator.geometry;

import java.awt.Dimension;
import java.awt.Point;
import java.awt.Rectangle;


public final class Region {
	/**
	 * Position of the region.
	 */
	private final Position position;
	
	/**
	 * Size of the region.
	 */
	private final Size size;
	
	/**
	 * Instantiates a representation of a region from a {@link Position} and
	 * {@link Size}.
	 * 
	 * @param position		Position of the region.
	 * @param size			Size of the region.
	 * @throws NullPointerException		When the position and/or the size is
	 * 									{@code null}.
	 */
	public Region(Position position, Size size) {
		super();
		if (position == null) {
			throw new NullPointerException("Position cannot be null.");
		}
		if (size == null) {
			throw new NullPointerException("Size cannot be null.");
		}
		
		this.position = position;
		this.size = size;
	}
	
	/**
	 * Returns the position of the region.
	 * 
	 * @return 				Position of the region.
	 */
	public Position getPosition() {
		return position;
	}
	
	/**
	 * Returns the size of the region.
	 * 
	 * @return 				Size of the region.
	 */
	public Size getSize() {
		return size;
	}
	
	/**
	 * Calculates the position and size of the enclosed region, relative to the
	 * enclosing region.
	 * <p>
	 * The portions of the enclosed region which lies outside the enclosing
	 * region are ignored. Effectively, the {@link Rectangle} returned by this
	 * method is an intersection of the enclosing and enclose regions.
	 * 
	 * @param outerWidth		Width of the enclosing region.
	 * @param outerHeight		Height of the enclosing region.
	 * @param flipHorizontal	Whether enclosed region should flip
	 * 							horizontally within the enclosing region.
	 * @param flipVertical		Whether enclosed region should flip
	 * 							vertically within the enclosing region.
	 * @param swapDimensions	Whether the components of the point and
	 * 							dimension of the enclosed region should be
	 * 							swapped.
	 * @return					Position and size of the enclosed region.
	 */
	public Rectangle calculate(
			int outerWidth,
			int outerHeight,
			boolean flipHorizontal,
			boolean flipVertical,
			boolean swapDimensions
	) {
		Dimension innerDimension = size.calculate(outerWidth, outerHeight);

		Point innerPoint = position.calculate(
				outerWidth, outerHeight, innerDimension.width, innerDimension.height, 0, 0, 0, 0
		);

		if (swapDimensions) {
			innerDimension = new Dimension(innerDimension.height, innerDimension.width);
			innerPoint = new Point(innerPoint.y, innerPoint.x);
		}

		if (flipHorizontal) {
			int newX = outerWidth - innerPoint.x - innerDimension.width;
			innerPoint.setLocation(newX, innerPoint.y);
		}
		if (flipVertical) {
			int newY = outerHeight - innerPoint.y - innerDimension.height;
			innerPoint.setLocation(innerPoint.x, newY);
		}

		Rectangle outerRectangle = new Rectangle(0, 0, outerWidth, outerHeight);
		Rectangle innerRectangle = new Rectangle(innerPoint, innerDimension);

		return outerRectangle.intersection(innerRectangle);
	}

	/** 
	 * Returns a {@code String} representation of this region.
	 * 
	 * @return		{@code String} representation of this region.
	 */
	@Override
	public String toString() {
		return "Region [position=" + position + ", size=" + size + "]";
	}
}
