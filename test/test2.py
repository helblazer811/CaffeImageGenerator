import image

gen=image.ImageGenerator("../caffe/examples/cifar10_copy/cifar10_full_iter_70000.caffemodel.h5","../caffe/examples/cifar10_copy/cifar10_full.prototxt","data","ip1","prob")

gen.generate_image_iterations(64,64,2,8,"ouput.jpg")

