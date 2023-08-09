

package net.coobird.thumbnailator.tasks;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import javax.imageio.ImageIO;

import net.coobird.thumbnailator.TestUtils;
import net.coobird.thumbnailator.ThumbnailParameter;
import net.coobird.thumbnailator.Thumbnailator;
import net.coobird.thumbnailator.builders.BufferedImageBuilder;
import net.coobird.thumbnailator.builders.ThumbnailParameterBuilder;
import net.coobird.thumbnailator.tasks.io.BufferedImageSink;
import net.coobird.thumbnailator.tasks.io.FileImageSource;
import net.coobird.thumbnailator.tasks.io.ImageSink;
import net.coobird.thumbnailator.tasks.io.ImageSource;
import net.coobird.thumbnailator.tasks.io.InputStreamImageSource;
import net.coobird.thumbnailator.tasks.io.OutputStreamImageSink;

import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

public class SourceSinkThumbnailTaskTest {

	@Rule
	public TemporaryFolder temporaryFolder = new TemporaryFolder();

	@SuppressWarnings("unchecked")
	@Test
	public void task_UsesPreferredFromDestination() throws Exception {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder()
				.size(50, 50)
				.format(ThumbnailParameter.DETERMINE_FORMAT)
				.build();
		
		ImageSource source = mock(ImageSource.class);
		when(source.read()).thenReturn(new BufferedImageBuilder(100, 100).build());
		when(source.getInputFormatName()).thenReturn("42a");
		
		ImageSink destination = mock(ImageSink.class);
		when(destination.preferredOutputFormatName()).thenReturn("42");
		
		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask(param, source, destination)
		);
		
		// then
		verify(source).read();

		verify(destination).preferredOutputFormatName();
		verify(destination).setOutputFormatName("42");
		verify(destination).write(any(BufferedImage.class));
	}
	
	@SuppressWarnings("unchecked")
	@Test
	public void task_UsesOriginalFormat() throws Exception {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder()
				.size(50, 50)
				.format(ThumbnailParameter.ORIGINAL_FORMAT)
				.build();
		
		ImageSource source = mock(ImageSource.class);
		when(source.read()).thenReturn(new BufferedImageBuilder(100, 100).build());
		when(source.getInputFormatName()).thenReturn("42");
		
		ImageSink destination = mock(ImageSink.class);
		when(destination.preferredOutputFormatName()).thenReturn("42a");
		
		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask(param, source, destination)
		);
		
		// then
		verify(source).read();
		
		verify(destination, never()).preferredOutputFormatName();
		verify(destination).setOutputFormatName("42");
		verify(destination).write(any(BufferedImage.class));
	}
	
	@Test
	public void task_SizeOnly_InputStream_BufferedImage() throws IOException {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder().size(50, 50).build();
		
		InputStream is = TestUtils.getResourceStream("Thumbnailator/grid.png");
		
		InputStreamImageSource source = new InputStreamImageSource(is);
		BufferedImageSink destination = new BufferedImageSink();
		
		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask<InputStream, BufferedImage>(param, source, destination)
		);

		// then
		BufferedImage thumbnail = destination.getSink();
		assertEquals(50, thumbnail.getWidth());
		assertEquals(50, thumbnail.getHeight());
	}
	
	
	@Test
	public void task_SizeOnly_InputStream_OutputStream() throws IOException {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder().size(50, 50).build();
		
		InputStream is = TestUtils.getResourceStream("Thumbnailator/grid.png");
		ByteArrayOutputStream os = new ByteArrayOutputStream();
		
		InputStreamImageSource source = new InputStreamImageSource(is);
		OutputStreamImageSink destination = new OutputStreamImageSink(os);

		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask<InputStream, OutputStream>(param, source, destination)
		);
		
		// then
		ByteArrayInputStream destIs = new ByteArrayInputStream(os.toByteArray());
		BufferedImage thumbnail = ImageIO.read(destIs);
		assertEquals(50, thumbnail.getWidth());
		assertEquals(50, thumbnail.getHeight());
		
		destIs = new ByteArrayInputStream(os.toByteArray());
		String formatName = TestUtils.getFormatName(destIs);
		
		assertEquals("png", formatName);
	}
	
	@Test
	public void task_ChangeOutputFormat_InputStream_OutputStream() throws IOException {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder().size(50, 50).format("jpg").build();

		InputStream is = TestUtils.getResourceStream("Thumbnailator/grid.png");
		ByteArrayOutputStream os = new ByteArrayOutputStream();
		
		InputStreamImageSource source = new InputStreamImageSource(is);
		OutputStreamImageSink destination = new OutputStreamImageSink(os);
		
		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask<InputStream, OutputStream>(param, source, destination)
		);
		
		// then
		ByteArrayInputStream destIs = new ByteArrayInputStream(os.toByteArray());
		BufferedImage thumbnail = ImageIO.read(destIs);
		assertEquals(50, thumbnail.getWidth());
		assertEquals(50, thumbnail.getHeight());
		
		destIs = new ByteArrayInputStream(os.toByteArray());
		String formatName = TestUtils.getFormatName(destIs);
		assertEquals("JPEG", formatName);
	}
	
	@Test
	public void task_ChangeOutputFormat_File_OutputStream() throws IOException {
		// given
		ThumbnailParameter param =
			new ThumbnailParameterBuilder().size(50, 50).format("jpg").build();
		
		ByteArrayOutputStream os = new ByteArrayOutputStream();

		File sourceFile = TestUtils.copyResourceToTemporaryFile(
				"Thumbnailator/grid.bmp", temporaryFolder
		);
		FileImageSource source = new FileImageSource(sourceFile);
		OutputStreamImageSink destination = new OutputStreamImageSink(os);
		
		// when
		Thumbnailator.createThumbnail(
				new SourceSinkThumbnailTask<File, OutputStream>(param, source, destination)
		);
		
		// then
		ByteArrayInputStream destIs = new ByteArrayInputStream(os.toByteArray());
		BufferedImage thumbnail = ImageIO.read(destIs);
		assertEquals(50, thumbnail.getWidth());
		assertEquals(50, thumbnail.getHeight());
		
		destIs = new ByteArrayInputStream(os.toByteArray());
		String formatName = TestUtils.getFormatName(destIs);
		assertEquals("JPEG", formatName);
	}
}
