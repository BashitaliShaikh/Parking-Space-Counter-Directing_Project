Here’s an updated version of your README file with your implementation details, future scope, and mobile interaction sections:

```markdown
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alperrkilic/Parking-Space-Counter-Project">
    <img src="readme-images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Parking Space Counter</h3>

  <p align="center">
    A Parking Space Counter Project
    <br />
    <a href="https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project">View Demo</a>
    ·
    <a href="https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#images">Images</a></li>
    <li><a href="#implementation">Implementation</a></li>
    <li><a href="#future-scope">Future Scope</a></li>
    <li><a href="#mobile-interaction">Mobile Interaction</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

The Parking Space Counter project is designed to help parking lot operators or drivers quickly and easily determine the number of available parking spaces in a lot. By using computer vision techniques to analyze video footage of the lot, the system can accurately count the number of open spaces and make this information available in real-time. This project can be easily applied to any parking space with just a camera and a computer, helping people find available parking spots quickly and easily.

Here's why:
* Saves time and reduces frustration: Finding a free parking space can be a challenge, especially in busy areas. With the Parking Space Counter, you can quickly and easily locate available parking spots without having to drive around and waste time searching.
* Increases efficiency and maximizes space utilization: By accurately counting the number of available parking spaces, the Parking Space Counter allows parking lot operators to make more informed decisions about space utilization. This can help increase efficiency, reduce congestion, and ultimately make the parking experience better for everyone involved.

In conclusion, the Parking Space Counter is a powerful tool that utilizes computer vision techniques to accurately count the number of available parking spaces in a given lot. With its customizable parameters and easy-to-use interface, the system is ideal for anyone looking to manage or navigate a busy parking lot. By using this tool, drivers can save time and reduce frustration, while parking lot operators can increase efficiency and maximize space utilization. Whether you're managing a large commercial lot or just looking for a free parking spot in a busy area, the Parking Space Counter is the solution you've been looking for.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The Parking Space Counter is a project that uses OpenCV and Python to count the number of available parking spaces in a given parking lot.

* [![Python][Python]][Python-url]
* [![openCV][openCV]][openCV-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The Parking Space Counter is a project that uses OpenCV and Python to count the number of available parking spaces in a given parking lot. In this project, parking spaces are counted according to the pixels that are counted from a dilated image. If the number of pixels are above 900, then the space is considered to be not available. However, if the number of pixels are below 900, then the space is considered to be an empty parking space.

Additionally, this project includes a script called ParkingSpacePicker.py, which allows you to manually add a parking space to the list of spaces to be checked.

### Prerequisites

To install the required files, please enter the following commands into your terminal: 
* pip
  ```sh
  pip install opencv-python 
  ```
  ```sh
  pip install cvzone
  ```
  ```sh
  pip install numpy
  ```

### Installation

_Installing the Parking Space Counter is quick and easy. Follow these simple steps to get started in just a few minutes!_

1. Create your virtual environment with Pycharm
2. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project
   ```
3. Install the required dependencies:
   ```sh
   pip install opencv-python numpy cvzone
   ```
   _Note: This project is built with Python 3.8, so make sure you have it installed on your machine._
