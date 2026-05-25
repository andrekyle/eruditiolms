"""Second-wave AI-901 quiz coverage: backfill questions targeting the new
AI-901 Foundry-implementation bullets (skills measured as of April 15, 2026).
This runs IN ADDITION to ai901_quiz_coverage_v1 (which covered the core AI
concept bullets carried over from AI-900). Idempotent.

Quiz -> Lesson:
  45 -> L3 Responsible AI
  46 -> L4 AI model components & configurations (how gen-AI models work, model
        selection, deployment options/parameters)
  47 -> L5 AI workloads (gen+agentic AI, text analysis, speech, CV, info extraction)
  48 -> L6 Generative AI apps & agents in Foundry
  49 -> L7 Text & speech in Foundry
  50 -> L8 Vision, image-gen, and information extraction in Foundry
"""
from __future__ import annotations
from app import app, db, Question, QuestionOption

MARKER = "<!-- ai901_coverage_v2 -->"


def add_question(quiz_id: int, prompt_html: str, options: list[tuple[str, bool]],
                 feedback: str, points: float = 1.0) -> None:
    qhtml = f"{MARKER}\n{prompt_html}"
    existing = (
        Question.query
        .filter_by(quiz_id=quiz_id)
        .filter(Question.question_html == qhtml)
        .first()
    )
    if existing is not None:
        return
    q = Question(
        quiz_id=quiz_id,
        question_type="multiple_choice",
        question_html=qhtml,
        points=points,
        feedback=feedback,
    )
    db.session.add(q)
    db.session.flush()
    for idx, (text, is_correct) in enumerate(options, start=1):
        db.session.add(QuestionOption(
            question_id=q.id,
            option_html=text,
            is_correct=is_correct,
            order=idx,
        ))


