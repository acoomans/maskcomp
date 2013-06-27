
function screen_compare(image_name, images_dir, results_dir) {

	var images_dir = (typeof images_dir !== 'undefined') ? images_dir : "screenshots";
	var results_dir = (typeof results_dir !== 'undefined') ? results_dir : "tmp";

	var target  = UIATarget.localTarget();

	target.captureScreenWithName(image_name);
	target.delay(2);

	var comparator = target.host().performTaskWithPathArgumentsTimeout("/usr/bin/which", ["mcomp.py"], 60).stdout.trim();

	var images = [
		results_dir+"/Run 1/"+image_name+".png",
		images_dir+"/"+image_name+".png",
		images_dir+"/"+image_name+"_mask.png",
	];

	var result = target.host().performTaskWithPathArgumentsTimeout(comparator, images, 60);
	return parseFloat(result.stdout.trim());
}