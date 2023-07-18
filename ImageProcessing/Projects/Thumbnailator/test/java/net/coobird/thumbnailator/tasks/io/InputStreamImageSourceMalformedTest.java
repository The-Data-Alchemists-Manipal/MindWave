

package net.coobird.thumbnailator.tasks.io;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

@RunWith(Parameterized.class)
public class InputStreamImageSourceMalformedTest {

	@Parameterized.Parameters(name = "type={0}, length={1}")
	public static Collection<Object> testCases() {
		List<Object[]> cases = new ArrayList<Object[]>();
		for (String type : Arrays.asList("jpg", "png", "bmp")) {
			for (int i = 1; i <= 40; i++) {
				cases.add(new Object[] { type, i });
			}
		}
		return Arrays.asList(cases.toArray());
	}

	@Parameterized.Parameter
	public String type;

	@Parameterized.Parameter(value = 1)
	public Integer length;

	@Before	@After
	public void cleanup() {
		System.clearProperty("thumbnailator.disableExifWorkaround");
	}

	@Test
	public void terminatesProperlyWithWorkaround() {
		runTest();
	}

	@Test
	public void terminatesProperlyWithoutWorkaround() {
		System.setProperty("thumbnailator.disableExifWorkaround", "true");
		runTest();
	}

	/**
	 * Test to check that reading an abnormal file won't cause image reading
	 * to end up in a bad state like in an infinite loop.
	 */
	private void runTest() {
		try {
			byte[] bytes = new byte[length];
			InputStream sourceIs = ClassLoader.getSystemResourceAsStream(String.format("Thumbnailator/grid.%s", type));
			sourceIs.read(bytes);
			sourceIs.close();

			ByteArrayInputStream is = new ByteArrayInputStream(bytes);
			InputStreamImageSource source = new InputStreamImageSource(is);

			source.read();

		} catch (Exception e) {
			// terminates properly, even if an exception is thrown.
		}
	}
}
