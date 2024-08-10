from flask import Flask, render_template, request, redirect, url_for
import threading
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from moviepy.editor import VideoFileClip
import webbrowser


app = Flask(__name__, template_folder='templates', static_folder='static') # Set the template and static folders

recording_event = threading.Event()
video_writer = None
capture_thread = None
recording = False
ip_address = 'localhost'  # Default IP address, should be set dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
avi_path = os.path.join(BASE_DIR, 'static', 'output.avi')  # Path to your AVI file in the root
mp4_path = os.path.join(BASE_DIR, 'static', 'output.mp4')  # Output path for MP4 file


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording, capture_thread, ip_address
    if not recording:
        ip_address = request.form['ip_address']
        duration = int(request.form['duration'])
        recording = True
        capture_thread = threading.Thread(target=capture_video, args=(ip_address, duration))
        capture_thread.start()
        return redirect(url_for('recording_page'))  # Redirect to minimal UI page
    return redirect(url_for('index'))

@app.route('/view/<ip_address>')
def view(ip_address):
    return render_template('camera.html', ip_address=ip_address)

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global video_writer, recording_event, recording

    recording_event.set()

    if capture_thread is not None:
        capture_thread.join()

    if video_writer is not None:
        video_writer.release()
        video_writer = None

    recording_event.clear()
    recording = False

    if os.path.exists(avi_path):
        video_clip = VideoFileClip(avi_path)
        video_clip.write_videofile(mp4_path, codec='libx264', audio_codec='aac')
        video_clip.close()

    return render_template('replay.html')

@app.route('/recording')
def recording_page():
    return render_template('recording.html')

def capture_video(ip_address, duration):
    global video_writer, recording_event

    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f'http://localhost:5000/view/{ip_address}')  # Load the stream in the background

    width = 640
    height = 480
    fps = 1
    frame_interval = 1 / fps

    while not recording_event.is_set():
        # Create a new video writer for each loop
        video_writer = cv2.VideoWriter(avi_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
        loop_start_time = time.time()

        while not recording_event.is_set() and (time.time() - loop_start_time < duration):
            frame_start_time = time.time()

            png = driver.get_screenshot_as_png()
            nparr = np.frombuffer(png, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            frame = cv2.resize(img_np, (width, height))
            video_writer.write(frame)

            # Display the frame (optional, can be commented out)
            cv2.imshow('Do not close here! Can be closed on main recording page only!', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #print('Exiting the loop.')                     
                break

            # Calculate time taken to capture and process the frame
            processing_time = time.time() - frame_start_time
            sleep_time = frame_interval - processing_time

            # Sleep to maintain the frame rate
            if sleep_time > 0:
                time.sleep(sleep_time)

        # Ensure recording duration is correct
        actual_duration = time.time() - loop_start_time
        #print(f"Recorded {fps * duration} frames in {actual_duration:.2f} seconds.")

        video_writer.release()

        # Optionally include a short sleep between loops
        time.sleep(1)

    driver.quit()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run(host='localhost', port=5000, debug=False) # Set debug to False for production
