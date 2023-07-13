

package net.coobird.thumbnailator.name;

import java.io.File;
import java.io.IOException;
import java.util.Iterator;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import static org.junit.Assert.*;

public class ConsecutiveNumbersTest {

	@Rule
	public TemporaryFolder temporaryFolder = new TemporaryFolder();

	@Test
	public void noArgConstructor() {
		// given
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames();
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File("0"), iter.next());
		assertEquals(new File("1"), iter.next());
		assertEquals(new File("2"), iter.next());
		assertEquals(new File("3"), iter.next());
	}
	
	@Test
	public void startNumberSpecified() {
		// given
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File("5"), iter.next());
		assertEquals(new File("6"), iter.next());
		assertEquals(new File("7"), iter.next());
		assertEquals(new File("8"), iter.next());
	}
	
	@Test
	public void givenParentDir() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "0"), iter.next());
		assertEquals(new File(dir, "1"), iter.next());
		assertEquals(new File(dir, "2"), iter.next());
		assertEquals(new File(dir, "3"), iter.next());
	}
	
	@Test
	public void givenParentDir_WithTrailingSlash() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "0"), iter.next());
		assertEquals(new File(dir, "1"), iter.next());
		assertEquals(new File(dir, "2"), iter.next());
		assertEquals(new File(dir, "3"), iter.next());
	}
	
	@Test(expected=IOException.class)
	public void givenParentDir_WithFile() throws IOException {
		try {
			// given
			File dir = temporaryFolder.newFile("file");

			// when
			new ConsecutivelyNumberedFilenames(dir);
		} catch (IOException e) {
			// then
			assertEquals("Specified path is not a directory or does not exist.", e.getMessage());
			throw e;
		}
	}
	
	@Test(expected=IOException.class)
	public void givenParentDir_WithNonExistentDir() throws IOException {
		try {
			// given
			File dir = new File(temporaryFolder.getRoot(), "foobar");
			
			// when
			new ConsecutivelyNumberedFilenames(dir);
		} catch (IOException e) {
			// then
			assertEquals("Specified path is not a directory or does not exist.", e.getMessage());
			throw e;
		}
	}

	@Test
	public void formatOnly_WithZeroPadding() {
		// given
		ConsecutivelyNumberedFilenames sAndC = new ConsecutivelyNumberedFilenames("hello-%04d.jpg");
		
		// when+then
		Iterator<File> iter = sAndC.iterator();
		
		assertEquals(new File("hello-0000.jpg"), iter.next());
		assertEquals(new File("hello-0001.jpg"), iter.next());
		assertEquals(new File("hello-0002.jpg"), iter.next());
		assertEquals(new File("hello-0003.jpg"), iter.next());
	}
	
	@Test
	public void formatOnly_WithText() {
		// given
		ConsecutivelyNumberedFilenames sAndC = new ConsecutivelyNumberedFilenames("hello-%d.jpg");
		
		// when+then
		Iterator<File> iter = sAndC.iterator();
		
		assertEquals(new File("hello-0.jpg"), iter.next());
		assertEquals(new File("hello-1.jpg"), iter.next());
		assertEquals(new File("hello-2.jpg"), iter.next());
		assertEquals(new File("hello-3.jpg"), iter.next());
	}
	
	
	@Test
	public void givenParentDir_StartNumberSpecified() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir, 5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "5"), iter.next());
		assertEquals(new File(dir, "6"), iter.next());
		assertEquals(new File(dir, "7"), iter.next());
		assertEquals(new File(dir, "8"), iter.next());
	}

	@Test(expected=IOException.class)
	public void givenParentDir_StartNumberSpecified_WhereDirIsInvalid() throws IOException {
		try {
			// given
			File dir = new File(temporaryFolder.getRoot(), "foobar");
			
			// when
			new ConsecutivelyNumberedFilenames(dir, 5);
		} catch (IOException e) {
			// then
			assertEquals("Specified path is not a directory or does not exist.", e.getMessage());
			throw e;
		}
		
	}
	
	@Test
	public void givenParentDir_formatWithZeroPadding() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir, "hello-%04d.jpg");
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "hello-0000.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0001.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0002.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0003.jpg"), iter.next());
	}
	
	@Test
	public void givenParentDir_formatWithText() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir, "hello-%d.jpg");
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "hello-0.jpg"), iter.next());
		assertEquals(new File(dir, "hello-1.jpg"), iter.next());
		assertEquals(new File(dir, "hello-2.jpg"), iter.next());
		assertEquals(new File(dir, "hello-3.jpg"), iter.next());
	}
	
	@Test(expected=IOException.class)
	public void givenParentDir_formatWithText_WhereDirIsInvalid() throws IOException {
		try {
			// given
			File dir = new File(temporaryFolder.getRoot(), "foobar");
			
			// when
			new ConsecutivelyNumberedFilenames(dir, "hello-%d.jpg");
		} catch (IOException e) {
			// then
			assertEquals("Specified path is not a directory or does not exist.", e.getMessage());
			throw e;
		}
	}
	
	@Test
	public void formatWithZeroPadding_StartNumberSpecified() {
		// given
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames("hello-%04d.jpg", 5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File("hello-0005.jpg"), iter.next());
		assertEquals(new File("hello-0006.jpg"), iter.next());
		assertEquals(new File("hello-0007.jpg"), iter.next());
		assertEquals(new File("hello-0008.jpg"), iter.next());
	}
	
	@Test
	public void formatWithText_StartNumberSpecified() {
		// given
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames("hello-%d.jpg", 5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File("hello-5.jpg"), iter.next());
		assertEquals(new File("hello-6.jpg"), iter.next());
		assertEquals(new File("hello-7.jpg"), iter.next());
		assertEquals(new File("hello-8.jpg"), iter.next());
	}
	
	@Test
	public void givenParentDir_formatWithZeroPadding_StartNumberSpecified() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir, "hello-%04d.jpg", 5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "hello-0005.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0006.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0007.jpg"), iter.next());
		assertEquals(new File(dir, "hello-0008.jpg"), iter.next());
	}
	
	@Test
	public void givenParentDir_formatWithText_StartNumberSpecified() throws IOException {
		// given
		File dir = temporaryFolder.getRoot();
		ConsecutivelyNumberedFilenames consecutiveNumbers = new ConsecutivelyNumberedFilenames(dir, "hello-%d.jpg", 5);
		
		// when+then
		Iterator<File> iter = consecutiveNumbers.iterator();
		
		assertEquals(new File(dir, "hello-5.jpg"), iter.next());
		assertEquals(new File(dir, "hello-6.jpg"), iter.next());
		assertEquals(new File(dir, "hello-7.jpg"), iter.next());
		assertEquals(new File(dir, "hello-8.jpg"), iter.next());
	}
	
	@Test(expected=IOException.class)
	public void givenParentDir_formatWithText_StartNumberSpecified_WhereDirIsInvalid() throws IOException {
		try {
			// given
			File dir = new File(temporaryFolder.getRoot(), "foobar");
			
			// when
			new ConsecutivelyNumberedFilenames(dir, "hello-%d.jpg", 5);
		} catch (IOException e) {
			// then
			assertEquals("Specified path is not a directory or does not exist.", e.getMessage());
			throw e;
		}
	}
}
