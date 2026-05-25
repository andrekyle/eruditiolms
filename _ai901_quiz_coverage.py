"""Backfill AI-901 quiz questions so every official AI-900 sub-skill is
covered (skills measured as of May 2, 2025).

Idempotent: each added question is tagged with a hidden marker so re-runs
don't duplicate. Question style: multiple_choice with four options and one
correct answer.

Quiz -> Lesson -> skill area:
  45 -> L3 Responsible AI            -> Area 1 (Responsible AI principles)
  46 -> L4 Model components          -> Area 2 (ML principles)
  47 -> L5 AI workloads              -> Area 1 (workload identification)
  48 -> L6 Gen AI apps & agents      -> Area 5 (Generative AI)
  49 -> L7 Text & speech             -> Area 4 (NLP)
  50 -> L8 Vision & info extraction  -> Area 3 (Computer Vision)
"""
from __future__ import annotations
from app import app, db, Quiz, Question, QuestionOption

MARKER = "<!-- ai901_coverage_v1 -->"


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
# Quiz 45 — Responsible AI (Area 1)
# ----------------------------------------------------------------------
QUIZ_45 = [
    (
        "Which Responsible AI principle is most directly addressed by encrypting "
        "training data at rest and limiting access to authorized personnel?",
        [
            ("Fairness", False),
            ("Privacy and security", True),
            ("Inclusiveness", False),
            ("Transparency", False),
        ],
        "Protecting data and access controls directly maps to the privacy and "
        "security principle.",
    ),
    (
        "An organization wants to ensure that a human can be held responsible for "
        "the outcomes of an AI system used in hiring decisions. Which Responsible "
        "AI principle does this best reflect?",
        [
            ("Accountability", True),
            ("Reliability and safety", False),
            ("Inclusiveness", False),
            ("Transparency", False),
        ],
        "Accountability requires that people (not the AI) own and remain "
        "responsible for the system's decisions.",
    ),
    (
        "An AI chatbot for emergency services must remain available and behave "
        "predictably under heavy load. Which Responsible AI principle is the "
        "primary focus?",
        [
            ("Reliability and safety", True),
            ("Inclusiveness", False),
            ("Privacy and security", False),
            ("Fairness", False),
        ],
        "Reliability and safety covers consistent operation, robustness under "
        "load, and predictable behavior in adverse conditions.",
    ),
    (
        "A vision model is being deployed in a public app. Which step most "
        "directly supports the inclusiveness principle?",
        [
            ("Add captions and alternative text to UI elements and ensure the model is tested across users with disabilities", True),
            ("Reduce the model's parameter count", False),
            ("Encrypt the model file at rest", False),
            ("Increase the temperature of generated text", False),
        ],
        "Inclusiveness means the solution works for and includes people of all "
        "abilities, backgrounds, and needs.",
    ),
    (
        "Which artefact best supports the transparency principle for an AI model "
        "released to business stakeholders?",
        [
            ("A model card describing intended use, training data, evaluation, and limitations", True),
            ("A signed NDA", False),
            ("A network-isolation policy", False),
            ("A load-test report", False),
        ],
        "Model/transparency cards document how a model was built and where it "
        "should and should not be used.",
    ),
    (
        "Which scenario is the strongest example of a fairness concern?",
        [
            ("A loan-approval model has materially different approval rates for equally qualified applicants of different demographic groups", True),
            ("A model file is 4 GB in size", False),
            ("A model returns a 200 OK in under 100 ms", False),
            ("A model has been quantized to 8-bit weights", False),
        ],
        "Disparate outcomes for protected groups is the canonical fairness "
        "issue Responsible AI addresses.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 46 — ML principles (Area 2)
# ----------------------------------------------------------------------
QUIZ_46 = [
    (
        "Predicting tomorrow's temperature from historical weather data is which "
        "type of machine-learning scenario?",
        [
            ("Regression", True),
            ("Classification", False),
            ("Clustering", False),
            ("Reinforcement learning", False),
        ],
        "Regression predicts a continuous numeric value (temperature, price, "
        "duration).",
    ),
    (
        "Sorting incoming customer emails into 'Billing', 'Support', or 'Sales' "
        "is which type of machine-learning scenario?",
        [
            ("Regression", False),
            ("Multi-class classification", True),
            ("Clustering", False),
            ("Anomaly detection", False),
        ],
        "Choosing one of several discrete categories for an item is "
        "multi-class classification.",
    ),
    (
        "Grouping customers into segments based on purchasing behaviour without "
        "any predefined labels is which type of machine-learning scenario?",
        [
            ("Clustering", True),
            ("Regression", False),
            ("Binary classification", False),
            ("Supervised learning", False),
        ],
        "Clustering is the canonical unsupervised technique for discovering "
        "groups in unlabeled data.",
    ),
    (
        "Which statement best describes a key feature of deep learning?",
        [
            ("It uses multi-layer neural networks that learn hierarchical representations of data", True),
            ("It is only used for tabular data", False),
            ("It requires no training data", False),
            ("It always uses decision trees", False),
        ],
        "Deep learning relies on stacked neural-network layers that learn "
        "progressively higher-level features.",
    ),
    (
        "Which capability is a defining feature of the Transformer architecture?",
        [
            ("Self-attention that weighs the importance of every token relative to others in a sequence", True),
            ("Convolutional filters over image pixels", False),
            ("Recurrent connections that process tokens one at a time only", False),
            ("Hand-engineered decision rules", False),
        ],
        "Self-attention is the core building block of Transformer models such "
        "as GPT and BERT.",
    ),
    (
        "In a tabular dataset used to predict house prices, the column "
        "<em>SalePrice</em> is the target you want to predict. The other columns "
        "(square footage, bedrooms, location) are inputs. Which statement is "
        "true?",
        [
            ("SalePrice is the label; the other columns are features", True),
            ("SalePrice is a feature; the other columns are labels", False),
            ("All columns are labels in supervised learning", False),
            ("Features are only used at inference, not during training", False),
        ],
        "Features are the input variables; the label is the value the model "
        "learns to predict.",
    ),
    (
        "Why do data scientists split data into training and validation sets?",
        [
            ("To measure how well the model generalizes to data it has not seen during training", True),
            ("To increase the number of features in the dataset", False),
            ("Because Azure Machine Learning requires exactly two files", False),
            ("To encrypt the data for production", False),
        ],
        "The validation set is held out from training so it can give an "
        "unbiased estimate of generalization performance.",
    ),
    (
        "Which Azure Machine Learning capability lets a business analyst train "
        "and compare many candidate models for a tabular dataset with minimal "
        "code?",
        [
            ("Automated machine learning (AutoML)", True),
            ("Azure Container Registry", False),
            ("Azure Key Vault", False),
            ("Azure Resource Manager templates", False),
        ],
        "AutoML in Azure ML automates algorithm selection, featurization, and "
        "hyperparameter tuning.",
    ),
    (
        "Which Azure Machine Learning concept lets you reproducibly run training "
        "on managed CPU or GPU virtual machines?",
        [
            ("Compute clusters (compute targets)", True),
            ("Data Lake Storage Gen2 only", False),
            ("Azure Front Door", False),
            ("Azure Cosmos DB containers", False),
        ],
        "Compute clusters provide on-demand, scalable compute targets for "
        "Azure ML jobs.",
    ),
    (
        "After training a model in Azure Machine Learning, which capability is "
        "most directly used to track versions of the model and approve it for "
        "production?",
        [
            ("The model registry in the Azure ML workspace", True),
            ("Azure Blob Storage immutable policies only", False),
            ("Azure Monitor metrics", False),
            ("Azure SQL Database elastic pools", False),
        ],
        "The Azure ML model registry stores, versions, and tags trained "
        "models, and feeds deployment workflows.",
    ),
    (
        "Which Azure Machine Learning option lets you serve a trained model as a "
        "low-latency real-time REST endpoint?",
        [
            ("Managed online endpoint", True),
            ("Batch transcription only", False),
            ("Cognitive Services container only", False),
            ("Azure Data Factory pipeline", False),
        ],
        "Managed online endpoints host a model behind a scalable REST endpoint "
        "with autoscaling and traffic-splitting.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 47 — Workload identification (Area 1)
# ----------------------------------------------------------------------
QUIZ_47 = [
    (
        "Tagging photos in a personal photo library as 'beach', 'mountain', or "
        "'city' is which type of AI workload?",
        [
            ("Image classification (computer vision)", True),
            ("Optical character recognition", False),
            ("Sentiment analysis", False),
            ("Forecasting", False),
        ],
        "Assigning a class label to an entire image is image classification.",
    ),
    (
        "Highlighting and labelling every car, pedestrian, and stop sign in a "
        "single photograph is which type of AI workload?",
        [
            ("Object detection", True),
            ("Image classification", False),
            ("Text translation", False),
            ("Clustering", False),
        ],
        "Object detection locates and labels multiple objects (with bounding "
        "boxes) within an image.",
    ),
    (
        "Extracting the printed text from a scanned book page so it can be "
        "searched is which type of AI workload?",
        [
            ("Optical character recognition (OCR)", True),
            ("Speech-to-text", False),
            ("Sentiment analysis", False),
            ("Forecasting", False),
        ],
        "OCR converts text inside images or PDFs into machine-readable text.",
    ),
    (
        "Pulling structured fields (vendor, total, line items) from an uploaded "
        "PDF invoice is which type of AI workload?",
        [
            ("Document processing (intelligent document processing)", True),
            ("Image classification", False),
            ("Reinforcement learning", False),
            ("Translation", False),
        ],
        "Extracting structured key-value or table data from forms and "
        "documents is the document-processing workload.",
    ),
    (
        "Detecting and identifying human faces in security camera footage is "
        "which AI workload type?",
        [
            ("Facial detection and facial analysis (computer vision)", True),
            ("Natural language processing", False),
            ("Anomaly detection", False),
            ("Translation", False),
        ],
        "Facial detection/analysis is a CV workload that locates and "
        "describes attributes of human faces.",
    ),
    (
        "A system summarizes long customer-support transcripts into a few "
        "sentences. This is primarily which AI workload type?",
        [
            ("Natural language processing (text summarization, a generative-AI use case)", True),
            ("Object detection", False),
            ("OCR", False),
            ("Forecasting", False),
        ],
        "Summarization is a text-understanding/generation NLP task.",
    ),
    (
        "A marketing tool produces brand-new product descriptions and images "
        "from a short brief. This is which AI workload type?",
        [
            ("Generative AI", True),
            ("Clustering", False),
            ("OCR", False),
            ("Object detection", False),
        ],
        "Creating new content (text, images, code, audio) from prompts is the "
        "generative-AI workload.",
    ),
    (
        "Which scenario is best described as a natural language processing "
        "workload rather than a generative AI workload?",
        [
            ("Extracting key phrases and sentiment from product reviews", True),
            ("Writing a new poem about a product launch", False),
            ("Generating a marketing image from text", False),
            ("Drafting an email reply from bullet notes", False),
        ],
        "Classic NLP tasks (sentiment, key phrases, entities, translation) "
        "analyze existing text rather than generate new content.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 48 — Generative AI (Area 5)
# ----------------------------------------------------------------------
QUIZ_48 = [
    (
        "Which statement best describes a foundational large language model "
        "(LLM)?",
        [
            ("A model trained on very large, diverse text corpora that can be adapted to many downstream tasks via prompting or fine-tuning", True),
            ("A small lookup table of canned responses", False),
            ("A rule-based parser for SQL statements", False),
            ("A vector database for image embeddings", False),
        ],
        "LLMs are large, general-purpose foundation models adaptable to many "
        "tasks.",
    ),
    (
        "Which is a defining feature of a multimodal generative AI model such "
        "as GPT-4o?",
        [
            ("It accepts and produces multiple modalities (e.g., text, images, audio)", True),
            ("It runs only on CPU", False),
            ("It cannot be deployed in Azure", False),
            ("It exclusively produces images", False),
        ],
        "Multimodal models reason across multiple input/output modalities.",
    ),
    (
        "Which is a typical business scenario for generative AI?",
        [
            ("Drafting and summarizing emails or reports", True),
            ("Replacing the relational database tier", False),
            ("Performing physical-layer network routing", False),
            ("Encrypting data at rest", False),
        ],
        "Content drafting/summarization is a flagship generative-AI use case.",
    ),
    (
        "Which is a responsible-AI consideration specific to generative AI?",
        [
            ("Mitigating hallucinations (fabricated facts) by grounding the model in trusted data and applying content filters", True),
            ("Lowering the network MTU on the application server", False),
            ("Forcing the model to use COBOL output only", False),
            ("Disabling all logging on the deployment", False),
        ],
        "Grounding, content filtering, and hallucination mitigation are key "
        "responsible-AI practices for generative models.",
    ),
    (
        "Which capability of Azure AI Foundry helps teams collaborate on "
        "generative-AI projects from data and model selection through "
        "evaluation, deployment, and monitoring?",
        [
            ("Azure AI Foundry projects (workspace) with model catalog, playgrounds, evaluations, and managed deployments", True),
            ("Azure DevTest Labs", False),
            ("Azure Front Door", False),
            ("Azure SQL elastic pool", False),
        ],
        "Foundry projects/workspaces provide the unified surface for the "
        "entire generative-AI lifecycle.",
    ),
    (
        "Which statement about Azure OpenAI Service is true?",
        [
            ("It provides REST and SDK access to OpenAI models (e.g., GPT-4o, GPT-4.1, embeddings) hosted in Azure with enterprise security, regional control, and content filtering", True),
            ("It is a free public API with no authentication", False),
            ("It only supports image classification", False),
            ("It can only be used from on-premises networks", False),
        ],
        "Azure OpenAI delivers OpenAI models in Azure with Microsoft Entra "
        "auth, regional deployment, and built-in content filters.",
    ),
    (
        "What is the primary purpose of the Azure AI Foundry model catalog?",
        [
            ("A curated catalog of foundation and partner models (OpenAI, Meta, Mistral, etc.) you can compare, deploy, and benchmark from Foundry", True),
            ("A registry of Azure SQL Database backups", False),
            ("A list of available Windows VM sizes", False),
            ("A repository of Bicep templates only", False),
        ],
        "The Foundry model catalog presents many first- and third-party "
        "models with deploy/benchmark/evaluate actions.",
    ),
    (
        "A team wants to compare three foundation models for a chat use case "
        "without writing client code, then promote one to a production "
        "endpoint. Which Foundry feature is most directly used?",
        [
            ("The Foundry portal playground combined with deploy-to-endpoint from the model catalog", True),
            ("Azure DNS record sets", False),
            ("Azure Blob Storage lifecycle rules", False),
            ("Azure Key Vault secret rotation", False),
        ],
        "Foundry playground + catalog deployment is the no-/low-code path "
        "from evaluation to a production endpoint.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 49 — NLP (Area 4)
# ----------------------------------------------------------------------
QUIZ_49 = [
    (
        "Which Azure AI Language feature extracts the main talking points (such "
        "as 'battery life', 'screen quality') from product reviews?",
        [
            ("Key phrase extraction", True),
            ("Sentiment analysis", False),
            ("Speech synthesis", False),
            ("Translator", False),
        ],
        "Key phrase extraction surfaces the most relevant noun phrases from "
        "text.",
    ),
    (
        "An app needs to detect what language an incoming user message is "
        "written in. Which Azure AI Language capability does this?",
        [
            ("Language detection", True),
            ("Question answering", False),
            ("Speech recognition", False),
            ("Custom Vision", False),
        ],
        "Language detection identifies the predominant language of a piece of "
        "text and returns an ISO code.",
    ),
    (
        "Which is the best Azure AI Language capability for building a chatbot "
        "that maps user utterances to predefined intents and entities?",
        [
            ("Conversational Language Understanding (CLU)", True),
            ("OCR", False),
            ("Image classification", False),
            ("Translator document translation", False),
        ],
        "CLU is the modern intent + entity recognition feature for "
        "conversational apps.",
    ),
    (
        "Which Azure AI Speech capability converts written text to a natural-"
        "sounding voice (audio)?",
        [
            ("Text-to-speech (TTS / speech synthesis)", True),
            ("Speech-to-text", False),
            ("Sentiment analysis", False),
            ("Language detection", False),
        ],
        "Speech synthesis (TTS) generates audio from text using neural "
        "voices.",
    ),
    (
        "Which Azure AI service is appropriate to translate documents across "
        "100+ languages while preserving formatting?",
        [
            ("Azure AI Translator (document translation)", True),
            ("Azure AI Vision", False),
            ("Azure AI Face", False),
            ("Azure Content Safety", False),
        ],
        "Translator document translation handles batch document translation "
        "across many languages with format preservation.",
    ),
    (
        "Which scenario is best described as language modeling (rather than a "
        "pre-built NLP feature)?",
        [
            ("Predicting the next likely word(s) in a sentence to power autocomplete or generation", True),
            ("Extracting an invoice number from a PDF", False),
            ("Detecting objects in an image", False),
            ("Encrypting a database at rest", False),
        ],
        "Language modeling predicts probabilities over token sequences and "
        "underlies generation and autocompletion.",
    ),
    (
        "Which Azure AI Speech capability lets you create a synthetic voice "
        "that mimics a target speaker for branded experiences (with appropriate "
        "consent)?",
        [
            ("Custom Neural Voice", True),
            ("Translator", False),
            ("Conversational Language Understanding", False),
            ("Anomaly Detector", False),
        ],
        "Custom Neural Voice trains a personalized neural TTS voice on "
        "consented samples.",
    ),
    (
        "Which Azure AI Language capability identifies and labels mentions of "
        "people, organizations, locations, and dates in text?",
        [
            ("Named entity recognition (NER)", True),
            ("Speech translation", False),
            ("Key phrase extraction", False),
            ("Sentiment analysis", False),
        ],
        "NER tags spans of text with entity types such as Person, "
        "Organization, Location, DateTime.",
    ),
]


# ----------------------------------------------------------------------
# Quiz 50 — Computer Vision (Area 3)
# ----------------------------------------------------------------------
QUIZ_50 = [
    (
        "Which Azure AI Vision capability tags an entire image with a single "
        "high-level label (e.g., 'dog', 'pizza')?",
        [
            ("Image classification", True),
            ("Object detection", False),
            ("Optical character recognition", False),
            ("Speech synthesis", False),
        ],
        "Image classification assigns a single class label to a whole image.",
    ),
    (
        "Which Azure AI Vision capability returns bounding boxes around each "
        "detected item in an image, along with a class label per box?",
        [
            ("Object detection", True),
            ("Image classification", False),
            ("Face attributes only", False),
            ("Translator", False),
        ],
        "Object detection localizes (bounding box) and labels multiple "
        "objects within the same image.",
    ),
    (
        "Which Azure AI Vision capability extracts printed and handwritten "
        "text from images and PDFs?",
        [
            ("Read (OCR) API in Azure AI Vision", True),
            ("Custom Neural Voice", False),
            ("Sentiment analysis", False),
            ("Translator document translation", False),
        ],
        "The Read API is the modern OCR capability in Azure AI Vision.",
    ),
    (
        "Which Azure AI service is purpose-built for detecting human faces and "
        "analyzing attributes such as head pose and facial landmarks?",
        [
            ("Azure AI Face", True),
            ("Azure AI Speech", False),
            ("Azure Cosmos DB", False),
            ("Azure SQL Database", False),
        ],
        "Azure AI Face is dedicated to face detection, identification, and "
        "verification.",
    ),
    (
        "Which generic feature is part of the Azure AI Vision service?",
        [
            ("Image analysis (tags, captions, dense captions, smart crops, OCR)", True),
            ("Train custom LLMs from scratch", False),
            ("Provision SQL Managed Instances", False),
            ("Deploy ARM templates", False),
        ],
        "Azure AI Vision provides image analysis (captions, tags, dense "
        "captions, OCR, smart crops, and more).",
    ),
    (
        "A retailer wants to train a custom classifier to recognize their own "
        "product SKUs from shelf photos. Which Azure AI Vision capability "
        "should they use?",
        [
            ("Azure AI Vision Image Analysis with a custom model (custom image classification)", True),
            ("Azure AI Speech batch transcription", False),
            ("Azure Translator", False),
            ("Azure AI Language NER", False),
        ],
        "Custom Vision / Azure AI Vision custom models let you train your own "
        "classifier or object detector on labeled images.",
    ),
    (
        "Which sentence best describes facial detection vs facial recognition?",
        [
            ("Detection locates faces in an image; recognition matches a detected face to a known identity", True),
            ("Detection and recognition are the same thing", False),
            ("Recognition only works on cartoons", False),
            ("Detection requires a custom-trained model only", False),
        ],
        "Detection finds faces; recognition (identification/verification) "
        "compares them to enrolled identities.",
    ),
    (
        "Which use case is a typical fit for the OCR (Read) feature of "
        "Azure AI Vision?",
        [
            ("Digitizing scanned paper forms and printed receipts into searchable text", True),
            ("Generating synthetic audio from text", False),
            ("Detecting faces and head pose", False),
            ("Forecasting product demand", False),
        ],
        "OCR converts text in images/PDFs into machine-readable text — ideal "
        "for digitizing paper documents.",
    ),
]


def main() -> None:
    with app.app_context():
        bundles = [
            (45, QUIZ_45),
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
