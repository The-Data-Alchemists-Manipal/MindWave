

package net.coobird.thumbnailator.tasks.io;

import net.coobird.thumbnailator.ThumbnailParameter;
import net.coobird.thumbnailator.builders.ThumbnailParameterBuilder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;

import static net.coobird.thumbnailator.TestUtils.copyResourceToTemporaryFile;
import static org.junit.Assert.assertTrue;

public class Issue156OutputStreamImageSinkTest {

	@Rule
	public TemporaryFolder temporaryFolder = new TemporaryFolder();

	@Test
	public void compressedPngDoesntGetLarger() throws IOException {
		File originalFile = copyResourceToTemporaryFile("Exif/original.png", temporaryFolder);
		BufferedImage originalImage = ImageIO.read(originalFile);

		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		OutputStreamImageSink imageSink = new OutputStreamImageSink(baos);

		ThumbnailParameter param = new ThumbnailParameterBuilder()
				.scale(1.0)
				.build();
		imageSink.setThumbnailParameter(param);

		imageSink.setOutputFormatName("png");
		imageSink.write(originalImage);

		assertTrue(baos.size() < originalFile.length());
	}
}
