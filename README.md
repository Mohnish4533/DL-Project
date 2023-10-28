# DL-Project
<h1> Music Recomendation System using Sentiment Analysis</h1>

<p> DL project is of 2 parts:<br>
1. Sentiment Analysis
2. Recommendation System
</p>

<h3><i> 1. Sentiment analysis</i></h3>
<p> - Creating Sentiment analysis model using 2 kaggle datasets<br>
a. https://www.kaggle.com/datasets/parulpandey/emotion-dataset?select=test.csv<br>
b. https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text/data<br>
</p><br><br>

<h3> Steps to run the model directly: </h3>
<p> i . You will need --> BoW_Vocab.txt, Sentiment_Prediction_Model.txt & Model_Application.py in the same location<br>
ii. Run the Model_Application.py file and give user input</p>

<p> For reference : OUTPUT for will be numeric digits which map to emotion experienced.</p><br>
<p> <b>MAPPING</b><br>
MAIN EMOTION     --     SUB EMOTIONS<br>
- sadness(0)     --     sadness, boredom, surprise <br> 
- joy(1)         --     enthusiasm, happiness, fun, neutral<br>
- love(2)        --     love<br>
- anger(3)       --     hate, anger, empty, relief<br>
- fear (4)       --     worry, <br><br>


* NOTE: Pre processing task can be improved *

<h3><i> 2. Recommendation System</i></h3>
<p> The recommendation system is built using Spotify Web API . <br> OAuth 2.0 flow type used : Client credentials <br>

<h4><b><i> Steps to run CLI App</i></b></h4>
<p>1. Install dependencies:<br>
<pre>
pip install python-dotenv
pip install requests
pip install json
</pre>
2. At 'App.py' directory add a file named '.env'. In this file type the below code: 
<pre> 
CLIENT_ID = <client_id_in_quotes> # mention your spotify api client id
CLIENT_SECRET = <client_secret_in_quotes> # mention your spotify api client secret in codes
</pre>
3. Open App.py and run <br></p>


