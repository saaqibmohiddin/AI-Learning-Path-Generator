# 30-Day AI Engineer Learning Roadmap

**Starting point:** Beginner; Python basics, HTML, CSS, and JavaScript  
**Study commitment:** 2 hours per day (about 60 hours total)  
**MCP-generated career path:** Python Programming → Mathematics for AI → NumPy and Pandas → Machine Learning → Deep Learning → Natural Language Processing → Generative AI → Build AI Projects

This plan follows the AI Engineer roadmap returned by `create_learning_roadmap`, with the user's existing Python and web skills treated as prerequisites. Each day's deliverable builds toward a small AI application; the schedule is an introduction, not a guarantee of job readiness.

## Suggested daily routine

- **25 minutes:** Read or watch the day's learning resource.
- **70 minutes:** Implement the exercise and mini-project.
- **25 minutes:** Test the result, write down what you learned, and commit or save the work.

## Daily plan

| Day | Topic and learning goal | Practical exercise and mini-project | Learning resources |
|---|---|---|---|
| 1 | Python refresh: functions, collections, loops, and comprehensions | Write reusable functions to clean a list of skill names; make a small command-line skill checklist. | [Python Tutorial](https://docs.python.org/3/tutorial/) |
| 2 | Python data structures, modules, and virtual environments | Create a small project with a module for loading and validating a list of learning goals. | [Python Tutorial](https://docs.python.org/3/tutorial/) |
| 3 | Files, exceptions, and JSON | Build a JSON-backed study tracker that records topics and completion status; handle a missing or malformed file. | [Python Tutorial: input and output](https://docs.python.org/3/tutorial/inputoutput.html) |
| 4 | Mathematics for AI: vectors, scalars, and basic notation | Represent feature vectors for three sample learners and calculate vector addition and scaling by hand and in Python. | [Khan Academy: Linear algebra](https://www.khanacademy.org/math/linear-algebra) |
| 5 | Dot products and cosine similarity intuition | Implement a dot product and cosine similarity; compare two short skill vectors and explain what the score means. | [Google ML Crash Course: embeddings and vector concepts](https://developers.google.com/machine-learning/crash-course) |
| 6 | Probability, averages, variance, and data distributions | Calculate mean, median, and standard deviation for a tiny dataset; simulate coin flips and compare observed and expected rates. | [Khan Academy: Probability and statistics](https://www.khanacademy.org/math/statistics-probability) |
| 7 | NumPy arrays and vectorized operations | Convert learner-feature lists to NumPy arrays; compute column means and normalize numeric features. | [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) |
| 8 | Pandas DataFrames, selecting, filtering, and sorting | Load a small CSV of course records; filter by topic and difficulty, then report counts and averages. | [pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) |
| 9 | Data cleaning and visualization | Handle missing values and duplicates in a sample course dataset; plot course counts by topic and level. | [pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) |
| 10 | Machine learning workflow: features, labels, and train/test split | Define a tiny tabular problem (for example, predict whether a learner completes a lesson); identify features and label, and create a split. | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) |
| 11 | Supervised learning: regression | Train a scikit-learn regression model on a small numeric dataset; predict a value and calculate a basic error metric. | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course), [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) |
| 12 | Supervised learning: classification | Train a simple classifier on a built-in dataset; inspect predicted classes and a confusion matrix. | [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) |
| 13 | Evaluation, overfitting, and baselines | Compare a simple baseline with a model using held-out data; explain why test data must not be used to fit the model. | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) |
| 14 | Preprocessing categorical and numeric data | Build a scikit-learn pipeline that scales numeric data and encodes categories before classification. | [scikit-learn: preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) |
| 15 | Mini-project: course completion predictor | Build a small, documented predictor using a toy dataset; include a baseline, train/test evaluation, and a note on limitations. | [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) |
| 16 | Deep learning concepts: tensors, layers, weights, and loss | Use a small neural-network visualizer or tutorial to trace input → prediction → loss; sketch the flow in your notes. | [DeepLearning.AI](https://www.deeplearning.ai/) |
| 17 | Build a first neural network | Follow a beginner framework tutorial and train a small model on a standard sample dataset; record training and validation results. | [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) |
| 18 | Training loops, epochs, and learning rate | Change one training setting at a time and compare loss curves; write down one sign of underfitting or overfitting. | [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) |
| 19 | Model inference and saving/loading | Save a trained model, reload it in a separate script, and run predictions on new examples. | [PyTorch: Saving and Loading Models](https://pytorch.org/tutorials/beginner/saving_loading_models.html) |
| 20 | Deep learning mini-project: simple image classifier | Train or adapt a small image classifier using a tutorial dataset; evaluate a few predictions and document errors. | [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) |
| 21 | NLP basics: tokens, vocabulary, and text normalization | Normalize a small set of course descriptions and inspect token counts; compare raw and cleaned text. | [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1) |
| 22 | Text classification and embeddings | Use a simple bag-of-words or TF-IDF representation to classify a few example learning-resource descriptions by topic. | [scikit-learn: Working with text data](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) |
| 23 | NLP mini-project: topic matcher | Build a small program that ranks course descriptions against a learner's topic query using TF-IDF and cosine similarity. | [scikit-learn: Working with text data](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) |
| 24 | Generative AI and large-language-model basics | Learn the roles of prompts, tokens, context, and model outputs; draft prompts for turning a goal into weekly study tasks. | [Hugging Face Learn](https://huggingface.co/learn) |
| 25 | Prompt design and structured outputs | Create and refine a prompt that requests a valid JSON study plan; check required fields and handle invalid output in code. | [Hugging Face Learn](https://huggingface.co/learn) |
| 26 | Retrieval-augmented generation (RAG) concept and grounding | Prepare a tiny set of trusted learning-resource notes; retrieve relevant text for a query and require answers to use only that context. | [Hugging Face Learn](https://huggingface.co/learn) |
| 27 | Capstone design: personalized AI study planner | Specify inputs (career goal, skills, level), output schema, success criteria, and a safe fallback; draw the data flow before coding. | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course), [Hugging Face Learn](https://huggingface.co/learn) |
| 28 | Capstone implementation: roadmap generation | Combine a deterministic topic sequence with learner-skill filtering; return a structured plan and test known and unknown career goals. | [Python Tutorial](https://docs.python.org/3/tutorial/), [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) |
| 29 | Capstone implementation: resource matching and interface | Add resource recommendations and a simple interface or CLI; use the user's HTML/CSS/JavaScript knowledge if building a web front end. | [Hugging Face Learn](https://huggingface.co/learn), [Python Tutorial](https://docs.python.org/3/tutorial/) |
| 30 | Test, document, and present the capstone | Test empty skills, unknown goals, and malformed inputs; document setup, approach, limitations, and next improvements; demonstrate one example plan. | [Python Tutorial](https://docs.python.org/3/tutorial/), [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) |

## End-of-plan deliverable

By Day 30, aim to have a small, documented study-planner prototype that accepts a career goal and current skills, produces a structured roadmap, and recommends relevant learning resources. Keep sample data clearly labeled, test edge cases, and disclose where recommendations are rule-based or generated.
