import image

gen=image.ImageGenerator("caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel","caffe/models/bvlc_googlenet/deploy.prototxt","data","loss3/classifier","prob")
for i in range(1):
    gen.generate_number_image(224,224,5000,31,"imagenet/ouput"+str(i)+".jpg")

