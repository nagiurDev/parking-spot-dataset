import os
import cv2
import matplotlib.pyplot as plt


def frame_extracted_status(output_path: str) -> list:
    """
    Check the status of extracted frames.
    
    Args:
    output_path (str): The path to the output directory.
    
    Returns:
    list: A list of videos already extracted.
    """
    
    print(f"Checking status of extracted frames at {output_path}...")
    
    all_raw_videos = os.listdir(raw_video_path)
    all_raw_videos = [video.replace(".mp4", "") for video in all_raw_videos if video.endswith(".mp4")]

    exist_extraction = []

    if os.path.exists(output_path):
        print("0. Video already extracted : ")
        for frames_exist_dir in sorted(os.listdir(output_path)):
            exist_extraction.append(frames_exist_dir)
            frames_exist_dir_path = os.path.join(output_path, frames_exist_dir)

            if os.path.isdir(frames_exist_dir_path):
                img_count = len([frame for frame in os.listdir(frames_exist_dir_path) 
                                if os.path.isfile(os.path.join(frames_exist_dir_path, frame))])
                
                print(f"\tThe directory '{frames_exist_dir}' contains {img_count} images in total.")

    else:
        os.makedirs(output_path)
        print("Video not yet extracted.")

    remain_extraction = sorted(list(set(all_raw_videos) - set(exist_extraction)))
    print(f"1. Total - {len(all_raw_videos)} videos")
    print(f"2. Remaining to be extracted - {len(remain_extraction)} videos:")
    for i, video in enumerate(remain_extraction):
        print(f" {video}", end='\n' if (i+1) % 10 == 0 else '  ')

    print("\n")
    print(f"3. Already extracted - {len(exist_extraction)} videos: {exist_extraction}")

    print("-----------------------------------------------------------------")

    return exist_extraction
    

def extract_frames_on_skipping(raw_video_path: str, output_path: str, exist_extraction: list) -> None:
    """Extract frames from a video file and save them as images."""

    video_name = input("Enter video name: ")
    video_path = os.path.join(raw_video_path, f"{video_name}.mp4")

    cap = cv2.VideoCapture(video_path)

    output_dir = os.path.join(output_path, video_name)

    if exist_extraction and video_name in exist_extraction:
        response = input(f"Output directory '{output_dir}' already exists. Do you want to extract again? (y/n): ")
        if response.lower() != 'y':
            print("Skipping extraction.")
            return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    skip_frames = 1
    for frame_id in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % skip_frames == 0:

            frame_name = f"{video_name}_{frame_id:04d}_0.jpg"
            frame_path = os.path.join(output_dir, frame_name)
            counter = 1
            while os.path.exists(frame_path):
                frame_name = f"{video_name}_{frame_id:04d}_new_{counter}.jpg"
                frame_path = os.path.join(output_dir, frame_name)
                counter += 1

            cv2.imwrite(frame_path, frame)


            print(f"Extracted frame {frame_name} from video {video_name}.")
    cap.release()


def extract_frames_on_motion(raw_video_path: str, output_path: str, exist_extraction: list, threshold: int = 25, min_motion_frames: int = 5) -> None:
    """Extract frames from a video file and save them as images."""

    video_name = input("Enter video name: ")
    video_path = os.path.join(raw_video_path, f"{video_name}.mp4")
    print(f"Video path: {video_path}")

    cap = cv2.VideoCapture(video_path)
    output_dir = os.path.join(output_path, video_name)

    if exist_extraction and video_name in exist_extraction:
        response = input(f"Output directory '{output_dir}' already exists. Do you want to extract again? (y/n): ")
        if response.lower() != 'y':
            print(f"Skipping extraction for video {video_name}.")
            return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Initialize variables for motion detection
    ret, prev_frame = cap.read()
    if not ret:
        print(f"Unable to read video {video_name}.")
        return

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    motion_frame_count = 0
    frame_id = 0
    extracted_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video reached or unable to read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Compute the difference between the current frame and the previous frame
        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, threshold, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Calculate motion level
        motion_level = cv2.countNonZero(thresh)
        print(f"Frame {frame_id}: Motion level = {motion_level}")

        # Check if the current frame has significant motion
        if motion_level > 0:
            motion_frame_count += 1
            print(f"Motion detected (count = {motion_frame_count})\n")
        else:
            motion_frame_count = 0

        # Extract frame if motion is detected continuously for the minimum required frames
        if motion_frame_count >= min_motion_frames:
            frame_name = f"{video_name}_{frame_id:04d}_0.jpg"
            frame_path = os.path.join(output_dir, frame_name)

            # Ensure that duplicate frame names are avoided
            counter = 1
            while os.path.exists(frame_path):
                frame_name = f"{video_name}_{frame_id:04d}_{counter}.jpg"
                frame_path = os.path.join(output_dir, frame_name)
                counter += 1

            # Save the extracted frame
            cv2.imwrite(frame_path, frame)
            print(f"Extracted motion frame {frame_name} from video {video_name}.")
            extracted_count += 1
            motion_frame_count = 0  # Reset motion frame count after saving a frame

        # Update the previous frame
        prev_gray = gray
        frame_id += 1

    cap.release()
    print("-----------------------------------------------------------------")
    print(f"Extracted {extracted_count} frames from video {video_name} based on motion detection.\n")



if __name__ == "__main__":
    raw_video_path = "../data/raw_videos/"
    output_path = "../data/extracted_frames/"
    
    exist_extraction = frame_extracted_status(output_path)

    extract_frames_on_motion(raw_video_path, output_path, exist_extraction)
