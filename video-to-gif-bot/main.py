import argparse
import cv2


def main(path):
    # create object capture video
    vid_capture = cv2.VideoCapture(path)

    print(dir(vid_capture))

    if vid_capture.isOpened():
        fps = vid_capture.get(5)
        print("Frame per second: ", fps, "FPS")
        frame_count = vid_capture.get(7)
        print("Frame frequency:", frame_count)
        print("Click to finish q or ESC...")
    else:
        print("Ошибка открытия видеофайла")

    file_count = 0
    while vid_capture.isOpened():
        ret, frame = vid_capture.read()
        if ret == True:
            cv2.imshow("Look", frame)
            file_count += 1
            # print('Frame {0:04d}'.format(file_count))


            key = cv2.waitKey(40)

            if key == ord('q') or key == 27:
                break
        else:
            break
    vid_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_video")
    main(parser.parse_args().path_to_video)
