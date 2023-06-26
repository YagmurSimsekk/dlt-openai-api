import dlt
import openai
import re
from dlt.sources.helpers import requests


@dlt.source
def openai_source(api_secret_key=dlt.secrets.value):
    return openai_resource(api_secret_key)


def _create_auth_headers(api_secret_key):
    """Constructs Bearer type authorization header which is the most common authorization method"""
    headers = {"Authorization": f"Bearer {api_secret_key}"}
    return headers


@dlt.resource(write_disposition="append")
def openai_resource(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    # check if authentication headers look fine
    print(headers)

    openai.api_key = api_secret_key

    # make an api call here
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": "name top AI movies"}],
        temperature=1,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0.25,
        presence_penalty=0
    )

    ai_response  = response['choices'][0]['message']['content']
    
    # finding all occurrences of a pattern in the response
    movies = re.findall(r'\d+\.\s(.+?)\s\((\d+)\)', ai_response)

    yield movies


if __name__ == "__main__":
    # configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name='openai_data', destination='duckdb', dataset_name='ai_movies'
    )

    #extract data
    data = openai_resource()

    # print the data yielded from resource
    print(data)
    # exit()

    # run the pipeline with your parameters
    load_info = pipeline.run(data, table_name= "movies")

    # pretty print the information on data that was loaded
    print(load_info)


