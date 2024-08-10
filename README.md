# Monitor Android Application Control Utility

## Overview

This utility is a Windows desktop application built using Flask in Python. It provides users with control over the recording and viewing of video streams from the **Monitor** Android application, which transforms your old Android phone (running Android 5.1 or later) into a security camera.

## Features

- **Local Control:** All recordings are saved directly on your desktop, ensuring complete control over your data.
- **Privacy Respecting:** No external network connections are made, and everything remains within your local network.
- **Ad-Free:** The application is completely free of advertisements, offering a seamless user experience.
- **Simple Setup:** Easily configure and start monitoring with just a few setup steps on your Android device and desktop.

## Disclaimer

This application is designed to operate strictly within your local network. **All recordings are stored locally on your desktop** where the app is running, providing full control and privacy. 

**Important:**
- This application does not support remote access; you can only view the camera feed from within your local network.
- Ensure that your network is secured with a strong password. The video stream itself is not encrypted, so if someone else is using your Wi-Fi and knows your camera's IP address, they could potentially view the feed.

## Setup Instructions

### Android Device Preparation

1. **Disable Screen Timeout:**
   - Set your Android device's screen timeout to "Never." If your device doesn’t support this, consider using an app like **Screen Alive** by Snapcore LLP (ad-free) to keep the screen on. You can uninstall the app after configuring the timeout.

2. **Turn Off Automated Screen Rotation:**
   - Go to `Settings` > `Display` and disable automatic screen rotation.

3. **Connect to Wi-Fi:**
   - Ensure your Android device is connected to the same Wi-Fi network as your desktop. The video stream is hosted on a simple web server running on your mobile device.

4. **Note the IP Address:**
   - Go to your Wi-Fi settings on your Android device. Tap on the connected SSID (Wi-Fi network name) to view the IP address, which typically looks like `192.168.1.104` (the last digits may vary). Remember or note this IP address.

### Desktop Device Setup

5. **Place the Monitor Shortcut:**
   - Place the Monitor shortcut in a convenient location on your desktop (e.g., the desktop screen itself).

6. **Run the Application:**
   - Double-click the Monitor shortcut to run the application.
   - If prompted by your antivirus software or Windows security, allow the application to run.

**Note:** This app is safe and contains no backdoors or uncontrolled features. It may be flagged by antivirus software or your operating system because it is not an officially distributed or digitally signed app.

## Usage

Once setup is complete, you can start monitoring your Android device’s camera feed from your desktop. Remember, this solution is designed for local network use only and prioritizes privacy by keeping all data within your control.

## Support the Developer

This application is ad-free and distributed on a "buy me a coffee" basis. If the app proves useful to you, please consider making a small donation:
- **$2** for a coffee with a roll
- **$1** for just a coffee

Your contributions help support further development and improvements. Constructive feedback is also welcome to help fix potential issues and enhance the application.

## Security Reminder

To ensure your setup remains secure:
- **Do not share your Wi-Fi password** with anyone who should not have access to your network.
- **Ensure your router uses a strong password** to prevent unauthorized access to your network and video stream.

---

You're now ready to monitor your environment using your Android device as a security camera! Enjoy peace of mind with complete control over your recordings.
