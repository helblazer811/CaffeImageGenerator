import image

gen=image.ImageGenerator("../caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel","../caffe/models/bvlc_googlenet/deploy.prototxt","data","loss3/classifier","prob")

gen.generate_image_iterations(224+10,224+10,5,31,"imagenet/ouput1.jpg")

