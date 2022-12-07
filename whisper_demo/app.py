import gradio as gr
from pytube import YouTube
import whisper

# define function for transcription
def whisper_transcript(model_size, url, audio_file):
    if url:
        link = YouTube(url)
        source = link.streams.filter(only_audio=True)[0].download(filename="audio.mp4")

    else:
        source = audio_file

    if model_size.endswith(".en"):
        language = "english"

    else:
        language = None

    options = whisper.DecodingOptions(without_timestamps=True)

    loaded_model = whisper.load_model(model_size)
    transcript = loaded_model.transcribe(source, language=language)

    return transcript["text"]

# define Gradio app interface
gradio_ui = gr.Interface(
    fn=whisper_transcript,
    title="Transcribe multi-lingual audio clips with Whisper",
    description="**How to use**: Select a model, paste in a Youtube link or upload an audio clip, then click submit. If your clip is **100% in English, select models ending in ‘.en’**. If the clip is in other languages, or a mix of languages, select models without ‘.en’",
    article="**Note**: The larger the model size selected or the longer the audio clip, the more time it would take to process the transcript.",
    inputs=[
        gr.Dropdown(
            label="Select Model",
            choices=[
                "tiny.en",
                "base.en",
                "small.en",
                "medium.en",
                "tiny",
                "base",
                "small",
                "medium",
                "large",
            ],
            value="base",
        ),
        gr.Textbox(label="Paste YouTube link here"),
        gr.Audio(label="Upload Audio File", source="upload", type="filepath"),
    ],
    outputs=gr.outputs.Textbox(label="Whisper Transcript"),
)

gradio_ui.queue().launch()