# ----------------------------------------------------------------------
# Quiz 46 — AI model components & configurations (AI-901)
# ----------------------------------------------------------------------
QUIZ_46 = [
    (
        "Which statement best describes how a modern generative AI model "
        "produces text?",
        [
            ("It predicts the next token in a sequence by sampling from a probability distribution learned during training", True),
            ("It looks up the answer in a fixed FAQ database", False),
            ("It runs a SQL query against the prompt", False),
            ("It compiles the prompt to assembly code", False),
        ],
        "LLMs generate text autoregressively, one token at a time, by sampling "
        "from a learned probability distribution.",
    ),
    (
        "You need a model that can take both an image and a text prompt and "
        "produce a natural-language answer. Which model capability should you "
        "look for?",
        [
            ("A multimodal model (e.g., GPT-4o)", True),
            ("A text-only embeddings model", False),
            ("A speech-to-text model", False),
            ("A tabular regression model", False),
        ],
        "Multimodal models accept multiple input modalities (text + image + "
        "sometimes audio) and reason across them.",
    ),
    (
        "You only need to convert text passages into vectors for similarity "
        "search. Which model type is most appropriate?",
        [
            ("An embeddings model (e.g., text-embedding-3)", True),
            ("A reasoning chat model", False),
            ("An image-generation model", False),
            ("A speech synthesis model", False),
        ],
        "Embeddings models output fixed-length vectors used for similarity / "
        "RAG retrieval, not chat responses.",
    ),
    (
        "Cost and latency are critical and the task is simple classification "
        "of short customer messages. Which model choice is most appropriate?",
        [
            ("A small language model (SLM) such as Phi", True),
            ("The largest available frontier reasoning model", False),
            ("A diffusion image-generation model", False),
            ("A speech translation model", False),
        ],
        "SLMs offer lower latency and cost and are usually sufficient for "
        "narrow, well-defined tasks.",
    ),
    (
        "Which model deployment option in Foundry/Azure OpenAI gives the most "
        "predictable throughput by reserving capacity in advance?",
        [
            ("Provisioned throughput units (PTU)", True),
            ("Standard (pay-as-you-go) deployment", False),
            ("Local CPU deployment", False),
            ("Free playground only", False),
        ],
        "PTU deployments reserve dedicated capacity, providing stable latency "
        "and throughput for production workloads.",
    ),
    (
        "Which inference parameter most directly controls how random or "
        "creative the model's output is?",
        [
            ("Temperature", True),
            ("Max tokens", False),
            ("Stop sequences", False),
            ("Frequency penalty", False),
        ],
        "Lower temperature -> more deterministic; higher temperature -> more "
        "varied/creative responses.",
    ),
    (
        "Which parameter caps the length of the model's response?",
        [
            ("Max tokens (max output tokens)", True),
            ("Temperature", False),
            ("Top-p", False),
            ("Presence penalty", False),
        ],
        "Max tokens limits how many tokens the model is allowed to generate.",
    ),
    (
        "Which parameter restricts the model to sample from only the smallest "
        "set of tokens whose cumulative probability exceeds a threshold?",
        [
            ("Top-p (nucleus sampling)", True),
            ("Frequency penalty", False),
            ("Stop sequence", False),
            ("Temperature only", False),
        ],
        "Top-p (nucleus) sampling truncates the candidate token set to those "
        "summing to a target probability mass.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 47 — AI workloads (AI-901 adds info-extraction + agentic AI focus)
# ----------------------------------------------------------------------
QUIZ_47 = [
    (
        "Which scenario is best described as an <strong>agentic AI</strong> "
        "workload rather than a plain generative-AI workload?",
        [
            ("An AI assistant that, given a goal, plans steps, calls tools/APIs, and acts on the user's behalf to complete the task", True),
            ("A model that produces a single email draft from bullet points", False),
            ("A model that translates one sentence to French", False),
            ("A model that classifies an image as cat or dog", False),
        ],
        "Agentic AI involves goal-driven planning + tool use + autonomous "
        "execution across multiple steps.",
    ),
    (
        "Pulling structured fields out of a stack of scanned purchase orders "
        "is best described as which AI workload?",
        [
            ("Information extraction (document/forms understanding)", True),
            ("Image classification", False),
            ("Speech synthesis", False),
            ("Anomaly detection", False),
        ],
        "Extracting structured data from documents/forms is the information-"
        "extraction workload.",
    ),
    (
        "Reducing a 10-page report to a 200-word executive summary is which "
        "text-analysis technique?",
        [
            ("Summarization", True),
            ("Keyword extraction", False),
            ("Entity detection", False),
            ("Sentiment analysis", False),
        ],
        "Summarization condenses long text while preserving meaning.",
    ),
    (
        "Identifying that the word 'Paris' in a sentence refers to a city "
        "(rather than the singer) is which text-analysis technique?",
        [
            ("Entity detection (named entity recognition)", True),
            ("Sentiment analysis", False),
            ("Keyword extraction", False),
            ("Summarization", False),
        ],
        "NER tags spans with entity types like Person, Organization, Location, "
        "DateTime.",
    ),
    (
        "Which is an example of an <strong>information-extraction</strong> "
        "workload over <em>audio and video</em>?",
        [
            ("Pulling speakers, topics, and key moments from a meeting recording", True),
            ("Generating a photorealistic image of a cat", False),
            ("Drafting marketing copy from bullet notes", False),
            ("Performing a regression on house prices", False),
        ],
        "Audio/video info extraction surfaces speakers, transcripts, topics, "
        "and timecoded moments.",
    ),
    (
        "Which is the best example of an <strong>image-generation</strong> "
        "workload (as opposed to a computer-vision analysis workload)?",
        [
            ("Producing a brand-new product mock-up from a text prompt", True),
            ("Counting cars in a parking-lot photo", False),
            ("Detecting a face in a security camera frame", False),
            ("Extracting text from a scanned receipt", False),
        ],
        "Image generation creates new images from prompts; CV analysis "
        "describes existing images.",
    ),
    (
        "Reading aloud the day's news headlines to a smart speaker user is "
        "which speech capability?",
        [
            ("Speech synthesis (text-to-speech)", True),
            ("Speech recognition", False),
            ("Speech translation", False),
            ("Speaker recognition", False),
        ],
        "Speech synthesis converts text into spoken audio.",
    ),
    (
        "Tagging product reviews as positive, neutral, or negative is which "
        "text-analysis technique?",
        [
            ("Sentiment analysis", True),
            ("Entity detection", False),
            ("Keyword extraction", False),
            ("Summarization", False),
        ],
        "Sentiment analysis assigns polarity / opinion labels to text.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 48 — Generative AI apps & agents in Foundry
# ----------------------------------------------------------------------
QUIZ_48 = [
    (
        "When building a generative-AI chat app, what is the primary purpose "
        "of the <strong>system prompt</strong>?",
        [
            ("To set the model's persona, behavior, scope, and safety constraints for the whole conversation", True),
            ("To capture the end user's question for this turn", False),
            ("To store the API key", False),
            ("To define the database schema", False),
        ],
        "The system prompt fixes the model's role/policy; user prompts vary "
        "turn by turn.",
    ),
    (
        "Which prompt-engineering technique most directly reduces hallucinated "
        "facts in a Foundry chat app?",
        [
            ("Grounding the model with retrieval-augmented generation (RAG) over trusted documents", True),
            ("Increasing temperature to 1.5", False),
            ("Removing the system prompt", False),
            ("Disabling content filters", False),
        ],
        "Grounding via RAG forces the model to cite from a trusted knowledge "
        "source, cutting hallucinations.",
    ),
    (
        "In the Foundry portal, what is the typical path to <strong>deploy a "
        "model</strong> so you can interact with it?",
        [
            ("Open the model catalog, choose a model, click Deploy to create an endpoint, then use the playground or SDK to call it", True),
            ("Email the Azure team to manually copy weights", False),
            ("Edit a Bicep template by hand and run az deployment", False),
            ("Upload a model into Azure Cosmos DB", False),
        ],
        "Foundry's model catalog -> Deploy flow is the standard path to a "
        "callable endpoint.",
    ),
    (
        "Which Foundry feature is the primary low-code surface for testing a "
        "deployed model with prompts before writing client code?",
        [
            ("The Foundry portal playground (chat / completions)", True),
            ("Azure Resource Graph", False),
            ("Azure Pipelines", False),
            ("Azure Migrate", False),
        ],
        "The playground lets you iterate on prompts and parameters against a "
        "deployed model.",
    ),
    (
        "You are writing a lightweight <strong>chat client</strong> with the "
        "Foundry SDK. Which is the standard call to send messages and receive "
        "a response?",
        [
            ("Call the chat completions / responses API with a list of role-tagged messages (system, user, assistant)", True),
            ("Call a REST endpoint for Azure SQL Database", False),
            ("Run kubectl apply", False),
            ("Open a TCP socket on port 1433", False),
        ],
        "Foundry/Azure OpenAI SDKs expose chat completions/responses APIs that "
        "accept role-tagged messages.",
    ),
    (
        "What does it mean to create a <strong>single-agent solution</strong> "
        "in the Foundry portal?",
        [
            ("You configure one agent with a system prompt, attach tools (e.g., function calling, code interpreter, file search), and test it in the portal", True),
            ("You deploy two agents that argue with each other", False),
            ("You deploy a model with no tools and call it a database", False),
            ("You write a Windows service in C++", False),
        ],
        "A single-agent solution = one agent + its instructions + its enabled "
        "tools, testable in the portal.",
    ),
    (
        "Which capability lets a Foundry agent take action in external systems "
        "(e.g., look up a customer, send an email)?",
        [
            ("Tools / function calling (the agent invokes tools you register)", True),
            ("Changing the model's temperature", False),
            ("Lowering max tokens", False),
            ("Increasing top-p only", False),
        ],
        "Tools / function calling are how agents reach out to APIs and "
        "external systems.",
    ),
    (
        "You are building a <strong>lightweight client application for an "
        "agent</strong>. What is the typical responsibility of the client?",
        [
            ("Authenticate, create or reuse a thread/conversation, send user messages to the agent, and render the agent's streamed responses", True),
            ("Train the agent's underlying model from scratch", False),
            ("Manage Azure subscription billing", False),
            ("Provision the database servers used by the agent", False),
        ],
        "Client apps for agents handle auth, threading/conversation state, "
        "and rendering — not training.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 49 — Text & speech in Foundry
# ----------------------------------------------------------------------
QUIZ_49 = [
    (
        "You are building a lightweight Foundry app that needs to extract "
        "sentiment and entities from customer feedback. Which is the most "
        "direct approach?",
        [
            ("Call Azure AI Language features (sentiment, NER) from the app, or call a deployed multimodal model with a text-analysis prompt", True),
            ("Train a custom convolutional neural network for sentiment", False),
            ("Use Azure SQL Database full-text search only", False),
            ("Use Azure Front Door routing rules", False),
        ],
        "Azure AI Language offers prebuilt text-analysis APIs; Foundry can "
        "also call multimodal models with text-analysis prompts.",
    ),
    (
        "A user records a voice question and the app should reply in natural "
        "language. Which Foundry pattern best fits 'respond to spoken prompts "
        "by using a deployed multimodal model'?",
        [
            ("Send the user's audio (and/or its transcription) to a deployed multimodal model and play back the model's response with text-to-speech", True),
            ("Forward the audio file to a relational database", False),
            ("Email the audio to support staff", False),
            ("Run the audio through Azure Cosmos DB triggers", False),
        ],
        "Multimodal models can accept speech input directly; pair them with "
        "TTS for spoken replies.",
    ),
    (
        "Which Foundry Tools feature lets you build voice experiences without "
        "stitching together separate STT/TTS SDK calls yourself?",
        [
            ("Azure Speech in Foundry Tools (speech-to-text and text-to-speech as built-in tools an agent or app can call)", True),
            ("Azure Resource Graph queries", False),
            ("Azure DevOps Pipelines", False),
            ("Azure Migrate", False),
        ],
        "Foundry Tools exposes Azure Speech (STT/TTS) as managed tools for "
        "voice-enabled apps and agents.",
    ),
    (
        "You want to give an agent the ability to read out its answers aloud. "
        "Which capability should you enable?",
        [
            ("Text-to-speech (speech synthesis) via Azure Speech in Foundry Tools", True),
            ("Speech-to-text only", False),
            ("Document Intelligence layout model", False),
            ("Azure AI Vision Image Analysis", False),
        ],
        "TTS converts the agent's textual response into spoken audio.",
    ),
    (
        "You want users to dictate questions to a voice agent. Which capability "
        "should you enable?",
        [
            ("Speech-to-text (speech recognition)", True),
            ("Text-to-speech only", False),
            ("Image classification", False),
            ("Object detection", False),
        ],
        "STT transcribes the user's audio into text the agent can process.",
    ),
    (
        "Which Azure AI Language feature is best suited to power an FAQ-style "
        "answer experience inside a Foundry-based chat app?",
        [
            ("Question answering (custom Q&A over a knowledge base)", True),
            ("Anomaly detection", False),
            ("Custom vision classification", False),
            ("Translator document translation", False),
        ],
        "Azure AI Language question answering serves answers from a curated "
        "Q&A knowledge base.",
    ),
    (
        "Which Azure AI Speech capability allows two parties speaking different "
        "languages to converse with real-time translated audio?",
        [
            ("Speech translation", True),
            ("Speaker recognition", False),
            ("Sentiment analysis", False),
            ("Custom neural voice", False),
        ],
        "Speech translation produces translated text/audio from spoken input "
        "in near real time.",
    ),
    (
        "Which capability lets a Foundry app determine the language of a piece "
        "of text before processing it further?",
        [
            ("Language detection (Azure AI Language)", True),
            ("Speech synthesis", False),
            ("Object detection", False),
            ("Image classification", False),
        ],
        "Language detection returns the predominant language for a text "
        "input, useful for routing/translation.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 50 — Vision, image generation, and information extraction
# ----------------------------------------------------------------------
QUIZ_50 = [
    (
        "You want a Foundry app where the user uploads a photo and asks a "
        "question about it. Which approach is best?",
        [
            ("Send the image plus the user's question to a deployed multimodal model and use the model's text response", True),
            ("OCR the image and ignore everything else", False),
            ("Use only a tabular regression model", False),
            ("Use Azure SQL Database to interpret pixels", False),
        ],
        "Multimodal chat models accept images alongside text and reason over "
        "them.",
    ),
    (
        "You need to produce brand-new marketing images from a text brief. "
        "Which kind of Foundry model should you deploy?",
        [
            ("An image-generation model (e.g., DALL·E / GPT-image)", True),
            ("A speech-to-text model", False),
            ("A small language model for classification", False),
            ("An anomaly detector", False),
        ],
        "Image-generation (diffusion / GPT-image) models create new images "
        "from prompts.",
    ),
    (
        "Which is the most direct Foundry Tools feature for <strong>extracting "
        "fields from invoices, receipts, and forms</strong>?",
        [
            ("Azure Content Understanding (document/forms analyzer)", True),
            ("Azure AI Speech batch transcription", False),
            ("Azure AI Translator", False),
            ("Azure Cosmos DB change feed", False),
        ],
        "Content Understanding provides document/form analyzers that extract "
        "structured fields from PDFs/images.",
    ),
    (
        "Which Foundry capability extracts structured information from "
        "<strong>images</strong> (e.g., signage, product photos)?",
        [
            ("An image analyzer in Azure Content Understanding", True),
            ("Speech-to-text batch transcription", False),
            ("Azure Front Door routing", False),
            ("Azure Resource Graph queries", False),
        ],
        "Content Understanding image analyzers extract fields/attributes "
        "from image inputs.",
    ),
    (
        "Which Foundry capability extracts structured information from "
        "<strong>audio and video</strong> (e.g., speakers, topics, key "
        "moments)?",
        [
            ("An audio/video analyzer in Azure Content Understanding", True),
            ("Azure AI Vision Image Analysis only", False),
            ("Azure SQL Hyperscale", False),
            ("Azure Bot Service channels", False),
        ],
        "Content Understanding has analyzers purpose-built for audio and "
        "video inputs.",
    ),
    (
        "You are building a lightweight Foundry app whose only job is to take "
        "uploaded PDFs and emit a JSON object of key fields. Which design fits "
        "best?",
        [
            ("Configure a Content Understanding analyzer with the desired schema, then call it from the app and return its JSON output", True),
            ("Train a brand-new diffusion model from scratch", False),
            ("Use only a key-phrase extraction API on the binary PDF bytes", False),
            ("Use Azure Bot Service as the OCR engine", False),
        ],
        "Schema-driven Content Understanding analyzers map directly to "
        "structured JSON extraction.",
    ),
    (
        "Which statement about multimodal models in Foundry is true?",
        [
            ("A single deployed multimodal model can answer questions about an image, draft text, and follow an instruction in one request", True),
            ("Multimodal models can only output images", False),
            ("Multimodal models cannot be deployed in Foundry", False),
            ("Multimodal models replace the need for any storage", False),
        ],
        "Multimodal models accept and reason over multiple modalities in one "
        "request.",
    ),
    (
        "Which is a responsible-AI consideration unique to <strong>image "
        "generation</strong> in Foundry apps?",
        [
            ("Apply content safety filters and watermarking/provenance to mitigate harmful or deceptive imagery", True),
            ("Disable all logging and auditing", False),
            ("Always run on the smallest VM size available", False),
            ("Generate images at the highest possible temperature for safety", False),
        ],
        "Image generation requires content-safety filters and provenance/"
        "watermarking to address misuse and deception risks.",
    ),
]


def main() -> None:
    with app.app_context():
        bundles = [
            (46, QUIZ_46),
            (47, QUIZ_47),
            (48, QUIZ_48),
            (49, QUIZ_49),
            (50, QUIZ_50),
        ]
        for quiz_id, items in bundles:
            before = Question.query.filter_by(quiz_id=quiz_id).count()
            for prompt, options, feedback in items:
                add_question(quiz_id, prompt, options, feedback)
            db.session.flush()
            after = Question.query.filter_by(quiz_id=quiz_id).count()
            print(f"  Quiz {quiz_id}: {before} -> {after} questions ({after - before} added)")
        db.session.commit()
        print("Done.")


if __name__ == "__main__":
    main()
