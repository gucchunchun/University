const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config();

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
const response = openai.createCompletion({
  model: "text-davinci-003",
  prompt: "Where to travel? answers should be in a format of json with keys(place, transportation, cost)",
  max_tokens: 2048,
  temperature: 0.8,
});

response.then(function(result) {
  console.log(result.data.choices[0].text);
});
