

package net.coobird.thumbnailator.filters;

import static net.coobird.thumbnailator.filters.ImageFilterTestUtils.assertImageTypeRetained;
import static org.junit.Assert.*;

import java.awt.image.BufferedImage;

import net.coobird.thumbnailator.test.BufferedImageComparer;
import net.coobird.thumbnailator.util.BufferedImages;

import org.junit.Test;

/**
 * Tests for the {@link Transparency} filter.
 * 
 *
 */
public class TransparencyTest {

	/**
	 * Checks that the input image contents are not altered, when using the
	 * {@link Transparency#Transparency(double)} constructor.
	 */
	@Test
	public void inputContentsAreNotAltered_DoubleConstructor() {
		// given
		BufferedImage originalImage = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
		BufferedImage copyImage = BufferedImages.copy(originalImage);
		
		ImageFilter filter = new Transparency(0.5);
		
		// when
		filter.apply(originalImage);
		
		// then
		assertTrue(BufferedImageComparer.isSame(originalImage, copyImage));
	}
	
	/**
	 * Checks that the input image contents are not altered, when using the
	 * {@link Transparency#Transparency(float)} constructor.
	 */
	@Test
	public void inputContentsAreNotAltered_FloatConstructor() {
		// given
		BufferedImage originalImage = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
		BufferedImage copyImage = BufferedImages.copy(originalImage);
		
		ImageFilter filter = new Transparency(0.5f);
		
		// when
		filter.apply(originalImage);
		
		// then
		assertTrue(BufferedImageComparer.isSame(originalImage, copyImage));
	}

	@Test
	public void imageTypeForInputAndOutputIsTheSame_DoubleConstructor() {
		assertImageTypeRetained(new Transparency(0.5));
	}

	@Test
	public void imageTypeForInputAndOutputIsTheSame_FloatConstructor() {
		assertImageTypeRetained(new Transparency(0.5f));
	}
}
