

package net.coobird.thumbnailator.filters;

import static net.coobird.thumbnailator.filters.ImageFilterTestUtils.assertImageTypeRetained;
import static org.junit.Assert.*;

import java.awt.Color;
import java.awt.image.BufferedImage;

import net.coobird.thumbnailator.test.BufferedImageComparer;
import net.coobird.thumbnailator.util.BufferedImages;

import org.junit.Test;

/**
 * Tests for the {@link Colorize} filter.
 * 
 *
 */
public class ColorizeTest {

	/**
	 * Checks that the input image contents are not altered.
	 */
	@Test
	public void inputContentsAreNotAltered() {
		// given
		BufferedImage originalImage = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
		BufferedImage copyImage = BufferedImages.copy(originalImage);
		
		ImageFilter filter = new Colorize(Color.blue);
		
		// when
		filter.apply(originalImage);
		
		// then
		assertTrue(BufferedImageComparer.isSame(originalImage, copyImage));
	}

	/**
	 * Checks that the input image contents are not altered for constructor with alpha.
	 */
	@Test
	public void inputContentsAreNotAltered_alphaConstructor() {
		// given
		BufferedImage originalImage = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
		BufferedImage copyImage = BufferedImages.copy(originalImage);

		ImageFilter filter = new Colorize(Color.blue, 0.5f);

		// when
		filter.apply(originalImage);

		// then
		assertTrue(BufferedImageComparer.isSame(originalImage, copyImage));
	}

	@Test
	public void imageTypeForInputAndOutputIsTheSame() {
		assertImageTypeRetained(new Colorize(Color.blue));
	}

	@Test
	public void imageTypeForInputAndOutputIsTheSame_alphaConstructor() {
		assertImageTypeRetained(new Colorize(Color.blue, 0.5f));
	}
}
