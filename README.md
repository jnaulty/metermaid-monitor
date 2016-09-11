# metermaid-monitor
Avoidance, Awareness, and Prevention. Tensorflow, PiCamera, and Metermaids. A Citizen's lovestory.

The purpose of this project was to provide a cheap alternative to worry about parking. People who park in residential areas, especially in `2 hour` limited parking will know the desire to park for as long as available. Normally what ruins that availability is the dreadful driveby of a metermaid [`Interceptor`](https://www.google.com/search?q=images+interceptor+metermaid&safe=off&espv=2&biw=1321&bih=659&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjjob2Ap4fPAhVfVWMKHaieC-YQ_AUIBigB). With this set of tools, one can park their car, knowing that a notification will arrive via text message notifying them of a passing metermaid. This _should_ mark their 'official' 2 hour parking time limit. As the metermaid should only be able to assume the car had just parked there.

We combined Tensorflow image classification with a raspberry pi motion detection and speed measuring program.


When Image is captured (moving car is in field of view), the image is sent for analysis to an instance running Tensorflow, with trained data.
If image is a match, a message is sent via twilio with a link to the image for human verification.

PiCamera Car Monitor --> TensorFlow Classification --> SMS Message

- Requires Installation of OpenCV 3.0.0 and Python3 and wifi-hotspot (for raspberry pi)
- Tensorflow was ran in docker following this [tutorial](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html?index=..%2F..%2Findex#5)
- Pictures were shamelessly downloadedfrom Google Images. 


**This is a free, open-source project and the developers are in _no_way_ accountable for parking tickets because of rebellious, citation-breaking citizens. 

Special Thanks
- Google [TensorFlow](https://www.tensorflow.org/)
- [Greg Tinkers](https://gregtinkers.wordpress.com/2016/03/25/car-speed-detector/) for his blog and car speed script.
- [@psukhanov](https://github.com/psukhanov) Partner in ~~parking~~ crime.
