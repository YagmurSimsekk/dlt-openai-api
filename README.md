# dlt-openai-api

This documentation provides a comprehensive guide to creating a simple and efficient pipeline using the **dlt** library and the OpenAI API.

# Getting Started

## Installation

To begin, clone the repository by running the following command in your terminal:

```bash
git clone https://github.com/YagmurSimsekk/dlt-openai-api.git
```

Next, install the necessary dependencies by executing the following commands:

```bash
pip install dlt

pip install -r requirements.txt
```

## Using the ready-to-use pipeline

To run the pre-built pipeline, you will need an OpenAI API key. If you do not have one, you can create it by visiting [this link.](https://platform.openai.com/account/api-keys)

Once you have obtained your API key, store it securely in a file named *secrets.toml* located in the *.dlt* directory. Use the following line to save your key in the *secrets.toml* file:

```bash
api_secret_key = "YOUR_API_KEY_starting_with_sk-"
```

After setting up your API key, execute the following command to run the pipeline:

```bash
python openai_api.py
```

This pipeline utilizes the GPT-3.5-turbo model to generate data related to "Top AI movies." If you wish to modify the prompt message, navigate to the *openai_api.py* file and make the necessary changes within the *openai_resource* function.

Please note that altering the prompt may cause malfunctions in the streamlit app and disrupt the pipeline creation process. It might be necessary to adjust the *openai_resource* function for each unique prompt.

To view the list of the Top AI movies, execute the following command: 

```bash
streamlit run streamlit_api.py
```






