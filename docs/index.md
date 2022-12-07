## Introduction

This page documents the process of installing and testing an audio transcription demonstration application based on the open-source automatic speech recognition (ASR) system called [Whisper](https://openai.com/blog/whisper/), released on September 21, 2022 by OpenAI.  

Whisper is a deep neural network trained on a large (680,000 hours of recordings) and diverse dataset collected from the web.  It represents a new milestone in speech recognition with "improved robustness to accents, background noise and technical language" among other advertised features.

## Background

The effort to research and investigate an easy to deploy practical ASR application was supported by a grant from the [Institute of Museum and Library Sciences](https://www.imls.gov/) (IMLS) as part of the “Re-Imagining Access” project carried out by the members of faculty, staff and students at the ArtCenter College of Design.

During the summer of 2021, students from the studio course instructed by Elise Co, Robert Dirig, Josh Halstead, & Todd Masilko proposed the "Double Check" prototype concept as part of an answer to a question: "How might we design an archive system that ensures accessibility from beginning to end?"  The term accessibility in this context refers to the need to make archive resources designed for individuals with disabilities in mind.

The students identified a list of potential use cases and corresponding capability requirements, rated according to their priority for the accessibility checker prototype concept.  Automatic transcription of archived audio and video files was identified as one high priority item on this list.  This accessibility feature was subsequently chosen as a focus of an investigation into a potential functional solution that could in principle be integrated as a feature of the archival systems employed by ArtCenter and other institutions.

## Audience

The primary purpose of this document is to provide some context and to outline the practical instructions for how to deploy a sample ASR application, which may be of interest to anyone engaged with archival systems or simply looking for a resource to walk through the process step by step.

There are many other online resources and tutorials covering the specifics of software installation, typically written by and for programmers.  While we also assume a certain level of technical familiarity with software development, such as  the use of command line tools, an attempt is made to provide some of the more basic instructions and contextual explanations that may be helpful for a non-programmer audience.

## Archival Software

As a starting point in identifying the technical platform for a functional feature demonstration we surveyed three popular archival software systems: Archivematica, ArchivesSpace, and [Preservica](https://preservica.com/).

Each of these systems offers a full-featured archival and digital preservation solution, used by major institutions and organizations around the world.  As with all technical systems, there are significant differences in approach inherent in each solution, summarized briefly below.  Our focus in reviewing archival software was on the underlying tools and frameworks used in their development, with an eye towards choosing a platform to facilitate the integration of a functional ASR demo.

### Archivematica

[Archivematica](https://archivematica.org/) is a digital preservation system developed by the Canadian-based company [Artefactual Systems](https://www.artefactual.com/) as a "web- and standards-based, open-source application which allows your institution to preserve long-term access to trustworthy, authentic and reliable digital content."   

Archivematica uses a [micro-services](http://en.wikipedia.org/wiki/Microservices) architecture to provide an integrated suite of software tools that allows users to process digital objects from ingest to access in compliance with the [Open Archival Information System (OAIS)](http://www.oais.info/) Reference Model. The application is developed using the Python programming language and built upon the [Django](https://www.djangoproject.com/) web framework, as well as many other open-source Python frameworks and libraries.

The application was initially released as an alpha version in February 2009.  [Archivematica repository](https://github.com/artefactual/archivematica) shows that at the time of this writing, the latest code update to the stable/current version of the application (v1.13.2) was committed on December 12, 2021.  Additional [Archivematica documentation](https://www.archivematica.org/en/docs/archivematica-1.13/) and overview of the [Archivematica API](https://www.archivematica.org/en/docs/archivematica-1.13/dev-manual/api/api-overview) for developers are available on the project website.

### ArchivesSpace

[ArchivesSpace](https://archivesspace.org/) is described as an open source web application for managing archives information that supports "collection management records, tracking of events, and a growing number of  administrative reports.  The application also functions as a metadata authoring tool, enabling the generation of EAD, MARCXML, MODS, Dublin Core, and METS formatted data."   

The first version of ArchivesSpace was released in September 2013, with support from the Andrew W. Mellon Foundation and collaboration between New York University, the University of Illinois Urbana-Champaign and the University of California San Diego.  The application is developed in the Java programming language and has been tested on Linux, Mac OS X, and Windows operating systems.

[ArchivesSpace repository](https://github.com/archivesspace/archivesspace) on Github shows that it is an actively developed project (at the time of this writing the latest code update was committed on November 22, 2022).  Additional documentation and overview of the application are available at [archivesspace.atlassian.net](https://archivesspace.atlassian.net/wiki/spaces/ADC/overview).  Developer API for the latest version of ArchivesSpace is documented on [ArchivesSpace Github Pages](https://archivesspace.github.io/archivesspace/api).


## Archivematica Architecture

[TODO: summary of Archivematica as a collection of microservices]

[TODO: explanation of how auto-transcription could work within Archivematica workflow]

## Whisper ASR Demo

[TODO: explanation of the standalone Whisper demo]

### Installation Requirements

As with many contemporary open-source projects, installation of the Whisper ASR demo application requires the use of the Git version control system and the command line (Terminal application on MacOS or Linux, Terminal or PowerShell on Windows).  

As the first step, [download Git](https://git-scm.com/downloads) for your OS and run the installer. The GitHub [Install Git](https://github.com/git-guides/install-git) guide outlines the instructions for major operating systems.  To verify that the command line tool is properly configured, open the terminal and enter the following command:

```
git version
```

In addition to Git, the command line package manager tools are recommended on operating systems other than Linux.  For Windows, follow the installation instructions for the [Chocolatey](https://chocolatey.org/install) package manager.  For MacOS, install [Homebrew](https://brew.sh/).  

To check that the package manager installed successfully on your system, open the terminal and type the command appropriate for your OS (under # comment):

```
# MacOS
brew --version

# Windows
choco --version
```

Whisper is written in the Python programming language and requires a Python interpreter version 3.7 or above.  Most computers come with Python pre-installed.  To check the version installed on your computer, type:

```
python --version
```

If needed, Python can be installed or upgraded using the official installer from [https://www.python.org/downloads/](https://www.python.org/downloads/)

Whisper also requires the audio-processing library [ffmpeg](https://ffmpeg.org/).  In order to install it on the command line, run the command appropriate for your operating system:

```
# Linux
sudo apt update && sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

### Virtual Environment Setup

Prior to proceeding with the installation of necessary Python libraries, we recommend setting up a virtual environment that will contain project dependencies.  To learn more about Python virtual environments, visit [www.realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/)

To set up a virtual environment within the current project directory and activate it, type the following on the command line:

```
python -m venv venv

# MacOS or Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

If setup was successful, the command line prompt should now display the name of the virtual environment in parentheses - in this case `(venv)`  

### Rust installation

The [Rust](https://www.rust-lang.org/learn/get-started) development environment may need to be available on some systems prior to Whisper installation.  In our testing, Rust was needed for MacOS, but not Windows.

```
# MacOS
brew install rust

# other Operating Systems
# https://forge.rust-lang.org/infra/other-installation-methods.html
```

### Whisper installation

After all the preparatory steps, the Whisper library can be installed with just one command:   

```
python -m pip install git+https://github.com/openai/whisper.git
```

At this point, it should be possible to test Whisper transcription capabilities on the command line with an audio file, such as the 1-minute clip from Keith Haring's lecture included in this repository.  The command below specifies the specific Whisper model to be used for transcription with the (optional) `--model` flag:

```
whisper audio/haring_1min.mp3 --model small
```

### Whisper in a Python program

To use Whisper as a library within a standalone Python program, 4 lines of code are sufficient:  

```
import whisper

model = whisper.load_model("small")
result = model.transcribe("audio/haring_1min.mp3")
print(result["text"])
```

The sample program above is included in this repository as `whisper_test.py` and can be run with:

`python whisper_test.py`

### Whisper GUI

To provide a more user-friendly demo, we considered the options for including a Graphical User Interface on top of the Python application. 
<!--[Whisper-WebUI](https://huggingface.co/spaces/aadnk/whisper-webui)--> 
[Whisper_Transcribe](https://huggingface.co/spaces/chinhon/whisper_transcribe) is one simple example of a web application featuring an easy-to-use GUI for Whisper, built with the [Gradio](https://gradio.app/) library and deployed on HuggingFace Spaces.

To create a version of <!--Whisper-WebUI--> Whisper_Transcribe running locally, clone the repository and run a command to install the required libraries:  

<!--
```
git clone https://huggingface.co/spaces/aadnk/whisper-webui
cd whisper-webui
python -m pip install -r requirements.txt
```
-->
```
git clone https://huggingface.co/spaces/chinhon/whisper_transcribe
cd whisper_transcribe
python -m pip install -r requirements.txt
```
<!--
Next, run the `app-local.py` file with Python to launch the application:   
```
python app-local.py
```
-->

Next, run the `app.py` file with Python to launch the application:   
```
python app.py
```

If successful, the application will start a web server on your local machine that can be accessed via any browser at [http://localhost:7860](http://localhost:7860).   

The local version of the application has the same functionality as the online version, while being accessible without a network connection and able to handle lengthy audio files as input.

[TODO: Explanation of potential next steps for the project]
