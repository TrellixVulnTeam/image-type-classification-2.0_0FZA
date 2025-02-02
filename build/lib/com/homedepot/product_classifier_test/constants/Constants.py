COMMA = ','
PIPE = '|'
FORWARD_SLASH = '/'
DOT = '.'
WHITE_THRESHOLD = 0.1
ASTERISK = '*'
IMAGE_SIZE = 224
EMPTY_LIST = []
EMPTY_STRING = ""
test_module_3_class = {
		"embeddings_extractor": ["gs://hd-datascience-np-artifacts/releases/com.homedepot.personalization/product-image-classifier-2.0/input-files/0.0.1/input-model-files/vgg16_embeddings_generic_3_class.h5", "gs://hd-datascience-np-artifacts/releases/com.homedepot.personalization/product-image-classifier-2.0/input-files/0.0.1/input-model-files/resnet50_embeddings_generic_3_class.h5"],
		"classifier": "gs://hd-datascience-np-artifacts/releases/com.homedepot.personalization/product-image-classifier-2.0/input-files/0.0.1/input-model-files/xgboost_random_image_filter_generic_3_class.h5",
		"classes": ["silo", "closeup", "lifestyle"],
		"opencv_feature_list": ["average_pixel_width", "touch_the_border", "dark_pctg"],
		"info": "This classifier distinguishes silo/closeup/lifestyle views"
	    }
test_module_10_class = {
            "embeddings_extractor": [],
            "classifier": "gs://hd-datascience-np-artifacts/releases/com.homedepot.personalization/product-image-classifier-2.0/input-files/0.0.1/input-model-files/vgg19_random_generic_10_class.h5",
            "classes": ["angled", "back", "front", "graphic", "lineart", "open", "set", "side", "swatch", "top"],
            "opencv_feature_list": [],
            "info": "This classifier distinguishes 10-class product views"
        }