

package net.coobird.thumbnailator.geometry;

import java.awt.Dimension;


public class AbsoluteSize implements Size {
	
	private final Dimension size;
	
	/**
	 * Instantiates an object which indicates size of an object.
	 * 
	 * @param size		Size of the enclosed object.
	 * @throws NullPointerException		If the size is {@code null}.
	 */
	public AbsoluteSize(Dimension size) {
		if (size == null) {
			throw new NullPointerException("Size cannot be null.");
		}
		this.size = new Dimension(size);
	}
	
	/**
	 * Instantiates an object which indicates size of an object.
	 * 
	 * @param width		Width of the enclosed object.
	 * @param height	Height of the enclosed object.
	 * @throws IllegalArgumentException		If the width and/or height is less
	 * 										than or equal to {@code 0}.
	 */
	public AbsoluteSize(int width, int height) {
		if (width <= 0 || height <= 0) {
			throw new IllegalArgumentException(
					"Width and height must be greater than 0."
			);
		}
		this.size = new Dimension(width, height);
	}

	public Dimension calculate(int width, int height) {
		if (width <= 0 || height <= 0) {
			throw new IllegalArgumentException(
					"Width and height must be greater than 0."
			);
		}
		return new Dimension(size);
	}

	/** 
	 * Returns a {@code String} representation of this object.
	 * 
	 * @return		{@code String} representation of this object.
	 */
	@Override
	public String toString() {
		return "AbsoluteSize [width=" + size.width + ", height=" + size.height + "]";
	}
}
