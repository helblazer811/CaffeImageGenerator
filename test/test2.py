import image

gen=image.ImageGenerator("../caffe/examples/cifar10_copy/cifar10_full_iter_70000.caffemodel.h5","../caffe/examples/cifar10_copy/cifar10_full.prototxt","data","ip1","prob")

gen.generate_image_iterations(72,72,100,8,"ouput.jpg",8)

