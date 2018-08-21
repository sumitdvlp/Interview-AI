# Interview.AI
The objective of this project is to find the best behavioral fit between candidates and companies with respect to their long term association with the company and satisfaction level with the job. The hack achieves this by creating a virtual interview system that asks a series of questions to the candidates and runs a complex machine learning algorithm to analyse the responses and calculate the satisfaction factor of the candidate on the scale of 0 to 1. Each company can define their own satisfaction factor to filter out candidates. For the hackathon, a satisfaction factor greater than 0.5 has been identified to denote a fit with the company where the company would like to move forward with the candidate in the interview process after the screening round via Interview.AI. The data is sourced from Kaggle to build the classification model based on Support Vector Machine (SVM). The Prediction model of the satisfaction level is based on the quantification of the following factors: time spent in previous company, number of projects involved, salary level, average hours worked weekly, last evaluation, promotion, work accident and still working or not. The hack also eliminates any bias which the companies may have while screening the candidates and automates the tedious task of initial screening of candidates.

The project is an attempt to address the challenge of finding the best fit candidates out of a huge number of applicants which is a pressing demand of modern day recruiting. It also finds itself aligned with the objectives of the startup Olivia-Recruiting.AI which is trying to solve the recruitment process with a meaningful use of AI.

The intelligent interview system utilizes the Voice UI interface of the Amazon Alexa to ask behavioral questions to the candidates to give a virtual feel of the interview.

## Setup
![alt text](https://github.com/sumitdvlp/Interview-AI/blob/master/arch.jpg)

### Machine Learning Algortihm
1. Install Google Machine Learning framework in python, TensorFlow.
2. Run the python script in /MachineLearning directory to get the optimized weights and bias for the Support Vector Machine (SVM) classifier based on your gradient descent. (We have done that and using it in our model).

To run this skill you need to do two things. The first is to deploy the example code in lambda, and the second is to configure the Alexa skill to use Lambda.

### AWS Lambda Setup
1. Go to the AWS Console and click on the Lambda link. Note: ensure you are in us-east or you wont be able to use Alexa with Lambda.
2. Click on the Create a Lambda Function or Get Started Now button.
3. Skip the blueprint
4. Name the Lambda Function "Interview".
5. Select the runtime as Java 8
6. Go to the the /alexa-skills-EHR/ directory containing pom.xml, and run 'mvn assembly:assembly -DdescriptorId=jar-with-dependencies package'. This will generate a zip file named "alexa-skills-kit-samples-1.0-jar-with-dependencies.jar" in the target directory.
7. Select Code entry type as "Upload a .ZIP file" and then upload the "alexa-skills-kit-samples-1.0-jar-with-dependencies.jar" file from the build directory to Lambda
8. Set the Handler as EHRSystem.EHRsystemSpeechletRequestStreamHandler (this refers to the Lambda RequestStreamHandler file in the zip).
9. Create a basic execution role and click create.
10. Leave the Advanced settings as the defaults.
11. Click "Next" and review the settings then click "Create Function"
12. Click the "Event Sources" tab and select "Add event source"
13. Set the Event Source type as Alexa Skills kit and Enable it now. Click Submit.
14. Copy the ARN from the top right to be used later in the Alexa Skill Setup.

### Alexa Skill Setup
1. Go to the [Alexa Console](https://developer.amazon.com/edw/home.html) and click Add a New Skill.
2. Set "Interview" as the skill name and "Interview" as the invocation name, this is what is used to activate the skill. For example you would say: "Alexa, start the Interview."
3. Select the Lambda ARN for the skill Endpoint and paste the ARN copied from above. Click Next.
4. Copy the Intent Schema from the included IntentSchema.json.
5. Copy the Sample Utterances from the included SampleUtterances.txt. Click Next.
6. Go back to the skill Information tab and copy the appId. Paste the appId into the EHRSystemSpeechletRequestStreamHandler.java file for the variable supportedApplicationIds,
   then update the lambda source zip file with this change and upload to lambda again, this step makes sure the lambda function only serves request from authorized source.
7. You are now able to start using the skill! You should be able to go to the [Echo webpage](http://echo.amazon.com/#skills) and see the skill enabled.
8. In order to test it, try to say some of the Sample Utterances from the Examples section below.
9. The skill is now saved and once you are finished testing you can continue to use it.

### Examples
#### One-shot model:
    User: "Alexa, start the Interview."
    Alexa: "Welcome to your virtual interview!"

## Alexa Skills Kit Documentation
The documentation for the Alexa Skills Kit used in this project is available on the [Amazon Apps and Services Developer Portal](https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit/).

## Resources
Here are a few direct links to Amazon's documentation that helped us in our project:

- [Using the Alexa Skills Kit Samples](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/using-the-alexa-skills-kit-samples)
- [Getting Started](https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit/getting-started-guide)
- [Invocation Name Guidelines](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/choosing-the-invocation-name-for-an-alexa-skill)
- [Developing an Alexa Skill as an AWS Lambda Function](https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function)

