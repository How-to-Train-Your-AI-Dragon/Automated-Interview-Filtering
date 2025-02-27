# Setting Up the Environment

<code>conda create -n automated_interview_filtering python=3.10.14</code>

<code>pip install -r requirements.txt</code>

<code>brew install ffmpeg</code>

</br>

# Creating a .env file

Create a <code>.env</code> file at the same directory level as this <code>ENV_SETUP.md</code> file, following the required field as listed in <code>.env.example</code>. You may visit the following to create free trial accounts and obtain your API keys:

- Llamaparse: <a href='https://cloud.llamaindex.ai/login'>https://cloud.llamaindex.ai/login</a>
- OpenAI: <a href='https://platform.openai.com/playground'>https://platform.openai.com/playground</a>
- Nvidia NIMs: <a href='https://build.nvidia.com/nvidia'>https://build.nvidia.com/nvidia</a>

</br>

# Running the Sample Code

<code>conda activate automated_interview_filtering</code>

<code>python -m src.main_test</code>

You can choose to either use NVIDIA-NIMs or OpenAI as the LLM Provider. This can be changed by selecting the YAML config files in <code>src/main_test.py</code>

</br>

# NOTE

<code>src/main_test.py</code> is a sample usage of the backend code. Please refer to <code>src/sample_inputs.py</code> for example of what the required input fields are.