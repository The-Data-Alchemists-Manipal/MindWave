

package net.coobird.thumbnailator.filters;

import static net.coobird.thumbnailator.filters.ImageFilterTestUtils.assertImageTypeRetained;
import static org.junit.Assert.*;

import java.awt.Color;
import java.awt.Font;
import java.awt.image.BufferedImage;

import net.coobird.thumbnailator.geometry.Position;
import net.coobird.thumbnailator.geometry.Positions;
import net.coobird.thumbnailator.test.BufferedImageComparer;
import net.coobird.thumbnailator.util.BufferedImages;

import org.junit.Test;

/**
 * Tests for the {@link Caption} filter.
 * 
 *
 */
public class CaptionTest {

	private static final String DEFAULT_CAPTION = "hello";
	private static final Font DEFAULT_FONT = new Font("Monospaced", Font.PLAIN, 14);
	private static final Color DEFAULT_COLOR = Color.black;
	private static final Position DEFAULT_POSITION = Positions.BOTTOM_CENTER;

	/**
	 * Checks that the input image contents are not altered.
	 */
	@Test
	public void inputContentsAreNotAltered() {
		// given
		BufferedImage originalImage = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
		BufferedImage copyImage = BufferedImages.copy(originalImage);
		
		ImageFilter filter = new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				0
		);
		
		// when
		filter.apply(originalImage);
		
		// then
		assertTrue(BufferedImageComparer.isSame(originalImage, copyImage));
	}

	@Test
	public void imageTypeForInputAndOutputIsTheSame() {
		ImageFilter filter = new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				0
		);

		assertImageTypeRetained(filter);
	}

	@Test(expected = NullPointerException.class)
	public void constructorNullCheckForCaption() {
		new Caption(
				null,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				0
		);
	}

	@Test(expected = NullPointerException.class)
	public void constructorNullCheckForFont() {
		new Caption(
				DEFAULT_CAPTION,
				null,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				0
		);
	}

	@Test(expected = NullPointerException.class)
	public void constructorNullCheckForColor() {
		new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				null,
				DEFAULT_POSITION,
				0
		);
	}

	@Test(expected = NullPointerException.class)
	public void constructorNullCheckForPosition() {
		new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				null,
				0
		);
	}

	@Test
	public void constructorAllowsPositiveInsets() {
		new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				10
		);
	}

	@Test(expected = IllegalArgumentException.class)
	public void constructorRejectsNegativeInsets() {
		new Caption(
				DEFAULT_CAPTION,
				DEFAULT_FONT,
				DEFAULT_COLOR,
				DEFAULT_POSITION,
				-1
		);
	}
}
