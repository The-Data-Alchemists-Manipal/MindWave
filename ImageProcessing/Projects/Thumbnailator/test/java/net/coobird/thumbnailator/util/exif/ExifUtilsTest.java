

package net.coobird.thumbnailator.util.exif;

import static net.coobird.thumbnailator.TestUtils.getResourceStream;
import static org.junit.Assert.assertEquals;

import java.io.InputStream;

import javax.imageio.ImageIO;
import javax.imageio.ImageReader;

import org.junit.Test;

/**
 * Tests the {@link ExifUtils} class to check that the Exif Orientation
 * tag is correctly acquired by the
 * {@link ExifUtils#getExifOrientation(ImageReader, int)} method.
 * <p>
 * The Exif Orientation tags has been added to the source images by using
 * <a href="http://owl.phy.queensu.ca/~phil/exiftool/index.html">ExifTool</a>.
 * 
 *
 */
public class ExifUtilsTest {
	
	@Test
	public void exifOrientation1() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_1.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));

		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(1), orientation);
	}
	
	@Test
	public void exifOrientation2() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_2.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(2), orientation);
	}
	
	@Test
	public void exifOrientation3() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_3.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(3), orientation);
	}
	
	@Test
	public void exifOrientation4() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_4.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(4), orientation);
	}
	
	@Test
	public void exifOrientation5() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_5.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(5), orientation);
	}
	
	@Test
	public void exifOrientation6() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_6.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(6), orientation);
	}
	
	@Test
	public void exifOrientation7() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_7.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(7), orientation);
	}
	
	@Test
	public void exifOrientation8() throws Exception {
		// given
		ImageReader reader = ImageIO.getImageReadersByFormatName("jpg").next();
		InputStream is = getResourceStream("Exif/orientation_8.jpg");
		reader.setInput(ImageIO.createImageInputStream(is));
		
		// when
		Orientation orientation = ExifUtils.getExifOrientation(reader, 0);
		is.close();
		
		// then
		assertEquals(Orientation.typeOf(8), orientation);
	}
}
