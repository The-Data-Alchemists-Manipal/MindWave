
package net.coobird.thumbnailator;

import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.rules.TemporaryFolder;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static net.coobird.thumbnailator.TestUtils.copyResourceToTemporaryFile;
import static net.coobird.thumbnailator.TestUtils.getResourceStream;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(Enclosed.class)
public class ThumbnailatorTranscodeTest {

	private static final List<String> SUPPORTED_FORMATS = Arrays.asList("jpg", "png", "bmp", "gif");

	@Ignore
	public static class SupportedFormatsBase {
		@Parameterized.Parameters(name = "format={0}")
		public static Collection<Object> testCases() {
			List<Object[]> cases = new ArrayList<Object[]>();
			for (String input : SUPPORTED_FORMATS) {
				cases.add(new Object[] { input });
			}
			return Arrays.asList(cases.toArray());
		}

		@Parameterized.Parameter
		public String supportedFormat;

		protected boolean isTestForGifOutputInJava5() {
			return "gif".equals(supportedFormat) && System.getProperty("java.version").startsWith("1.5");
		}
	}

	@Ignore
	public static class InputOutputExpectationBase {
		@Parameterized.Parameters(name = "input={0}, output={1}, expected={2}")
		public static Collection<Object> testCases() {
			List<Object[]> cases = new ArrayList<Object[]>();

			Map<String, String> expectedFormatNames = new HashMap<String, String>() {{
				put("jpg", "JPEG");
				put("png", "png");
				put("bmp", "bmp");
				put("gif", "gif");
			}};

			for (String input : SUPPORTED_FORMATS) {
				for (String output : SUPPORTED_FORMATS) {
					if (input.equals(output)) {
						continue;
					}
					cases.add(new Object[] { input, output, expectedFormatNames.get(output) });
				}
			}

			return Arrays.asList(cases.toArray());
		}

		@Parameterized.Parameter
		public String inputFormat;

		@Parameterized.Parameter(value = 1)
		public String outputFormat;

		@Parameterized.Parameter(value = 2)
		public String expectedFormatName;

		protected boolean isTestForGifOutputInJava5() {
			return "gif".equals(outputFormat) && System.getProperty("java.version").startsWith("1.5");
		}
	}

	@RunWith(Parameterized.class)
	public static class InputStreamToOutputStreamTest extends InputOutputExpectationBase {

		@Test
		public void createThumbnailForInputStreamToOutputStream() throws IOException {
			// Skip in Java 5, as GIF writer was first included in Java 6.
			if (isTestForGifOutputInJava5()) {
				return;
			}

			InputStream is = TestUtils.getResourceStream(String.format("Thumbnailator/grid.%s", inputFormat));
			ByteArrayOutputStream os = new ByteArrayOutputStream();

			Thumbnailator.createThumbnail(is, os, outputFormat, 50, 50);

			InputStream thumbIs = new ByteArrayInputStream(os.toByteArray());
			BufferedImage img = ImageIO.read(thumbIs);

			assertEquals(
					expectedFormatName,
					ImageIO.getImageReaders(
							ImageIO.createImageInputStream(
									new ByteArrayInputStream(os.toByteArray()))
					).next().getFormatName()
			);
			assertEquals(50, img.getWidth());
			assertEquals(50, img.getHeight());
		}
	}

	@RunWith(Parameterized.class)
	public static class FileToFileTest extends InputOutputExpectationBase {

		@Rule
		public TemporaryFolder temporaryFolder = new TemporaryFolder();

		@Test
		public void createThumbnailForFileToFile() throws IOException {
			// Skip in Java 5, as GIF writer was first included in Java 6.
			if (isTestForGifOutputInJava5()) {
				return;
			}

			File inputFile = copyResourceToTemporaryFile(String.format("Thumbnailator/grid.%s", inputFormat), temporaryFolder);
			File outputFile = temporaryFolder.newFile(String.format("test.%s", outputFormat));

			Thumbnailator.createThumbnail(inputFile, outputFile, 50, 50);

			assertTrue(outputFile.exists());
			BufferedImage img = ImageIO.read(outputFile);
			assertEquals(
					expectedFormatName,
					ImageIO.getImageReaders(
							ImageIO.createImageInputStream(outputFile)
					).next().getFormatName()
			);
			assertEquals(50, img.getWidth());
			assertEquals(50, img.getHeight());
		}
	}

	@RunWith(Parameterized.class)
	public static class SupportedInputFormatsForFiles extends SupportedFormatsBase {
		@Rule
		public TemporaryFolder temporaryFolder = new TemporaryFolder();

		@Test
		public void testCreateThumbnailForFileToFile() throws IOException {
			// Skip in Java 5, as GIF writer was first included in Java 6.
			if (isTestForGifOutputInJava5()) {
				return;
			}

			File inputFile = copyResourceToTemporaryFile(String.format("Thumbnailator/grid.%s", supportedFormat), temporaryFolder);
			File outputFile = temporaryFolder.newFile(String.format("tmp.%s", supportedFormat));

			Thumbnailator.createThumbnail(inputFile, outputFile, 50, 50);

			assertTrue(outputFile.exists());
			BufferedImage img = ImageIO.read(outputFile);
			assertEquals(50, img.getWidth());
			assertEquals(50, img.getHeight());
		}

		@Test
		public void testCreateThumbnailForFileToBufferedImage() throws IOException {
			// Skip in Java 5, as GIF writer was first included in Java 6.
			if (isTestForGifOutputInJava5()) {
				return;
			}

			File inputFile = copyResourceToTemporaryFile(String.format("Thumbnailator/grid.%s", supportedFormat), temporaryFolder);

			BufferedImage img = Thumbnailator.createThumbnail(inputFile, 50, 50);
			assertEquals(50, img.getWidth());
			assertEquals(50, img.getHeight());
		}
	}

	@RunWith(Parameterized.class)
	public static class SupportedInputFormatsForStreams extends SupportedFormatsBase {
		@Test
		public void testCreateThumbnailForInputStreamToOutputStream() throws IOException {
			// Skip in Java 5, as GIF writer was first included in Java 6.
			if (isTestForGifOutputInJava5()) {
				return;
			}

			InputStream is = getResourceStream(String.format("Thumbnailator/grid.%s", supportedFormat));
			ByteArrayOutputStream os = new ByteArrayOutputStream();

			Thumbnailator.createThumbnail(is, os, 50, 50);

			InputStream thumbIs = new ByteArrayInputStream(os.toByteArray());
			BufferedImage thumb = ImageIO.read(thumbIs);
			assertEquals(50, thumb.getWidth());
			assertEquals(50, thumb.getHeight());
		}
	}
}