4. Open the project in Visual Studio Code or your preferred code editor.
   ```js
   That's it! You're now ready to use the Parking Space Counter project.
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Images -->
## Images

[![Screen Shots][parking-spaces-to-be-checked]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_Places that are considered as parking spaces manually selected with ParkingSpacePicker.py_


<tr>
    <td>
      <img src="readme-images/single-parking-frame.png"></img>
    </td>
    <td>
      <img src="readme-images/single-parking-frame-without-rectangle.png"></img>
    </td>
</tr>

_After selecting the parking spaces, storing them into CarParkPos file and splitting each frame that are selected with ParkingSpacePicker.py_

[![Screen Shots][blurred-img]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_Blurring the image after making it grayscale_

[![Screen Shots][threshold-img]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_Converting image into a binary image with Thresholding_

[![Screen Shots][dilated-img]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_After thresholding, to remove unwanted white pixels we are dilating the threshold image_

[![Screen Shots][median-img]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_To adjust the thickness, we're generating the median image_

<tr>
    <td>
      <img src="readme-images/single-frame-after-dilation-empty-space.png">
      </img>
    </td>
    <td>
      <img src=" readme-images/single-frame-after-dilation-car-parked.png">
      </img>
    </td>
</tr>

_After dilation and median images, it's evident whether there's a car in a parking spot or not._

[![Screen Shots][spaces-with-counters]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_Now, on our original dilated image, we can count the white pixels and display their numbers on the image. If a parking space is empty, the number of white pixels is expected to be less than 900. However, if the number of white pixels is more than 900, it is an indication that there is a car present in the parking space._


[![Screen Shots][product-screenshot]](https://github.com/BashitaliShaikh/Parking-Space-Counter-Directing_Project)

_Finally, we count the number of available parking spaces and draw rectangles around each parking spot. If a parking space is available, we mark it with a green color, and if it is occupied, we mark it with a red color._


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Implementation

This project uses OpenCV and Python to detect empty parking spaces in a parking lot. The process is as follows:
1. **Camera Setup:** The camera captures real-time footage of the parking lot.
2. **Image Preprocessing:** Images are first converted to grayscale, blurred for noise reduction, and then thresholded to create a binary image where the parking spots are distinguishable.
3. **Detection:** Using contours, the project identifies parking spaces and checks whether each space is occupied based on the pixel count.
4. **Counting:** The number of empty spaces is calculated based on the number of pixels detected in the thresholded image.
5. **Display:** Available parking spaces are marked with green rectangles, and occupied spots are marked with red rectangles, with the count of available spaces displayed in real time.

This system can be enhanced with real-time notifications and integration with existing parking management systems.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Scope

The future scope of this project includes:
- **Real-Time Parking Management Integration:** Integrating this project into a larger parking management system to automate parking assignments and payments.
- **Cloud-Based Reporting:** Creating a cloud-based dashboard where users can check the real-time availability of parking spaces.
- **AI-Powered Vehicle Detection:** Enhancing the system with AI-powered models to better detect different types of vehicles in a parking space, such as motorcycles and larger vehicles.
- **Adaptive System:** Developing the system to automatically adapt to changes in parking space layouts or lighting conditions.
- **Long-Term Monitoring:** Implementing a long-term monitoring system to track parking trends and optimize parking space allocation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Mobile Interaction

This project can be adapted to work with mobile applications, enabling users to view real-time parking availability directly from their smartphones. Some features for mobile integration include:
- **Mobile App for Parking Availability:** A mobile app that allows users to view available parking spaces and navigate to them.
- **Push Notifications:** Notify users when parking spaces become available.
- **Camera Integration:** Use the phone’s camera for localized parking space detection for smaller lots.
- **QR Code Scanning:** Users can scan QR codes at parking entrances to check space availability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bashitali Shaikh - [@bashitalishaikh](https://www.linkedin.com/in/bashitali-shaikh-3b590616a/) - bashitalishaikh@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Creating a project like the Parking Space Counter requires a lot of research, experimentation, and dedication. I would like to take this opportunity to acknowledge and thank the many individuals, channels, and websites that helped me along the way. Without their guidance and support, this project would not have been possible. In particular, I would like to recommend the following channels and websites for their invaluable resources and contributions to the field of computer vision and image processing.

* [Computer Vision Zone](https://www.computerv

ision.zone/)
* [OpenCV Documentation](https://docs.opencv.org/4.x/)
* [Python Documentation](https://docs.python.org/3/)
* [OpenCV Python Tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

This README now covers the steps for installation, the images of the system in action, detailed implementation steps, and future plans to improve and expand the project, including integration with mobile applications.
