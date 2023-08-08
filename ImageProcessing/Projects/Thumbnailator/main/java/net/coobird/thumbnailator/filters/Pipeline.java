

package net.coobird.thumbnailator.filters;

import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import net.coobird.thumbnailator.util.BufferedImages;


public final class Pipeline implements ImageFilter {
	
	private final List<ImageFilter> filtersToApply;
	
	private final List<ImageFilter> unmodifiableFiltersToApply;
	
	/**
	 * Instantiates a new {@link Pipeline} with no image filters to apply.
	 */
	public Pipeline() {
		this(Collections.<ImageFilter>emptyList());
	}
	
	/**
	 * Instantiates a new {@link Pipeline} with an array of {@link ImageFilter}s
	 * to apply.
	 * 
	 * @param filters		An array of {@link ImageFilter}s to apply.
	 */
	public Pipeline(ImageFilter... filters) {
		this(Arrays.asList(filters));
	}
	
	/**
	 * Instantiates a new {@link Pipeline} with a list of {@link ImageFilter}s
	 * to apply.
	 * 
	 * @param filters		A list of {@link ImageFilter}s to apply.
	 */
	public Pipeline(List<ImageFilter> filters) {
		if (filters == null) {
			throw new NullPointerException("Cannot instantiate with a null" +
			"list of image filters.");
		}
		
		filtersToApply = new ArrayList<ImageFilter>(filters);
		unmodifiableFiltersToApply =
			Collections.unmodifiableList(filtersToApply);
	}
	
	/**
	 * Adds an {@code ImageFilter} to the pipeline.
	 *
	 * @param filter		An {@code ImageFilter}.
	 */
	public void add(ImageFilter filter) {
		if (filter == null) {
			throw new NullPointerException("An image filter must not be null.");
		}
		
		filtersToApply.add(filter);
	}
	
	/**
	 * Adds an {@code ImageFilter} to the beginning of the pipeline.
	 *
	 * @param filter		An {@code ImageFilter}.
	 */
	public void addFirst(ImageFilter filter) {
		if (filter == null) {
			throw new NullPointerException("An image filter must not be null.");
		}
		
		filtersToApply.add(0, filter);
	}
	
	/**
	 * Adds a {@code List} of {@code ImageFilter}s to the pipeline.
	 * 
	 * @param filters			A list of filters to add to the pipeline.
	 */
	public void addAll(List<ImageFilter> filters) {
		if (filters == null) {
			throw new NullPointerException("A list of image filters must not be null.");
		}
		
		filtersToApply.addAll(filters);
	}
	
	/**
	 * Returns a list of {@link ImageFilter}s which will be applied by this
	 * {@link Pipeline}.
	 * 
	 * @return					A list of filters which are applied by this
	 * 							pipeline.
	 */
	public List<ImageFilter> getFilters() {
		return unmodifiableFiltersToApply;
	}
	
	public BufferedImage apply(BufferedImage img) {
		if (filtersToApply.isEmpty()) {
			return img;
		}
		
		BufferedImage image = BufferedImages.copy(img);
		
		for (ImageFilter filter : filtersToApply) {
			image = filter.apply(image);
		}
		
		return image;
	}
}
