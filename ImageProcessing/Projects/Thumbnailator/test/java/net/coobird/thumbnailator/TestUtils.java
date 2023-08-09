

package net.coobird.thumbnailator;

import org.junit.rules.TemporaryFolder;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

import javax.imageio.ImageIO;

public class TestUtils {
	/**
	 * Copies a specified length of the source file.
	 * 
	 * @param sourceFile		The source file.
	 * @param destFile			The destination file.
	 * @param length			Length of source file to copy.
	 * @throws IOException		If an IOException is thrown.
	 */
	public static void copyFile(File sourceFile, File destFile, long length) throws IOException {
		FileInputStream fis = new FileInputStream(sourceFile);
		FileOutputStream fos = new FileOutputStream(destFile);
		fis.getChannel().transferTo(0, length, fos.getChannel());
		fis.close();
		fos.close();
	}

	/**
	 * Copies a file.
	 *
	 * @param sourceFile		The source file.
	 * @param destFile			The destination file.
	 * @throws IOException		If an IOException is thrown.
	 */
	public static void copyFile(File sourceFile, File destFile) throws IOException {
		copyFile(sourceFile, destFile, sourceFile.length());
	}

	/**
	 * Returns the format of an image which is read through the {@link InputStream}.
	 * 
	 * @param is			The {@link InputStream} to an image.
	 * @return				File format of the image.
	 * @throws IOException
	 */
	public static String getFormatName(InputStream is) throws IOException {
		return ImageIO.getImageReaders(
				ImageIO.createImageInputStream(is)
		).next().getFormatName();
	}

	public static URL getResource(String resourceName) throws IOException {
		URL url = ClassLoader.getSystemClassLoader().getResource(resourceName);
		if (url == null) {
			throw new IOException("Resource not found: " + resourceName);
		}
		return url;
	}

	public static InputStream getResourceStream(String resourceName) throws IOException {
		InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream(resourceName);
		if (is == null) {
			throw new IOException("Resource not found: " + resourceName);
		}
		return is;
	}

	public static File copyResourceToFile(String resourceName, File destination) throws IOException {
		InputStream is = getResourceStream(resourceName);
		FileOutputStream fos = new FileOutputStream(destination);

		byte[] buffer;
		int bytesAvailable;
		while ((bytesAvailable = is.available()) != 0) {
			buffer = new byte[bytesAvailable];
			int bytesRead = is.read(buffer, 0, buffer.length);
			fos.write(buffer, 0, bytesRead);
		}
		is.close();
		fos.close();

		return destination;
	}

	public static File copyResourceToTemporaryFile(String resourceName, TemporaryFolder folder) throws IOException {
		String name;
		if (resourceName.contains("/")) {
			name = resourceName.substring(resourceName.lastIndexOf("/") + 1);
		} else {
			name = resourceName;
		}
		File destination = folder.newFile(name);

		return copyResourceToFile(resourceName, destination);
	}

	public static File copyResourceToTemporaryFile(String resourceName, String namedAs, TemporaryFolder folder) throws IOException {
		return copyResourceToFile(resourceName, folder.newFile(namedAs));
	}

	public static BufferedImage getImageFromResource(String resourceName) throws IOException {
		InputStream is = getResourceStream(resourceName);
		try {
			return ImageIO.read(is);
		} finally {
			is.close();
		}
	}
}
