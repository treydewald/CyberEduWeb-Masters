Survey.StylesManager.applyTheme("modern");

var surveyJSON = {"pages":[{"name":"page1","elements":[{"type":"radiogroup","name":"question1",
            "title":"Is English your native language?","isRequired":true,"choices":["Yes","No"]},
            {"type":"radiogroup","name":"question2","title":"What is your gender?","isRequired":true,"choices":
                    ["Male","Female","Other"]},{"type":"radiogroup","name":"question3","title":"What is your age?",
                "choices":["12-23","24-38","39-50","51-65","66+"]},{"type":"radiogroup","name":"question6",
                "title":"What is the highest level of education you have received?","choices":["Less than High School",
                    "High School / GED","Some College","2-year College Degree","4-year College Degree","Master’s Degree"
                    ,"Doctoral Degree","Professional/Medical Degree (JD, MD)","Other__________________"]},
            {"type":"radiogroup","name":"question4","title":"How knowledgeable are you about computers in general?",
                "choices":["Novice","Beginner","Competent","Proficient","Expert"]},{"type":"radiogroup",
                "name":"question5","title":"Have you ever received formal training in computer science" +
                    ", software engineering, IT, computer networks, or a related technical field?",
                "choices":["Yes","No"]}]}]}

function sendDataToServer(survey) {
    //send Ajax request to your web server.
    alert("The results are:" + JSON.stringify(survey.data));
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});