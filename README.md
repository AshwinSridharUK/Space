# Space
Education is one of the most powerful tools in the world, enabling youth to achieve their futures. However, accessing educational resources is growing increasingly hard with inequality across the world despite modern technology. Many cannot access the internet due to a lack of infrastructure and "Cosmodit" aims to narrow this gap through a SMS chatbot, allowing information to be accessed with minimal infrastructure across the world.

# How I Adressed The Challenge
The solution designed for the education inequality gap is a chatbot solution.

The solution allows access to (space) information anywhere in the world with basic SMS infrastructure. This technology requires minimal infrastructure and technology to use, and has a wider reach in both developed and developing nations, allowing wireless access. For this to work, students/learners simply have to send a command along with a question phrase to the SMS number, which automatically responds with a block of information. This allows for both teachers to set lesson tasks (for example) and for students to interact with a chatbot to answer any questions. This should enable increased access to education and learning, offering students the opportunities to remotely delve into topics with minimal technology at hand.

The solution allows for full remote learning, using Nasa's lessons regarding space topics, allowing for increased access to equality with minimal technology required from almost anywhere in the world. Solutions like these could help fellow high-schoolers across the world to access high-quality education and pave a better future of tomorrow.

# How I Developed This Project
SMS Chatbot
The solution was created using two main technologies: AWS Lex and Twilio.
![Image of Flowchart](https://sa-2019.s3.amazonaws.com/media/images/6f7ac7b0-0e3e-4279-a289-d3dd0ed545a0.max-1000x1000.png)

This shows the basic flowchart for how the data was being sent and received. One of the biggest issues I faced was to send data to multiple chatbots. I wanted a chatbot per topic/lesson, otherwise the process would be to complex. Whilst I was able to make multiple chatbots, the issue was to write a piece of logic to decide which one it should go to. I created a flask server (something I am new to) and wrote a small code which detects for a certain code in the text message, e.g. "PS1" would mean Pulsar Lesson 1. This would then send a message to the correct chatbot based on the unique code.

How I Used Space Agency Data in This Project
(1): The use of multiple open lessons regarding space topics were used in the solution, allowing for access via SMS. Examples include White Dwarfs, Quasars etc.

(2): The SMS solution also allows users to request data from NASA api through a simple text, making it extremely easy to access API information. In the demo, I used the RBE API and CME API from DONKI.

Project Demo
https://docs.google.com/presentation/d/1-mwThMyB9160-ozgPe8BUrha5Xhk9kitRbLqfpIDkyc/edit?usp=sharing

Data & Resources
https://imagine.gsfc.nasa.gov/science/objects/dwarfs2.html

https://www.nasa.gov/subject/8731/pulsars

https://api.nasa.gov/DONKI/CME?startDate=2017-01-03&endDate=2017-01-03&api_key=DEMO_KEY

https://api.nasa.gov/DONKI/RBE?startDate=2016-01-01&endDate=2016-01-31&api_key=DEMO_KEY

https://api.nasa.gov/DONKI/GST?startDate=2016-01-01&endDate=2016-01-30&api_key=DEMO_KEY

https://api.nasa.gov/DONKI/IPS?startDate=2016-01-01&endDate=2016-01-30&api_key=DEMO_KEY

https://api.nasa.gov/DONKI/FLR?startDate=2016-01-01&endDate=2016-01-30&api_key=DEMO_KEY

https://science.nasa.gov/astrophysics/focus-areas/black-holes

https://www.nasa.gov/audience/forstudents/5-8/features/nasa-knows/what-is-a-black-hole-58.html
