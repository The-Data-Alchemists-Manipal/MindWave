

package net.coobird.thumbnailator.tasks.io;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import net.coobird.thumbnailator.TestUtils;
import net.coobird.thumbnailator.ThumbnailParameter;
import net.coobird.thumbnailator.builders.ThumbnailParameterBuilder;
import net.coobird.thumbnailator.geometry.AbsoluteSize;
import net.coobird.thumbnailator.geometry.Coordinate;
import net.coobird.thumbnailator.geometry.Positions;
import net.coobird.thumbnailator.geometry.Region;
import net.coobird.thumbnailator.test.BufferedImageAssert;
import net.coobird.thumbnailator.test.BufferedImageComparer;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.rules.TemporaryFolder;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.containsString;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.fail;

@RunWith(Enclosed.class)
public class FileImageSourceTest {

	public static class Tests {
		@Rule
		public TemporaryFolder temporaryFolder = new TemporaryFolder();

		@Test(expected=FileNotFoundException.class)
		public void fileDoesNotExists() throws IOException {
			// given
			File nonExistentFile = new File(temporaryFolder.getRoot(), "nonExistentFile");
			FileImageSource source = new FileImageSource(nonExistentFile);

			try {
				// when
				source.read();
			} catch (FileNotFoundException e) {
				// then
				assertThat(e.getMessage(), containsString("Could not find file"));
				throw e;
			}
			fail();
		}

		@Test(expected=FileNotFoundException.class)
		public void fileDoesNotExists_AsString() throws IOException {
			// given
			File nonExistentFile = new File(temporaryFolder.getRoot(), "nonExistentFile");
			FileImageSource source = new FileImageSource(nonExistentFile.getAbsolutePath());

			try {
				// when
				source.read();
			} catch (FileNotFoundException e) {
				// then
				assertThat(e.getMessage(), containsString("Could not find file"));
				throw e;
			}
			fail();
		}

		@Test(expected=IllegalStateException.class)
		public void fileExists_getInputFormatNameBeforeRead() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			FileImageSource source = new FileImageSource(sourceFile);

			try {
				// when
				source.getInputFormatName();
			} catch (IllegalStateException e) {
				// then
				assertEquals("Input has not been read yet.", e.getMessage());
				throw e;
			}
		}

