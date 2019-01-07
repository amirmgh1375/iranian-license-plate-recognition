
    # result = cv2.rotate(plate, rotateCode=0)
    # image_center = tuple(np.array(plate.shape[1::-1]) / 2)
    # rot_mat = cv2.getRotationMatrix2D(image_center, 20, 1.0)
    # result = cv2.warpAffine(plate, rot_mat, plate.shape[1::-1], flags=cv2.INTER_LINEAR)