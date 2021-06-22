import pyqrcode
import png
from pyqrcode import QRCode

# Links which represent the QR codes
link1 = "https://www.linkedin.com/in/sinchan-panda-aab615212/"
link2 = "https://github.com/sinchan1999"

# Representing my dummy details in QR code
studentDetails = "Name: SINCHAN PANDA\nRoll: 1704522 \n Branch: EEE\n KIIT UNIVERSITY, Bhubaneswar"


# Generating QR codes
url1 = pyqrcode.create(link1)
url2 = pyqrcode.create(link2)

info = pyqrcode.create(studentDetails)


# Saving the png file naming "myProfile.png"
url1.png("myProfile.png", scale=4)
url2.png("myGithubProfile.png", scale=4)

info.png("studentDetails.png", scale=4)
