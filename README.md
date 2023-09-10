# Domain Centric Chatbot (Langchain, OpenAI, Vector DB from MongoDB Atlas)

# Your Gateway to Domain-Specific Insights!

**"Empowering Open Source Language Models with Real-Time Knowledge"**

🚀 Welcome to a chatbot experience that brings the latest information right to your fingertips. Say goodbye to outdated data woes and hello to dynamic, up-to-the-minute responses. This chatbot is your all-access pass to real-time knowledge.

As available open-source models are trained on old data and retraining them with new data is often unfeasible and costly, this chatbot leverages these models and supplements them with the freshest context-specific insights.

🌐 Imagine a chatbot that can effortlessly adapt to any domain you desire. With a simple URL change, it transforms into your go-to expert, making it perfect for a wide range of applications. Whether you're exploring financial trends, diving into healthcare insights, or unraveling the mysteries of technology, the chatbot has you covered.

🎬 Curious to see it in action? Check out this [video link](https://www.youtube.com/watch?v=gzPGWUQT8HI)

![Example](https://github.com/Soham7777/Domain-Centric-Chatbot/assets/66548809/72bdaddc-25c2-4e3c-8efb-e7eefa53653c)

## Project Overview

- **ChatBot Architecture**: The project leverages Langchain and OpenAI to build an adaptable chatbot that can be fine-tuned for specific domains, ensuring the latest information is always at your fingertips. Also uses MongoDB cluster to store and retreive embeddings through the knowledge base aka Vector DB

- **Data Retrieval**: The chatbot is equipped with the capability to fetch the latest information from websites. **Note:** Websites need to be bot-friendly

 ### Work Done
- [x] **Development Status**: The working model is deployed with streamlit and ready to use for real time user interaction
- [x] **VectoreStore Integration**: Used MongoDB atlas as vector store which is hassle free to setup and efficient to use.

## Getting Started

Follow these steps to set up and run the project:

1. **Fork Repository:** Start by forking this repository to your own GitHub account.

2. **Create a Virtual Environment:** It's recommended to create a virtual environment to isolate dependencies. You can use conda or Python's built-in `venv` module or `conda` environment.

3. **Install Dependencies:** Install the project dependencies by running the following command in your virtual environment:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MongoDB Atlas Cluster:** Deploy a free MongoDB Atlas cluster by following the steps in this [link](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/).

5. **Create Cluster Index:** Create a cluster index with the specific embedding model into your MongoDB cluster. Make sure to adjust the vector dimensions according to the embeddings you are using. For more details, refer to the [documentation](https://python.langchain.com/docs/integrations/vectorstores/mongodb_atlas).

6. **Configure Environment Variables:** Define your MongoDB cluster URIs, OpenAI API keys, and the URLs for which domains you want your chatbot to work within the `utils.py` file.

7. **Run the Application:** Once everything is set up, you are ready to go. Start the application by running the following command:

    ```bash
    streamlit run main.py
    ```

Now, you can start using and testing the chatbot. Happy chatting!


# Future Enhancements

I have exciting plans for enhancing this project in the future. Here's what's on the horizon:

- [ ] **Text Summarization and Query Refinements:** Aiming to improve the chatbot's response accuracy by incorporating advanced text summarization techniques and refining query handling for more precise interactions.
- [ ] **Support for PDF Loaders:** This will enable the user to chat with documents and make the most out of the internal information available without speding hours of scrolling through documents. 

- [ ] **Containerization with Docker:** To streamline deployment and ensure consistency across different environments, I plan to containerize the application using Docker, making it easier to set up and run.

- [ ] **ETL and ML Flow for Pipelines:** Implementing Extract, Transform, Load (ETL) processes and using MLflow for pipeline management will enhance data preprocessing and model training workflows, further optimizing performance.

- [ ] **Open-Source Alternatives:** I understand the importance of accessibility and cost-effectiveness. Exploring alternatives to OpenAI's paid models, such as integrating with Hugging Face models or other open-source libraries. The goal is to make the entire chatbot solution open source and free to use for everyone.

Stay tuned for these exciting enhancements that will make the chatbot even more powerful and accessible to the community!


## Collaboration

 Feel free to contribute, share ideas, and let's take this chatbot to the next level.

