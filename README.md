Maskcomp
========

Maskcomp is a library utility to compare two images, like iPhone screenshots, optionally with a mask.

Maskcomp includes:

- _mcomp.py_: compares two images with an optional mask
- _screen.js_ (in _extras/uiautomation_): a javascript for calling _mcomp_ during uiautomation tests (instruments for iOS)


## Requirement

Maskcomp depends on _PIL_.

## Usage

### mcomp.py

Install _maskcomp_:

	python setup.py install

Then run _mcomp.py_:

	mcomp.py img1 img2 [mask]
	
The two images and the mask have to be of the same size. The mask is typically a black and white picture, where black zones are ignored during comparison. It returns a float value representing the difference between the images; 0 means the images are equal, > 0 means the images are different.

If you want to use the comparator as a module in your own code:
	
	from maskcomp.maskcomparator import compare
	compare(image1, image2, mask)
	
_imageN_ and _mask_ can be a PIL Image or a string.

	
### screen.js

For _screen.js_:

	#import "path/to/screen.js"
	
	if (screen_compare("signin")) {
		UIALogger.logFail("Sign in screens don't match");
	}
	
Note: _screen.js_ is available under _python/site-packages/Maskcomp.egg/uiautomation/screen.js_ (or similar) after install.
	
The function takes multiple arguments:

	screen_compare(image_name, images_dir, results_dir)
	
_image_name_: the filename of the screenshot and the reference image to compare. The mask is the _image_name_ with __mask.png_ appended to it.

_images_dir_: the directory containing references and masks images. ("screenshots" by default)

_results_dir_: the directory where screenshots are taken by UIAutomation's _captureScreenWithName_ or _captureRectWithName_. This is specified by the _UIARESULTSPATH_ variable for instruments running from the command line.



	








# Tests

Run the tests with:
	python -m tests.maskcomparator_tests