		/*
		 *
		 *     +------+-----------+
		 *     |XXXXXX|           |
		 *     |XXXXXX|           |
		 *     +------+           |
		 *     |      region      |
		 *     |                  |
		 *     |                  |
		 *     |                  |
		 *     |                  |
		 *     +------------------+
		 *                        source
		 */
		@Test
		public void appliesSourceRegion() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);
			source.setThumbnailParameter(
					new ThumbnailParameterBuilder()
						.region(new Region(Positions.TOP_LEFT, new AbsoluteSize(40, 40)))
						.size(20, 20)
						.build()
			);

			// when
			BufferedImage img = source.read();

			// then
			BufferedImage expectedImg = sourceImage.getSubimage(0, 0, 40, 40);
			assertTrue(BufferedImageComparer.isRGBSimilar(expectedImg, img));
		}

		/*
		 *
		 *     +------------------+ source
		 *     |  +------------------+
		 *     |  |XXXXXXXXXXXXXXX|  |
		 *     |  |XXXXXXXXXXXXXXX|  |
		 *     |  |XX  final  XXXX|  |
		 *     |  |XX  region XXXX|  |
		 *     |  |XXXXXXXXXXXXXXX|  |
		 *     |  |XXXXXXXXXXXXXXX|  |
		 *     |  |XXXXXXXXXXXXXXX|  |
		 *     +--|---------------+  |
		 *        +------------------+
		 *                             region
		 */
		@Test
		public void appliesSourceRegionTooBig() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);
			source.setThumbnailParameter(
					new ThumbnailParameterBuilder()
						.region(new Region(new Coordinate(20, 20), new AbsoluteSize(100, 100)))
						.size(80, 80)
						.build()
			);

			// when
			BufferedImage img = source.read();

			// then
			BufferedImage expectedImg = sourceImage.getSubimage(20, 20, 80, 80);
			assertTrue(BufferedImageComparer.isRGBSimilar(expectedImg, img));
		}

		/*
		 *   +-----------------+
		 *   |                 |
		 *   | +---------------|--+
		 *   | |XXXXXXXXXXXXXXX|  |
		 *   | |XXXXXXXXXXXXXXX|  |
		 *   | |XXXX final XXXX|  |
		 *   | |XXXX regionXXXX|  |
		 *   | |XXXXXXXXXXXXXXX|  |
		 *   | |XXXXXXXXXXXXXXX|  |
		 *   +-----------------+  |
		 *     |                region
		 *     +------------------+
		 *                        source
		 */
		@Test
		public void appliesSourceRegionBeyondOrigin() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);
			source.setThumbnailParameter(
					new ThumbnailParameterBuilder()
						.region(new Region(new Coordinate(-20, -20), new AbsoluteSize(100, 100)))
						.size(80, 80)
						.build()
			);

			// when
			BufferedImage img = source.read();

			// then
			BufferedImage expectedImg = sourceImage.getSubimage(0, 0, 80, 80);
			assertTrue(BufferedImageComparer.isRGBSimilar(expectedImg, img));
		}

		@Test
		public void appliesSourceRegionNotSpecified() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);
			source.setThumbnailParameter(
					new ThumbnailParameterBuilder()
						.size(20, 20)
						.build()
			);

			// when
			BufferedImage img = source.read();

			// then
			assertTrue(BufferedImageComparer.isRGBSimilar(sourceImage, img));
		}

		@Test
		public void useExifOrientationIsTrue_OrientationHonored() throws Exception {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Exif/source_2.jpg", temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);

			ThumbnailParameter param =
					new ThumbnailParameterBuilder()
							.size(20, 20)
							.useExifOrientation(true)
							.build();

			source.setThumbnailParameter(param);

			// when
			source.read();

			// then
			BufferedImage result = param.getImageFilters().get(0).apply(sourceImage);
			BufferedImageAssert.assertMatches(
					result,
					new float[] {
							1, 1, 1,
							1, 1, 1,
							1, 0, 0,
					}
			);
		}

		@Test
		public void useExifOrientationIsFalse_OrientationIgnored() throws Exception {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					"Exif/source_2.jpg", temporaryFolder
			);
			FileImageSource source = new FileImageSource(sourceFile);

			ThumbnailParameter param =
					new ThumbnailParameterBuilder()
							.size(20, 20)
							.useExifOrientation(false)
							.build();

			source.setThumbnailParameter(param);

			// when
			BufferedImage result = source.read();

			// then
			assertTrue(param.getImageFilters().isEmpty());
			BufferedImageAssert.assertMatches(
					result,
					new float[] {
							1, 1, 1,
							1, 1, 1,
							0, 0, 1,
					}
			);
		}

		// What we really want to check the file resource is released.
		@Test
		public void canRemoveSourceImage() throws IOException {
			// given
			File inputFile = TestUtils.copyResourceToTemporaryFile(
					"Thumbnailator/grid.png", temporaryFolder
			);
			FileImageSource source = new FileImageSource(inputFile);

			// when
			source.read();

			// then
			assertEquals(inputFile, source.getSource());
			assertTrue(inputFile.exists());
			assertTrue(inputFile.delete());
			assertFalse(inputFile.exists());
		}

		// What we really want to check the file resource is released.
		// Reproducible on Windows, not Linux. (Issue #143)
		@Test
		public void canRemoveSourceImageOnReadFailure() throws IOException {
			// given
			File inputFile = temporaryFolder.newFile("something.png");
			TestUtils.copyFile(
					TestUtils.copyResourceToTemporaryFile(
							"Thumbnailator/grid.png", temporaryFolder
					)
					, inputFile, 200
			);

			FileImageSource source = new FileImageSource(inputFile);

			// when
			try {
				source.read();
				fail();
			} catch (Exception e) {
				// expected
			}

			// then
			assertEquals(inputFile, source.getSource());
			assertTrue(inputFile.exists());
			assertTrue(inputFile.delete());
			assertFalse(inputFile.exists());
		}
	}

	@RunWith(Parameterized.class)
	public static class FileReadTests {
		@Parameterized.Parameters
		public static Object[][] formats() {
			return new Object[][] {
					new Object[] { "png", "png" },
					new Object[] { "jpg", "JPEG" },
					new Object[] { "bmp", "bmp" },
			};
		}

		@Parameterized.Parameter
		public String format;

		@Parameterized.Parameter(1)
		public String expectedFormat;

		@Rule
		public TemporaryFolder temporaryFolder = new TemporaryFolder();

		private interface FileImageSourceSupplier {
			FileImageSource get(File sourceFile);
		}

		private void test(FileImageSourceSupplier supplier) throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					String.format("Thumbnailator/grid.%s", format), temporaryFolder
			);
			FileImageSource source = supplier.get(sourceFile);

			// when
			BufferedImage img = source.read();

			// then
			assertEquals(100, img.getWidth());
			assertEquals(100, img.getHeight());
			assertEquals(expectedFormat, source.getInputFormatName());
		}

		@Test
		public void fileExistsUsingFile() throws IOException {
			test(new FileImageSourceSupplier() {
				public FileImageSource get(File sourceFile) {
					return new FileImageSource(sourceFile);
				}
			});
		}

		@Test
		public void fileExistsUsingString() throws IOException {
			test(new FileImageSourceSupplier() {
				public FileImageSource get(File sourceFile) {
					return new FileImageSource(sourceFile.getAbsolutePath());
				}
			});
		}
	}

	@RunWith(Parameterized.class)
	public static class OrientationTests {
		@Parameterized.Parameters(name = "orientation={0}")
		public static Object[] values() {
			return new Integer[] { 1, 2, 3, 4, 5, 6, 7, 8 };
		}

		@Parameterized.Parameter
		public int orientation;

		@Rule
		public TemporaryFolder temporaryFolder = new TemporaryFolder();

		/**
		 * Check that `FileImageSource.read` behaves like `ImageIO.read`.
		 */
		@Test
		public void readImageUnaffectedByOrientation() throws IOException {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					String.format("Exif/source_%s.jpg", orientation), temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);

			ThumbnailParameter param =
					new ThumbnailParameterBuilder().size(20, 20).build();
			source.setThumbnailParameter(param);

			// when
			BufferedImage img = source.read();

			// then
			assertTrue(BufferedImageComparer.isRGBSimilar(sourceImage, img));
		}

		/**
		 * Check that the Exif orientation is honored by default.
		 */
		@Test
		public void containsCorrectFilterForOrientation() throws Exception {
			// given
			File sourceFile = TestUtils.copyResourceToTemporaryFile(
					String.format("Exif/source_%s.jpg", orientation), temporaryFolder
			);
			BufferedImage sourceImage = ImageIO.read(sourceFile);

			FileImageSource source = new FileImageSource(sourceFile);

			ThumbnailParameter param =
					new ThumbnailParameterBuilder().size(20, 20).build();
			source.setThumbnailParameter(param);

			// when
			source.read();

			// then
			if (orientation == 1) {
				assertTrue(param.getImageFilters().isEmpty());
				return;
			}

			BufferedImage result = param.getImageFilters().get(0).apply(sourceImage);
			BufferedImageAssert.assertMatches(
					result,
					new float[] {
							1, 1, 1,
							1, 1, 1,
							1, 0, 0,
					}
			);
		}
	}
}
