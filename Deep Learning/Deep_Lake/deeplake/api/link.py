from deeplake.core.linked_sample import LinkedSample
from typing import Optional, Dict


def link(
    path: str,
    creds_key: Optional[str] = None,
) -> LinkedSample:
    """Utility that stores a link to raw data. Used to add data to a Deep Lake Dataset without copying it. See :ref:`Link htype`.

  


    Examples:
        >>> ds = deeplake.dataset("test/test_ds")
        >>> ds.create_tensor("images", htype="link[image]", sample_compression="jpeg")
        >>> ds.images.append(deeplake.link("https://picsum.photos/200/300"))

    See more examples :ref:`here <linked_sample_examples>`.
    """
    return LinkedSample(path, creds_key)
